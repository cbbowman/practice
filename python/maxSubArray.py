import time

def main():
    test1 = maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    test2 = maxSubArray([3,-3,2,-3]) == 3
    test3 = maxSubArray([-1,-2,3,-1,-2,1,1]) == 3

    print(test1)
    print(test2)
    print(test3)

def maxSubArray(nums):

    if nums == []:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    i = 0
    j = 0
    sum = nums[i]
    max_sum = sum

    while i < len(nums):
        if nums[i] <= 0:
            if max_sum > sum:
                i += 1
                continue

            if nums[i] > sum:
                sum = nums[i]
                max_sum = sum

            i += 1

        else:
            sum = nums[i]
            j = 1
            if i+j >= len(nums):
                if sum > max_sum:
                    max_sum = sum
                return max_sum
            while nums[i+j] >= 0:
                sum += nums[i+j]
                if sum > max_sum:
                    max_sum = sum
                j += 1
                if i+j >= len(nums):
                    return max_sum
            
            if sum > max_sum:
                max_sum = sum

            while sum > 0:
                time.sleep(1)
                print([i,j,sum,max_sum,nums])
                sum += nums[i+j]
                if sum > max_sum:
                    max_sum = sum
                j += 1
                if i+j >= len(nums):
                    return max_sum
            
            i += 1
            
    return max_sum


if __name__ == "__main__":
    main()