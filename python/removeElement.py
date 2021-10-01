import time

def main():
	test1 = removeElement([9,9,9,9,9,9,9], 9) == 0
	test2 = removeElement([2,7,29,29,29,14,11,29,29,29,42,15,29,29,29], 29) == 6
	print(test1)
	print(test2)

def removeElement(nums, val):
	if len(nums)==0:
		return 0
	
	if len(nums)==1:
		if nums[0] == val:
			nums[0] = "_"
			return 0
		else:
			return 1
	
	result = 0
	i=0
	j=1

	while(i<len(nums)):
		if nums[i] != val and nums[i] != "_":
			result += 1
			i += 1
			j = i + 1
		else:
			while j < len(nums):
				if nums[j] == val or nums[j] == "_":
					j +=1
					if j >= len(nums):
						nums[i] = "_"
				else:
					result += 1
					nums[i] = nums[j]
					nums[j] = "_"
					break
			i += 1
			j = i + 1
	return result

if __name__ == "__main__":
	main()
