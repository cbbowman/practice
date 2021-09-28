def main():
    test1 = longestCommonPrefix(["flower","flow","flight"]) == "fl"
    test2 = longestCommonPrefix(["dog","racecar","car"]) == ""
    test3 = longestCommonPrefix([""]) == ""
    print(test1)
    print(test2)
    print(test3)

def longestCommonPrefix(strs):
    for s in strs:
        if s == "":
            return ""
    if len(strs) == 1:
        return strs[0]
    lcp = ""

    min = 200

    for s in strs:
        if len(s) < min:
            min = len(s)

    for i in range(min):
        p = strs[0][i]
        for s in strs:
            if s[i] == p:
                continue
            else:
                return lcp
        lcp += p
    return lcp


if __name__ == "__main__":
    main()