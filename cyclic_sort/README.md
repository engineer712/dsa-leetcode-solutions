# 🔁 Cyclic Sort Pattern

Cyclic Sort is a powerful array manipulation technique used when the input array contains numbers in the range **1 to N** (or `0 to N`) and you need to find missing, duplicate, or corrupt numbers efficiently.

---

## 🧠 Core Idea

Every number has a **correct position**.

* If range is `1..N` → correct index = `value - 1`
* If range is `0..N` → correct index = `value`

We swap numbers until each one is placed at its correct index.

---

## 🔍 How to Identify This Pattern

Look for phrases like:

* “Array contains numbers from 1 to N”
* “One number is missing / duplicated”
* “Find the corrupt pair”
* “Find first missing positive”

---

## 🛠️ Template

```python
i = 0
while i < len(nums):
    correct = nums[i] - 1
    if nums[i] != nums[correct]:
        nums[i], nums[correct] = nums[correct], nums[i]
    else:
        i += 1
```

---
## ⚠️ Common Mistakes

* Incrementing index after swap
* Not handling duplicates → infinite loop
* Using when numbers are not in range
* Forgetting final scan after sorting

---

## 🧪 Must Practice Problems

* LeetCode 268 – Missing Number
* LeetCode 287 – Find Duplicate Number
* LeetCode 442 – Find All Duplicates
* LeetCode 41 – First Missing Positive

---


