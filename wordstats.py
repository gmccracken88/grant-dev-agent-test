"""Small text statistics application."""

import re
from collections import Counter

_WORD_RE = re.compile(r"[a-zA-Z]+")


def word_count(text: str) -> int:
    """Count the number of words in text (words are letter runs)."""
    return len(_WORD_RE.findall(text))


def unique_word_count(text: str) -> int:
    """Count the number of distinct words in text (case-insensitive)."""
    return len({w.lower() for w in _WORD_RE.findall(text)})


def char_count(text: str) -> int:
    """Count all characters, including whitespace and punctuation."""
    return len(text)


def top_words(text: str, n: int = 3) -> list[tuple[str, int]]:
    """Return the n most common words as (word, count) pairs, case-insensitive."""
    words = [w.lower() for w in _WORD_RE.findall(text)]
    return Counter(words).most_common(n)


def is_palindrome(text: str) -> bool:
    """Return True if text is a palindrome (letters only, case-insensitive)."""
    letters = [c.lower() for c in text if c.isalpha()]
    return letters == letters[::-1]
