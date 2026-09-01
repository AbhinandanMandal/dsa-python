# A pangram is a sentence that contains every letter of the English alphabet at least once.

def ValidPangram(string: str):
    letters = set()
    for char in string.lower():
        if char.isalpha():
            letters.add(char)
    # cause atleast every letter has to be there 1 times
    return len(letters) == 26


# print(ValidPangram("Abhinandan"))
print(ValidPangram("thequickbrownfoxjumpsoverthelazydog"))

# Time complexity: O(n), Space complexity: O(1)
