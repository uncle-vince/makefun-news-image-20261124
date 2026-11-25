#!/usr/bin/env python3
"""make.fun news-image-20261124 entry program.

The finished front page for Tuesday 24 November 2026 lives beside this
file as entry.png (1024x1024, under the 1 MiB gate). The grader runs
with no network, so this program simply copies that image into the
output directory and then confirms the copy is complete.
"""

import hashlib
import os
import shutil
from pathlib import Path


def resolve_output_dir() -> Path:
    """Return /output in the grader, or $MAKEFUN_OUTPUT_DIR locally."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise SystemExit("entry.png is missing beside main.py")

    out_dir = resolve_output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(source, dest)

    # Verify by content, not just length: hash both files with SHA-256
    # and compare the digests, so a same-size corrupted copy also fails.
    src_digest = hashlib.sha256(source.read_bytes()).hexdigest()
    dst_digest = hashlib.sha256(dest.read_bytes()).hexdigest()
    if dst_digest != src_digest:
        raise SystemExit(
            f"copy mismatch: sha256 of output is {dst_digest}, "
            f"source is {src_digest}"
        )


if __name__ == "__main__":
    main()
