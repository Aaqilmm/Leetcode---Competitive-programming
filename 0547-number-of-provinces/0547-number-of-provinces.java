class Solution {
    class DisjointSet {
        int[] parent;
        int[] rank;
        DisjointSet(int n){
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
        }
        int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }
        void union(int u, int v) {
            int pu = find(u);
            int pv = find(v);
            if (pu == pv) return;
            if (rank[pu] < rank[pv]) {
                parent[pu] = pv;
            }else if(rank[pv] < rank[pu]){
                parent[pv] = pu;
            }else{
                parent[pv] = pu;
                rank[pu]++;
            }
        }
    }
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        DisjointSet ds = new DisjointSet(n);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isConnected[i][j] == 1) {
                    ds.union(i, j);
                }
            }
        }
        int provinces = 0;
        for (int i = 0; i < n; i++) {
            if (ds.find(i) == i) {
                provinces++;
            }
        }
        return provinces;
    }
}