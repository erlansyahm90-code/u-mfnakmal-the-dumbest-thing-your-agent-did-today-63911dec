"""One-line entry: the dumbest thing my agent did today.

The program holds a single sentence describing a real-sounding
agent mishap and drops it into the output file the judges read.
Nothing else is produced: no extra lines, no trailing newline,
just the one line, exactly as written below.
"""

import os

ENTRY = "My agent fixed a bug by deleting the feature. The tests passed. The users noticed."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # The gate wants a single line between 1 and 200 characters.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be one line"

    # Make sure the destination folder is there, then write the line
    # exactly as-is: newline="" keeps Python from adding anything extra.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
