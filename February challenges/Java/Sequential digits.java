import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        int[] ls = {12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,1234,
                2345,3456,4567,5678,6789,12345,23456,34567,45678,56789,
                123456,234567,345678,456789,1234567,2345678,3456789,
                12345678,23456789,123456789};

        int st = binarySearchLeft(ls, low);
        int last = binarySearchRight(ls, high);
        List<Integer> res = new ArrayList<>();
        for (int i = st; i < last; i++) {
            res.add(ls[i]);
        }
        return res;
    }

    private int binarySearchLeft(int[] arr, int target) {
        int low = 0;
        int high = arr.length;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] < target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }

    private int binarySearchRight(int[] arr, int target) {
        int low = 0;
        int high = arr.length;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] <= target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> result = solution.sequentialDigits(100, 300);
        System.out.println(result);
    }
}
