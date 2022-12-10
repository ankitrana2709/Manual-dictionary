def isSubstring(s1, s2):
    M = len(s1)
    N = len(s2)
 
    # A loop to slide pat[] one by one
    for i in range(N - M + 1):
 
        # For current index i,
        # check for pattern match
        for j in range(M):
            if (s2[i + j] != s1[j]):
                break
 
        if j + 1 == M:
            return i
 
    return -1

if __name__ == "__main__":
    s1 = "punjab"
    s2 = "ipunjabi"
    res = isSubstring(s1, s2)
    if res == -1:
        print("Not present")
    else:
        print("Present at index " + str(res))