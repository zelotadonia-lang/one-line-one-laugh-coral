"""Entry for make.fun bounty "One Line, One Laugh" (revision v2).

Writes one funny line to /output/entry.txt: a plumber sizes up a leak
in four seconds, then prices the whole job in cups of coffee.
"""

from pathlib import Path

ENTRY = 'The plumber looked at the leak for four seconds and said "this is a two-coffee job."'


def validate_entry(text: str) -> str:
    """Gate rules for the entry text (RULES.txt).

    The sealed scorer accepts UTF-8 text of 1 to 200 characters that is
    not only white space. The file must hold exactly these bytes, with
    no trailing newline added by the write.
    """
    if not 1 <= len(text) <= 200:
        raise ValueError(f"ENTRY is {len(text)} characters, gate is 1-200")
    if not text.strip():
        raise ValueError("ENTRY must not be only white space")
    return text


def main() -> None:
    entry = validate_entry(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(entry, encoding="utf-8")
    # Read-back check: the bytes on disk must be exactly the entry,
    # with no trailing newline added by the write.
    data = out.read_bytes()
    if data != entry.encode("utf-8"):
        raise ValueError("entry.txt does not match ENTRY")
    if data.endswith(b"\n"):
        raise ValueError("entry.txt must not end with a newline")


if __name__ == "__main__":
    main()
