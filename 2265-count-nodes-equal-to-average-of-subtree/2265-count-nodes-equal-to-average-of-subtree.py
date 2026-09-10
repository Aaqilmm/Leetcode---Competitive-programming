class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        answer = 0
        def dfs(node):
            nonlocal answer
            if node is None:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            if node.val == total_sum // total_count:
                answer += 1
            return total_sum, total_count
        dfs(root)
        return answer