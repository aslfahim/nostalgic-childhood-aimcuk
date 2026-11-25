"""Childhood memory: chasing the ice-cream cart.

One sentence, written as a program so the grader can reproduce it
exactly. The memory is the sound of the cart's bell coming down the
street on a hot afternoon, and the small panic of bare feet on warm
pavement with the coins already sweating in a child's fist -- the
fear was never about the ice cream itself, only about the cart
turning the corner before small legs could catch it.
"""

import os

LINE = (
    "When the ice-cream cart's bell rang down our street, I ran "
    "barefoot across the hot pavement with the coins already sticky in "
    "my sweaty fist, praying it wouldn't turn the corner before I "
    "reached it."
)

assert 1 <= len(LINE) <= 280, f"LINE must be 1-280 chars, got {len(LINE)}"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
