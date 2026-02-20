#
# @lc app=leetcode id=225 lang=python3
# @lcpr version=30400
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack:

    def __init__(self):
        self.q = [] 
        self.top_elem = 0 

    def push(self, x: int) -> None:
        self.q.append(x)
        self.top_elem = x 

    def pop(self) -> int:
        size = len(self.q)
        # 我们需要留下最后一个元素不处理（它是要被弹出的人）
        # 处理前 size - 1 个元素
        while size > 2:
            self.q.append(self.q.pop(0))
            size -= 1
        
        # 关键点：倒数第二个元素重新入队时，它是新的栈顶
        if size == 2:
            new_top = self.q.pop(0)
            self.q.append(new_top)
            self.top_elem = new_top
            
        # 弹出最初的那个“末尾元素”
        return self.q.pop(0)

    def top(self) -> int:
        return self.top_elem 

    def empty(self) -> bool:
        return len(self.q) == 0 
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end



#
# @lcpr case=start
# ["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]\n
# @lcpr case=end

#

