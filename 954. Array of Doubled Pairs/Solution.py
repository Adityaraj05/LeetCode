class Solution:
  def canReorderDoubled(self, arr: List[int]) -> bool:
    # count = Counter({4: 1, -2: 1, 2: 1, -4: 1})
    count = collections.Counter(arr)
    # We then iterate through the keys of the count dictionary, sorted based on their absolute values:
    for key in sorted(count, key=abs):
      if count[key] > count[2 * key]:
        return False
      count[2 * key] -= count[key]

    return True
