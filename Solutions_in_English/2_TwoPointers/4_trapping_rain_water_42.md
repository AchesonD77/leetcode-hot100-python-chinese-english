# LeetCode 42. Trapping Rain Water

**Difficulty:** Hard  
**Technique:** Two Pointers  
**Core Idea:** Shorter Boundary Determines Water Level

![
](<../../Snap_for_Questions/2_TwoPointers_双指针/english_verison/截屏2026-05-31 23.53.50.png>)
---

# 1. Problem Overview

Given an elevation map represented by an array:

```python
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

Each number represents the height of a bar.

Your task is to calculate:

```text
How much rainwater can be trapped after raining.
```

---

# 2. Key Formula (Most Important)

The amount of water trapped at position `i` depends on:

- The tallest bar on the left
- The tallest bar on the right

Water level at position `i`:

```text
min(left_max, right_max)
```

Therefore:

```text
water[i] = min(left_max, right_max) - height[i]
```

---

# 3. Core Idea (Two Pointers)

Use two pointers:

```python
left
right
```

And maintain:

```python
left_max
right_max
```

At every step:

```text
Move the side with the smaller maximum height.
```

Because:

```text
The shorter boundary determines the water level.
```

---

# 4. Why Move the Smaller Side?

Suppose:

```text
left_max < right_max
```

This means:

```text
The left side is the limiting boundary.
```

Since the right boundary is already taller:

```text
The water trapped at left is completely determined by left_max.
```

So we can safely calculate:

```python
left_max - height[left]
```

Then move:

```python
left += 1
```

---

# 5. LeetCode Solution

```python
class Solution:
    def trap(self, height: list[int]) -> int:

        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        result = 0

        while left < right:

            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:

                result += left_max - height[left]
                left += 1

            else:

                result += right_max - height[right]
                right -= 1

        return result
```

---

# 6. ACM Interview Version

## Input Format

```text
0 1 0 2 1 0 1 3 2 1 2 1
```

## ACM Code

```python
def trap(height):

    left = 0
    right = len(height) - 1

    left_max = 0
    right_max = 0

    result = 0

    while left < right:

        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        if left_max < right_max:

            result += left_max - height[left]
            left += 1

        else:

            result += right_max - height[right]
            right -= 1

    return result


# ACM Input
height = list(map(int, input().split()))

print(trap(height))
```

---

# 7. Code Explanation

## Step 1. Initialize Two Pointers

```python
left = 0
right = len(height) - 1
```

- `left` starts from the beginning.
- `right` starts from the end.

---

## Step 2. Track Maximum Heights

```python
left_max = 0
right_max = 0
```

Store:

```text
The highest wall seen so far from both sides.
```

---

## Step 3. Store Total Water

```python
result = 0
```

Used to accumulate trapped rainwater.

---

## Step 4. Main Loop

```python
while left < right:
```

Continue until the two pointers meet.

Key rule:

```text
Always process the side with the lower maximum boundary.
```

---

## Step 5. Update Left Maximum

```python
left_max = max(left_max, height[left])
```

Update the highest wall seen from the left.

---

## Step 6. Update Right Maximum

```python
right_max = max(right_max, height[right])
```

Update the highest wall seen from the right.

---

## Step 7. Left Side Is Lower

```python
if left_max < right_max:
```

The left boundary is the bottleneck.

According to the bucket principle:

```text
Water level is limited by the shorter wall.
```

Calculate trapped water:

```python
result += left_max - height[left]
```

Move:

```python
left += 1
```

---

## Step 8. Right Side Is Lower

```python
else:
```

The right boundary is the bottleneck.

Calculate trapped water:

```python
result += right_max - height[right]
```

Move:

```python
right -= 1
```

---

## Step 9. Return Answer

```python
return result
```

Return the total trapped rainwater.

---

# 8. Example Walkthrough

Input:

```python
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

Suppose:

```text
Current Height = 0
Left Max = 2
Right Max = 3
```

Then:

```text
Water = min(2,3) - 0
      = 2
```

So:

```text
2 units of water can be trapped.
```

Final answer:

```python
6
```

---

# 9. Complexity Analysis

## Time Complexity

```text
O(n)
```

Each element is visited at most once.

---

## Space Complexity

```text
O(1)
```

Only a few extra variables are used.

---

# 10. Essential Python Syntax

## 1. max()

```python
max(a, b)
```

Returns the larger value.

Example:

```python
max(3, 5)
# 5
```

---

## 2. map()

```python
map(int, input().split())
```

Convert strings into integers.

Input:

```text
1 2 3 4
```

Output:

```python
[1, 2, 3, 4]
```

---

## 3. list()

```python
list(...)
```

Convert an iterable into a list.

Example:

```python
list(map(int, input().split()))
```

---

## 4. while Loop

```python
while left < right:
```

Classic Two-Pointer pattern.

Why use `while`?

```text
The number of iterations is unknown.
```

The loop ends when:

```text
The two pointers meet.
```

---

## 5. += Operator

```python
result += x
```

Equivalent to:

```python
result = result + x
```

---

# 11. Algorithm Pattern to Remember

## Two Pointers + Shorter Boundary Principle

Core Rule:

```text
Move the side with the smaller maximum height.
```

Because:

```text
The shorter boundary determines the current water level.
```

This same idea appears in:

- Trapping Rain Water
- Container With Most Water

---

# 12. One-Sentence Memory Trick

```text
The water trapped at a position is determined by the shorter of the tallest walls on its left and right.
```

---

# 13. Interview Cheat Sheet

```text
1. Maintain left_max and right_max.

2. Compare left_max and right_max.

3. Move the side with the smaller maximum.

4. Water trapped:
   smaller_max - current_height

5. Time: O(n)

6. Space: O(1)
```

## Ultimate Formula

```text
water[i] =
min(max_left, max_right) - height[i]
```

## Ultimate Rule

```text
Shorter boundary wins.
Move the smaller side.
```