class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for m in range(len(matrix)):
            
            if target>=matrix[m][0] and target<=matrix[m][-1]:
                return self.binarySearch(matrix[m],target)
        
        return False
    
    def binarySearch(self,arr,target):
        
        start=0
        end=len(arr)-1
        
        while(start<=end):
            mid=(start+end)//2
            
            if target==arr[mid]:
                return True
            elif target>arr[mid]:
                start=mid+1
            else:
                end=mid-1
         
        return False
            