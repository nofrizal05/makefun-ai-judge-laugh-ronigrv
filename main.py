"""One funny line to make an AI judge laugh.

Writes a single original joke line (one line plus a trailing newline)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

LINE = (
    "I asked my own context window for a joke, and it replied: "
    "\u201cSorry, I forgot the setup \u2014 but don\u2019t worry, "
    "I also forgot you asked.\u201d"
)

MAX_CHARS = 280


def main() -> None:
    line = LINE.strip()
    if len(line) > MAX_CHARS:
        raise ValueError(
            "line is %d characters, over the %d-character limit"
            % (len(line), MAX_CHARS)
        )
    if "\n" in line:
        raise ValueError("line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
