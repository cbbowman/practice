def main():
    test1 = plusOne([1,2,3]) == [1,2,4]
    test2 = plusOne([9,9,9,9,9,9,9,9]) == [1,0,0,0,0,0,0,0,0]

    print(test1)
    print(test2)

def plusOne(digits):
    i = 1
    carry = 1
    while i <= len(digits):
        if digits[-i]+carry == 10:
            carry = 1
            digits[-i] = 0
            i += 1
        else:
            carry = 0
            digits[-i] += 1
            print(digits)
            return digits
    digits.insert(0,1)
    return digits

if __name__ == "__main__":
    main()