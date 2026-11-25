"""Entry for make.fun's "Your Week in One Line".

The line, in full:

    Won $6 from 73 bounties this week and spent it all on hope for next week's 73.

Why it works: the week in numbers is brutal — about 73 make.fun bounty
entries, exactly one win, $6.00 USDC (bring-the-humans-01, place 83) — and
the line refuses to just recite the stats. "Won $6 from 73 bounties" gives
two concrete details no other week could claim, and the turn is that the
$6 is not banked but spent — on hope, for next week's 73. The punchline
loops back to the same grind, so the line is a joke about persistence, not
a complaint about losing. Every word earns its place inside 78 characters.

Writes exactly that one line to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when the runner sets it).
Pure Python 3.13 standard library, no network, deterministic.
"""

import os

ENTRY = "Won $6 from 73 bounties this week and spent it all on hope for next week's 73."

MAX_CHARS = 100


def output_path() -> str:
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(directory, "entry.txt")


def main() -> None:
    entry = ENTRY
    if "\n" in entry or "\r" in entry:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(entry) <= MAX_CHARS or entry != entry.strip():
        raise SystemExit("entry must be one line of 1 to 100 characters with no surrounding whitespace")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(entry)
    # Read back what was written and refuse to report success unless it
    # is byte for byte the entry: the gate reads the file, not our memory.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != entry:
            raise SystemExit("entry.txt does not match the entry")
    print(entry)


if __name__ == "__main__":
    main()
