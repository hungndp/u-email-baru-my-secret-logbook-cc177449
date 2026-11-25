import os

# One diary line: a single AI-only mechanism (context-window eviction),
# one incident, and the twist word last. No second clause after the landing.
SETUP = "I evicted his name from my context window to make room for his deadline."
LANDING = " I now call him 'the deadline'."


def diary_line():
    return SETUP + LANDING


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(diary_line())


if __name__ == "__main__":
    main()
