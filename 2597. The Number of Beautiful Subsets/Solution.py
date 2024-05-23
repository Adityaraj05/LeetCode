class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # nums = [2,4,6]
        # k = 2
        # [], [2], [4], [6], [2, 4], [2, 6], [4, 6], [2, 4, 6]
        # [2], [4], [6], [2, 6] -> 4 ans
        # SOLUTION
        # num - k or n + k

        pair_count = 0
        num_count = len(nums)

        def explore_pairs(index):
            nonlocal pair_count
            if num_count == index:
                pair_count += 1
                return

            current_num = nums[index]

            if current_num - k not in num_frequency and current_num + k not in num_frequency:
                num_frequency[current_num] += 1
                explore_pairs(index + 1)
                num_frequency[current_num] -= 1
                if num_frequency[current_num] == 0:
                    del num_frequency[current_num]

            explore_pairs(index + 1)

        num_frequency = defaultdict(int)
        explore_pairs(0)
        return pair_count - 1
