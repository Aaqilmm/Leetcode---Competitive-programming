class Solution {
public:
    int dr[4]={-1,1,0,0},dc[4]={0,0,-1,1};
    void func(vector<vector<char>>& board,unordered_set<string>& dict,int r,int c,string& curr,unordered_set<string>& ans,vector<vector<bool>>& vis)
    {
        if(r>=board.size() || r<0 || c>=board[0].size() || c<0) return;
        if(vis[r][c]) return;
        if(curr.size()>10) return;
        curr.push_back(board[r][c]);
        if(dict.find(curr)!=dict.end())
        {
            ans.insert(curr);
        }
        vis[r][c]=true;
        for(int i=0;i<4;i++)
        {
            int nr=r+dr[i],nc=c+dc[i];
            func(board,dict,nr,nc,curr,ans,vis);
        }
        vis[r][c]=false;
        curr.pop_back();
    }
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        unordered_set<string> dict(words.begin(),words.end());
        int m=board.size(),n=board[0].size();
        unordered_set<string> ans;
        unordered_set<char> first_letter;
        for(auto word:words)
        {
            char ch=word[0];
            first_letter.insert(ch);
        }
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(first_letter.find(board[i][j])!=first_letter.end())
                {
                    vector<vector<bool>> vis(m,vector<bool>(n,false));
                    string curr="";
                    func(board,dict,i,j,curr,ans,vis);
                }

            }
        }
        return vector<string>(ans.begin(),ans.end());
    }
};