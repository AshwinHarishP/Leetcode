nums = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
prev_hashmap = {}

for n in nums:
    k = target - n
            
    if k in prev_hashmap:
        print([k, n])
    else:
        prev_hashmap[n] = True
