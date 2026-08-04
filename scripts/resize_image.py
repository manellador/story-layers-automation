#!/usr/bin/env python3
"""
resize_image.py — Linux/cloud replacement for the old PowerShell + System.Drawing
resize step in the Story Layers playbook (Step 4 "Hosting the image").

Cloud routines run in a Linux sandbox, so the original Windows-only resize
(`System.Drawing`, quality ~85, 1080px width) is rewritten here with Pillow.

Usage:
    # Resize a local file:
    python resize_image.py --in downloaded.jpg --out post-2026-08-04-resized.jpg

    # Download from a URL first, then resize:
    python resize_image.py --url "https://.../signed.jpg" --out post-2026-08-04-resized.jpg

Defaults match the playbook: target width 1080px, JPEG quality 85.
Prints the final output path on success.

Dependencies: pillow (and requests only if --url is used).
    pip install pillow requests
"""
import argparse
import sys
from io import BytesIO

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is required: pip install pillow")


def load_image(in_path: str | None, url: str | None) -> Image.Image:
    if url:
        import requests
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        return Image.open(BytesIO(resp.content))
    if in_path:
        return Image.open(in_path)
    sys.exit("Provide either --in <path> or --url <url>.")


def resize(img: Image.Image, target_width: int) -> Image.Image:
    # Only downscale; never upscale a smaller source.
    if img.width <= target_width:
        return img
    ratio = target_width / float(img.width)
    target_height = int(round(img.height * ratio))
    return img.resize((target_width, target_height), Image.LANCZOS)


def main() -> None:
    p = argparse.ArgumentParser(description="Resize an image to a target width as JPEG.")
    p.add_argument("--in", dest="in_path", help="Local source image path.")
    p.add_argument("--url", dest="url", help="Remote image URL to download first.")
    p.add_argument("--out", dest="out_path", required=True, help="Output JPEG path.")
    p.add_argument("--width", type=int, default=1080, help="Target width in px (default 1080).")
    p.add_argument("--quality", type=int, default=85, help="JPEG quality (default 85).")
    args = p.parse_args()

    img = load_image(args.in_path, args.url)

    # Flatten transparency / non-RGB modes onto white so JPEG save never fails.
    if img.mode in ("RGBA", "LA", "P"):
        background = Image.new("RGB", img.size, (255, 255, 255))
        rgba = img.convert("RGBA")
        background.paste(rgba, mask=rgba.split()[-1])
        img = background
    elif img.mode != "RGB":
        img = img.convert("RGB")

    img = resize(img, args.width)
    img.save(args.out_path, "JPEG", quality=args.quality, optimize=True)
    print(args.out_path)


if __name__ == "__main__":
    main()
