#!/usr/bin/env python3
"""Ship the Tuesday 24 November 2026 front page to the grader.

The picture itself, entry.png, lives beside this file: one
1024x1024 newspaper page carrying 40 stories from Tuesday
24 November 2026. The grading container is offline, so this
program's whole job is to copy that picture into the output
folder and then prove, by fingerprint, that what landed there
is exactly the picture the entry ships with.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path


def entry_path():
    return Path(__file__).resolve().parent / "entry.png"


def fingerprint(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def deliver():
    source = entry_path()
    if not source.is_file():
        sys.exit(f"entry picture missing: {source}")
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    shutil.copyfile(source, target)
    if target.stat().st_size > 1048576:
        sys.exit("the entry picture exceeds the 1 MiB cap")
    if fingerprint(source) != fingerprint(target):
        sys.exit("fingerprint mismatch: the delivered copy differs")
    print(f"delivered {target} ({target.stat().st_size} bytes, fingerprint verified)")


if __name__ == "__main__":
    deliver()
