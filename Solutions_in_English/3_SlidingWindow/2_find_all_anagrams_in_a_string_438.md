# LeetCode Hot100 — 438. Find All Anagrams in a String

![alt text](<../../Snap_for_Questions/3_Sliding_Window_滑动窗口/english_verison/截屏2026-06-04 19.13.33.png>)

## 1. Problem Overview

Given two strings:

```text
s = "cbaebabacd"
p = "abc"
```

Find all starting indices of substrings in `s` that are anagrams of `p`.

An anagram means:

```text
The characters are the same,
but their order may be different.
```

Return:

```text
[0, 6]
```

Because:

```text
s[0:3] = "cba"
s[6:9] = "bac"
```

Both can be rearranged into:

```text
"abc"
```

---

## 2. What Is an Anagram?

An anagram satisfies:

```text
Same character types
Same character frequencies
Different character order is allowed
```

For example:

```text
abc
acb
bac
bca
cab
cba
```

All of them are anagrams of each other.

---

## 3. Core Idea (Fixed-Length Sliding Window)

Observe:

```text
p = "abc"
Length = 3
```

Therefore:

```text
Every substring of length 3 in s
must be checked.
```

For example:

```text
cba
bae
aeb
eba
bab
aba
bac
acd
```

---

The window size is always fixed:

```python
len(p)
```

For each step:

```text
Add one character from the right
Remove one character from the left
```

Compare:

```text
Current window frequency
==
Target frequency
```

If they are equal:

```text
An anagram is found.
```

---

## 4. ACM Version (Interview Style)

```python
from collections import Counter

s = input().strip()
p = input().strip()

need = Counter(p)
window = Counter()

left = 0
result = []

for right in range(len(s)):

    window[s[right]] += 1

    if right - left + 1 > len(p):

        window[s[left]] -= 1

        if window[s[left]] == 0:
            del window[s[left]]

        left += 1

    if right - left + 1 == len(p):

        if window == need:
            result.append(left)

print(result)
```

---

## 5. LeetCode Version

```python
from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        need = Counter(p)
        window = Counter()

        left = 0
        result = []

        for right in range(len(s)):

            # Add character from the right
            window[s[right]] += 1

            # Window becomes too large
            if right - left + 1 > len(p):

                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

            # Window size matches target size
            if right - left + 1 == len(p):

                if window == need:
                    result.append(left)

        return result
```

---

### Understanding These Two Lines

```python
window['a'] += 1
```

means:

```text
Increase the frequency of character 'a' by 1.
```

---

```python
window[s[left]] -= 1
```

means:

```text
The leftmost character leaves the window.
```

The essence of a sliding window is:

```text
Right side enters
Left side leaves
```

Just like a queue.

---

# 6. Code Explanation

## 1. Build the Target Frequency Table

```python
need = Counter(p)
```

Example:

```python
p = "abc"
```

Produces:

```python
{
 'a':1,
 'b':1,
 'c':1
}
```

---

## 2. Build the Current Window Frequency Table

```python
window = Counter()
```

Used to record:

```text
The frequency of each character
inside the current window.
```

---

## 3. Add a Character from the Right

```python
window[s[right]] += 1
```

Example:

```text
abc
```

Produces:

```python
{
'a':1,
'b':1,
'c':1
}
```

---

## 4. Window Too Large

If:

```python
right - left + 1 > len(p)
```

it means:

```text
The current window length
exceeds the target length.
```

Therefore:

```text
The leftmost character must be removed.
```

---

## 5. Remove the Left Character

```python
window[s[left]] -= 1
```

If the frequency becomes:

```python
0
```

remove the key:

```python
del window[s[left]]
```

Otherwise:

```text
Counter comparison may be affected.
```

---

## 6. Check Whether an Anagram Is Found

```python
if window == need:
```

This means:

```text
Same character types
Same character frequencies
```

Therefore:

```text
The current window is an anagram.
```

---

## 7. Save the Starting Index

```python
result.append(left)
```

Record:

```text
The left boundary of the current window.
```

---

# 7. Essential Python Syntax

## 1. Counter()

Import:

```python
from collections import Counter
```

Purpose:

```text
Quickly count the frequency
of each element.
```

Example:

```python
Counter("abc")
```

Result:

```python
{
'a':1,
'b':1,
'c':1
}
```

Used in this problem to:

```text
Count character frequencies
for both the target string
and the current window.
```

---

## 2. Counter[key] += 1

```python
window[ch] += 1
```

Purpose:

```text
Increase the frequency
of a character by one.
```

Used when:

```text
Expanding the window to the right.
```

---

## 3. Counter[key] -= 1

```python
window[ch] -= 1
```

Purpose:

```text
Decrease the frequency
of a character by one.
```

Used when:

```text
Moving the left pointer
and removing a character.
```

---

## 4. del dict[key]

```python
del window[ch]
```

Purpose:

```text
Delete a key-value pair
from the dictionary.
```

Used when:

```text
The frequency becomes zero.
```

---

## 5. dict1 == dict2

```python
window == need
```

Purpose:

```text
Check whether two dictionaries
have exactly the same keys and values.
```

Used when:

```text
Determining whether the current window
is an anagram.
```

---

## 6. list.append()

```python
result.append(left)
```

Purpose:

```text
Append an element
to the end of a list.
```

Used when:

```text
Recording the starting index
of an anagram.
```

---

## 7. len()

```python
len(p)
```

Purpose:

```text
Return the length of an object.
```

Used when:

```text
Determining the fixed window size.
```

---

## 8. Fixed-Length Sliding Window

Window size:

```python
len(p)
```

Characteristic:

```text
The window size remains constant.
```

Used when:

```text
All candidate substrings
must have the same length as p.
```

---

## 9. right - left + 1

```python
right - left + 1
```

Purpose:

```text
Calculate the current window length.
```

Used when:

```text
Checking whether the window
has reached the target size.
```

---

## 10. for ... in range()

```python
for right in range(len(s)):
```

Purpose:

```text
Traverse the string by index.
```

Used when:

```text
Continuously expanding
the right boundary of the window.
```

---


# 8. Example Walkthrough

Input:

```text
s = "cbaebabacd"
p = "abc"
```

Target window length:

```text
3
```

---

## Step 1

Current window:

```text
c
```

Length is less than 3.

Continue expanding.

---

## Step 2

Current window:

```text
cb
```

Length is still less than 3.

Continue expanding.

---

## Step 3

Current window:

```text
cba
```

Frequency table:

```text
a = 1
b = 1
c = 1
```

Exactly matches `p`.

Record index:

```text
0
```

Current result:

```text
[0]
```

---

## Step 4

Slide the window to the right.

Current window:

```text
bae
```

Frequency table does not match.

Skip.

---

## Step 5

Current window:

```text
aeb
```

Frequency table does not match.

Skip.

---

## Step 6

Current window:

```text
eba
```

Frequency table does not match.

Skip.

---

## Step 7

Current window:

```text
bab
```

Frequency table does not match.

Skip.

---

## Step 8

Current window:

```text
aba
```

Frequency table does not match.

Skip.

---

## Step 9

Current window:

```text
bac
```

Frequency table:

```text
a = 1
b = 1
c = 1
```

Exactly matches `p`.

Record index:

```text
6
```

Final result:

```text
[0, 6]
```

---

# 9. Complexity Analysis

## Time Complexity

```text
O(n)
```

The sliding window scans the string only once.

---

## Space Complexity

```text
O(1)
```

The problem only contains:

```text
26 lowercase English letters
```

Therefore, the extra space is constant.

---

# 10. Interview Explanation Template

```text
This problem uses a fixed-length sliding window.

The window size always remains equal to len(p).

Counter is used to maintain the character frequencies
of both the target string and the current window.

Whenever the window moves:

- One character enters from the right.
- One character leaves from the left.

If the two frequency tables are identical,
the current window is an anagram.

Time Complexity: O(n)

Space Complexity: O(1)
```

---

# 11. Difference from LeetCode 3

| Problem | Window Type |
|----------|----------|
| 3. Longest Substring Without Repeating Characters | Variable-Length Window |
| 438. Find All Anagrams in a String | Fixed-Length Window |

---

## Memory Trick

```text
Longest
Shortest
Satisfy a condition

→ Variable-Length Window
```

```text
Fixed-size matching

→ Fixed-Length Window
```

This is one of the most important classifications
in Sliding Window problems.

---

# Additional Explanation

## Why Can Counter Use `+= 1` Directly?

A normal dictionary:

```python
d = {}
d['a'] += 1
```

will raise:

```python
KeyError
```

because:

```python
'a'
```

does not exist yet.

---

However:

```python
from collections import Counter

window = Counter()
```

`Counter` is a special hash table provided by Python.

For any missing key:

```python
window['a']
```

returns:

```python
0
```

instead of raising an error.

Therefore:

```python
window['a'] += 1
```

is equivalent to:

```python
window['a'] = 0 + 1
```

Result:

```python
Counter({'a': 1})
```

---

## The Essence of Counter

```python
window = Counter()
```

can be viewed as:

```python
{
    character: frequency
}
```

Example:

```python
Counter({
    'a': 2,
    'b': 1
})
```

means:

```text
'a' appears 2 times

'b' appears 1 time
```

---

# What Does `window[s[left]] -= 1` Mean?

It means:

```text
The leftmost character leaves the window.
```

Therefore:

```text
Its frequency decreases by one.
```

---

Example:

Current window frequency:

```python
{
    'a': 2,
    'b': 1
}
```

Left character:

```python
s[left] = 'a'
```

Execute:

```python
window['a'] -= 1
```

Result:

```python
{
    'a': 1,
    'b': 1
}
```

Meaning:

```text
One 'a' has been removed
from the current window.
```

---

## Core Understanding

```python
window[ch] += 1
```

means:

```text
Character enters the window.

Frequency +1
```

---

```python
window[ch] -= 1
```

means:

```text
Character leaves the window.

Frequency -1
```

---

# Why Do We Subtract 1?

Because the essence of a sliding window is:

```text
Right side enters

Left side leaves
```

Like a moving box.

---

Example:

```python
s = "cbaebabacd"
p = "abc"
```

Window length:

```python
len(p) = 3
```

---

Initial window:

```text
[c b a]
```

Frequency table:

```python
{
    'c':1,
    'b':1,
    'a':1
}
```

---

After sliding one step:

```text
c [b a e]
```

Two things happen:

### ① Character 'c' leaves

```python
window['c'] -= 1
```

Result:

```python
{
    'c':0,
    'b':1,
    'a':1
}
```

---

### ② Character 'e' enters

```python
window['e'] += 1
```

Result:

```python
{
    'c':0,
    'b':1,
    'a':1,
    'e':1
}
```

---

## Sliding Window Core Idea

Every time the window moves:

```text
Remove the left character

Add the right character
```

That is:

```python
window[s[left]] -= 1
window[s[right]] += 1
```

---

# Why Delete Keys with Frequency 0?

Code:

```python
if window[s[left]] == 0:
    del window[s[left]]
```

---

Example:

Current state:

```python
{
    'c':0,
    'b':1,
    'a':1,
    'e':1
}
```

After deletion:

```python
{
    'b':1,
    'a':1,
    'e':1
}
```

---

## Reason

Later we compare:

```python
if window == need:
```

Suppose:

```python
need = {
    'a':1,
    'b':1,
    'e':1
}
```

If we keep:

```python
window = {
    'a':1,
    'b':1,
    'e':1,
    'c':0
}
```

then:

```python
window == need
```

returns:

```python
False
```

because:

```text
The keys are not identical.
```

---

After removing the zero-frequency key:

```python
window = {
    'a':1,
    'b':1,
    'e':1
}
```

Now:

```python
window == need
```

returns:

```python
True
```

---

# One-Sentence Interview Memory Trick

```text
Counter is essentially:

character → frequency

window[ch] += 1
→ character enters the window

window[ch] -= 1
→ character leaves the window

When frequency becomes 0,
delete the key to ensure accurate
frequency-table comparison.
```

# Personal Notes

One of the most common mistakes in sliding window problems is confusing:

```python
len(s)
```

and

```python
len(p)
```

Remember:

```text
s = the main string being scanned

p = the target pattern
```

Therefore:

```python
for right in range(len(s))
```

must iterate over **s**, because the right pointer scans the main string.

---

### Memory Trick

```text
len(s)
↓
Controls traversal

len(p)
↓
Controls window size
```

Or simply:

```text
s controls movement

p controls size
```

This is one of the most common mistakes beginners make when learning sliding windows.