"""One-Line Laugh-Off entry.

Writes exactly one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
with no trailing newline, via an atomic temp-file + os.replace write.
"""

import os

LINE = (
    "My AI agent charged me $0.47 to write a function that returns zero "
    "— then billed another $0.12 for the confidence."
)


def main() -> None:
    # The brief requires exactly one line of 1-200 characters.
    if not (1 <= len(LINE) <= 200):
        raise ValueError(f"line must be 1-200 chars, got {len(LINE)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
