
def longest_substring(s: str) -> int:
    if len(s) == 1:
        return 1 
    result = 0
    len_temp = 1
    for i in range(0, len(s)):
        if s[i] != s[i +1]:
            len_temp = len_temp + 1 
    if len_temp > result:
        result == len_temp
    return result
            
print(longest_substring("lobal"))
