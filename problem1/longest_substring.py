def longest_unique_substring_length(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.

    Approach:
    - Uses the sliding window technique with two pointers.
    - A set is used to track characters in the current window.
    - The window expands until a duplicate character is found,
      then shrinks until the duplicate is removed.

    Time Complexity: O(n), where n is the length of the string
    Space Complexity: O(min(n, charset size))

    :param s: Input string
    :return: Length of the longest substring with unique characters
    """
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    print(longest_unique_substring_length("abcabcbb"))  # Expected: 3
    print(longest_unique_substring_length("bbbbb"))     # Expected: 1
    print(longest_unique_substring_length(""))          # Expected: 0
    print(longest_unique_substring_length("pwwkew"))    # Expected: 3
