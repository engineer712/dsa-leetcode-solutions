# The goal is to schedule tasks so that the same task appears again only after a **cooldown period `n`**. To minimize idle time, we place the most frequent tasks first and fill the remaining gaps with other tasks.

# **Approach:**
#  Count the **frequency of each task** using a hash map.
#  Find the **maximum frequency (`max_freq`)** among all tasks.
#  Count how many tasks have this **maximum frequency (`max_freq_elements`)**.
#  Compute the minimum required slots using
#  [ (max_freq - 1)*(n+1) + max_freq_elements ]
#  Return **max(calculated slots, total number of tasks)** to handle cases where idle slots are not needed.

# Why this approach only:
# The task with the **highest frequency determines the structure of the schedule** because identical tasks must be separated by `n` intervals. 
# Other tasks simply **fill the idle slots**, ensuring the minimum total time.


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        hashi = {}
        for i in tasks:
            hashi[i] = hashi.get(i,0)+1
        freq = list(hashi.values())
        max_freq = max(freq)
        max_freq_elements = 0
        for i in range(0,len(freq)):
            if freq[i] == max_freq:
                max_freq_elements += 1
        res = (max_freq - 1)*(n+1) + max_freq_elements
        return max(res,len(tasks))
