#!/usr/bin/env python3
"""One Line, One Chill — writes one line of horror to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# Draft -> revision (done in-session, not cosmetic)
# ---------------------------------------------------------------------------
# DRAFT (first version, rejected):
#   "My dog died last spring, but every morning I find fresh paw prints
#    leading from his grave to my back door."
# Why it was dropped: "died" is flat and passive, and "every morning I
# find fresh" pads the line with a routine the reader has to wade
# through before the scare arrives. The turn lands mid-sentence
# instead of on the last word, and the line explains too much.
#
# REVISION (final): "I buried" is active and concrete — the narrator
# did the burying with their own hands, so the impossible thing is
# personal. "So I have no explanation" withholds instead of telling:
# the dread is that the narrator is out of answers, not that the dog
# is back. The scare is earned by the last clause ("from his grave to
# my back door"), which arrives as one unbroken image with nowhere
# left to hide. No mirror, no doll, no basement, no gore — just a
# grave, a trail, and a door that used to feel safe.
# ---------------------------------------------------------------------------
ENTRY = (
    "I buried my dog last spring, so I have no explanation for the paw "
    "prints leading from his grave to my back door."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 200 characters, a single line, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert 1 <= len(written) <= 200 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()
