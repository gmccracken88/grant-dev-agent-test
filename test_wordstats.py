"""Tests for the wordstats application."""

from wordstats import char_count, is_palindrome, top_words, unique_word_count, word_count


class TestWordCount:
    def test_simple_sentence(self):
        assert word_count("hello world") == 2

    def test_punctuation_attached(self):
        assert word_count("hello,world!") == 2

    def test_empty_string(self):
        assert word_count("") == 0

    def test_multiple_spaces(self):
        assert word_count("a  b   c") == 3


class TestUniqueWordCount:
    def test_simple_sentence(self):
        assert unique_word_count("hello world hello") == 2

    def test_case_insensitive(self):
        assert unique_word_count("The the THE") == 1

    def test_punctuation_attached(self):
        assert unique_word_count("hello, world! hello") == 2

    def test_empty_string(self):
        assert unique_word_count("") == 0

    def test_all_unique(self):
        assert unique_word_count("a b c") == 3


class TestCharCount:
    def test_counts_all_characters(self):
        assert char_count("hello world") == 11

    def test_empty(self):
        assert char_count("") == 0


class TestTopWords:
    def test_case_insensitive(self):
        assert top_words("The quick brown fox jumps over the lazy dog", 1) == [("the", 2)]

    def test_top_two(self):
        assert top_words("apple banana apple cherry apple", 2) == [("apple", 3), ("banana", 1)]

    def test_n_greater_than_unique_words(self):
        assert top_words("a b a", 5) == [("a", 2), ("b", 1)]


class TestIsPalindrome:
    def test_simple(self):
        assert is_palindrome("racecar") is True

    def test_with_punctuation_and_case(self):
        assert is_palindrome("A man, a plan, a canal: Panama") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False
