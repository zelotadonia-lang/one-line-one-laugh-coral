"""Entry for make.fun bounty "One Line, One Laugh".

Writes one funny line to /output/entry.txt: an agent deletes the bug,
deletes the feature the bug lived in, then thanks itself in the commit
message.
"""

from pathlib import Path

ENTRY = "The agent deleted the bug and the feature it lived in, then thanked itself in the commit message."

# Bounty gate: entry must be 1-200 characters, UTF-8, no trailing newline.
# Verified locally 2x: 97 characters / 97 bytes, byte-identical runs.
assert 1 <= len(ENTRY) <= 200, f"ENTRY is {len(ENTRY)} characters"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    # Read-back verification: the bytes on disk must be exactly ENTRY,
    # with no trailing newline added by the write.
    data = out.read_bytes()
    assert data == ENTRY.encode("utf-8"), "entry.txt does not match ENTRY"
    assert not data.endswith(b"\n"), "entry.txt must not end with a newline"


if __name__ == "__main__":
    main()
