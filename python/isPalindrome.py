def isPalindrome(x: int) -> bool:
        num = x
        if x == 0:
            return True
        neg = False
        if x < 0:
            return False
        result = 0
        i = 1
        while 10**i <= x:
            i+=1
        i=i-1
        
        for j in range(0, i+1):
            digit = (10**j)*(x//(10**(i-j)))
            if ((2**31)-1) - digit < result:
                return 0
            if (((2**31)) - digit < result) and neg:
                return 0
            
            result += digit
            x = x % (10**(i-j))
        
        if neg:
            return -1 * result

        return num == result

def main():
    print(isPalindrome(0))

if __name__ == "__main__":
    main()