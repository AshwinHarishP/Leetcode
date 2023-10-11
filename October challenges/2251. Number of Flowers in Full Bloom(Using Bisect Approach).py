from bisect import bisect_left,bisect_right
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start_time = sorted(start for start,end in flowers)
        end_time = sorted(end for start,end in flowers)

        for i in range(len(people)):
            
            right_index = bisect_right(start_time, people[i])
            left_index = bisect_left(end_time, people[i])

            people[i] = right_index - left_index
        return people
