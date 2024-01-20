import java.util.ArrayList;
import java.util.Stack;

class Solution {
    public int sumSubarrayMins(int[] arr) {
        final int MOD = 1_000_000_007;
        int n = arr.length;
        int[] left = new int[n];
        int[] right = new int[n];
        Stack<Integer> stLeft = new Stack<>();
        Stack<Integer> stRight = new Stack();

        // Calculate left boundaries
        for (int i = 0; i < n; i++) {
            while (!stLeft.isEmpty() && arr[i] <= arr[stLeft.peek()]) {
                stLeft.pop();
            }
            left[i] = stLeft.isEmpty() ? -1 : stLeft.peek();
            stLeft.push(i);
        }

        // Calculate right boundaries
        for (int i = n - 1; i >= 0; i--) {
            while (!stRight.isEmpty() && arr[i] < arr[stRight.peek()]) {
                stRight.pop();
            }
            right[i] = stRight.isEmpty() ? n : stRight.peek();
            stRight.push(i);
        }

        // Calculate the result
        long result = 0;
        for (int i = 0; i < n; i++) {
            result = (result + (long) arr[i] * (i - left[i]) * (right[i] - i)) % MOD;
        }

        return (int) result;
    }
}
