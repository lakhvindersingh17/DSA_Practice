# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        start=0
        end=n
        badVersion=n
        
        while(start<=end):
            mid=(start+end)//2
            
            if(isBadVersion(mid)):
                end=mid-1
                badVersion=mid
            else:
                start=mid+1
                
        return badVersion        
        