#Example 1
# s= "This is an example string 234"

# output =3

# s= "This is Form16 submis$ion date"
# output =3

#   your task is to do 
# has at least 3 characters
# contains only alphanumeric characters (a-z , A-Z ,0-9)
# contains at least one vowel (a, e, i, o, u) case sensitive
# contains at least one consonant (b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z) case sensitive

# def count_valid_words(s: str)-> int:
# has_vowel = False
# has_consonant = False
# vowels= "aeiouAEIOU"
# count=0
# for word in s.split():
#         if len(word)>=3 and word.isalnum():
        
#     for ch in word:
#         if ch.isalpha():
#             if ch in vowels:
#                 has_vowels=True
#             else:
#                   has_consonant = True
#                   if has_vowel and has_consonant:
#                         count += 1
#                         return count

def count_valid_words(s: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0

    for word in s.split():
        # Condition 1: length >= 3
        # Condition 2: only alphanumeric
        if len(word) >= 3 and word.isalnum():

            has_vowel = False
            has_consonant = False

            for ch in word:
                if ch.isalpha():  # consider only letters
                    if ch in vowels:
                        has_vowel = True
                    else:
                        has_consonant = True

            # Condition 3 & 4
            if has_vowel and has_consonant:
                count += 1

    return count

# Test Case 1
s1 = "This is an example string 234"
print("Output 1:", count_valid_words(s1))  # Expected: 3

# Test Case 2
s2 = "This is Form16 submis$ion date"
print("Output 2:", count_valid_words(s2))  # Expected: 3
# filtering and validation and counting approach 

