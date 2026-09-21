

# A less efficient approach
"""
def AnagramSearch(text, pattern):
    text = list(text)
    patternHash = {}
    windowHash = {}
    stride = len(pattern)
    anagram_count = 0

    # We'll get pattern hash value from it
    for char in pattern:
        patternHash[char] = patternHash.get(char, 0)+1

    # We'll get window hash from it
    for i in range(len(text)):
        window = ''.join(text[i:stride+i])
        for char in window:
            windowHash[char] = windowHash.get(char, 0)+1
        if windowHash == patternHash:
            anagram_count += 1
        windowHash = {}
        i += 1
    return anagram_count


text = "BACDGABCDA"
pattern = "ABCD"
print(AnagramSearch(text, pattern))
"""


# A more efficient approach
def AnagramSearch(text, pattern):
    patternHash = {}
    windowHash = {}
    window_size = len(pattern)
    anagram_count = 0

    # For the frequency of characters in pattern
    for char in pattern:
        patternHash[char] = patternHash.get(char, 0)+1

    # For the frequency of characters in first window
    for i in range(window_size):
        char = text[i]
        windowHash[char] = windowHash.get(char, 0)+1

    # Sliding the window
    for i in range(window_size, len(text)):  # From 4th to len(text)
        # First check if window hash and pattern hash are same or not
        if windowHash == patternHash:
            anagram_count += 1

        # Leaving character
        outgoing = text[i-window_size]
        windowHash[outgoing] -= 1

        if windowHash[outgoing] == 0:
            del windowHash[outgoing]

        # Incoming character
        incoming = text[i]
        windowHash[incoming] = windowHash.get(incoming, 0)+1

    # At final
    if windowHash == patternHash:
        anagram_count += 1
    return anagram_count


text = "BACDGABCDA"
pattern = "ABCD"
print(AnagramSearch(text, pattern))
# Time complexityL O(n)
# Space complexity: O(k), k is number of distinct characters
