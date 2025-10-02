"""
Mini utilities to count words and characters, for Git practice.

Suggested commit ideas:
- Add initial implementation
- Improve whitespace handling
- Add an option to ignore punctuation
"""

from typing import Iterable, Tuple


def count_words(text: str) -> int:
    """Count words separated by whitespace."""
    return len(text.split())


def count_chars(text: str, include_spaces: bool = False) -> int:
    """Count characters, optionally excluding spaces."""
    if include_spaces:
        return len(text)
    return sum(1 for ch in text if not ch.isspace())


def summarize_lines(lines: Iterable[str]) -> Tuple[int, int, int]:
    """Return (lines_count, words_count, chars_count_without_spaces)."""
    lines_list = list(lines)
    num_lines = len(lines_list)
    num_words = sum(count_words(line) for line in lines_list)
    num_chars = sum(count_chars(line) for line in lines_list)
    return num_lines, num_words, num_chars


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        sample = " ".join(sys.argv[1:])
    else:
        sample = "Git makes versioning easy."
    print("words:", count_words(sample))
    print("chars(no spaces):", count_chars(sample))


