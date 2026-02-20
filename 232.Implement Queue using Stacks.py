#
# @lc app=leetcode id=232 lang=python3
# @lcpr version=30400
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.s1 = [] 
        self.s2 = []

    # 添加元素到队尾
    def push(self, x: int) -> None:
        self.s1.append(x)
    
    # 删除队头元素并返回
    def pop(self) -> int:
        self.peek()
        return self.s2.pop() 

    # 返回队头元素
    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]
        
    # 判断队列是否为空
    def empty(self) -> bool:
        return not self.s1 and not self.s2 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end



#
# @lcpr case=start
# ["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]\n
# @lcpr case=end

#

