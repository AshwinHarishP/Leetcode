import java.util.LinkedList;
import java.util.Queue;
class MyQueue {
    private Queue<Integer> Q;

    public MyQueue() {
        Q = new LinkedList<>();
    }
    
    public void push(int x) {
        Q.add(x);
    }
    
    public int pop() {
        return Q.poll();
    }
    
    public int peek() {
        return Q.peek();
    }
    
    public boolean empty() {
        return Q.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
