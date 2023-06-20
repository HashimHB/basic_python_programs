def RemoveElements(nums,val):
    i =0
    while(i<len(nums)):
        if(nums[i]==val):
            nums.remove(nums[i])
        else:
            i+=1
    # return(len(nums))
    return(nums)


nums = [2,3,3,2,3]
val = 3
print(RemoveElements(nums,val))

