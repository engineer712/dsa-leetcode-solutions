# Approach: Two Pointers + Greedy

# Sort the people array to easily pair the lightest and heaviest persons.
# Use two pointers:
# l → lightest person
# r → heaviest person
# If people[l] + people[r] <= limit, pair them in one boat and move l forward.
# Always place the heaviest person (r) in a boat, so decrement r and increase boat count.
# Continue until pointers meet.
# If one person is left (l == r), add one more boat.


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        l = 0
        r = len(people) - 1
        ans = 0
        while l<r:
            total = people[l] + people[r]
            if total <= limit:
                l = l+1
            ans+=1
            r-=1
        if l==r:
            ans+=1
        return ans






       
        
