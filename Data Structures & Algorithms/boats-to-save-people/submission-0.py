class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        l = 0
        r = len(people) - 1

        while l <= r:
            remaining = limit - people[r]
            if remaining >= people[l]:
                l += 1
            r -= 1
            boat += 1
        return boat