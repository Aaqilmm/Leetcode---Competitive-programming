class Solution{
    public List<List<Integer>> fourSum(int[] nums, int target){
        Set<List<Integer>> set = new HashSet<>();
        int n = nums.length;
        Arrays.sort(nums);
        if(n<4) 
        return new ArrayList<>(set);  
        for(int i=0;i<n-3;i++){
            for(int j=i+1;j<n-2;j++){
                int left=j+1;
                int right=n-1;
                while(left<right){
                    long sum = (long) nums[i] + (long) nums[j] + (long) nums[left] + (long) nums[right];
                    if(sum==target){
                        set.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        left++;
                        right--;
                    }
                    else if(sum>target)
                    right--;
                    if(sum<target)
                    left++;
                }
            }
        }
        return new ArrayList<>(set);    
    }
}