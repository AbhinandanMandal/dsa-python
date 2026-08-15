# 01 Stack Introduction

A **Stack** is a **linear data structure** that follows a specific order in which operations are performed.

## LIFO (Last In, First Out)

The **LIFO (Last In, First Out)** principle states that the element inserted last is the first one to be removed.

### Example

Think of a stack of plates:

- The last plate placed on top is the first one removed.
- The plate placed first stays at the bottom until all plates above it are removed.

```
    Top
   ┌───┐
   │ 4 │ ← Removed first
   ├───┤
   │ 3 │
   ├───┤
   │ 2 │
   ├───┤
   │ 1 │ ← Removed last
   └───┘
```

---

# Basic Operations

| Operation          | Description                                 |
| ------------------ | ------------------------------------------- |
| `push()`           | Inserts an element into the stack           |
| `pop()`            | Removes the top element from the stack      |
| `top()` / `peek()` | Returns the top element without removing it |
| `isEmpty()`        | Returns `true` if the stack is empty        |
| `size()`           | Returns the number of elements in the stack |

---

# Push Operation

Adds a new element to the top of the stack.

> If the stack is already full (for fixed-size implementations), it results in an **Overflow** condition.

## Algorithm

```text
begin
    if stack is full
        return
    endif

    top = top + 1
    stack[top] = value
end
```

### Illustration

Before Push(40)

```
Top
 ↓
┌────┐
│ 30 │
├────┤
│ 20 │
├────┤
│ 10 │
└────┘
```

After Push(40)

```
Top
 ↓
┌────┐
│ 40 │
├────┤
│ 30 │
├────┤
│ 20 │
├────┤
│ 10 │
└────┘
```

---

# Pop Operation

Removes the topmost element from the stack.

> If the stack is empty, it results in an **Underflow** condition.

## Algorithm

```text
begin
    if stack is empty
        return
    endif

    value = stack[top]
    top = top - 1
    return value
end
```

### Illustration

Before Pop()

```
Top
 ↓
┌────┐
│ 40 │
├────┤
│ 30 │
├────┤
│ 20 │
├────┤
│ 10 │
└────┘
```

After Pop()

```
Top
 ↓
┌────┐
│ 30 │
├────┤
│ 20 │
├────┤
│ 10 │
└────┘
```

---

# Top (Peek)

Returns the top element **without removing it**.

## Algorithm

```text
begin
    return stack[top]
end
```

---

# isEmpty()

Checks whether the stack contains any elements.

## Algorithm

```text
begin
    if top < 0
        return true
    else
        return false
end
```

---

# size()

Returns the total number of elements currently present in the stack.

```text
size = top + 1
```

---

# Practical Understanding

One of the simplest real-life examples of a stack is a pile of plates.

- Plates are placed one over another.
- The last plate placed is removed first.
- The first plate placed is removed last.

This perfectly follows the **LIFO (Last In, First Out)** principle.

Other examples include:

- Browser Back button
- Undo operation in text editors
- Function call stack
- Expression evaluation
- Parentheses matching

---

# Time Complexity

| Operation   | Time Complexity |
| ----------- | --------------- |
| `push()`    | **O(1)**        |
| `pop()`     | **O(1)**        |
| `top()`     | **O(1)**        |
| `isEmpty()` | **O(1)**        |
| `size()`    | **O(1)**        |

---

# Types of Stack

## 1. Register Stack

A **Register Stack** is implemented using CPU registers.

### Characteristics

- Very small storage capacity
- Extremely fast access
- Height is fixed
- Used inside processors for temporary storage

---

## 2. Memory Stack

A **Memory Stack** resides in the main memory (RAM).

### Characteristics

- Can store a large amount of data
- Flexible size (depending on available memory)
- Used by programs for:
  - Function calls
  - Local variables
  - Recursion
  - Runtime memory management

---

# Summary

- Stack is a **Linear Data Structure**
- Follows **LIFO (Last In, First Out)**
- Insertion → `push()`
- Deletion → `pop()`
- Access top → `top()`
- Check empty → `isEmpty()`
- Find size → `size()`
- All major operations take **O(1)** time.

---

# 02 Stack Implementation in Python

A **Stack** is a **linear data structure** that stores elements in **LIFO (Last In, First Out)** or **FILO (First In, Last Out)** order.

In a stack:

- New elements are inserted only at the **top**.
- Elements are removed only from the **top**.
- Insertion is called **Push**.
- Deletion is called **Pop**.

---

# Stack Operations

| Operation          | Description                                 | Time Complexity |
| ------------------ | ------------------------------------------- | --------------- |
| `empty()`          | Returns whether the stack is empty          | **O(1)**        |
| `size()`           | Returns the number of elements              | **O(1)**        |
| `top()` / `peek()` | Returns the top element without removing it | **O(1)**        |
| `push(x)`          | Inserts `x` at the top                      | **O(1)**        |
| `pop()`            | Removes the top element                     | **O(1)**        |

---

# Ways to Implement a Stack in Python

Python provides multiple ways to implement a stack:

1. Using **List**
2. Using **collections.deque**
3. Using **queue.LifoQueue**
4. Using a **Singly Linked List**

---

# 1. Stack using List

Python's built-in **list** can be used as a stack.

- `append()` → Push
- `pop()` → Pop

## Example

```python
# Stack using List

stack = []

# Push
stack.append('a')
stack.append('b')
stack.append('c')

print("Initial Stack:")
print(stack)

# Pop
print("\nElements popped:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\nStack after popping:")
print(stack)

# stack.pop()  # Raises IndexError
```

### Output

```text
Initial Stack:
['a', 'b', 'c']

Elements popped:
c
b
a

Stack after popping:
[]
```

### Advantages

- Very easy to use.
- Built into Python.
- No additional imports required.

### Disadvantages

As the list grows, Python may need to allocate a larger memory block and copy all elements, making some `append()` operations slower.

---

# 2. Stack using `collections.deque`

The **deque (Double Ended Queue)** from the `collections` module is preferred when frequent insertions and deletions are required.

Unlike lists, deque provides **O(1)** insertion and deletion from both ends.

## Example

```python
from collections import deque

stack = deque()

# Push
stack.append('a')
stack.append('b')
stack.append('c')

print("Initial Stack:")
print(stack)

# Pop
print("\nElements popped:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\nStack after popping:")
print(stack)

# stack.pop()  # Raises IndexError
```

### Output

```text
Initial Stack:
deque(['a', 'b', 'c'])

Elements popped:
c
b
a

Stack after popping:
deque([])
```

### Advantages

- Fast insertion and deletion from both ends.
- Better performance than lists for stack operations.

---

# 3. Stack using `queue.LifoQueue`

Python's `queue` module provides **LifoQueue**, a thread-safe stack implementation.

It is mainly used in **multithreaded applications**.

---

## Common Functions

| Function       | Description             |
| -------------- | ----------------------- |
| `put(item)`    | Push an element         |
| `get()`        | Pop an element          |
| `qsize()`      | Returns stack size      |
| `empty()`      | Returns `True` if empty |
| `full()`       | Returns `True` if full  |
| `put_nowait()` | Push without blocking   |
| `get_nowait()` | Pop without blocking    |

---

## Example

```python
from queue import LifoQueue

stack = LifoQueue(maxsize=3)

print(stack.qsize())

# Push
stack.put('a')
stack.put('b')
stack.put('c')

print("Full:", stack.full())
print("Size:", stack.qsize())

# Pop
print("\nElements popped:")
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty:", stack.empty())
```

### Output

```text
0

Full: True
Size: 3

Elements popped:
c
b
a

Empty: True
```

### Advantages

- Thread-safe.
- Suitable for concurrent programming.

### Disadvantages

- Slightly slower than `list` or `deque` because of synchronization overhead.

---

# 4. Stack using Singly Linked List

A stack can also be implemented using a **Singly Linked List**.

The head node represents the **top of the stack**.

Push and Pop operations are performed at the head, giving **O(1)** complexity.

---

## Operations

| Operation     | Description                   |
| ------------- | ----------------------------- |
| `getSize()`   | Returns stack size            |
| `isEmpty()`   | Checks whether stack is empty |
| `peek()`      | Returns the top element       |
| `push(value)` | Inserts at the head           |
| `pop()`       | Removes from the head         |

---

## Example

```python
# Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""

        while cur:
            out += str(cur.value) + "->"
            cur = cur.next

        return out[:-2]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")

        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):

        if self.isEmpty():
            raise Exception("Popping from an empty stack")

        remove = self.head.next
        self.head.next = remove.next
        self.size -= 1

        return remove.value


# Driver Code
stack = Stack()

for i in range(1, 11):
    stack.push(i)

print("Stack:", stack)

for _ in range(5):
    print("Pop:", stack.pop())

print("Stack:", stack)
```

### Output

```text
Stack:
10->9->8->7->6->5->4->3->2->1

Pop: 10
Pop: 9
Pop: 8
Pop: 7
Pop: 6

Stack:
5->4->3->2->1
```

---

# Comparison of Implementations

| Implementation  | Push   | Pop  | Thread Safe | Recommended                          |
| --------------- | ------ | ---- | ----------- | ------------------------------------ |
| **List**        | O(1)\* | O(1) | ❌          | Small programs                       |
| **deque**       | O(1)   | O(1) | ❌          | ✅ Best general-purpose stack        |
| **LifoQueue**   | O(1)   | O(1) | ✅          | Multithreading                       |
| **Linked List** | O(1)   | O(1) | ❌          | Educational / Custom implementations |

> **Note:** `list.append()` is _amortized_ **O(1)** because occasional memory reallocations may occur.

---

# Which Implementation Should You Use?

| Scenario                   | Recommended Choice     |
| -------------------------- | ---------------------- |
| General-purpose stack      | ✅ `collections.deque` |
| Small scripts              | `list`                 |
| Multithreaded applications | `queue.LifoQueue`      |
| Learning data structures   | Singly Linked List     |

---

# Summary

- A **Stack** follows the **LIFO (Last In, First Out)** principle.
- Python supports multiple stack implementations.
- **`collections.deque`** is generally the most efficient and recommended implementation.
- **`queue.LifoQueue`** is ideal for thread-safe applications.
- **Linked List** implementation helps understand how stacks work internally.

---

# 03 Stack Implementation using Linked List in Python

A **Stack** can be efficiently implemented using a **Singly Linked List**. Since a stack follows the **LIFO (Last In, First Out)** principle, all insertions and deletions are performed at the **head (top)** of the linked list.

Unlike an array-based implementation, a linked list implementation **grows and shrinks dynamically**, eliminating the need for a fixed-size stack.

---

# How Stack Works with a Linked List

In this implementation:

- The **head node** acts as the **top** of the stack.
- Every **Push** inserts a new node at the beginning.
- Every **Pop** removes the first node.
- **Peek** returns the value of the head node.
- **Display** traverses the linked list from head to tail.

```
Top
 ↓
┌────┐    ┌────┐    ┌────┐    ┌────┐
│ 44 │──► │ 33 │──► │ 22 │──► │ 11 │──► NULL
└────┘    └────┘    └────┘    └────┘
```

---

# Why Use a Linked List?

### Advantages

- Dynamic memory allocation.
- No fixed capacity.
- No risk of stack overflow due to array size limitations.
- Push and Pop operations are always performed at the head.

### Disadvantages

- Requires extra memory for pointers.
- Slightly slower than arrays due to pointer manipulation.

---

# Stack Operations

| Operation    | Description                                |
| ------------ | ------------------------------------------ |
| `push(data)` | Insert a new element at the top            |
| `pop()`      | Remove and return the top element          |
| `peek()`     | Return the top element without removing it |
| `display()`  | Print all stack elements                   |

---

# Push Operation

Insert a new node at the beginning of the linked list.

## Algorithm

```text
1. Create a new node.
2. Store the data in the node.
3. Make the new node point to the current head.
4. Update head to the new node.
```

### Illustration

Before Push(44)

```
Top
 ↓
┌────┐    ┌────┐    ┌────┐
│ 33 │──► │ 22 │──► │ 11 │──► NULL
└────┘    └────┘    └────┘
```

After Push(44)

```
Top
 ↓
┌────┐    ┌────┐    ┌────┐    ┌────┐
│ 44 │──► │ 33 │──► │ 22 │──► │ 11 │──► NULL
└────┘    └────┘    └────┘    └────┘
```

---

# Pop Operation

Remove the node at the beginning of the linked list.

## Algorithm

```text
1. Check if the stack is empty.
2. Store the head node in a temporary pointer.
3. Move head to the next node.
4. Delete the old head node.
5. Return its value.
```

### Illustration

Before Pop()

```
Top
 ↓
┌────┐    ┌────┐    ┌────┐    ┌────┐
│ 44 │──► │ 33 │──► │ 22 │──► │ 11 │──► NULL
└────┘    └────┘    └────┘    └────┘
```

After Pop()

```
Top
 ↓
┌────┐    ┌────┐    ┌────┐
│ 33 │──► │ 22 │──► │ 11 │──► NULL
└────┘    └────┘    └────┘
```

---

# Peek Operation

Return the data stored in the top node without removing it.

## Algorithm

```text
1. Check if the stack is empty.
2. Return head.data.
```

---

# Display Operation

Traverse the linked list from the head to the last node and print each element.

## Algorithm

```text
1. Create a temporary pointer.
2. Initialize it with head.
3. Traverse until NULL.
4. Print each node.
```

---

# Python Implementation

```python
# Stack implementation using a Singly Linked List

class Node:
    """Represents a node of the linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    # Check whether the stack is empty
    def isempty(self):
        return self.head is None

    # Push an element onto the stack
    def push(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Pop the top element
    def pop():

        if self.isempty():
            return None

        popped = self.head
        self.head = self.head.next
        popped.next = None

        return popped.data

    # Return the top element
    def peek(self):

        if self.isempty():
            return None

        return self.head.data

    # Display stack contents
    def display(self):

        if self.isempty():
            print("Stack Underflow")
            return

        current = self.head

        while current:
            print(current.data, end="")
            current = current.next

            if current:
                print(" -> ", end="")

        print()


# Driver Code
if __name__ == "__main__":

    stack = Stack()

    stack.push(11)
    stack.push(22)
    stack.push(33)
    stack.push(44)

    print("Stack:")
    stack.display()

    print("Top Element:", stack.peek())

    stack.pop()
    stack.pop()

    print("\nStack after popping:")
    stack.display()

    print("Top Element:", stack.peek())
```

---

# Output

```text
Stack:
44 -> 33 -> 22 -> 11

Top Element: 44

Stack after popping:
22 -> 11

Top Element: 22
```

---

# Complexity Analysis

| Operation   | Time Complexity |
| ----------- | --------------- |
| `push()`    | **O(1)**        |
| `pop()`     | **O(1)**        |
| `peek()`    | **O(1)**        |
| `isEmpty()` | **O(1)**        |
| `display()` | **O(N)**        |

---

# Space Complexity

- **Auxiliary Space:** **O(N)**

where **N** is the number of elements stored in the stack.

---

# Advantages over Array Implementation

| Linked List Stack                 | Array Stack                                  |
| --------------------------------- | -------------------------------------------- |
| Dynamic size                      | Fixed size (unless resized)                  |
| No overflow due to fixed capacity | May overflow if capacity is reached          |
| No memory wastage                 | Extra unused capacity may exist              |
| O(1) Push/Pop                     | O(1) Push/Pop (amortized for dynamic arrays) |

---

# Summary

- The **head node** represents the **top** of the stack.
- **Push** inserts a node at the beginning.
- **Pop** removes the first node.
- **Peek** returns the first node without removing it.
- **Display** traverses the linked list from top to bottom.
- Push, Pop, and Peek all run in **O(1)** time, making the linked list an efficient implementation for stacks.

---

# 04 Applications of Stack

A **Stack** is a **linear data structure** that follows the **LIFO (Last In, First Out)** principle. The last element inserted into the stack is the first one to be removed.

A real-life example is a **stack of plates**:

- Plates are placed one on top of another.
- The last plate placed is removed first.
- The first plate placed is removed last.

Stacks can be implemented using:

- Arrays
- Linked Lists

---

# Basic Stack Operations

## Primary Operations

| Operation    | Description                               |
| ------------ | ----------------------------------------- |
| `push(data)` | Insert an element at the top of the stack |
| `pop()`      | Remove and return the top element         |

---

## Auxiliary Operations

| Operation          | Description                                                      |
| ------------------ | ---------------------------------------------------------------- |
| `top()` / `peek()` | Returns the top element without removing it                      |
| `size()`           | Returns the number of elements in the stack                      |
| `isEmpty()`        | Returns `True` if the stack is empty                             |
| `isFull()`         | Returns `True` if the stack is full (only for fixed-size stacks) |

---

# Types of Stack

## 1. Register Stack

A **Register Stack** is implemented using CPU registers.

### Characteristics

- Small storage capacity
- Very fast access
- Fixed size
- Used internally by processors

---

## 2. Memory Stack

A **Memory Stack** is stored in the system's main memory (RAM).

### Characteristics

- Can store a large amount of data
- Flexible size
- Used during program execution
- Supports function calls and recursion

---

# What is the Top of a Stack?

The **Top** is a pointer (or index) that always refers to the **topmost element** of the stack.

All stack operations such as:

- Push
- Pop
- Peek

are performed using the **Top** pointer.

```
Top
 ↓
┌────┐
│ 40 │
├────┤
│ 30 │
├────┤
│ 20 │
├────┤
│ 10 │
└────┘
```

---

# Applications of Stack

Stacks are widely used in computer science because of their **LIFO** behavior.

## 1. Expression Evaluation

Stacks are used to evaluate mathematical expressions such as:

- Prefix expressions
- Postfix expressions

Example:

```
2 3 + 5 *
```

---

## 2. Infix to Postfix / Prefix Conversion

Compilers use stacks to convert expressions.

Example:

```
Infix:
A + B * C

Postfix:
ABC*+

Prefix:
+A*BC
```

---

## 3. Parentheses Matching

Stacks help determine whether parentheses are balanced.

Example:

```text
((a+b)*(c+d))
```

Balanced ✔️

```text
((a+b)
```

Not Balanced ❌

---

## 4. HTML and XML Tag Matching

Browsers use stacks to verify nested tags.

Example:

```html
<html>
  <body>
    <h1>Hello</h1>
  </body>
</html>
```

---

## 5. Function Calls (Call Stack)

Every function call is pushed onto the **Call Stack**.

When a function finishes, it is popped from the stack.

Example:

```
main()

↓

A()

↓

B()

↓

Return B

↓

Return A

↓

Return main
```

---

## 6. Recursion

Recursive functions rely on the call stack to store:

- Local variables
- Parameters
- Return addresses

Example:

```python
factorial(5)
```

---

## 7. Undo / Redo Operations

Applications such as:

- Microsoft Word
- VS Code
- Photoshop

store previous actions using stacks.

```
Write A
↓

Write B
↓

Write C
↓

Undo

↓

C removed
```

---

## 8. Browser History

Web browsers maintain visited pages using stacks.

```
Page A

↓

Page B

↓

Page C

↓

Back Button

↓

Page B
```

---

## 9. Backtracking Algorithms

Stacks are heavily used in:

- Maze solving
- Sudoku solving
- N-Queens Problem
- Depth First Search (DFS)

---

## 10. Depth First Search (DFS)

DFS uses an explicit stack (or recursion) to traverse graphs and trees.

```
A
│
├── B
│   ├── D
│   └── E
│
└── C
```

Traversal:

```
A → B → D → E → C
```

---

## 11. String Reversal

Stacks can reverse strings.

Example:

```
Input:
HELLO

Push:
H E L L O

Pop:
O L L E H
```

---

## 12. Memory Management

Operating systems use stacks to store:

- Function parameters
- Local variables
- Return addresses

---

# Real-Life Applications

Some everyday examples of stacks include:

- 📀 CD/DVD stand
- 📚 Stack of books
- ✍️ Undo/Redo in text editors
- 🌐 Browser Back button
- 📞 Call history
- 📧 Email history
- 🖼️ Gallery (latest images first)
- 📥 YouTube downloads
- 🔔 Notification panels
- 📱 Recent apps list (in many operating systems)

---

# Advantages of Stack

- Simple and easy to implement.
- Follows the efficient **LIFO** principle.
- Supports **O(1)** Push and Pop operations.
- Useful for recursion and function calls.
- Helps in systematic memory management.
- Used by virtual machines such as the **JVM**.
- Automatic cleanup of local variables after function returns.
- Provides better control over memory allocation and deallocation.
- More secure since memory is automatically managed.

---

# Disadvantages of Stack

- Limited memory (stack size is finite).
- Stack size must be predefined in some implementations.
- Excessive recursion may cause **Stack Overflow**.
- Random access is not possible.
- Only the top element can be accessed directly.
- Overflow or memory exhaustion may terminate the program.

---

# Complexity Analysis

| Operation   | Time Complexity |
| ----------- | --------------- |
| `push()`    | **O(1)**        |
| `pop()`     | **O(1)**        |
| `peek()`    | **O(1)**        |
| `isEmpty()` | **O(1)**        |
| `size()`    | **O(1)**        |

---

# Summary

- A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle.
- The **Top** pointer identifies the current top element.
- Stacks are fundamental in:
  - Expression evaluation
  - Function calls
  - Recursion
  - Browser history
  - Undo/Redo systems
  - Backtracking algorithms
  - Depth First Search (DFS)
- Stack operations are highly efficient, with **O(1)** time complexity for insertion and deletion.

---

# 05 Stack with `getMin()` in **O(1)**

## Problem Statement

Design a special stack called **SpecialStack** that supports all standard stack operations along with an additional operation:

- `push(x)`
- `pop()`
- `peek()`
- `isEmpty()`
- `isFull()` _(for fixed-size stacks)_
- `getMin()` → Returns the minimum element currently present in the stack.

> **Requirement:** Every operation must run in **O(1)** time and **O(1)** extra space.

> **Constraint:** Only the standard **Stack** data structure may be used. No auxiliary arrays, lists, or additional stacks.

---

# Example

Consider the following stack:

```text
Top
 ↓
16
15
29
19
18
```

Calling:

```text
getMin()
```

returns

```text
15
```

After performing:

```text
pop()
pop()
```

The stack becomes:

```text
Top
 ↓
29
19
18
```

Now,

```text
getMin()
```

returns

```text
18
```

---

# Idea Behind the Solution

Instead of maintaining another stack to store minimum elements, we store only a single variable:

```python
minEle
```

which always stores the **current minimum** element.

Whenever a new minimum is pushed, we **encode** its value before storing it.

---

# Encoding Formula

If

```text
x < minEle
```

instead of pushing `x`, we push

```text
2*x - minEle
```

and update

```text
minEle = x
```

The encoded value helps recover the previous minimum when this element is popped.

---

# Push Operation

## Case 1: Stack is Empty

```text
Push x

↓

Insert x

↓

minEle = x
```

---

## Case 2: x ≥ minEle

Simply push the value.

```text
Push x

↓

Stack.push(x)
```

---

## Case 3: x < minEle

Push the encoded value.

```text
encoded = 2*x - minEle

Stack.push(encoded)

minEle = x
```

### Example

Previous minimum

```text
3
```

Push

```text
2
```

Encoded value

```text
2×2 − 3 = 1
```

Stack stores

```text
1
```

Current minimum becomes

```text
2
```

---

# Pop Operation

Suppose the top element is `y`.

---

## Case 1: y ≥ minEle

The popped value is the original value.

```text
Return y
```

Minimum remains unchanged.

---

## Case 2: y < minEle

The popped value is actually the current minimum.

Restore the previous minimum using

```text
previousMin = 2*minEle - y
```

Update

```text
minEle = previousMin
```

---

### Example

Current minimum

```text
2
```

Encoded value popped

```text
1
```

Restore previous minimum

```text
2×2 − 1 = 3
```

So,

```text
minEle = 3
```

---

# Important Observations

- The stack **does not always store the real values**.
- Whenever a new minimum is inserted, an **encoded value** is stored.
- The **actual minimum** is always available in the variable

```python
minEle
```

---

# Push Illustration

Insert values in order:

```text
3
5
2
1
1
-1
```

| Inserted | Stored in Stack | Current Minimum |
| -------- | --------------- | --------------- |
| 3        | 3               | 3               |
| 5        | 5               | 3               |
| 2        | 1               | 2               |
| 1        | 0               | 1               |
| 1        | 1               | 1               |
| -1       | -3              | -1              |

---

# Pop Illustration

Initial minimum

```text
-1
```

| Removed | Actual Removed | New Minimum |
| ------- | -------------- | ----------- |
| -3      | -1             | 1           |
| 1       | 1              | 1           |
| 0       | 1              | 2           |
| 1       | 2              | 3           |
| 5       | 5              | 3           |

---

# Python Implementation

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.minimum = None

    def isEmpty(self):
        return self.top is None

    def getMin(self):

        if self.isEmpty():
            print("Stack is empty")
            return

        print("Minimum Element:", self.minimum)

    def peek(self):

        if self.isEmpty():
            print("Stack is empty")
            return

        if self.top.value < self.minimum:
            print("Top Element:", self.minimum)
        else:
            print("Top Element:", self.top.value)

    def push(self, value):

        if self.top is None:

            self.top = Node(value)
            self.minimum = value

        elif value < self.minimum:

            encoded = 2 * value - self.minimum

            node = Node(encoded)
            node.next = self.top
            self.top = node

            self.minimum = value

        else:

            node = Node(value)
            node.next = self.top
            self.top = node

        print("Inserted:", value)

    def pop():

        if self.isEmpty():
            print("Stack is empty")
            return

        removed = self.top.value
        self.top = self.top.next

        if removed < self.minimum:

            print("Removed:", self.minimum)

            self.minimum = 2 * self.minimum - removed

        else:

            print("Removed:", removed)


# Driver Code
stack = Stack()

stack.push(3)
stack.push(5)

stack.getMin()

stack.push(2)
stack.push(1)

stack.getMin()

stack.pop()

stack.getMin()

stack.pop()

stack.peek()
```

---

# Output

```text
Inserted: 3
Inserted: 5

Minimum Element: 3

Inserted: 2
Inserted: 1

Minimum Element: 1

Removed: 1

Minimum Element: 2

Removed: 2

Top Element: 5
```

---

# Why Does the Encoding Work?

When

```text
x < minEle
```

we store

```text
encoded = 2*x - minEle
```

We know

```text
x < minEle
```

Therefore,

```text
x - minEle < 0
```

Adding `x` to both sides,

```text
2*x - minEle < x
```

Since

```text
x = new minimum
```

we get

```text
encoded < new minimum
```

Hence, whenever we pop an element smaller than `minEle`, we immediately know that it is **not a real value**, but an encoded one.

---

# Recovering the Previous Minimum

Suppose

```text
encoded = 2*x - previousMin
```

After insertion,

```text
minEle = x
```

While popping,

```text
previousMin = 2*minEle - encoded
```

Substituting,

```text
= 2*x - (2*x - previousMin)

= previousMin
```

Thus, the previous minimum is recovered in **O(1)** time.

---

# Complexity Analysis

| Operation  | Time Complexity | Extra Space |
| ---------- | --------------- | ----------- |
| `push()`   | **O(1)**        | **O(1)**    |
| `pop()`    | **O(1)**        | **O(1)**    |
| `peek()`   | **O(1)**        | **O(1)**    |
| `getMin()` | **O(1)**        | **O(1)**    |

---

# Advantages

- Retrieves the minimum element in **constant time**.
- Uses only **one stack**.
- Requires only **O(1)** extra space.
- No auxiliary stack is needed.
- Every operation runs in **O(1)** time.

---

# Summary

- Maintain a variable `minEle`.
- If a new minimum arrives, store an **encoded value**:

  ```text
  2*x - minEle
  ```

- When an encoded value is popped, recover the previous minimum using:

  ```text
  previousMin = 2*minEle - encoded
  ```

- Achieves:
  - ✅ `push()` → **O(1)**
  - ✅ `pop()` → **O(1)**
  - ✅ `peek()` → **O(1)**
  - ✅ `getMin()` → **O(1)**
  - ✅ **O(1)** extra space

---

# 06 Check for Balanced Parentheses

Given an expression containing parentheses, determine whether the parentheses are **balanced**.

A string is considered **balanced** if:

- Every opening bracket has a corresponding closing bracket.
- Brackets are closed in the correct order.
- Every closing bracket matches the most recent unmatched opening bracket.

---

# Examples

### Example 1

```text
Input:
{[]{()}}

Output:
Balanced
```

---

### Example 2

```text
Input:
[{}{}(]

Output:
Unbalanced
```

---

### Example 3

```text
Input:
((()

Output:
Unbalanced
```

---

# Approach 1: Using Stack (Recommended)

A **Stack** is the most common and efficient way to solve this problem.

## Algorithm

1. Create an empty stack.
2. Traverse the expression character by character.
3. If the current character is an opening bracket:
   - Push it onto the stack.
4. If the current character is a closing bracket:
   - Check whether the stack is empty.
     - If yes, return **Unbalanced**.
   - Otherwise compare the top element with the corresponding opening bracket.
     - If they match, pop the stack.
     - Otherwise return **Unbalanced**.
5. After processing all characters:
   - If the stack is empty → **Balanced**
   - Otherwise → **Unbalanced**

---

## Dry Run

Expression:

```text
{[]{()}}
```

| Character | Stack   | Action |
| --------- | ------- | ------ |
| `{`       | `{`     | Push   |
| `[`       | `{ [`   | Push   |
| `]`       | `{`     | Pop    |
| `{`       | `{ {`   | Push   |
| `(`       | `{ { (` | Push   |
| `)`       | `{ {`   | Pop    |
| `}`       | `{`     | Pop    |
| `}`       | Empty   | Pop    |

Final Stack:

```text
Empty
```

Result:

```text
Balanced
```

---

## Python Implementation

```python
open_list = ["(", "{", "["]
close_list = [")", "}", "]"]


def check(expression):

    stack = []

    for ch in expression:

        if ch in open_list:

            stack.append(ch)

        elif ch in close_list:

            pos = close_list.index(ch)

            if stack and stack[-1] == open_list[pos]:
                stack.pop()
            else:
                return "Unbalanced"

    return "Balanced" if not stack else "Unbalanced"


# Driver Code
print("{[]{()}} -", check("{[]{()}}"))
print("[{}{}(] -", check("[{}{}(]"))
print("((() -", check("((()"))
```

---

## Output

```text
{[]{()}} - Balanced
[{}{}(] - Unbalanced
((() - Unbalanced
```

---

### Complexity Analysis

| Complexity | Value    |
| ---------- | -------- |
| Time       | **O(N)** |
| Space      | **O(N)** |

where **N** is the length of the expression.

---

# Approach 2: Using Queue-like Mapping

Instead of storing opening brackets, store the **expected closing bracket**.

When an opening bracket is encountered:

```text
(

↓

Push )
```

When a closing bracket is encountered:

- Pop from the stack.
- Compare both symbols.

---

## Algorithm

1. Create a dictionary:

```text
( → )
{ → }
[ → ]
```

2. Traverse the expression.
3. Push expected closing brackets.
4. Compare every closing bracket with the top element.
5. Return Balanced if the stack becomes empty.

---

## Python Implementation

```python
def check(expression):

    opening = tuple("({[")
    closing = tuple(")}]")

    mapping = dict(zip(opening, closing))

    stack = []

    for ch in expression:

        if ch in opening:

            stack.append(mapping[ch])

        elif ch in closing:

            if not stack or ch != stack.pop():
                return "Unbalanced"

    return "Balanced" if not stack else "Unbalanced"


# Driver Code
print("{[]{()}} -", check("{[]{()}}"))
print("((() -", check("((()"))
```

---

## Output

```text
{[]{()}} - Balanced
((() - Unbalanced
```

---

### Complexity Analysis

| Complexity | Value    |
| ---------- | -------- |
| Time       | **O(N)** |
| Space      | **O(N)** |

---

# Approach 3: Elimination Method

This approach repeatedly removes matching bracket pairs until no more pairs remain.

If the final string becomes empty, the parentheses were balanced.

---

## Algorithm

1. Store valid pairs:

```text
()
{}
[]
```

2. Repeatedly remove them.
3. Continue until no more replacements occur.
4. If the string becomes empty → Balanced.

---

## Example

Initial string

```text
{[]{()}}
```

↓

Remove

```text
()
```

↓

```text
{[]{}}
```

↓

Remove

```text
[]
```

↓

```text
{{}}
```

↓

Remove

```text
{}
```

↓

```text
{}
```

↓

Remove

```text
{}
```

↓

```text
Empty
```

Result

```text
Balanced
```

---

## Python Implementation

```python
def check(expression):

    pairs = ["()", "{}", "[]"]

    while any(pair in expression for pair in pairs):

        for pair in pairs:
            expression = expression.replace(pair, "")

    return not expression


# Driver Code
expression = "{[]{()}}"

print(
    expression,
    "-",
    "Balanced" if check(expression) else "Unbalanced"
)
```

---

## Output

```text
{[]{()}} - Balanced
```

---

### Complexity Analysis

| Complexity | Value                                    |
| ---------- | ---------------------------------------- |
| Time       | **O(N²)** (multiple string replacements) |
| Space      | **O(N)**                                 |

---

# Comparison of Approaches

| Approach                  | Time      | Space    | Recommended           |
| ------------------------- | --------- | -------- | --------------------- |
| Stack                     | **O(N)**  | **O(N)** | ✅ Best               |
| Expected Closing Brackets | **O(N)**  | **O(N)** | ✅ Elegant            |
| Elimination Method        | **O(N²)** | **O(N)** | Suitable for learning |

---

# Why Stack is Preferred?

Stacks naturally follow the **LIFO (Last In, First Out)** principle.

Whenever an opening bracket is encountered:

```text
Push
```

Whenever a closing bracket is encountered:

```text
Pop
```

The most recently opened bracket must always be closed first, making a stack the ideal data structure for this problem.

---

# Applications

Balanced parentheses checking is widely used in:

- Compiler design
- Syntax checking
- Expression parsing
- HTML/XML tag validation
- Mathematical expression evaluation
- IDE code formatting
- JSON/XML validation

---

# Summary

- A balanced expression requires every opening bracket to have a matching closing bracket in the correct order.
- The **Stack** approach is the most efficient solution with **O(N)** time complexity.
- Another elegant solution stores the **expected closing bracket** instead of the opening one.
- The elimination method is simple but less efficient because it repeatedly scans the string.

---
