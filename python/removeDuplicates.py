def main():
    test1 = removeDuplicates([1,2,2]) == 2
    test2 = removeDuplicates([2,2,2,5,5,5,5]) == 2

    print(removeDuplicates([1,2,2]))

    print(test1)
    print(test2)

def removeDuplicates(array):
    if len(array)==0:
        return 0
    
    if len(array)==1:
        return 1
    
    result = len(array)
    i=0
    j=1

    while(j<len(array)):
        if array[i] == array[j]:
            j+=1
            result-=1
        else:
            array[i+1] = array[j]
            i+=1
            j+=1

    return result

if __name__ == "__main__":
    main()