class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroPos=-1
        
        for i in range(len(nums)):
            if nums[i]==0:
                if(zeroPos==-1):
                    zeroPos=i
            
            elif(zeroPos!=-1):
                nums[zeroPos],nums[i]=nums[i],0
                zeroPos+=1
        