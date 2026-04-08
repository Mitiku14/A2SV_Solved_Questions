# 2708. Maximum-Strength-of-a-Group

**Difficulty:** Medium

**Problem:** [Maximum-Strength-of-a-Group](https://leetcode.com/problems/maximum-strength-of-a-group)

---

You are given a **0-indexed** integer array `nums` representing the score of students in an exam. The teacher would like to form one **non-empty** group of students with maximal **strength**, where the strength of a group of students of indices `i 0`, `i 1`, `i 2`, ... , `i k` is defined as `nums[i 0 ] * nums[i 1 ] * nums[i 2 ] * ... * nums[i k ​]`.

Return the maximum strength of a group the teacher can create .

Example 1:

```
Input:  nums = [3,-1,-5,2,5,-9]
Output:  1350
Explanation:  One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.
```

Example 2:

```
Input:  nums = [-4,-5,-4]
Output:  20
Explanation:  Group the students at indices [0, 1] . Then, we&rsquo;ll have a resulting strength of 20. We cannot achieve greater strength.
```

**Constraints:**

- `1 <= nums.length <= 13`

- `-9 <= nums[i] <= 9`