char* removeKdigits(char* num, int k) {
    int len = strlen(num);
    if(len == k){
        char* ans = (char*)malloc(2*sizeof(char));
        ans[0] = '0';
        ans[1] = '\0';
        return ans;
    }
    
    char* stack = (char*)malloc(len*sizeof(char));
    int top = -1;
    
    for(int i=0; i<len; i++){
        char ch = num[i];
        while(top>=0 && k>0 && stack[top]>ch){
            top--;
            k--;
        }
        stack[++top] = ch;
    }
    
    while(k>0){
        top--;
        k--;
    }
    
    while(top>=0 && stack[top]=='0'){top--;}
    
    if(top == -1){
        char* ans = (char*)malloc(2*sizeof(char));
        ans[0] = '0';
        ans[1] = '\0';
        return ans;
    }
    
    char* ans = (char*)malloc((top+2)*sizeof(char));
    for(int i=0; i<=top; i++){ ans[i] = stack[i];}
    ans[top+1] = '\0';
    return ans;
}

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int sumNumbers(struct TreeNode* root) {
    if(!root) return 0;
    int stack[1000];
    int top = -1;
    int count = 0;
    stack[++top] = root->val;
    if(!root->left && !root->right){
        count = root->val;
    }
    if(root->left){
        count += dfs(root->left, stack, top);
    }
    if(root->right){
        count += dfs(root->right, stack, top);
    }
    return count;
}

int dfs(struct TreeNode* root, int* stack, int top){
    stack[++top] = root->val;
    int count = 0;
    if(!root->left && !root->right){
        for(int i=0; i<=top; i++){
            count = count*10 + stack[i];
        }
    }
    if(root->left){
        count += dfs(root->left, stack, top);
    }
    if(root->right){
        count += dfs(root->right, stack, top);
    }
    return count;
}

struct TreeNode* addOneRow(struct TreeNode* root, int val, int depth) {
    if(depth == 1){
        struct TreeNode* newRoot = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        newRoot->val = val;
        newRoot->left = root;
        newRoot->right = NULL;
        return newRoot;
    }
    
    struct TreeNode* layer[1000];
    int layerSize = 1;
    layer[0] = root;
    
    for(int i=2; i<depth; i++){
        struct TreeNode* nextLayer[1000];
        int nextLayerSize = 0;
        for(int j=0; j<layerSize; j++){
            struct TreeNode* node = layer[j];
            if(node->left){
                nextLayer[nextLayerSize++] = node->left;
            }
            if(node->right){
                nextLayer[nextLayerSize++] = node->right;
            }
        }
        layerSize = nextLayerSize;
        for(int j=0; j<layerSize; j++){
            layer[j] = nextLayer[j];
        }
    }
    
    for(int i=0; i<layerSize; i++){
        struct TreeNode* node = layer[i];
        struct TreeNode* left = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        left->val = val;
        left->left = node->left;
        left->right = NULL;
        node->left = left;
        
        struct TreeNode* right = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        right->val = val;
        right->left = NULL;
        right->right = node->right;
        node->right = right;
    }
    
    return root;
}

#define MIN_CHAR 'a'

void dfs(struct TreeNode* root, char* sb, int depth, char** sans) {
    if (root == NULL) {
        return;
    }

    sb[depth] = root->val + MIN_CHAR;
    if (root->left == NULL && root->right == NULL) {
        sb[depth + 1] = '\0';
        char* rev = strdup(sb);
        strrev(rev);
        if (*sans == NULL || strcmp(rev, *sans) < 0) {
            free(*sans);
            *sans = rev;
        } else {
            free(rev);
        }
    } else {
        dfs(root->left, sb, depth + 1, sans);
        dfs(root->right, sb, depth + 1, sans);
    }
}

void strrev(char *str) {
    if (str) {
        char *end = str + strlen(str) - 1;
        
        while (str < end) {
            char temp = *str;
            *str = *end;
            *end = temp;

            str++;
            end--;
        }
    }
}

char* smallestFromLeaf(struct TreeNode* root) {
    char* sb = malloc(8501);
    char* sans = NULL;
    dfs(root, sb, 0, &sans);
    free(sb);
    return sans;
}

int islandPerimeter(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = *gridColSize, res = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                if (i == 0 || grid[i - 1][j] == 0) {
                    res++;
                }
                if (i == m - 1 || grid[i + 1][j] == 0) {
                    res++;
                }
                if (j == 0 || grid[i][j - 1] == 0) {
                    res++;
                }
                if (j == n - 1 || grid[i][j + 1] == 0) {
                    res++;
                }
            }
        }
    }
    return res;
}


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findFarmland(int** land, int landSize, int* landColSize, int* returnSize, int** returnColumnSizes) {
    int maxFarmlands = landSize * (*landColSize);  // Maximum possible number of farmlands
    int** farmlands = (int**)malloc(maxFarmlands * sizeof(int*));
    *returnColumnSizes = (int*)malloc(maxFarmlands * sizeof(int));
    *returnSize = 0;
    for (int i = 0; i < landSize; i++) {
        for (int j = 0; j < *landColSize; j++) {
            if (land[i][j] == 1) {
                int row = i, col = j;
                while (row < landSize && land[row][j] == 1) {
                    row++;
                }
                while (col < *landColSize && land[i][col] == 1) {
                    col++;
                }
                for (int x = i; x < row; x++) {
                    for (int y = j; y < col; y++) {
                        land[x][y] = 0;  // Mark as visited
                    }
                }
                farmlands[*returnSize] = (int*)malloc(4 * sizeof(int));
                farmlands[*returnSize][0] = i;
                farmlands[*returnSize][1] = j;
                farmlands[*returnSize][2] = row - 1;
                farmlands[*returnSize][3] = col - 1;
                (*returnColumnSizes)[*returnSize] = 4;
                (*returnSize)++;
            }
        }
    }
    return farmlands;
}

int openLock(char** deadends, int deadendsSize, char* target) {
    bool visited[10000] = {false};
    for (int i = 0; i < deadendsSize; i++) {
        visited[atoi(deadends[i])] = true;
    }
    if (visited[0]) {
        return -1;
    }
    int targetNum = atoi(target);
    if (targetNum == 0) {
        return 0;
    }
    int steps = 0;
    queue<int> q;
    q.push(0);
    visited[0] = true;
    while (!q.empty()) {
        steps++;
        int size = q.size();
        for (int i = 0; i < size; i++) {
            int num = q.front();
            q.pop();
            for (int j = 1; j <= 1000; j *= 10) {
                int digit = (num / j) % 10;
                int up = num + (digit == 9 ? -9 * j : j);
                if (up == targetNum) {
                    return steps;
                }
                if (!visited[up]) {
                    q.push(up);
                    visited[up] = true;
                }
                int down = num + (digit == 0 ? 9 * j : -j);
                if (down == targetNum) {
                    return steps;
                }
                if (!visited[down]) {
                    q.push(down);
                    visited[down] = true;
                }
            }
        }
    }
    return -1;
}


#include <stdlib.h>

// Function to perform a breadth-first search (BFS) to find the deepest node(s)
// starting from the given root.
int bfs(struct TreeNode* root) {
    // Initialize a queue for BFS traversal
    struct TreeNode** queue = (struct TreeNode**)malloc(10000 * sizeof(struct TreeNode*));
    int front = 0, rear = 0;
    queue[rear++] = root;
    int depth = 0;
    
    // Perform BFS
    while (front < rear) {
        int size = rear - front;
        for (int i = 0; i < size; i++) {
            struct TreeNode* node = queue[front++];
            if (node->left) queue[rear++] = node->left;
            if (node->right) queue[rear++] = node->right;
        }
        depth++;
    }
    
    // Free memory
    free(queue);
    
    return depth;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findMinHeightTrees(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    if (n == 1) {
        *returnSize = 1;
        int* result = (int*)malloc(sizeof(int));
        result[0] = 0;
        return result;
    }

    // Initialize adjacency list to store the graph
    int** adj = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        adj[i] = (int*)malloc(0); // Initialize an empty array for each node
    }
    // Initialize an array to store the degree of each node
    int* degree = (int*)calloc(n, sizeof(int));

    // Populate adjacency list and degree array
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u] = (int*)realloc(adj[u], (degree[u] + 1) * sizeof(int));
        adj[u][degree[u]++] = v;
        adj[v] = (int*)realloc(adj[v], (degree[v] + 1) * sizeof(int));
        adj[v][degree[v]++] = u;
    }

    // Initialize a queue to store leaves
    int* queue = (int*)malloc(n * sizeof(int));
    int front = 0, rear = 0;
    for (int i = 0; i < n; i++) {
        if (degree[i] == 1) { // Leaf node
            queue[rear++] = i;
        }
    }

    // Remove leaves layer by layer until 1 or 2 nodes left
    while (n > 2) {
        int size = rear - front;
        n -= size;
        for (int i = 0; i < size; i++) {
            int node = queue[front++];
            for (int j = 0; j < degree[node]; j++) {
                int neighbor = adj[node][j];
                if (--degree[neighbor] == 1) {
                    queue[rear++] = neighbor;
                }
            }
        }
    }

    // Now, queue contains 1 or 2 nodes, representing potential roots
    // Iterate through the queue and perform BFS to find the deepest node(s)
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 0;
    for (int i = front; i < rear; i++) {
        int root = queue[i];
        // Initialize a binary tree node for BFS
        struct TreeNode* tree = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        tree->val = root;
        tree->left = NULL;
        tree->right = NULL;
        // Perform BFS to find the depth
        int depth = bfs(tree);
        // Check if this depth is deeper than the current deepest depth
        if (depth > *returnSize) {
            *returnSize = depth;
            result[0] = root;
            result[1] = -1; // Reset the second element
        } else if (depth == *returnSize) {
            result[1] = root; // Store the second root
        }
        // Free memory allocated for the binary tree node
        free(tree);
    }

    // If there's only one root, set the second root to -1
    if (*returnSize == 1) {
        result[1] = -1;
    }

    // Free memory
    free(queue);
    free(degree);
    for (int i = 0; i < n; i++) {
        free(adj[i]);
    }
    free(adj);

    return result;
}



int tribonacci(int n){
    if(n == 0) return 0;
    if(n == 1) return 1;
    if(n == 2) return 1;
    int a = 0, b = 1, c = 1;
    for(int i=3; i<=n; i++){
        int temp = a + b + c;
        a = b;
        b = c;
        c = temp;
    }
    return c;
}

int tribonacci(int n){
    if(n == 0) return 0;
    if(n == 1 || n == 2) return 1;
    int* dp = (int*)malloc((n+1)*sizeof(int));
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 1;
    for(int i=3; i<=n; i++){
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
    }
    return dp[n];
}

int longestIdealString(char* s, int k) {
    int* dp = (int*)malloc(26*sizeof(int));
    for (char c = 'a'; c <= strlen(s); c++) {
        int l = 0, ci = c - 'a';
        for (int i = 0; i < 26; i++) {
            if (abs(ci - i) <= k) l = max(l, dp[i] + 1);
        }
        dp[ci] = l;
    }
    int res = 0;
    for (int i = 0; i < 26; i++) {
        res = max(res, dp[i]);
    }
    return res;
}



int minFallingPathSum(int** grid, int gridSize, int* gridColSize) {
    int first_min = 0, second_min = 0, first_col = -1;
    for(int i = 0; i < gridSize; i++) {
        // Find the minimum and second minimum values in the current row
        int a = 1e9, b = 1e9, c; // 1e9 = 10^9
        for(int j = 0; j < gridColSize[i]; j++) {
            // Update the current cell value
            grid[i][j] += (j == first_col) ? second_min : first_min;
            // Update the minimum and second minimum values
            if(grid[i][j] < a) {
                b = a;
                a = grid[i][j];
                c = j;
            } else if(grid[i][j] < b) {
                b = grid[i][j];
            }
        }
        // Update the minimum and second minimum values for the next row
        first_min = a;
        second_min = b;
        first_col = c;
    }  
    return first_min;
}

int findRotateSteps(char* ring, char* key) {
    int n = strlen(ring), m = strlen(key);
    int dp[m + 1][n];
    memset(dp, 0x3f, sizeof(dp));
    dp[0][0] = 0;
    for (int i = 1; i <= m; i++) {
        for (int j = 0; j < n; j++) {
            if (ring[j] == key[i - 1]) {
                for (int k = 0; k < n; k++) {
                    if (dp[i - 1][k] != 0x3f3f3f3f) {
                        int diff = abs(j - k);
                        dp[i][j] = fmin(dp[i][j], dp[i - 1][k] + fmin(diff, n - diff));
                    }
                }
            }
        }
    }
    int result = 0x3f3f3f3f;
    for (int j = 0; j < n; j++) {
        result = fmin(result, dp[m][j]);
    }
    return result + m;
}


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumOfDistancesInTree(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    int* result = (int*)malloc(n * sizeof(int));
    int* count = (int*)malloc(n * sizeof(int));
    int* sum = (int*)malloc(n * sizeof(int));
    int** adj = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        adj[i] = (int*)malloc(0);
    }
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0];
        int v = edges[i][1];
        if (count[u] < INT_MAX) {
            adj[u] = (int*)realloc(adj[u], (count[u] + 1) * sizeof(int));
            adj[u][count[u]++] = v;
        }
        if (count[v] < INT_MAX) {
            adj[v] = (int*)realloc(adj[v], (count[v] + 1) * sizeof(int));
            adj[v][count[v]++] = u;
        }
    }
    dfs1(0, -1, adj, count, sum);
    dfs2(0, -1, adj, count, sum, result, n);
    free(count);
    free(sum);
    for (int i = 0; i < n; i++) {
        free(adj[i]);
    }
    free(adj);
    *returnSize = n;
    return result;
}

void dfs1(int node, int parent, int** adj, int* count, int* sum) {
    sum[node] = 0;
    for (int i = 0; i < count[node]; i++) {
        int neighbor = adj[node][i];
        if (neighbor != parent) {
            dfs1(neighbor, node, adj, count, sum);
            sum[node] += sum[neighbor] + count[neighbor];
        }
    }
}

void dfs2(int node, int parent, int** adj, int* count, int* sum, int* result, int n) {
    result[node] = sum[node];
    for (int i = 0; i < count[node]; i++) {
        int neighbor = adj[node][i];
        if (neighbor != parent) {
            int sum_node = sum[node], count_node = count[node];
            int sum_neighbor = sum[neighbor], count_neighbor = count[neighbor];
            sum[node] -= sum[neighbor] + count[neighbor];
            count[node] -= count[neighbor];
            sum[neighbor] += sum[node] + count[node];
            count[neighbor] += count[node];
            dfs2(neighbor, node, adj, count, sum, result, n);
            sum[node] = sum_node;
            count[node] = count_node;
            sum[neighbor] = sum_neighbor;
            count[neighbor] = count_neighbor;
        }
    }
}

#include <unordered_map>
#include <algorithm>
#include <climits>

int minOperations(int* nums, int numsSize, int k) {
    int b = nums[0]
    for (int i = 1; i < numsSize; i++) {
        b ^= nums[i];
    }
    int res = 0;
    
    while (b != 0 || k != 0) {
        int bit1 = b & 1;
        int bit2 = k & 1;
        if (bit1 == 0 && bit2 == 0) {
            b >>= 1;
            k >>= 1;
        } else if (bit1 == 1 && bit2 == 1) {
            b >>= 1;
            k >>= 1;
        } else {
            res++;
            b >>= 1;
            k >>= 1;
        }
    }
    return res;
}

int numRescueBoats(int* people, int peopleSize, int limit) {
    int res = 0;
    int left = 0, right = peopleSize - 1;
    sort(people, people + peopleSize);
    while (left <= right) {
        if (people[left] + people[right] <= limit) {
            left++;
        }
        right--;
        res++;
    }
    return res;
}

int sort