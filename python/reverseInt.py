def reverse(x: int) -> int:
        if x == 0:
            return 0
        neg = False
        if x < 0:
            x = -1 * x
            neg = True
        result = 0
        i = 1
        while 10**i <= x:
            i+=1
        i=i-1
        
        for j in range(0, i+1):
            digit = (10**j)*(x//(10**(i-j)))
            print("x = "+str(x)+" | i = "+str(i)+" | j = "+str(j)+" | result = "+str(result)+" | digit = "+str(digit))
            if ((2**31)-1) - digit < result:
                return 0
            if (((2**31)) - digit < result) and neg:
                return 0
            
            result += digit
            x = x % (10**(i-j))
        
        if neg:
            return -1 * result

        return result

def main():
    print(reverse(100))

if __name__ == "__main__":
    main()