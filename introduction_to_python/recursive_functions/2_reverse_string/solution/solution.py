def reverse(string):
    if not string:
        return string 
    if len(string) == 1:
        return string
    return reverse(string[-1]) + reverse(string[:-1])