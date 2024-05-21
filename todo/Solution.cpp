#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#include <sstream>
#include <queue>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <string>
#include <cmath>
#include <numeric>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <bitset>
#include <functional>
#include <iterator>
#include <utility>
#include <array>
#include <regex>
#include <random>
#include <chrono>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <future>
#include <atomic>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#include <climits>
#include <cfloat>
#include <ciso646>
#include <cstddef>
#include <cinttypes>
#include <cstdarg>
#include <cwchar>
#include <cwctype>
#include <limits>
#include <exception>
#include <stdexcept>
#include <new>
#include <typeinfo>
#include <initializer_list>
#include <tuple>
#include <scoped_allocator>
#include <memory>
#include <memory_resource>
#include <climits>
#include <cfloat>
#include <cstdint>
#include <cstddef>



using namespace std;

// class Solution {
// public:
//     int sumNumbers(TreeNode* root)
//     {
//         std::vector<std::string> stack;
//         return dfs(root, stack);
//     }

//     int dfs(TreeNode* root, std::vector<std::string>& stack) {
//         if (!root) return 0;
//         stack.push_back(std::to_string(root->val));
//         int count = 0;
//         if (!root->left && !root->right) {
//             std::stringstream ss;
//             for(const auto& s: stack) {
//                 ss << s;
//             }
//             count = std::stoi(ss.str());
//         }
//         count += dfs(root->left, stack);
//         count += dfs(root->right, stack);
//         stack.pop_back();
//         return count;
//     }
// };

class Solution {
    public:
        TreeNode* addOneRow(TreeNode* root, int val, int depth) {
            if (depth == 1) return new TreeNode(val, root, nullptr);
            vector<TreeNode*> layer { root };
            for (int i = 2; i < depth; i++) {
                vector<TreeNode*> nextLayer;
                for (TreeNode* node: layer) {
                    if (node->left) nextLayer.push_back(node->left);
                    if (node->right) nextLayer.push_back(node->right);
                }
                swap(layer, nextLayer);
            }
            for (TreeNode* node: layer) {
                node->left = new TreeNode(val, node->left, nullptr);
                node->right = new TreeNode(val, nullptr, node->right);
            }
            return root;
        }
};

class Solution
{
public:
    string smallestFromLeaf(TreeNode *root)
    {
        string res = "";
        dfs(root, "", res);
        return res;
    }
    void dfs(TreeNode *root, string path, string &res)
    {
        if (!root)
            return;
        path = char('a' + root->val) + path;
        if (!root->left && !root->right)
        {
            if (res == "")
                res = path;
            else
                res = min(res, path);
        }
        dfs(root->left, path, res);
        dfs(root->right, path, res);
    }
};

class Solution
{
public:
    int islandPerimeter(vector<vector<int>> &grid)
    {
        int m = grid.size(), n = grid[0].size(), res = 0;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == 1)
                {
                    if (i == 0 || grid[i - 1][j] == 0)
                        res++;
                    if (i == m - 1 || grid[i + 1][j] == 0)
                        res++;
                    if (j == 0 || grid[i][j - 1] == 0)
                        res++;
                    if (j == n - 1 || grid[i][j + 1] == 0)
                        res++;
                }
            }
        }
        return res;
    }
};

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size(), res = 0;
        int islands = 0;
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (grid[row][col] == '1') {
                    islands++;
                    dfs(grid, row, col);
                }
            }
        }
        return islands;
    }
    void dfs(vector<vector<char>>& grid, int row, int col) {
        if (row < 0 || col < 0 || row >= grid.size() || col >= grid[0].size() || grid[row][col] == '0') {
            return;
        }
        grid[row][col] = '0';
        dfs(grid, row + 1, col);
        dfs(grid, row - 1, col);
        dfs(grid, row, col + 1);
        dfs(grid, row, col - 1);
    }
};

class Solution
{
public:
    vector<vector<int>> findFarmland(vector<vector<int>> &land)
    {
        vector<vector<int>> res;
        int m = land.size(), n = land[0].size();
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (land[i][j] == 1)
                {
                    int x = i, y = j;
                    while (x < m && land[x][j] == 1)
                        x++;
                    while (y < n && land[i][y] == 1)
                        y++;
                    for (int a = i; a < x; a++)
                    {
                        for (int b = j; b < y; b++)
                        {
                            land[a][b] = 0;
                        }
                    }
                    res.push_back({i, j, x - 1, y - 1});
                }
            }
        }
        return res;
    }
};

class Solution
{
public:
    int openLock(vector<string> &deadends, string target)
    {
        unordered_set<string> dead(deadends.begin(), deadends.end());
        if (dead.count("0000")) return -1;
        if (target == "0000") return 0;
        queue<string> q;
        q.push("0000");
        int res = 0;
        while (!q.empty())
        {
            res++;
            int size = q.size();
            for (int i = 0; i < size; i++)
            {
                string t = q.front();
                q.pop();
                for (int j = 0; j < 4; j++)
                {
                    for (int k = -1; k <= 1; k += 2)
                    {
                        string s = t;
                        s[j] = (s[j] - '0' + k + 10) % 10 + '0';
                        if (s == target)
                            return res;
                        if (!dead.count(s))
                        {
                            q.push(s);
                            dead.insert(s);
                        }
                    }
                }
            }
        }
        return -1;
    }
};

class Solution
{
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>> &edges)
    {
        if (n == 1) return {0};
        vector<unordered_set<int>> adj(n);
        for (auto &e : edges)
        {
            adj[e[0]].insert(e[1]);
            adj[e[1]].insert(e[0]);
        }
        queue<int> q;
        for (int i = 0; i < n; i++)
        {
            if (adj[i].size() == 1) q.push(i);
        }
        while (n > 2)
        {
            int size = q.size();
            n -= size;
            for (int i = 0; i < size; i++)
            {
                int t = q.front();
                q.pop();
                for (int a : adj[t])
                {
                    adj[a].erase(t);
                    if (adj[a].size() == 1) q.push(a);
                }
            }
        }
        vector<int> res;
        while (!q.empty())
        {
            res.push_back(q.front());
            q.pop();
        }
        return res;
    }
};

class Solution
{
public:
    int tribonacci(int n)
    {
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;
        int a = 0, b = 1, c = 1, d;
        for (int i = 3; i <= n; i++)
        {
            d = a + b + c;
            a = b;
            b = c;
            c = d;
        }
        return c;
    }
};

class Solution {
public:
    int tribonacci(int n) {
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;
        vector<int> dp(n + 1);
        dp[1] = dp[2] = 1;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
        }
        return dp[n];
    }
};


class Solution {
public:
    int longestIdealString(string s, int k) {
        vector<int> dp(26);
        for (char c : s) {
            int l = 0, ci = c - 'a';
            for (int p = 0; p < 26; p++) {
                if (abs(ci - p) <= k) l = max(l, dp[p] + 1);
            }
            dp[ci] = l;
        }
        return *max_element(dp.begin(), dp.end());
    }
};

class Solution
{
public:
    int minFallingPathSum(vector<vector<int>> &grid)
    {
        int n = grid.size(), ans = 5e6;
        /*
        This is a bottom-up approach, in which we start
        from the second last row and move upwards
        */
        vector<vector<int>> dp(2, vector<int>(n, 0));
        for (int i = n - 1; i > 0; i--)
        {
            for (int j = 0; j < n; j++)
            {
                int res = 5e6;
                for (int k = 0; k < n; k++)
                {
                    if (k != j)
                        // We are taking the minimum of the previous row
                        res = min(res, dp[!(i & 1)][k] + grid[i][k]);
                }
                // Updating the current row
                // & 1 is used to alternate between the two rows
                dp[i & 1][j] = res;
            }
        }
        for (int i = 0; i < n; i++)
            // Finding the minimum path sum in the first row
            ans = min(ans, dp[1][i] + grid[0][i]);
        return ans;
    }
};

class Solution {
public:
    int findRotateSteps(string ring, string key) {
        int n = ring.size();
        vector<int> dp(n);
        for (int i = key.size() - 1; i >= 0; i--) {
            vector<int> dp2(n, INT_MAX);
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (key[i] == ring[k]) dp2[j] = min(dp2[j], dp[k] + min(abs(j - k), n - abs(j - k)) + 1);
                }
            }
            swap(dp, dp2);
        }
        return dp[0];
    }
};

class Solution
{
public:
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>> &edges)
    {
        vector<vector<int>> tree(n);
        for (auto &e : edges)
        {
            tree[e[0]].push_back(e[1]);
            tree[e[1]].push_back(e[0]);
        }
        vector<int> count(n, 1), res(n, 0);
        function<void(int, int)> postOrder = [&](int node, int parent) {
            for (int child : tree[node])
            {
                if (child == parent)
                    continue;
                postOrder(child, node);
                count[node] += count[child];
                res[node] += res[child] + count[child];
            }
        };
        function<void(int, int)> preOrder = [&](int node, int parent) {
            for (int child : tree[node])
            {
                if (child == parent)
                    continue;
                res[child] = res[node] - count[child] + n - count[child];
                preOrder(child, node);
            }
        };
        postOrder(0, -1);
        preOrder(0, -1);
        return res;
    }
};

class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        for (int num : nums) k ^= num;
        return __builtin_popcount(k);
    }
};

class Solution
{
public:
    long long wonderfulSubstrings(string word)
    {
        long long wonderful = 0;
        vector<int> seen(1 << 10 + 1);
        seen[0]++;
        int mask = 0;
        for (int i = 0; i < word.size(); i++)
        {
            mask ^= 1 << (word[i] - 'a');
            wonderful += seen[mask];
            for (int c = 0; c < 10; c++)
                wonderful += seen[mask ^ (1 << c)];
            seen[mask]++;
        }
        return wonderful;
    }
};


class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int count =1;
        int n = people.size();
        int l = 0, r = n-1;
        while(l <= r){
            if(people[l] + people[r] <= limit){
                l++;
                r--;
            } else {
                r--;
            }
            count++;
        }
        return count - 1;
    }
};

class Solution
{
public:
    ListNode *doubleIt(ListNode *head)
    {
        if (head->val > 4)
        {
            head = new ListNode(0, head);
        };
        ListNode* node = head; 
        while (head)
        {
            node->val = (node->val * 2) % 10;
            if (node->next && node->next->val > 4)
            {
                node->val++;
            }
            node = node->next;
        }
        return head;
    }
};

class Solution
{
public:
    vector<string> findRelativeRanks(vector<int> &score)
    {
        vector<int> ordered(score);
        sort(ordered.rbegin(), ordered.rend());
        unordered_map<int, string> ranks;
        for (int i = 0; i < ordered.size(); i++)
        {
            if (i == 0)
                ranks[ordered[i]] = "Gold Medal";
            else if (i == 1)
                ranks[ordered[i]] = "Silver Medal";
            else if (i == 2)
                ranks[ordered[i]] = "Bronze Medal";
            else
                ranks[ordered[i]] = to_string(i + 1);
        }
        vector<string> result;
        for (int s : score)
            result.push_back(ranks[s]);
        return result;
    }
};

class Solution
{
public:
    int distributeCoins(TreeNode *root)
    {
        int moves = 0;
        dfs(root, moves);
        return moves;
    }
    int dfs(TreeNode *root, int &moves)
    {
        if (!root)
            return 0;
        int left = dfs(root->left, moves);
        int right = dfs(root->right, moves);
        moves += abs(left) + abs(right);
        return root->val + left + right - 1;
    }
    int abs(int x)
    {
        return x < 0 ? -x : x;
    }
};

class Solution {
public:
    long long maximumValueSum(vector<int>& nums, int k, vector<vector<int>>& edges) {
        int N = nums.size();
        vector<long long> deltas;
        for (int x : nums) {
            deltas.push_back((x ^ k) - x);
        }
        sort(deltas.rbegin(), deltas.rend());
        long long total = accumulate(nums.begin(), nums.end(), 0LL);
        long long best = total;
        int i = 0;
        while (i + 1 < N) {
            total += deltas[i] + deltas[i + 1];
            best = max(best, total);
            i += 2;
        }
        return best;
    }
};

class Solution
{
public:
    int subsetXORSum(vector<int> &nums)
    {
        int n = nums.size();
        int res = 0;
        for (int i = 0; i < (1 << n); i++)
        {
            int xorSum = 0;
            for (int j = 0; j < n; j++)
            {
                if (i & (1 << j))
                    xorSum ^= nums[j];
            }
            res += xorSum;
        }
        return res;
    }
};