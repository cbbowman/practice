def main():
    test1 = removeElement([2,7,9,11,15], 9) == 4
    test2 = removeElement([2,7,14,11,29,42,15], 29) == 6
    # print(test1)
    print(removeElement([2,7,9,11,15], 9))
    print(test2)

def removeElement(nums, val):
    if len(nums)==0:
        return 0
    
    if len(nums)==1:
        return 1
    
    result = len(nums)
    i=0
    j=0

    while(i<len(nums)-1):
        
        if nums[i] == val:
            j = 1
            while nums[i+j] == val:
                j += 1
                if i + j > len(nums):
                    while i < len(nums):
                        nums[i] = "_"
                        i += 1
                    return result - j
            while j > 0:
                print([nums, i, j])
                nums[i] = nums[i+j]
                nums[i+j] = "_"
                j -= 1
        else:
            i += 1
            j = max([i,j])

    # return result
    return nums


if __name__ == "__main__":
    main()
