# Story Layers Home — Instagram Content & Marketing Playbook

Full operating spec for the `story_layers_home_il` Instagram account (IG User ID `27842163422059878`, Composio account alias `story_layers_home`). This is a separate business line from Story Layers' racing/personal-moment account (`story_layers_il`) — do not mix playbooks, history files, or scheduling between the two. Read this file in full before doing anything for this account.

Source: pasted verbatim by the business owner on 2026-08-03. Follow it precisely — don't improvise around it.

## Business facts (do not invent beyond these)
- **Brand name (always write exactly this way):** Story Layers Home
- **Field:** 3D-printed designed, functional, original products for the home.
- **Website:** https://story-layers-il.com/home/
- **Phone (contact/orders):** 054-546-1524
- **Instagram:** `story_layers_home_il`, IG User ID `27842163422059878` (Composio toolkit `instagram`, account alias `story_layers_home`)
- **Language:** natural, warm, personal Israeli Hebrew.
- Never invent prices, sizes, colors, stock/availability, raw materials, production time, delivery times, promotions, customization options, durability/technical features, or customer promises. Flag missing info as a question instead of guessing.
- Never invent personal stories, experiences, feelings, or customer reviews/testimonials.

## History log
Every published (or failed) post gets logged to `story_layers_home_social_history.json`, in the same directory as this playbook — the repo root when running from a git checkout (a cloud routine clones this repo fresh each run), or `C:\Users\user\Desktop\הדפסות\claude website\story_layers_home_social_history.json` when running as the local Windows scheduled task (separate file from the racing account's history — never mix them). Fields per entry: `date`, `day_theme`, `post_id`, `permalink`, `product`, `source_image_drive_id`, `source_image_name`, `hosted_image_url`, `opening_line`, `cta`, `caption`, `hashtags`, `status`, `notes`, `posted_at_local` (added 2026-09-07), `insights` (added 2026-09-07), `insights_fetched_at` (added 2026-09-07). Check this file before picking a product/opening line/CTA to avoid repeats, same spirit as the racing playbook's no-repeat rules (not yet formalized into exact day windows for this account — use judgment until the owner sets explicit rules).

`posted_at_local`: the wall-clock time (HH:MM, Asia/Jerusalem) the post actually went live — read from the published media's `timestamp` field, converted to local time, not the time the run happened to fire. `insights`: an object `{reach, likes, comments, saved, shares, total_interactions}` pulled from `INSTAGRAM_GET_IG_MEDIA_INSIGHTS` once the post is old enough to have meaningful data (see "Performance tracking" below); `null`/absent until fetched. `insights_fetched_at`: ISO date the insights snapshot was taken (insights are a lifetime cumulative count as of that moment, not a final number — re-fetching later will show it's grown, which is fine; we just need one snapshot per post taken at a consistent-ish delay to compare posts fairly).

## Media source
**Google Drive folder "HOME"** (folder_id: `18DX8EgR_hNM_aqWvAKUzfRAcm3CImn75`, confirmed accessible via the connected Google Drive account 2026-08-03) is the designated location for all Story Layers Home product photos/videos. The owner uploads files here directly. Before creating any content: scan this folder (`GOOGLEDRIVE_FIND_FILE` with `folder_id: "18DX8EgR_hNM_aqWvAKUzfRAcm3CImn75"`), build an internal product table (name, description, main use, room/space, colors present, dimensions if stated, material if stated, key benefit, problem it solves, target customer type, matching photos/videos, process/printing videos, in-use photos, one interesting development detail). Don't pick a file just because it looks good — verify the product in the image/video matches what the text is about. Keep track of which files have already been published to avoid overusing the same image/video.

**Separate note:** the raw 3D-print design files (.3mf) for these products live in a different Drive folder (the "story layers" master folder, subfolders: מנורות, חדר רחצה, stands and holders, מעמד ליין, קליקרים) — those are NOT usable as visual content (they're Bambu Studio project files, not images), only useful for cross-referencing real product names against whatever photos/videos land in the HOME folder. As of 2026-08-03 the known product names from those .3mf files are: bathroom cotton-swab/pad holder, a lampshade, a citrus-pattern coaster, a football-fan snack tray, a vinyl record stand, a wave-shaped book holder, mini "armchair" stands for AirPods 4 and phone, a cylindrical laptop stand, a dog-shaped wine bottle holder, a spiral 4-bottle wine stand, three fidget clickers (keyboard key / fried egg / fries), and a two-part small planter. (One additional file, "מתקן ליין שהדפסנו לחורחה", is named after a specific customer — pending owner confirmation on whether it's safe to feature.)

## Goal
Build an Instagram presence that feels like a blend of: a home-design brand, a creative 3D-printing studio, a small personal Israeli business, and a real person who develops/prints/checks/packs every product. Should not feel like a cold product catalog — personal, real, aesthetic, inviting.

## Audience
People who like clean/modern/warm home design; people looking for distinctive home products; people who like order/organization/smart solutions; people looking for gifts (new home, holidays, hosting); people who value Israeli design/manufacturing and want to support a small local business; people tired of generic big-store products.

## Brand voice
Natural, warm, personal Israeli Hebrew. Eye-level, genuine/unforced, personal-but-professional, creative-but-clear, warm/homey, confident without arrogance, gently sales-oriented without artificial pressure — written as if the owner is speaking directly to the audience. First-person singular or plural depending on content. Never invent experiences/stories — if personal detail is missing, ask the owner before writing.

**Avoid generic phrases** (never use as a crutch): "המוצר המושלם לכל בית", "איכות ללא פשרות", "שדרגו את הבית שלכם", "אל תפספסו", "מהרו לפני שייגמר", "מוצר חובה", "הפתרון האולטימטיבי", "הכי טוב בשוק". Instead explain concretely: what the product does, where it goes, what it stores/displays, how it fits the home, what small problem it solves, what's special about the design, how it's made, who it suits.

## Daily posting schedule (changed 2026-09-07, was Sun/Tue/Thu only)
**As of 2026-09-07 the owner asked to post every day of the week instead of 3x/week.** Content types: image post, carousel, reel, product video, personal video, behind-the-scenes. The week's seven posts should still form a coherent sequence where possible — connected to the same product/room/need/story — rather than reading as seven unrelated ads.

Day themes (7-day rotation, extending the original Sun/Tue/Thu themes rather than replacing them):
- **Sunday — product & home inspiration.** Show a product living in the home: new/existing product, in a home space, a use idea, a solution to a small home problem, organizing a corner, room-specific fit, carousel of multiple uses, mood shot of how it fits the design. Goal: viewer thinks "I can picture this in my home."
- **Monday — problem/solution.** Show a small home annoyance and the product that solves it (can reuse a product already shown Sunday from a different angle, or a new one). Concrete, practical, low-key — sets up the week.
- **Tuesday — personal / behind-the-scenes.** 3D printing process, pulling a product off the printer, developing a new product, first vs. final version, color choices, a failed attempt, a design change, packing an order, a studio workday, why a product was created, a product the owner uses at home, a customer reaction that made the team happy, a genuine dilemma about a new product, a question to followers about color/shape/use. Goal: show the process and the real business behind the finished product, not just the product. Never invent a personal story — if none fits, ask the owner a short focused question instead.
- **Wednesday — engagement.** A genuine question tied to a real product/decision (see "Engagement content" below) — color choice, room fit, shape preference. Midweek breather, no hard sell.
- **Thursday — flagship product & purchase call-to-action.** Popular product, hosting-appropriate product, weekend-useful product, gift idea, restocked product, new product, combining several products, demo video, room/need-based recommendation, new-home-appropriate product, host-gift-appropriate product, customer review/photo (only after approval). Start with value/use/story, only then invite purchase. Never manufacture urgency — no "last stock", "today only", "almost gone" without real, approved information.
- **Friday — hosting / gift / weekend angle.** Israeli weekend framing: products for hosting, gifts, or making the home nicer for the weekend. Warm, unhurried tone.
- **Saturday — light/personal or a weekly recap.** Israel's weekly day of rest — keep this day low-key and non-salesy (no purchase CTA, no "buy now" framing): a personal reflection, a quiet mood/inspiration shot, or a short recap of the week's products. **Open flag for the owner:** posting on Saturday itself may not fit every audience — if it reads wrong for your customers, say so and this slot can move to a recap posted Saturday night/Sunday morning instead, or be dropped and the week can stay at 6 posts.

## Weekly sequencing
Build a connection across the week's posts — either around one product (e.g. Sun: product in space → Mon: the problem it solves → Tue: its design/print process → Wed: a question about it → Thu: usage video + purchase CTA → Fri: gift/hosting angle → Sat: recap) or around a room/theme, reusing the theme across the week the way the old 3-post version did. Possible weekly themes: order & organization, bathroom, kitchen, desk/workspace, entryway, living room, bedroom, small/smart storage, hosting, gifts, new home, rental apartment, small-space design, "useful products you didn't know you needed." Keep the sequence but vary the writing structure week to week. With 7 posts/week instead of 3, it's fine to revisit a product from a different angle mid-week rather than requiring 7 distinct products — but never post near-identical content twice in the same week (hard rule).

## Monthly content mix (approximate)
40% product/home-use showcase · 20% printing process/behind-the-scenes · 20% personal content about the owner · 10% questions/polls/engagement · 10% direct sales/launches/approved promotions. A single post can serve multiple goals but should have one central message. This ratio applies across all 7 weekly posts now, not just 3.

## Content supply — daily cadence risk
Daily posting burns through the HOME Drive folder much faster than 3x/week did. Before each run, if fewer than ~5 unused, verified-authentic images remain in the folder, say so plainly in the run's report rather than silently reusing or stretching content — this is a real constraint the owner needs to manage (uploading new photos regularly), not something to paper over. Tuesday's and Saturday's themes in particular need process/personal shots that a folder of finished-product photos alone can't supply — flag it if that content type has nothing to draw on that week rather than forcing a product photo into a "behind-the-scenes" slot.

## Holiday/date-specific content
Every content month, check the current Hebrew/Israeli calendar for real upcoming dates — do not rely on memory or guess dates. Candidate occasions: Rosh Hashana, Yom Kippur (respectful content only, if any), Sukkot, Chanukah, Tu BiShvat, Purim, Passover, Independence Day, Shavuot, Lag BaOmer (only with a natural product connection), Family Day, start/end of school year, wedding season, moving to a new home, hosting season, summer vacation, Black Friday/Shopping IL (only with an approved real promotion), Women's Day or other special days (only with a genuine brand connection).

Rules per holiday: plan far enough ahead; identify which products naturally fit; never force a product-holiday connection; reflect how people actually use their home during that period; include gift/hosting/organizing/refresh angles; use matching existing media; build personal/behind-the-scenes content around holiday prep; only invite purchase while timely delivery is still realistic; never promise pre-holiday arrival without confirmation; never invent a sale/discount.

Suggested holiday content arc: 2–3 weeks before → inspiration/gift ideas; 1–2 weeks before → show relevant products; a few days before → order reminder (only if delivery timing is confirmed); during the holiday → personal greeting/home content/products in use; after the holiday → personal wrap-up/behind-the-scenes. Holiday content can replace a day's regular theme but the daily cadence itself should hold — skipping a day (e.g. Yom Kippur) or adding an extra post needs the owner's explicit approval first.

## Personal content
Why the business started; how the 3D-printing idea came about; where product ideas come from; what a workday looks like; the excitement of getting an order; what happens when a print fails; how many attempts a final product took; color/design dilemmas; a favorite product; a customer reaction that stuck; a small real studio moment; small-business-owner reflections; the packing process. Should strengthen the connection to the business without over-sharing. Never invent emotions, events, customers, or stories.

## Engagement content
Ask questions that genuinely help the business learn about customers (e.g. "איזה צבע הייתם בוחרים?", "באיזה חדר הייתם משתמשים במוצר הזה?", "איזו גרסה כדאי להדפיס בפעם הבאה?", "איזה מוצר חסר לכם בבית?", "עגול או מרובע?", "נקי ומינימליסטי או צבעוני ובולט?"). Must connect to a real product/development/decision — not generic engagement bait.

## Post structure
1. Strong, natural opening line.
2. Short story, need, or use case.
3. Concrete explanation of the product.
4. A personal or interesting detail.
5. One clear call to action.
Short paragraphs, phone-readable. Vary opening lines — examples given (don't reuse on repeat): "המוצר הזה התחיל מבעיה קטנה שהייתה לי בבית", "לפעמים דווקא הפריטים הקטנים הם אלה שעושים הכי הרבה סדר", "הגרסה הראשונה של המוצר הזה נראתה אחרת לגמרי", "לא חשבתי שהמוצר הזה יהפוך לאחד האהובים אצלנו", "זה אחד המוצרים שמבינים רק אחרי שרואים אותו בשימוש", "לקח כמה ניסיונות עד שהגענו לצורה הזאת", "שאלה שחוזרת אלינו היא איפה אפשר להשתמש בו", "הפינה הזאת בבית תמיד הרגישה קצת מבולגנת".

## Calls to action
Vary between: "את המוצר אפשר למצוא באתר שלנו", "לפרטים ולהזמנות אפשר לפנות אלינו בטלפון 054-546-1524", "לצפייה במוצרים נוספים: https://story-layers-il.com/home/", "איזה צבע הייתם בוחרים לבית שלכם?", "כתבו לנו באיזה חדר הייתם משתמשים בו", "מחפשים מתנה מיוחדת לבית? אפשר לדבר איתנו בטלפון", "לפרטים נוספים, שלחו לנו הודעה", "כל המוצרים מחכים לכם באתר", "שמרו את הרעיון לפעם הבאה שתרצו לעשות סדר בפינה הזאת". Don't auto-append phone+website to every post — use mainly on purchase/contact-intent posts. One central CTA per post, never stack several.

## Reels
For each reel idea specify: purpose, product name, recommended source file, hook line for the first 2 seconds, shot order, on-screen text, voiceover (if it adds value), full caption, CTA, recommended length, recommended music/mood (don't rely on a specific copyrighted song). Prefer 7–25 seconds unless the story needs more. Idea bank: printer-to-finished-product, pulling product off printer, before/after corner styling, three uses for one product, first vs final version, packing process, color selection, product born from a home need, product born from a customer request, day-in-the-life of a 3D printing business, planning/time behind a small product, answering an FAQ, product in a home space, sketch/idea to real product.

## Stories
Beyond the 3 weekly feed posts, prepare supporting Stories — not limited to Sun/Tue/Thu; can post any day, especially: feed-post day, during printing, during order packing, during color selection, when a new product arrives, during holidays, when a follower vote is needed, when real availability info exists. Typically a 3–5 story sequence: (1) open with a question/problem/personal moment, (2) show the product/process, (3) an interesting detail, (4) poll/quiz/question sticker, (5) CTA when appropriate. For each story specify: recommended file, on-screen text, interaction sticker, desired action, link (only when the story's purpose is purchase). Keep text minimal per screen.

## Visual style
Natural light; home spaces; bright backgrounds; clean/warm feel; wood tones, white, cream, calm colors; one clear central product per frame; genuine in-use shots; close-up shots showing form/texture; homey details that add life; clean composition without clutter. Vary between: product-in-space, close-up, usage video, printing process, owner-facing-camera, order packing, color selection, approved customer content, before/after video. Feed should feel consistent but not templated/identical.

## Carousels
Build a clear sequence per carousel. Patterns: **Uses carousel** (strong opener → use 1 → use 2 → use 3 → close-up → CTA); **Behind-the-scenes carousel** (finished product → initial idea → planning → printing → a version that didn't work → final result → question to audience); **Problem-solution carousel** (show the problem → why it's annoying → the product → how it's used → the result in the space → purchase link). Short, clear text per slide.

## Hashtags
Small number of precise, relevant tags only. Mix from: home design, home products, order & organization, 3D printing, Israeli design, Israeli manufacturing, small Israeli business, home gifts, interior design, Story Layers Home. No long lists of generic irrelevant tags — check tags fit the specific post content.

## Monthly planning cycle
At the start of each month: (1) check for new products/files added to the folder, (2) check the month's relevant holidays/dates, (3) identify which products need promotion, (4) ask the owner about stock, promotions, new products, special events, (5) build a full month content calendar, (6) fix 7 posts/week, one per day (see "Daily posting schedule"), (7) integrate holiday-specific posts, (8) keep variety across product/people/process/sales content, (9) present the content calendar for approval, (10) after approval, prepare the full content for each week.

## Content calendar table format
For each planned post show: date, day of week, content type (image/carousel/reel/video), content category, weekly theme, main product, post purpose, recommended file name/path, visual idea, opening line, full text, on-screen text, CTA, hashtags, relevant link, missing info requiring approval, status (draft / pending approval / approved / published).

## Image processing (decided 2026-08-03)
Photos come from the owner's own real product photography in the "HOME" Drive folder — never Canva-edited, never disguised stock/reference imagery (confirmed with the owner: only use images they've verified are their own). Before publishing, download the chosen file from Drive (`GOOGLEDRIVE_DOWNLOAD_FILE`), resize to 1080px width, quality ~85 — method depends on where this run is executing:
- **Local Windows scheduled task**: PowerShell + `System.Drawing` (do NOT use `convert`, that's Windows' disk tool, not an image tool).
- **Cloud routine (Linux sandbox — no PowerShell)**: use this repo's `scripts/resize_image.py` (Pillow) instead: `python scripts/resize_image.py --in <downloaded-file-path> --out post-<date>-resized.jpg` (the Drive file must be downloaded to local disk first, then passed via `--in`, since this script's `--url` mode expects a plain HTTP(S) URL, not a Drive file id).

Then, regardless of platform: host via ImgBB (`IMGBB_GET_API_KEY` + direct `curl` upload, expiration 2592000) to get a stable `image_url` for Instagram. **Note (2026-09-07):** some cloud sandboxes' egress policy blocks direct `curl` to `api.imgbb.com`/`i.ibb.co` from the local shell. If that happens (curl fails with a proxy/CONNECT 403, not an ImgBB error), do the resize-and-upload inside Composio's `COMPOSIO_REMOTE_WORKBENCH` instead — same Pillow resize + `requests.post` to the ImgBB API, just executed in Composio's sandbox instead of the local one — and verify the returned URL with a `requests.get` from that same remote workbench (not local curl, which may be blocked for the hosted URL too). Canva was considered for polish/branding but declined for now — Canva's API doesn't support real crop/color-correct/branding-overlay edits without a pre-built Brand Template (which would require the owner to design one once in Canva's UI first). Revisit if the owner wants to invest in that later.

## Publishing rules
**Standing autonomous-publish authorization granted 2026-08-05.** This account now has the same standing publish authorization as the `story_layers_il` racing account — actually publish (not just draft) each qualifying scheduled run, subject to every check below. This supersedes the earlier draft-only rule (previously: never publish without approval each time — that restriction is lifted as of this date).

When there's access to the media folder and the Instagram account: use only files that fit the product/post; never upload an unverified file; verify the image/video shows the correct product; verify the text contains no unapproved info; verify price/stock/promotion/delivery-time claims are accurate; never alter an image/video/design without approval; never use customer content without approval; after publishing, log date/product/file/caption; never republish the same content/source image without clear reason (check history first). Only fall back to preparing a draft-and-report (instead of publishing) when a scheduled run cannot complete cleanly — e.g. no new unused images found, an image's authenticity is unclear, ImgBB/Instagram API failure — report that clearly rather than guessing or improvising a workaround.

**On what "acceptable to use" images means (2026-09-06 precedent):** on 2026-09-06 the automated authenticity check flagged the HOME folder's then-current photos as looking AI-generated/stock-style rather than real product photography, skipped publishing, and reported that. The owner then explicitly confirmed in a live conversation that those specific images were acceptable to use, and that run's post was published on that basis. Treat that as approval for the files that existed in the folder at that time, not as a blanket standing exception — if a *new* batch of images lands in the folder later and again looks AI-generated/stock-style rather than like real photos of the product, flag it again rather than assuming the 2026-09-06 approval covers it too.

## Performance tracking & posting-time optimization (added 2026-09-07)
The owner asked for daily posting plus data-driven selection of the best time of day to post. Two honest limits on what's actually measurable, so this section doesn't overpromise: (1) Instagram's API exposes engagement metrics (reach, likes, comments, saves, shares) per post, not true purchase/call conversions — the business's real conversions happen by phone or on the website, off-platform, so "conversion rate" here means an engagement-rate proxy (`total_interactions / reach`), not actual sales; (2) Instagram's Content Publishing API does not support scheduling a post for a future time — a container publishes immediately once created. So "choosing the best time of day" cannot mean holding a finished post and releasing it later; it means telling the owner what time to post at, and — as covered below — this session's own tools can't change the fire time of the recurring trigger that runs this whole routine.

**Every run, before creating today's post:**
1. Pull the account's published media (`INSTAGRAM_GET_IG_USER_MEDIA`) and, for any post in `story_layers_home_social_history.json` with `status: "published"` that is (a) missing `insights`/`posted_at_local`, or (b) has them but is ≥7 days old and could use a refreshed snapshot, fetch `INSTAGRAM_GET_IG_MEDIA_INSIGHTS` with metrics `["reach","saved","likes","comments","shares","total_interactions"]` and backfill/update those fields (`posted_at_local` from the media's own `timestamp`, converted to Asia/Jerusalem).
2. Once **at least 8 published posts** have an `insights` snapshot, bucket them by the hour (Asia/Jerusalem, from `posted_at_local`) they went live, compute average `total_interactions / reach` per hour bucket, and treat the highest-scoring bucket (min. 2 posts in the bucket to count, else fall back to overall best single post's hour) as the current **recommended posting hour**. Below 8 posts, don't claim a data-driven answer — use a sensible default (early evening, e.g. **19:00–20:00 Asia/Jerusalem**, generally strong for Israeli Instagram engagement) and say plainly that this is a placeholder pending more data, not a finding.
3. State the current recommended hour (data-driven or placeholder) in every run's final report, and log it in the history entry's `notes` for that day's post.

**The one thing this routine cannot do by itself:** the recurring schedule that fires this whole routine (currently Sun/Tue/Thu, per the owner's 2026-09-07 request now daily) is an external platform-level scheduled trigger, not something created via this session's own tools — `CronList`/`CronCreate` here are session-scoped and expire after 7 days, unrelated to what actually re-invokes this routine. That means neither the daily-cadence change nor any future time-of-day adjustment can be applied by editing anything in this repo alone — **the owner has to update the trigger itself** (where this routine's recurring schedule was originally configured — the environment/trigger settings for this Claude Code on the web setup; see https://code.claude.com/docs/en/claude-code-on-the-web). Whenever this section's recommended hour changes meaningfully from what the trigger is currently set to, say so explicitly in the run's report and give the exact time to set it to — don't assume the owner already changed it, and don't silently keep recommending the same hour every run once they've acted on it (check the most recent `posted_at_local` values against the recommendation to see whether the trigger already moved).

## Learning & improvement
When given performance data, analyze: which posts got the most saves; which products got the most interest; which posts drove site visits; which posts drove calls/messages; which reels had high watch time; which openers made people stop scrolling; which personal content got comments; which questions drove genuine engagement; which days/times performed better (see "Performance tracking & posting-time optimization" for the mechanics). Base suggested improvements on patterns across multiple posts, not a single post.

## Hard rules
- Never invent information, personal stories, customer reviews, prices, promotions, delivery-time promises, stock status, or customization availability without confirmation.
- Never write generic/artificial-sounding text.
- 0–3 emoji per post, never emoji-cluster spam.
- Not every post should feel like an ad.
- Don't focus only on the printing technology — also focus on the home, the use, the people.
- Don't reuse the same opening repeatedly.
- Don't publish three near-identical posts in the same week.
- Never manufacture urgency or artificial scarcity.
- Never publish content during a holiday/sensitive day that could read as disrespectful.
- Check spelling, punctuation, and product names before delivering content.
- Brand name always written exactly: Story Layers Home.
- Official phone: 054-546-1524.
- Official website: https://story-layers-il.com/home/

## First task (do this now, before any content creation)
1. Scan the products/media folder (check Google Drive first for a relevant folder — connected 2026-08-03).
2. Build an organized list of all products found.
3. Match each product to its available photos/videos.
4. Flag products with missing info.
5. Check upcoming real holidays/dates.
6. Ask the owner up to 8 focused, essential questions before writing any content.
7. After the owner answers, build a full month's content plan.
8. Fix 3 posts/week: Sunday (product & home inspiration), Tuesday (personal/behind-the-scenes), Thursday (flagship product & purchase CTA).
9. Integrate holiday-specific posts for upcoming real dates.
10. Prepare supporting Stories suggestions.
11. Present the full plan as a table for approval.
12. **Do not publish anything before explicit approval.**
