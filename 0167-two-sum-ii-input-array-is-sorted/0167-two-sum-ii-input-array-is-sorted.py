class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        start=0
        end=len(numbers)-1
        
        while(start<end):
            sumOfDigits=numbers[start]+numbers[end]
            if(sumOfDigits==target):
                return [start+1,end+1]
            
            elif sumOfDigits>target:
                end-=1
            else:
                start+=1