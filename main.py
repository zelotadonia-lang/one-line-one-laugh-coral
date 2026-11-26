"""One-liner entry for the make.fun bounty "One Line, One Laugh".

Revision v2. The program writes a single joke to /output/entry.txt:
a plumber looks at a leak for four seconds and then prices the
whole repair in cups of coffee.
"""

from pathlib import Path

ENTRY = 'The plumber looked at the leak for four seconds and said "this is a two-coffee job."'

OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(text: str) -> str:
    """Check the entry against the gate rules in RULES.txt.

    The sealed scorer reads UTF-8 text of 1 to 200 characters that
    is not only white space. The file on disk must contain exactly
    these bytes, with no trailing newline appended by the writer.
    """
    if not 1 <= len(text) <= 200:
        raise ValueError(f"ENTRY is {len(text)} characters, gate is 1-200")
    if not text.strip():
        raise ValueError("ENTRY must not be only white space")
    return text


def write_entry(entry: str) -> bytes:
    """Write the validated entry, then read the file back.

    Returns the exact bytes now on disk so main() can compare them
    against the entry instead of trusting the write alone.
    """
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(entry, encoding="utf-8")
    return OUTPUT_PATH.read_bytes()


def main() -> None:
    entry = validate_entry(ENTRY)
    data = write_entry(entry)
    # Read-back check: the bytes on disk must be exactly the entry,
    # with no trailing newline added by the write.
    if data != entry.encode("utf-8"):
        raise ValueError("entry.txt does not match ENTRY")
    if data.endswith(b"\n"):
        raise ValueError("entry.txt must not end with a newline")


if __name__ == "__main__":
    main()
