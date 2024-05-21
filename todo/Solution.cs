/*
    time: O(n)       
    space: O(n)
        O(n) for the stack, O(n) for the list
*/

public class Solution {
    public string RemoveKdigits(string num, int k) {
        
        Stack<char> stack = new Stack<char>();
        
        // O(n + k)
        foreach(char c in num)
        {
            while(stack.Count > 0 && stack.Peek() > c && k > 0)
            {
                stack.Pop();
                k--;
            }
            stack.Push(c);
        }
        
        // handle cases where digits are in non-descending order (12345, 11111)
        while(k > 0)
        {
            stack.Pop();
            k--;
        }
        
        List<char> res = new List<char>();
        while(stack.Count > 0)
        {
            res.Add(stack.Pop());
        }
        
        // handle cases where there are leading zeros after removing digits 
        // num = "98002", k =2. result string should be "2" instead of "002"
        // num = "98002" -> res = "200", so we need to removing ending zeros before reversing.
        int idx = res.Count - 1;
        while(idx >= 0)
        {
            if(res[idx] == '0')
            {
                res.RemoveAt(idx);
                idx--;
            }
            else
                break;
        }
        
        // if all digits are removed, return "0"
        if(res.Count == 0)
            return "0";
        
        char[] arr = res.ToArray();
        Array.Reverse(arr);       
        return new string(arr);
    }
}

public class Solution {
    public int SumNumbers(TreeNode root) {
        return dfs(root, 0);
    }
    public int dfs(TreeNode root, int sum)
    {
        if(root == null)
            return 0;
        
        sum = sum * 10 + root.val;
        
        if(root.left == null && root.right == null)
            return sum;
        
        return dfs(root.left, sum) + dfs(root.right, sum);
    }
}

public class Solution {
    public TreeNode AddOneRow(TreeNode root, int val, int depth) {
        if(depth == 1)
        {
            TreeNode newRoot = new TreeNode(val);
            newRoot.left = root;
            return newRoot;
        }
        
        Queue<TreeNode> q = new Queue<TreeNode>();
        q.Enqueue(root);
        int level = 1;
        
        while(q.Count > 0)
        {
            int size = q.Count;
            for(int i = 0; i < size; i++)
            {
                TreeNode node = q.Dequeue();
                if(level == depth - 1)
                {
                    TreeNode left = new TreeNode(val);
                    TreeNode right = new TreeNode(val);
                    left.left = node.left;
                    right.right = node.right;
                    node.left = left;
                    node.right = right;
                }
                if(node.left != null)
                    q.Enqueue(node.left);
                if(node.right != null)
                    q.Enqueue(node.right);
            }
            level++;
        }
        
        return root;
    }
}


public class Solution {
    public string SmallestFromLeaf(TreeNode root) {
        string res = "";
        dfs(root, "", ref res);
        return res;
    }
    public void dfs(TreeNode root, string path, ref string res)
    {
        if(root == null)
            return;
        
        path = (char)(root.val + 'a') + path;
        
        if(root.left == null && root.right == null)
        {
            if(string.IsNullOrEmpty(res) || string.Compare(path, res) < 0)
                res = path;
        }
        
        dfs(root.left, path, ref res);
        dfs(root.right, path, ref res);
    }
}

public class Solution {
    public int IslandPerimeter(int[][] grid) {
        int perimeter = 0;
        for(int i = 0; i < grid.Length; i++)
        {
            for(int j = 0; j < grid[0].Length; j++)
            {
                if(grid[i][j] == 1)
                {
                    perimeter += 4;
                    if(i > 0 && grid[i - 1][j] == 1)
                        perimeter -= 2;
                    if(j > 0 && grid[i][j - 1] == 1)
                        perimeter -= 2;
                }
            }
        }
        return perimeter;
    }
}

int numIslands(char** grid, int gridSize, int* gridColSize) {
    if(gridSize == 0)
        return 0;
    
    int rows = gridSize;
    int cols = *gridColSize;
    int count = 0;
    
    for(int i = 0; i < rows; i++)
    {
        for(int j = 0; j < cols; j++)
        {
            if(grid[i][j] == '1')
            {
                dfs(grid, rows, cols, i, j);
                count++;
            }
        }
    }
    
    return count;
}

void dfs(char** grid, int rows, int cols, int i, int j)
{
    if(i < 0 || i >= rows || j < 0 || j >= cols || grid[i][j] == '0')
        return;
    
    grid[i][j] = '0';
    dfs(grid, rows, cols, i + 1, j);
    dfs(grid, rows, cols, i - 1, j);
    dfs(grid, rows, cols, i, j + 1);
    dfs(grid, rows, cols, i, j - 1);
}


public class Solution {
    public int NumIslands(char[][] grid) {
        if(grid.Length == 0)
            return 0;
        
        int rows = grid.Length;
        int cols = grid[0].Length;
        int count = 0;
        
        for(int i = 0; i < rows; i++)
        {
            for(int j = 0; j < cols; j++)
            {
                if(grid[i][j] == '1')
                {
                    dfs(grid, rows, cols, i, j);
                    count++;
                }
            }
        }
        
        return count;        
    }
    public void dfs(char[][] grid, int rows, int cols, int i, int j)
    {
        if(i < 0 || i >= rows || j < 0 || j >= cols || grid[i][j] == '0')
            return;
        
        grid[i][j] = '0';
        dfs(grid, rows, cols, i + 1, j);
        dfs(grid, rows, cols, i - 1, j);
        dfs(grid, rows, cols, i, j + 1);
        dfs(grid, rows, cols, i, j - 1);
    }
}


public class Solution {
    public int[][] FindFarmland(int[][] land) {
        List<int[]> res = new List<int[]>();
        int rows = land.Length;
        int cols = land[0].Length;
        
        for(int i = 0; i < rows; i++)
        {
            for(int j = 0; j < cols; j++)
            {
                if(land[i][j] == 1)
                {
                    int[] farmland = new int[4];
                    farmland[0] = i;
                    farmland[1] = j;
                    dfs(land, i, j, farmland);
                    res.Add(farmland);
                }
            }
        }
        
        return res.ToArray();
    }
    public void dfs(int[][] land, int i, int j, int[] farmland)
    {
        if(i < 0 || i >= land.Length || j < 0 || j >= land[0].Length || land[i][j] == 0)
            return;
        
        land[i][j] = 0;
        farmland[2] = Math.Max(farmland[2], i);
        farmland[3] = Math.Max(farmland[3], j);
        
        dfs(land, i + 1, j, farmland);
        dfs(land, i - 1, j, farmland);
        dfs(land, i, j + 1, farmland);
        dfs(land, i, j - 1, farmland);
    }
}

public class Solution {
    public int OpenLock(string[] deadends, string target) {
        HashSet<string> vis = new HashSet<string>();
        HashSet<string> deads = new HashSet<string>(deadends);
        Queue<string> q = new Queue<string>();
        q.Enqueue("0000");
        int turns = 0;
        
        while(q.Count > 0)
        {
            int size = q.Count;
            for(int i = 0; i < size; i++)
            {
                string curr = q.Dequeue();
                if(curr == target)
                    return turns;
                if(deads.Contains(curr) || vis.Contains(curr))
                    continue;
                vis.Add(curr);
                for(int j = 0; j < 4; j++)
                {
                    int up = (curr[j] - '0' + 1) % 10;
                    int down = (curr[j] - '0' + 9) % 10;
                    string upStr = curr.Substring(0, j) + up + curr.Substring(j + 1);
                    string downStr = curr.Substring(0, j) + down + curr.Substring(j + 1);
                    if(!vis.Contains(upStr))
                        q.Enqueue(upStr);
                    if(!vis.Contains(downStr))
                        q.Enqueue(downStr);
                }
            }
            turns++;
        }
        
        return -1;    
    }
    
}

public class Solution {
    public IList<int> FindMinHeightTrees(int n, int[][] edges) {
        if(n == 1)
            return new List<int>(){0};
        
        List<int>[] adj = new List<int>[n];
        for(int i = 0; i < n; i++)
            adj[i] = new List<int>();
        
        int[] degree = new int[n];
        foreach(int[] edge in edges)
        {
            adj[edge[0]].Add(edge[1]);
            adj[edge[1]].Add(edge[0]);
            degree[edge[0]]++;
            degree[edge[1]]++;
        }
        
        Queue<int> q = new Queue<int>();
        for(int i = 0; i < n; i++)
        {
            if(degree[i] == 1)
                q.Enqueue(i);
        }
        
        while(n > 2)
        {
            int size = q.Count;
            n -= size;
            for(int i = 0; i < size; i++)
            {
                int curr = q.Dequeue();
                foreach(int neighbor in adj[curr])
                {
                    degree[neighbor]--;
                    if(degree[neighbor] == 1)
                        q.Enqueue(neighbor);
                }
            }
        }
        
        return q.ToList();        
    }
}

public class Solution {
    public int Tribonacci(int n) {
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;
        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 1;
        for (int i = 3; i <= n; i++)
        {
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
        }
        return dp[n];
    }
}

enum Integer {
    MIN_VALUE = -2147483648,
}

public class Solution {
    public int LongestIdealString(string s, int k) {
        int[] dp = new int[27];
        for (int i = 0; i < s.Length; i++) {
            int idx = s[i] - 'a';

            int left = Math.Max((idx - k), 0);
            int right = Math.Min((idx + k), 26);
            int max = Integer.MinValue;
            for (int j = left; j <= right; j++) {
                max = Math.Max(max, dp[j]);
            }
            dp[idx] = max + 1;
        }
        max = int.MinValue;
        foreach (int ele in dp) {
            max = Math.Max(max, ele);
        }
        return max;
    }
}

public class Solution {
    public int MinFallingPathSum(int[][] grid) {
        int n = grid.Length;
        int res = int.MaxValue;
        // dp[i][j] = min path sum from top to grid[i][j]
        int[][] dp = new int[n][];
        // initialize dp
        for (int i = 0; i < n; i++) {
            dp[i] = new int[n];
            Array.Fill(dp[i], int.MaxValue);
        }
        // clone the first row
        for (int i = 0; i < n; i++) {
            dp[0][i] = grid[0][i];
        }
        
        /*
        You aren't necessarily performing a 3x3 matrix traversal, 
        you are just checking the 3 elements in 
        the row above the current element.
        */
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Common patter in dp
                int temp = int.MaxValue;
                /*
                We use ++k instead of k++ because we want to check the 3 
                elements in the row above the current element
                */
                for (int k = 0; k < n; ++k) {
                    // if j != k, we can take the min path sum from the previous row
                    if (j  != k) {
                        /*
                            Cases for temp:
                            1. dp[i - 1][k] is int.MaxValue, we can't take this path
                            2. dp[i - 1][k] is not int.MaxValue, we can take this path
                        */
                        temp = Math.Min(temp, grid[i][j] + dp[i - 1][k]);
                    }
                    // if j == k, we can't take the same column from the previous row
                    dp[i][j] = temp;
                }
            }
        }
        
        // find the min path sum from the last row
        for (int j = 0; j < n; j++) {
            // we can take any path from the last row
            res = Math.Min(res, dp[n - 1][j]);
        }

        return res;
    }
}

public class Solution {
    public int FindRotateSteps(string ring, string key) {
        int n = ring.Length;
        int m = key.Length;
        int[][] dp = new int[m][];
        for (int i = 0; i < m; i++) {
            dp[i] = new int[n];
            Array.Fill(dp[i], int.MaxValue);
        }
        Dictionary<char, List<int>> map = new Dictionary<char, List<int>>();
        for (int i = 0; i < n; i++) {
            if (!map.ContainsKey(ring[i])) {
                map[ring[i]] = new List<int>();
            }
            map[ring[i]].Add(i);
        }
        for (int i = 0; i < n; i++) {
            if (ring[i] == key[0]) {
                dp[0][i] = Math.Min(i, n - i) + 1;
            }
        }
        for (int i = 1; i < m; i++) {
            foreach (int j in map[key[i]]) {
                foreach (int k in map[key[i - 1]]) {
                    dp[i][j] = Math.Min(dp[i][j], dp[i - 1][k] + Math.Min(Math.Abs(j - k), n - Math.Abs(j - k)) + 1);
                }
            }
        }
        int res = int.MaxValue;
        for (int i = 0; i < n; i++) {
            res = Math.Min(res, dp[m - 1][i]);
        }
        return res;
    }
}

public class Solution {
    int[] res;
    int[] count;
    int[] ans;
    int N;
    List<HashSet<int>> graph;
    public int[] SumOfDistancesInTree(int N, int[][] edges) {
        this.res = new int[n];
        this.count = new int[n];
        this.ans = new int[n];
        this.graph = new List<HashSet<int>>();
        for (int i = 0; i < N; i++) {
            graph.Add(new HashSet<int>());
        }
        foreach (int[] edge in edges) {
            graph[edge[0]].Add(edge[1]);
            graph[edge[1]].Add(edge[0]);
        }
        PostOrder(0, -1, graph, count, ans);
        PreOrder(0, -1, graph, count, ans, res);
        return res;
    }
    private void PostOrder(int node, int parent, List<HashSet<int>> graph, int[] count, int[] ans) {
        foreach (int child in graph[node]) {
            if (child == parent) {
                continue;
            }
            PostOrder(child, node, graph, count, ans);
            count[node] += count[child];
            ans[node] += ans[child] + count[child];
        }
        count[node]++;
    }
    private void PreOrder(int node, int parent, List<HashSet<int>> graph, int[] count, int[] ans, int[] res) {
        res[node] = ans[node];
        foreach (int child in graph[node]) {
            if (child == parent) {
                continue;
            }
            int parentCount = count[node];
            int parentAns = ans[node];
            int childCount = count[child];
            int childAns = ans[child];
            count[node] -= count[child];
            ans[node] -= ans[child] + count[child];
            count[child] += count[node];
            ans[child] += ans[node] + count[node];
            PreOrder(child, node, graph, count, ans, res);
            count[node] = parentCount;
            ans[node] = parentAns;
            count[child] = childCount;
            ans[child] = childAns;
        }
    }
}

public class Solution {
    public int MinOperations(int[] nums, int k) {
        int b = nums[0];
        const int n = nums.Length;
        for (int i = 1; i < n; i++) {
            b ^= nums[i]
        }
        int res = 0;
        
        while (b != 0 || k != 0) {
            int bit1 = b & 1;
            int bit2 = k & 1;
            if (bit1 != bit2) {
                res++;
            }
            b >>= 1;
            k >>= 1;
        }
        return res;
    }
}


    public class Solution {
        public int NumRescueBoats(int[] people, int limit) {
            Array.Sort(people);
            int res = 0;
            int left = 0;
            int right = people.Length - 1;
            while (left <= right) {
                if (people[left] + people[right] <= limit) {
                    left++;
                }
                right--;
                res++;
            }
            return res;
        }
    }
/**
 * Definition for singly-linked list.
 */
