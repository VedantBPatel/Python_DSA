def distninct_substrings(s):
    substrings=set()
    n=len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            substrings.add(s[i:j])
    return substrings
    
if __name__=="__main__":
    s='abc'
    result=distninct_substrings(s)
    print("Distinct Substrings are: ",result)
    print("Total Count is:",len(result))

# Function computes all distinct substrings of a given string 's'

# Input string: s = "abc"
# Length of the string, n = 3

# Outer Loop: i iterates from 0 to n-1 (starting index of substring)

# For i = 0:
#   Inner Loop: j iterates from i+1 to n (ending index of substring, exclusive)
#   Generates substrings:
#     - s[0:1] = "a"
#     - s[0:2] = "ab"
#     - s[0:3] = "abc"
#   Adds "a", "ab", "abc" to the set

# For i = 1:
#   Inner Loop: j iterates from i+1 to n (ending index of substring, exclusive)
#   Generates substrings:
#     - s[1:2] = "b"
#     - s[1:3] = "bc"
#   Adds "b", "bc" to the set

# For i = 2:
#   Inner Loop: j iterates from i+1 to n (ending index of substring, exclusive)
#   Generates substrings:
#     - s[2:3] = "c"
#   Adds "c" to the set

# Final set of distinct substrings: {"a", "ab", "abc", "b", "bc", "c"}
# Total Count of distinct substrings = 6
