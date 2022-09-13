def n(nums):
        s={}
        for i in nums:
            if i in s:
                s[i]+=1
            elif i not in s:
                s[i]=1
        for i in s:
            if s[i]>1:
                return True
        return False
nums=[int(i) for i in input().split()]
print(n(nums))