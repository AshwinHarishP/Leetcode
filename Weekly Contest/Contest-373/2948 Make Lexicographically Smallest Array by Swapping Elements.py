class Solution:
  def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
    tmp, num_to_group, curr_group = sorted(list(nums)), {}, 0
    prev_val = tmp[0]
    for v in tmp:
      if v - prev_val > limit:
        curr_group += 1

      num_to_group[v] = curr_group
      prev_val = v

    groups = [[] for _ in range(curr_group + 1)]
    positions = [0 for _ in range(curr_group + 1)]
    for pos, v in enumerate(nums):
      groups[num_to_group[v]].append(v)

    for g in groups:
      g.sort()

    for i, v in enumerate(nums):
      g = num_to_group[v]
      nums[i] = groups[g][positions[g]]
      positions[g] += 1

    return nums
