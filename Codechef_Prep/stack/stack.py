'''
    - Stack is a linear data structure which follows a particular order in which the operations are performed
    - The order may be LIFO(Last In First Out) or FILO(First In Last Out)
    - Stack operations:
        - Push O(1)
        - Pop O(1)
        - Empty O(1)
        - Peek O(1)
'''

class UnderflowException(Exception):
    pass

class OverflowException(Exception):
    pass

class Stack(object):
    def __init__(self):
        self._stack = []
        self.__top = -1

    def __str__(self):
        return ', '.join([str(i) for i in self._stack])

    def push(self, element):
        '''
            :param element: data element to be pushed onto stack
        '''
        self._stack.append(element)
        self.__top += 1
        return

    def pop(self):
        '''
            pops the topmost element from stack
        '''
        if not self.is_empty():
            self.__top -= 1
            value = self._stack[self.__top + 1]
            del self._stack[self.__top + 1]
            return value
        else:
            raise UnderflowException

    def is_empty(self):
        '''
            returns True if stack is empty else returns false
        '''
        return len(self._stack) == 0

    def peek(self):
        '''
            returns the top element from the stack
        '''
        if self.is_empty():
            return -1
        return self._stack[self.__top]
        
if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack)
    print(stack.peek())
    stack.pop()
    stack.pop()
    print(stack)
