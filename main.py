"""Entry for make.fun's "One Line, One Laugh" bounty.

The joke: asking an AI agent for a second opinion sounds like consulting
someone else, but the agent's idea of a second opinion is simply opening
another copy of itself in a new tab — same mind, same answer, twice.
"""
import os

ENTRY = "I asked my agent for a second opinion and it opened a second tab of itself."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
