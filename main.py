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


def _validate_entry(text: str) -> None:
    """Validate the entry text before writing.

    The gate requires 1-280 characters, UTF-8, a single line, and
    not only whitespace. The text itself is never altered here.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 280):
        raise ValueError("entry must be 1-280 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must have no leading or trailing whitespace")
    text.encode("utf-8")


def main() -> None:
    _validate_entry(ENTRY)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
