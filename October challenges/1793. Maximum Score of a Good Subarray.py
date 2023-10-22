class Solution:
    def maximumScore(self, nums, k):

        i = k
        j = k

        maxi = float('-inf')
        # Get the length of the nums list
        n = len(nums)
        # Initialize a variable mini to the value at position k
        mini = nums[k]

        # Loop while i is greater than or equal to 0 and j is less than n
        while i >= 0 and j < n:
            # Calculate the maximum score using mini and the current window size
            maxi = max(maxi, mini * (j - i + 1))

            # Check conditions for moving the pointers
            if j + 1 < n and i - 1 >= 0:
                # Compare the next elements to determine which pointer to move
                if nums[j + 1] > nums[i - 1]:
                    j += 1
                    mini = min(mini, nums[j])
                else:
                    i -= 1
                    mini = min(mini, nums[i])
            elif j + 1 >= n:
                i -= 1
                if i >= 0:
                    mini = min(mini, nums[i])
            elif i - 1 < 0:
                j += 1
                if j < n:
                    mini = min(mini, nums[j])

        # Return the maximum score
        return maxi
