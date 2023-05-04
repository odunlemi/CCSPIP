# The Towers of Hanoi

# Modelling a stack
from typing import TypeVar, Generic, List  # the import of Generic enables the class Stack to be generic over a particular type in type hints
T = TypeVar('T')
# The arbitrary type T is defined here can be any type
# When a type hint is later used for a Stack to solve the Hanoi problem, it it type-hinted as Stack[int]
# Which means T is filled with the type int; the stack is a stack of integers

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    def push(self, item: T) -> None:
        self._container.append(item)
    def pop(self) -> T:
        return self._container.pop()
    # The class Stack implements __repr__() so the contents of the 'towers' are easily explored 
    def __repr__(self) -> str:  # __repr__() is what will output when print() is applied to a stack
        return repr(self._container)
    
# Defining the 'towers' as Stacks and filling the first with discs
num_discs: int = 3  # discs
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for _ in range(1, num_discs + 1):
    tower_a.push(_)

# A recursive algorithm to move the discs
def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n -1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)

if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)