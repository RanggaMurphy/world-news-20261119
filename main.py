#!/usr/bin/env python3
"""Entry for make.fun's news-image-20261119 — "Sum up 19 November's world news in one image".

The image beside this file (entry.png) is a one-page broadsheet of Thursday
19 November 2026: the first Trump–Xi–Putin three-way summit in Shenzhen, the
third attack in a week on the Crimea Bridge, the worldwide launch of Grand
Theft Auto VI, Israeli tanks crossing Gaza's ceasefire line, Cyclone Akvan
bearing down on India's east coast, Hakeem Jeffries' historic nomination for
Speaker, the EU's proposed €45 billion loan for Ukraine, gold's slump to a
14-month low, and Pew's projection that Islam becomes the world's largest
religion by 2035. It was designed and rendered from frontpage.html in this
repository.

The program's whole job is to copy that image to the output directory as
entry.png — byte for byte, so two runs always write identical bytes and no
network is needed.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / "entry.png"
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()
