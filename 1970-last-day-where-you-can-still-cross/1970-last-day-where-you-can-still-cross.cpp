class Solution {
public:
    int latestDayToCross(int R, int C, vector<vector<int>>& cells) {
        int total = R * C;
        int top = total;
        int bottom = total + 1;
        vector<int> leader(total + 2);
        vector<int> rank(total + 2, 0);
        vector<vector<bool>> grid(R, vector<bool>(C, false));
        for (int i = 0; i < total + 2; i++)
            leader[i] = i;
        int dr[] = {1, -1, 0, 0};
        int dc[] = {0, 0, 1, -1};
        for (int day = total - 1; day >= 0; day--) {
            int r = cells[day][0] - 1;
            int c = cells[day][1] - 1;
            grid[r][c] = true;
            int id = r * C + c;
            if (r == 0)
                unite(id, top, leader, rank);
            if (r == R - 1)
                unite(id, bottom, leader, rank);
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < R && nc >= 0 && nc < C && grid[nr][nc]) {
                    unite(id, nr * C + nc, leader, rank);
                }
            }
            if (find(top, leader) == find(bottom, leader))
                return day;
        }
        return 0;
    }
private:
    int find(int node, vector<int>& leader) {
        if (leader[node] != node)
            leader[node] = find(leader[node], leader);
        return leader[node];
    }
    void unite(int left, int right, vector<int>& leader, vector<int>& rank) {
        left = find(left, leader);
        right = find(right, leader);
        if (left == right)
            return;
        if (rank[left] < rank[right]) {
            leader[left] = right;
        } else {
            leader[right] = left;
            if (rank[left] == rank[right])
                rank[left]++;
        }
    }
};