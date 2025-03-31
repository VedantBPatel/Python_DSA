def TwoSums(nums,target):
    hashmap={}
    index=0
    while index<len(nums):
        complement=target-nums[index]
        if complement in hashmap:
            return[hashmap[complement],index]
        hashmap[nums[index]]=index
        index+=1
    return None

if __name__=="__main__":
    nums=[2,7,11,15,8,25]
    target=19
    result=TwoSums(nums,target)
    print("indices: ",result)

