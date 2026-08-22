class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        Stack<Integer> stack = new Stack<>();
        int max = 0;
        for(int i=0; i<n; i++){
            while(!stack.isEmpty() && heights[i] < heights[stack.peek()] ){
                int height = heights[stack.pop()];
                int nextSmall = i;
                int prevSmall = stack.isEmpty()?-1:stack.peek();
                int width = nextSmall - prevSmall-1;
                max = Math.max(max , height*width);
            }
            stack.push(i);
        }
        while(!stack.isEmpty()){
            int height = heights[stack.pop()];
            int nextSmall = n;
            int prevSmall = stack.isEmpty()?-1:stack.peek();
            int width = nextSmall - prevSmall-1;
            max = Math.max(max,height*width);
        }
        return max;
    }
}