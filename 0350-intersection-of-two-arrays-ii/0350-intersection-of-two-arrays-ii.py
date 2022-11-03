class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        obj={}
        result=[]
        for i in nums1:
            if i in obj:
                obj[i]+=1
            else:
                obj[i]=1
        
        for i in nums2:
            if i in obj and obj[i]!=0:
                result.append(i)
                obj[i]-=1
                
        return result
        
        