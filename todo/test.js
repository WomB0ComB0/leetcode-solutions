/**
 * @param {number[]} deck
 * @return {number[]}
 */
var deckRevealedIncreasing = function (deck) {
  deck.sort((a, b) => a - b);
  let result = [];
  result.push(deck.pop());
  while (deck.length > 0) {
    result.unshift(result.pop());
    result.unshift(deck.pop());
  }
  return result;
};

/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
  let leftMax = 0, rightMax = 0, left = 0, right = height.length - 1, res = 0;
  while (left < right) {
    if (height[left] < height[right]) {
      res += Math.max(leftMax - height[left], 0);
      leftMax = Math.max(leftMax, height[left]);
      left++;
    } else {
      res += Math.max(rightMax - height[right], 0);
      rightMax = Math.max(rightMax, height[right]);
      right--;
    }
  }
  return res
};

/**
 * @param {TreeNode} root
 * @return {number}
 */
var sumNumbers = function (root) {
  return dfs(root, []);
};

function dfs(node, path) {
  if (!node) return 0;
  path.push(node.val);
  if (!node.left && !node.right) {
    return parseInt(path.join(''));
  }
  let left = dfs(node.left, path.slice());
  let right = dfs(node.right, path.slice());
  return left + right;
}

/**
 * @param {TreeNode} root
 * @param {number} val
 * @param {number} depth
 * @return {TreeNode}
 */
var addOneRow = function (root, val, depth) {
  if (depth === 1) {
    let newRoot = new TreeNode(val);
    newRoot.left = root;
    return newRoot;
  }
  return () => {
    let queue = [root];
    let level = 1;
    while (queue.length) {
      let size = queue.length;
      for (let i = 0; i < size; i++) {
        let node = queue.shift();
        if (level === depth - 1) {
          let left = new TreeNode(val);
          let right = new TreeNode(val);
          left.left = node.left;
          right.right = node.right;
          node.left = left;
          node.right = right;
        }
        if (node.left) queue.push(node.left);
        if (node.right) queue.push(node.right);
      }
      level++;
    }
    return root;
  }
};

var smallestFromLeaf = function (root) {
  let result = '';
  dfs(root, '');
  return result;
};

function dfs(node, path) {
  if (!node) return;
  path = String.fromCharCode(node.val + 97) + path;
  if (!node.left && !node.right) {
    result = result ? result < path ? result : path : path;
  }
  dfs(node.left, path);
  dfs(node.right, path);
}

/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function (grid) {
  let perimeter = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === 1) {
        perimeter += 4;
        if (i > 0 && grid[i - 1][j] === 1) perimeter -= 2;
        if (j > 0 && grid[i][j - 1] === 1) perimeter -= 2;
      }
    }
  }
  return perimeter;
};

/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  let count = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === '1') {
        dfs(grid, i, j);
        count++;
      }
    }
  }
  return count;
};

const dfs = (grid, i, j) => {
  if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] === '0') return;
  grid[i][j] = '0';
  dfs(grid, i - 1, j);
  dfs(grid, i + 1, j);
  dfs(grid, i, j - 1);
  dfs(grid, i, j + 1);
}

/**
 * @param {number[][]} land
 * @return {number[][]}
 */
var findFarmland = function (land) {
  let result = [];
  for (let i = 0; i < land.length; i++) {
    for (let j = 0; j < land[0].length; j++) {
      if (land[i][j] === 1) {
        let farmland = [i, j];
        dfs(land, i, j, farmland);
        result.push(farmland);
      }
    }
  }
  return result;
};

const dfs = (land, i, j, farmland) => {
  if (i < 0 || j < 0 || i >= land.length || j >= land[0].length || land[i][j] === 0) return;
  land[i][j] = 0;
  farmland[2] = i;
  farmland[3] = j;
  dfs(land, i - 1, j, farmland);
  dfs(land, i + 1, j, farmland);
  dfs(land, i, j - 1, farmland);
  dfs(land, i, j + 1, farmland);
}

/**
 * @param {string[]} deadends
 * @param {string} target
 * @return {number}
 */
var openLock = function (deadends, target) {
  let dead = new Set(deadends);
  if (dead.has('0000')) return -1;
  let queue = ['0000'];
  let visited = new Set(queue);
  let steps = 0;
  while (queue.length) {
    let size = queue.length;
    for (let i = 0; i < size; i++) {
      let current = queue.shift();
      if (current === target) return steps;
      for (let j = 0; j < 4; j++) {
        for (let k = -1; k <= 1; k += 2) {
          let next = current.slice(0, j) + (Number(current[j]) + k + 10) % 10 + current.slice(j + 1);
          if (!visited.has(next) && !dead.has(next)) {
            queue.push(next);
            visited.add(next);
          }
        }
      }
    }
    steps++;
  }
  return -1;
};

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var findMinHeightTrees = function (n, edges) {
  if (n === 1) return [0];
  // Create adjacency list
  const adjList = [...Array(n)].map((_e) => new Set());
  // Add edges to adjacency list
  for (const [n1, n2] of edges) {
    adjList[n1].add(n2);
    adjList[n2].add(n1);
  }
  // Create a queue with all the leaf nodes
  const deq = new Queue()
  for (let index = 0; index < adjList.length; index++) {
    // If the node has only one neighbor, it is a leaf node
    if (adjList[index].size === 1) {
      // Add the leaf node to the queue
      deq.enqueue(index);
    }
  }

  // Remove the leaf nodes level by level
  while (n > 2) {
    let size = deq.size();
    n -= size;
    // Remove the leaf nodes
    for (let i = 0; i < size; i++) {
      let node = deq.dequeue();
      // Get the only neighbor of the leaf node
      for (let neighbor of adjList[node]) {
        // Remove the leaf node from the neighbor
        adjList[neighbor].delete(node);
        // If the neighbor becomes a leaf node, add it to the queue
        if (adjList[neighbor].size === 1) {
          // Add the leaf node to the queue
          deq.enqueue(neighbor);
        }
      }
    }
  }
  // Return the remaining nodes in the queue
  return deq.toArray();
};

/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function (n) {
  if (n === 0) return 0;
  if (n === 1 || n === 2) return 1;
  let dp = [0, 1, 1];
  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
  }
  return dp[n];
};

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestIdealString = function (s, k) {
  const cache = [...Array(26).fill(0)];
  for (const char of s) {
    const code = char.charCodeAt(0) - 97;
    let max = 0;
    for (let index = Math.max(code - k, 0); index < Math.min(code + k + 1, 26); index += 1) {
      max = Math.max(max, cache[index] + 1);
    }
    cache[code] = max;
  }
  return Math.max(...cache);
};

/**
 * @param {number[][]} grid
 * @return {number}
 */
var minFallingPathSum = function (grid) {
  const n = grid.length;
  for (let i = 1; i < n; i++) {
    for (let j = 0; j < n; j++) {
      let min = grid[i - 1][j];
      if (j > 0) min = Math.min(min, grid[i - 1][j - 1]);
      if (j < n - 1) min = Math.min(min, grid[i - 1][j + 1]);
      grid[i][j] += min;
    }
  }
  return Math.min(...grid[n - 1]);
};



/**
 * @param {number[][]} grid
 * @return {number}
 */
var minFallingPathSum = function (grid) {
  const N = grid.length;
  let DP = grid[0]

  for (let i = 1; i < N; i++) {
    // We need to find the two smallest numbers in the previous row
    let index1 = DP.indexOf(Math.min(...DP));
    // We need to find the second smallest number in the previous row
    let index2 = DP.indexOf(Math.min(...DP.slice(0, index1).concat(DP.slice(index1 + 1))));
    for (let j = 0; j < N; j++) {
      // If the current column is not the same as the first smallest number in the previous row
      if (j !== index1) {
        // Add the first smallest number in the previous row
        grid[i][j] += DP[index1];
      } else {
        grid[i][j] += DP[index2];
      }
    }
    // Update the DP array
    DP = grid[i];
  }
  return Math.min(...DP);
};



/**
 * @param {string} ring
 * @param {string} key
 * @return {number}
 */
var findRotateSteps = function (ring, key) {
  const n = ring.length;
  const m = key.length;
  const pos = new Array(26).fill(0).map(() => new Array());
  for (let i = 0; i < n; i++) {
    pos[ring[i].charCodeAt(0) - 97].push(i);
  }
  const dp = new Array(m).fill(0).map(() => new Array(n).fill(Number.MAX_SAFE_INTEGER));
  for (const i of pos[key[0].charCodeAt(0) - 97]) {
    dp[0][i] = Math.min(i, n - i) + 1;
  }
  for (let i = 1; i < m; i++) {
    for (const j of pos[key[i].charCodeAt(0) - 97]) {
      for (const k of pos[key[i - 1].charCodeAt(0) - 97]) {
        dp[i][j] = Math.min(dp[i][j], dp[i - 1][k] + Math.min(Math.abs(j - k), n - Math.abs(j - k)) + 1);
      }
    }
  }
  return Math.min(...dp[m - 1]);
};


/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var sumOfDistancesInTree = function (n, edges) {
  const graph = new Array(n).fill(0).map(() => new Array());
  const count = new Array(n).fill(1);
  const ans = new Array(n).fill(0);
  const dfs = (node, parent) => {
    for (const child of graph[node]) {
      if (child === parent) continue;
      dfs(child, node);
      count[node] += count[child];
      ans[node] += ans[child] + count[child];
    }
  };
  const dfs2 = (node, parent) => {
    for (const child of graph[node]) {
      if (child === parent) continue;
      ans[child] = ans[node] - count[child] + n - count[child];
      dfs2(child, node);
    }
  };
  for (const [u, v] of edges) {
    graph[u].push(v);
    graph[v].push(u);
  }
  dfs(0, -1);
  dfs2(0, -1);
  return ans;
};

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function (nums, k) {
  const bits = nums.reduce((acc, val) => acc ^ val, 0).toString(2).padStart(32, "0");
  const target = (k >>> 0).toString(2).padStart(32, "0");
  let res = 0;
  for (let index = 0; index < 32; index += 1) {
    res += bits[index] !== target[index];
  }
  return res;
};

var minOperations = function (nums, k) {
  var count = k;
  for (let i = 0; i < nums.length; i++) {
    count = count ^ nums[i];
  }
  var total = 0;
  while (count) {
    count = (count & count - 1);
    total++;
  }
  return total
}

/**
 * @param {string} word
 * @return {number}
 */
var wonderfulSubstrings = function (word) {
  let wonderful = 0;
  let seen = new Map([[0, 1]]);
  let mask = 0;

  for (let i = 0; i < word.length; i++) {
    mask ^= 1 << (word.charCodeAt(i) - 97);
    wonderful += seen.get(mask) || 0;
    for (let j = 0; j < 10; j++) {
      wonderful += seen.get(mask ^ (1 << j)) || 0;
    }
    seen.set(mask, (seen.get(mask) || 0) + 1);
  }
  return wonderful;
};



var removeNodes = function (head) {
  if (head === null) return head;
  let stack = [];
  let current = head;
  while (current) {
    while (stack.length && stack[stack.length - 1].val < current.val) stack.pop();
    if (stack.length) stack[stack.length - 1].next = current;
    stack.push(current);
    current = current.next;
  }
  return stack[0];
};

var distributeCoins = function(root) {
  let moves = 0;
  const dfs = (node) => {
    if (!node) return 0;
    let left = dfs(node.left);
    let right = dfs(node.right);
    moves += Math.abs(left) + Math.abs(right);
    return node.val + left + right - 1;
  }
  dfs(root);
  return moves;
};


/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number[][]} edges
 * @return {number}
 */
var maximumValueSum = function (nums, k, edges) {
  const N = nums.length;
  const deltas = nums.map(x => (x ^ k) - x);
  deltas.sort((a, b) => b - a);
  let total = nums.reduce((acc, val) => acc + val, 0);
  let best = total;
  let i = 0;
  while (i + 1 < N) {
    total += deltas[i] + deltas[i + 1];
    best = Math.max(best, total);
    i += 2;
  }
  return best;
};


/**
 * class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        N = len(nums)
        deltas = []
        
        for x in nums:
            deltas.append((x ^ k)  -x)
        
        deltas.sort(reverse=True)
        total = sum(nums)
        best = total

        i = 0 
        while (i + 1 < N):
            total += deltas[i] + deltas[i + 1]
            best = max(best, total)
            i += 2
        return best
 * 
*/