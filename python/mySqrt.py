def main():
    test1 = mySqrt(2) == 1
    test2 = mySqrt(100) == 10

    print(test1)
    print(test2)

def mySqrt(x):
    if x == 0 or x == 1:
        return x
    else:
        guess = 1
        d = ((x - (guess*guess)) // (2*guess))
        while not (guess*guess < x and (guess+1)*(guess+1)>x):
            if guess*guess == x:
                break
            guess = guess + d
            d = ((x - (guess*guess)) // (2*guess))
        return guess

if __name__ == "__main__":
    main()