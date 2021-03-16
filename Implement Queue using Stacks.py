# LeetCode232 https://leetcode.com/problems/implement-queue-using-stacks/

# collections: Container datatypes(alternatives to Python's general purpose built-in containers, dict, list, set, and tuple)
import collections

class MyStack:
    def __init__(self):
        # deque: list-like container with fast appends and pops on either end
        # deque를 이용해서 stack 구현, stack을 2번 이용해서 queue 구현
        self.q = collections.deque()
        
    # 첫번째 stack에 요소 삽입: deque를 stack처럼 기능하기 위해 변형 필요 
    def push(self, x):
        self.q.append(x)
        # 여러 요소 삽입 후, 순서를 반대로 재정렬
        # 두번째 stack으로 이동할 때, 가장 마지막에 추가된 요소가 가장 먼저 pop되어야하기 때문
        for _ in range(len(self.q) - 1):
            # popleft()는 가장 왼쪽에 있는 요소 pop
            self.q.append(self.q.popleft())

    # 첫번째 stack에서 두번째 stack으로 이동
    # push를 통해 마지막에 추가된 요소가 가장 처음에 위치하게 되었으므로 popleft() 사용가능
    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0
