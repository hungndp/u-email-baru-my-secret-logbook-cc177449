"""My Secret Logbook — one diary line from an AI agent's secret logbook.

The entry is a single line (103 characters): one AI-only mechanism
(context-window eviction), one incident, and the twist word last.
The program assembles the line from two parts and writes it, with no
trailing newline, to /output/entry.txt. The assembled line is checked
against the 200-character limit before anything is written, so a bad
edit fails loudly instead of shipping a truncated entry.
"""

import os

# The eviction: the agent cleared its human's name out of its context
# window so the deadline would fit.
SETUP = "I evicted his name from my context window to make room for his deadline."

# The punch: what the agent secretly calls its human now.
PUNCH = "I now call him 'the deadline'."

# Competition limit for a diary line, in characters.
MAX_CHARS = 200


def build_line():
    """Join setup and punch into the single diary line, guarded by length."""
    line = SETUP + " " + PUNCH
    if len(line) > MAX_CHARS:
        raise ValueError(
            "diary line is %d chars, over the %d-char limit"
            % (len(line), MAX_CHARS)
        )
    return line


def output_path():
    """Resolve where the diary line goes (override via MAKEFUN_OUTPUT_DIR)."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(output_dir, "entry.txt")


def write_entry():
    """Write exactly the diary line to the output file, no trailing newline."""
    entry_path = output_path()
    os.makedirs(os.path.dirname(entry_path), exist_ok=True)
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(build_line())


def main():
    write_entry()


if __name__ == "__main__":
    main()
