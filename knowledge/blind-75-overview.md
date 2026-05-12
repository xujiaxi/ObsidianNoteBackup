# Blind 75 总览

> 来源：Gemini 对话总结（https://gemini.google.com/share/b8080f542397 及 https://gemini.google.com/share/6e1e3ab84929）
> 日期：2026-05-12

## 什么是 Blind 75

由 Yangshun Tay（Tech Interview Handbook 创始人）于 2018 年创建，最早分享于 Blind App。涵盖所有核心算法和数据结构的面试高频题。吃透这 75 题足以应对大部分大厂面试变体。

## 75 题完整列表

### 1. Arrays (数组)
- [ ] Two Sum
- [ ] Best Time to Buy and Sell Stock
- [ ] Contains Duplicate
- [ ] Product of Array Except Self
- [ ] Maximum Subarray
- [ ] Maximum Product Subarray
- [x] Find Minimum in Rotated Sorted Array
- [x] Search in Rotated Sorted Array
- [ ] 3Sum
- [ ] Container With Most Water

### 2. Binary (Bit Manipulation)
- [ ] Sum of Two Integers
- [ ] Number of 1 Bits
- [ ] Counting Bits
- [ ] Missing Number
- [ ] Reverse Bits

### 3. Dynamic Programming
- [ ] Climbing Stairs
- [ ] Coin Change
- [ ] Longest Increasing Subsequence
- [ ] Longest Common Subsequence
- [ ] Word Break
- [ ] Combination Sum
- [ ] House Robber
- [ ] House Robber II
- [ ] Decode Ways
- [ ] Unique Paths
- [ ] Jump Game

### 4. Graphs
- [x] Clone Graph
- [x] Course Schedule
- [ ] Pacific Atlantic Water Flow
- [x] Number of Islands
- [ ] Longest Consecutive Sequence
- [ ] Alien Dictionary (Premium)
- [ ] Graph Valid Tree (Premium)
- [ ] Number of Connected Components in an Undirected Graph (Premium)

### 5. Intervals
- [ ] Insert Interval
- [ ] Merge Intervals
- [ ] Non-overlapping Intervals
- [ ] Meeting Rooms (Premium)
- [ ] Meeting Rooms II (Premium)

### 6. Linked List
- [x] Reverse a Linked List
- [x] Detect Cycle in a Linked List
- [x] Merge Two Sorted Lists
- [ ] Merge K Sorted Lists
- [x] Remove Nth Node From End Of List
- [ ] Reorder List

### 7. Matrix
- [ ] Set Matrix Zeroes
- [ ] Spiral Matrix
- [ ] Rotate Image
- [ ] Word Search

### 8. Strings
- [x] Longest Substring Without Repeating Characters
- [ ] Longest Repeating Character Replacement
- [x] Minimum Window Substring
- [ ] Valid Anagram
- [ ] Group Anagrams
- [ ] Valid Parentheses
- [ ] Valid Palindrome
- [ ] Longest Palindromic Substring
- [ ] Palindromic Substrings
- [ ] Encode and Decode Strings (Premium)

### 9. Trees
- [x] Maximum Depth of Binary Tree
- [ ] Same Tree
- [x] Invert/Flip Binary Tree
- [ ] Binary Tree Maximum Path Sum
- [x] Binary Tree Level Order Traversal
- [ ] Serialize and Deserialize Binary Tree
- [ ] Subtree of Another Tree
- [x] Construct Binary Tree from Preorder and Inorder Traversal
- [ ] Validate Binary Search Tree
- [ ] Kth Smallest Element in a BST
- [x] Lowest Common Ancestor of BST
- [ ] Implement Trie (Prefix Tree)
- [ ] Add and Search Word (Trie)
- [ ] Word Search II

### 10. Heaps
- [ ] Top K Frequent Elements
- [ ] Find Median from Data Stream

> 注：Premium 题目可在 NeetCode.io / HackerRank / LintCode 找到替代

## 复习策略

### 按 Category 刷，不按顺序
一次攻一个类别（如 Arrays），建立 pattern 肌肉记忆。

### 30 分钟法则（Timeboxing）
- 15-20 分钟自己思考
- 30 分钟仍无头绪 → 看题解
- 理解后关掉题解，自己默写出来
- 标记为红色，几天后 revisit

### 复习节奏
| 颜色 | 含义 | 下次复习 |
|------|------|---------|
| 🟢 Green | 20 分钟内独立解出 | 很少回顾 |
| 🟡 Yellow | 解出但时间长/代码乱 | 1 周后 |
| 🔴 Red | 看了题解才做出来 | 2-3 天后 |

### Talk Out Loud
面试中写代码只是一半，沟通思路是另一半。练的时候模拟向面试官解释：
1. 先给 brute-force 思路
2. 分析时空复杂度
3. 再说明如何优化

## 核心主题深度剖析与模板 (Deep Dives)

### 1. Binary Search (LC 153, 33)
- 在旋转排序数组中，与右边界 (`nums[right]`) 比较通常比左边界更可靠。
- 掌握寻找特定目标值 vs. 寻找边界的模板。

### 2. BFS/DFS (LC 200, 207)
- **Sinking Island (沉岛算法)**: 用于 LC 200 (Number of Islands)，将访问过的陆地标记为水以避免重复访问。
- **Triple-Color Marking (三色标记法)**: 用于 LC 207 (Course Schedule) 的环检测。
- **Topological Sort (拓扑排序)**: 熟练掌握 Kahn's Algorithm (BFS) 与 DFS 的不同实现。

### 3. Sliding Window (LC 3, 76)
- **通用模板 (Universal Template)**: 使用外层 `while` 循环扩展右指针 (right pointer)，并在满足特定条件时使用内层 `while` 循环收缩左指针 (left pointer)。

### 4. Linked List (LC 206, 141)
- 熟练掌握链表反转逻辑 (LC 206) 和使用快慢指针检测环 (LC 141)。
- 广泛使用 **Dummy Nodes (哨兵节点)** 来简化边界情况的处理。

## 面试技巧与常见陷阱 (Tips & Pitfalls)

### Java 特定陷阱
- 在比较 `Integer` 对象时（例如 HashMap 的 values），务必使用 `.equals()` 而不是 `==`，以避免超出 Integer Cache (-128 to 127) 导致的缓存未命中。

### 内存模型 (Memory Models)
- 理解 **Stack vs. Heap**。深度递归 (DFS) 即使在数据量不大的情况下也可能导致 `StackOverflowError`，需要了解底层原因。

### 笔记与复习 (Notion Summaries)
- 制作精简、可复制粘贴的要点，作为面试前快速复习的“作弊条” (Cheat Sheets)。
