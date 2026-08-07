#!/usr/bin/env python3
"""Crop a captured screenshot to a region and save it into the docs image tree.

Reusable docs-screenshot helper (the repeatable half of the hybrid capture harness).
Usage:
    python3 tools/shots/crop.py RAW.png content/images/<area>/<name>.png --box L,T,R,B
The box is left,top,right,bottom in pixels of the raw capture. Eyeball the result after.
"""
import argparse
from PIL import Image


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--box", required=True, help="left,top,right,bottom (pixels)")
    a = ap.parse_args()
    box = tuple(int(x) for x in a.box.split(","))
    if len(box) != 4:
        raise SystemExit("--box must be left,top,right,bottom")
    im = Image.open(a.src).crop(box)
    im.save(a.dst)
    print(f"saved {a.dst} {im.size}")


if __name__ == "__main__":
    main()
