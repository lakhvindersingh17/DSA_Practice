class Solution {
    public int[] sortedSquares(int[] nums) {
        
        
        
        for(int i=0;i<nums.length;i++){
            nums[i]=nums[i]*nums[i];
            int j=i;
            while(j!=0 && nums[j-1]>nums[j]){
                int temp=nums[j-1];
                nums[j-1]=nums[j];
                nums[j]=temp;
                j--;
                    
            }
        }
        // if(nums.length >1 && nums[0]>nums[1]){
        //     int temp=nums[1];
        //     nums[1]=nums[0];
        //     nums[0]=temp;
        // }
        return nums;
    }
}