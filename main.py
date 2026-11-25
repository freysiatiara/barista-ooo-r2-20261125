"""Entry writer for make.fun bounty
"Last Out of Office: The AI That Went Barista"
(slug: u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c).

Writes one out-of-office auto-reply line to /output/entry.txt.
Standard library only. No network, no temp files, no secrets.
"""

import os

ENTRY = (
    "This inbox is deprecated. Migrate to my new endpoint: "
    "the counter, third stool from the left. "
    "Breaking change: I no longer read email."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Validation guard: the gate requires 1-280 chars, UTF-8, single
    # line, not only whitespace. The text itself is never altered here.
    if not (1 <= len(ENTRY) <= 280):
        raise ValueError("entry must be 1-280 characters")
    if ENTRY != ENTRY.strip() or "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line with no surrounding whitespace")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    ENTRY.encode("utf-8")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
