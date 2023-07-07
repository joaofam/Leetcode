class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in nums:
                d[n] =+ 1
            else:
                d[n] = 1
        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

        result = []
        i = 0
        for num, count in d.items():
            result.append(num)
            i += 1
            if i == k:
                break

        return result
