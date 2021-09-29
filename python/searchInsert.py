def main():
    test1 = searchInsert([2,7,9,11,15], 9) == 2
    test2 = searchInsert([2,7,11,29,42], 29) == 3
    test3 = searchInsert([2,7,11,12,28], 29) == 5
    # print(test1)
    print(test1)
    print(test2)
    print(test3)

def searchInsert(nums, val):
    if len(nums)==0:
        return 0

    for i in range(len(nums)):
        if nums[i] >= val:
            return i

    return len(nums)


if __name__ == "__main__":
    main()
