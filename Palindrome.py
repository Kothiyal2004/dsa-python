#Making an Program to check if the given string is a palindrome or not
def is_palindrome(s: str) -> bool:
    #
    cleaned_s = s.replace(" ", "").lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]
# Test Cases
print(is_palindrome("A man a plan a canal Panama"))  # Expected: True
print(is_palindrome("Hello World"))  # Expected: False
print(is_palindrome("naman"))  # Expected: True




def reverse(s:int) -> int:
    pass

