# Story Layers — Automation Repo

Source-of-truth repo for the Story Layers Instagram automation, so it can run
from an Anthropic Cloud routine (isolated Linux sandbox) instead of a local
Windows machine. A cloud routine clones this repo, reads the playbook + history,
generates and publishes a post, then commits the updated history back.

## Contents

| File | Purpose |
|---|---|
| `story_layers_social_playbook.md` | Operating playbook for `story_layers_il` — concept selection, no-repeat rules, image gen + QA, Hebrew caption rules, two-step Instagram publish flow, history logging. **Single source of truth** — edit here only. |
| `story_layers_social_history.json` | Post history log for `story_layers_il` (one entry per published/failed post). Routine reads this to avoid repeats and writes a new entry back after each run. |
| `story_layers_home_social_playbook.md` | Playbook for the separate `story_layers_home_il` account (draft-only, no auto-publish). |
| `story_layers_home_social_history.json` | Post history for `story_layers_home_il`. |
| `scripts/resize_image.py` | Linux/Pillow replacement for the old Windows PowerShell + `System.Drawing` resize step (1080px width, quality 85). Cloud sandboxes are Linux, so the PowerShell step could not run as-is. |

## Accounts (do not confuse the two)

- `story_layers_il` — main account. IG User ID `37417051787909830`. All auto-publishing targets this one.
- `story_layers_home_il` (`Story Layers Home`) — separate, unrelated account. Draft-only for now.

## Image hosting step (updated for cloud)

Old flow used Windows PowerShell to resize. New flow:

1. Download the generated image (Gemini signed URL is short-lived).
2. Resize to 1080px width via `scripts/resize_image.py` (Pillow, quality 85):
   `python scripts/resize_image.py --url "<gemini-url>" --out post-<date>-resized.jpg`
   (or `--in <local.jpg>` for an already-downloaded file).
3. Get the ImgBB key via the `IMGBB_GET_API_KEY` Composio tool.
4. Upload with `curl -X POST "https://api.imgbb.com/1/upload" -F "key=<key>" -F "expiration=2592000" -F "image=@<resized path>"`.
5. Use the returned `data.url` as the Instagram `image_url`.

## Cloud migration status / open items

- Files now live in git (this repo) so a cloud routine can reach them. ✅
- PowerShell resize rewritten in Python/Pillow. ✅
- **Connectors:** cloud routines only get the MCP servers attached to them via the routine config, pulled from claude.ai → Connectors — not from the local desktop app's MCP setup. Needs live `connector_uuid` values for `composio` (instagram / gemini / imgbb toolkits), and Gmail + Google Calendar for the races/fairs digest.
- **Cutover rule:** keep each local scheduled task running until its cloud routine has fired successfully at least once, then disable the local one — never run both against `story_layers_il` at the same time (double-post risk).
