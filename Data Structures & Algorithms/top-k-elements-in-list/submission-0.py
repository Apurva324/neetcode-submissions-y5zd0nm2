class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = dict()
        for i in range(0, len(nums)):
            if nums[i] in freq_map:
                freq_map[nums[i]] += 1
            else:
                freq_map[nums[i]] = 1
        sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        result = [item[0] for item in sorted_items[:k]]
        return result
        