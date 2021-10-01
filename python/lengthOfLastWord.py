def main():
    test1 = lengthOfLastWord("Hello World") == 5
    test2 = lengthOfLastWord("   fly me   to   the moon  ") == 4
    test3 = lengthOfLastWord("luffy is still joyboy") == 6
    test4 = lengthOfLastWord("day") == 3

    print(test1)
    print(test2)
    print(test3)
    print(test4)

def lengthOfLastWord(s):

    i = 1

    while s[-i] == " ":
        i += 1
    
    length = 1
    i += 1

    while i <=  len(s):
        print([s[-i],i])
        if s[-i] != " ":
            length += 1
            i += 1
        else: 
            return length

    return length

if __name__ == "__main__":
    main()