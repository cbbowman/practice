def main():
    test1 = twoSum([2,7,11,15], 9) == [0,1]
    test2 = twoSum([2,7,14,11,42,15], 29) == [2,5]
    print(test1)
    print(test2)

def twoSum(array, target):
    for i in range(len(array)):
        if array[i] > target:
            continue
        difference = target - array[i]
        for j in range(i+1,len(array)):
            if array[j] == difference:
                return [i,j]

if __name__ == "__main__":
    main()