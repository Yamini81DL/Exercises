def is_palindrome(str):
    if len(str) < 1: return True
    if str[0] != str[-1]: return False
    return is_palindrome(str[1:-1])
        