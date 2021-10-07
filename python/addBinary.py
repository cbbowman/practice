def main():
    test1 = addBinary("1010", "1011") == "10101"
    test2 = addBinary("1", "11") == "100"

    print(test1)
    print(test2)

def addBinary(a, b):
        i = 1
        carry = 0
        
        len_a = len(a)
        len_b = len(b)
        c = ""
        
        while i <= len_a and i <= len_b:
            sum = carry + int(a[-i]) + int(b[-i])
            if sum > 1:
                carry = 1
                c = str(sum - 2) + c
            else:
                carry = 0
                c = str(sum) + c
            i += 1
                
        if i > len_a:
            longer = b
            m = len_b
        else:
            longer = a
            m = len_a
        
        while i <= m:
            sum = carry + int(longer[-i])
            if sum > 1:
                carry = 1
                c = str(sum - 2) + c
            else:
                carry = 0
                c = str(sum) + c
            i += 1
        
        if carry == 1:
            c = str(1) + c
        
        return c

if __name__ == "__main__":
    main()