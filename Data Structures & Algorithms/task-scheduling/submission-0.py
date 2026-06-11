class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks).values()
        maxf = max(counts)
        maxf_f = list(counts).count(maxf)

        return max( (maxf-1)*(n+1) + maxf_f, len(tasks) )