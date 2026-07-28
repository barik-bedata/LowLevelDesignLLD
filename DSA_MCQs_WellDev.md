# Top 50 DSA MCQs for WellDev Recruitment (C++ & Algorithms)

## Complexity Analysis (Big O)

**1. What is the time complexity of accessing an element in an array by its index?**
- a) O(n)
- b) O(log n)
- c) O(1)
- d) O(n log n)
> **Answer:** c

**2. Which of the following time complexities is the most efficient?**
- a) O(n log n)
- b) O(2^n)
- c) O(n)
- d) O(log n)
> **Answer:** d

**3. What is the worst-case time complexity of inserting an element at the beginning of a singly linked list?**
- a) O(n)
- b) O(1)
- c) O(log n)
- d) O(n^2)
> **Answer:** b

**4. What is the space complexity of an algorithm that creates an N x N matrix?**
- a) O(N)
- b) O(N^2)
- c) O(1)
- d) O(N log N)
> **Answer:** b

**5. Amortized time complexity of inserting an element into a dynamic array (like std::vector in C++) is:**
- a) O(1)
- b) O(n)
- c) O(log n)
- d) O(n^2)
> **Answer:** a

## Basic Programming (C++)

**6. Which operator in C++ is used to allocate memory dynamically?**
- a) malloc
- b) alloc
- c) new
- d) create
> **Answer:** c

**7. What is the size of a pointer in a 64-bit architecture?**
- a) 4 bytes
- b) 8 bytes
- c) 2 bytes
- d) 16 bytes
> **Answer:** b

**8. Which of the following allows function overloading in C++?**
- a) Different return types only
- b) Different number or types of arguments
- c) Different function names
- d) Same arguments but different return types
> **Answer:** b

**9. In C++, `std::map` is typically implemented using which data structure?**
- a) Hash Table
- b) Array
- c) Red-Black Tree
- d) Linked List
> **Answer:** c

**10. What is a pure virtual function in C++?**
- a) A function with no return type
- b) A function declared as virtual and assigned to 0
- c) A function that cannot be overridden
- d) A static member function
> **Answer:** b

## Array, String, and Hashing

**11. Which data structure is best for finding the frequency of characters in a string in O(N) time?**
- a) Stack
- b) Queue
- c) Hash Map
- d) Binary Search Tree
> **Answer:** c

**12. In C++, what is the time complexity of searching for an element in `std::unordered_set` on average?**
- a) O(log n)
- b) O(n)
- c) O(n log n)
- d) O(1)
> **Answer:** d

**13. To check if two strings are anagrams, which approach is the most optimal?**
- a) Sort both strings and compare (O(N log N))
- b) Use a Hash Map or Frequency Array (O(N))
- c) Compare all substrings (O(N^2))
- d) Use a Stack
> **Answer:** b

**14. What is the standard way to find the length of a null-terminated string in C?**
- a) Checking the size attribute
- b) Iterating until '\0' is found
- c) Using sizeof() operator on the pointer
- d) Checking for an empty space
> **Answer:** b

**15. If a hashing function produces the same index for two different keys, it is called a:**
- a) Deadlock
- b) Collision
- c) Fragmentation
- d) Race condition
> **Answer:** b

## Two Pointers, Prefix Sum, Sliding Window

**16. The Two-Pointer technique is generally most efficient when applied to:**
- a) Unsorted arrays
- b) Sorted arrays
- c) Linked Lists only
- d) Hash Maps
> **Answer:** b

**17. What is the primary purpose of a Prefix Sum array?**
- a) To sort the array in O(N)
- b) To find the maximum element in O(1)
- c) To calculate the sum of elements in a given range in O(1) time
- d) To reverse the array
> **Answer:** c

**18. Which problem is best solved using the Sliding Window technique?**
- a) Finding the shortest path in a graph
- b) Finding the maximum sum of a subarray of size K
- c) Sorting a list of strings
- d) Reversing a Linked List
> **Answer:** b

**19. To solve the "Two Sum" problem (finding two elements that add up to a target) in O(N) time, we should use:**
- a) Two Pointers on an unsorted array
- b) Binary Search
- c) A Hash Map
- d) A Priority Queue
> **Answer:** c

**20. In the Sliding Window technique, how is the window updated when moving one step forward?**
- a) The entire window is recalculated from scratch
- b) The new element is added and the oldest element is removed
- c) The window size doubles
- d) The window splits in half
> **Answer:** b

## Stack, Queue, Priority Queue, Linked List

**21. Which data structure follows the LIFO (Last In First Out) principle?**
- a) Queue
- b) Linked List
- c) Stack
- d) Tree
> **Answer:** c

**22. Evaluating a postfix expression is most easily done using a:**
- a) Queue
- b) Stack
- c) Binary Tree
- d) Hash Table
> **Answer:** b

**23. A Min-Heap (Priority Queue) allows extracting the minimum element in what time complexity?**
- a) O(1)
- b) O(n)
- c) O(log n)
- d) O(n log n)
> **Answer:** c

**24. How do you detect a cycle in a Singly Linked List?**
- a) Binary Search
- b) Floyd's Cycle-Finding Algorithm (Slow and Fast Pointers)
- c) Depth First Search
- d) Bubble Sort
> **Answer:** b

**25. Which scenario perfectly fits a Deque (Double Ended Queue)?**
- a) CPU Task Scheduling
- b) Undo operation in text editors
- c) Checking for Palindromes
- d) Sliding Window Maximum problem
> **Answer:** d

## Searching and Sorting

**26. Binary Search requires the array to be:**
- a) Contains only positive numbers
- b) Sorted
- c) Without duplicates
- d) Dynamically allocated
> **Answer:** b

**27. What is the worst-case time complexity of Quick Sort?**
- a) O(N log N)
- b) O(N)
- c) O(N^2)
- d) O(log N)
> **Answer:** c

**28. Which sorting algorithm is considered "stable" by default?**
- a) Merge Sort
- b) Quick Sort
- c) Heap Sort
- d) Selection Sort
> **Answer:** a

**29. The time complexity of Merge Sort in the best, average, and worst case is:**
- a) O(N^2)
- b) O(N)
- c) O(N log N)
- d) O(log N)
> **Answer:** c

**30. Which algorithm repeatedly swaps adjacent elements if they are in the wrong order?**
- a) Insertion Sort
- b) Selection Sort
- c) Bubble Sort
- d) Merge Sort
> **Answer:** c

## Trees (Binary Tree, BST)

**31. In a Binary Search Tree (BST), the left child of a node is:**
- a) Always greater than the node
- b) Always lesser than the node
- c) Equal to the node
- d) Can be any value
> **Answer:** b

**32. Which tree traversal visits the nodes in ascending order in a BST?**
- a) Pre-order
- b) Post-order
- c) In-order
- d) Level-order
> **Answer:** c

**33. What is the maximum number of nodes at level 'L' in a binary tree? (Root is level 0)**
- a) 2^L
- b) L^2
- c) 2L
- d) 2^(L-1)
> **Answer:** a

**34. What is the worst-case time complexity of searching in an unbalanced Binary Search Tree?**
- a) O(log N)
- b) O(N)
- c) O(N log N)
- d) O(1)
> **Answer:** b

**35. A tree with N nodes always has exactly how many edges?**
- a) N
- b) N+1
- c) N-1
- d) 2N
> **Answer:** c

## Recursion and Backtracking

**36. A function calling itself directly or indirectly is known as:**
- a) Iteration
- b) Polymorphism
- c) Recursion
- d) Encapsulation
> **Answer:** c

**37. Every recursive function must have a:**
- a) Return type of int
- b) Base condition
- c) Global variable
- d) While loop
> **Answer:** b

**38. The N-Queens problem is a classic example of solving using:**
- a) Greedy Algorithm
- b) Backtracking
- c) Two Pointers
- d) Divide and Conquer
> **Answer:** b

**39. Excessive recursion without a proper base case leads to which error?**
- a) Memory Leak
- b) Stack Overflow
- c) Segmentation Fault
- d) Null Pointer Exception
> **Answer:** b

**40. What is the time complexity of solving the Tower of Hanoi problem with N disks?**
- a) O(N)
- b) O(N log N)
- c) O(N^2)
- d) O(2^N)
> **Answer:** d

## Graphs (BFS, DFS, Shortest Paths)

**41. Which data structure is used to implement Breadth-First Search (BFS)?**
- a) Stack
- b) Queue
- c) Priority Queue
- d) Hash Map
> **Answer:** b

**42. Which traversal is generally used for finding connected components in a Graph?**
- a) Binary Search
- b) Depth-First Search (DFS)
- c) Dijkstra's Algorithm
- d) Kruskal's Algorithm
> **Answer:** b

**43. Dijkstra’s Algorithm is used for finding the single-source shortest path. What is a major limitation of it?**
- a) It cannot handle unweighted graphs
- b) It cannot handle negative weight edges
- c) It takes O(N^3) time
- d) It only works on Trees
> **Answer:** b

**44. Which algorithm can find the shortest path in a graph with negative edge weights?**
- a) Prim's Algorithm
- b) Dijkstra's Algorithm
- c) Bellman-Ford Algorithm
- d) Kruskal's Algorithm
> **Answer:** c

**45. Checking if a graph is Bipartite (Bi-colorable) can be done using:**
- a) BFS or DFS
- b) Binary Search
- c) Bellman-Ford
- d) Floyd-Warshall
> **Answer:** a

## Dynamic Programming (DP)

**46. Dynamic Programming is mainly an optimization over:**
- a) Greedy Algorithms
- b) Plain Recursion (overlapping subproblems)
- c) Backtracking
- d) Iteration
> **Answer:** b

**47. Storing the results of expensive function calls to avoid repeated calculations in DP is called:**
- a) Hashing
- b) Memoization
- c) Serialization
- d) Partitioning
> **Answer:** b

**48. In the 0/1 Knapsack problem, "0/1" means:**
- a) Items have 0 or 1 weight
- b) You can either pick an item entirely or not pick it at all
- c) The profit is between 0 and 1
- d) Only one item exists in the knapsack
> **Answer:** b

**49. The naive recursive approach for finding the N-th Fibonacci number has a time complexity of O(2^N). With DP, it reduces to:**
- a) O(1)
- b) O(log N)
- c) O(N)
- d) O(N^2)
> **Answer:** c

**50. Longest Common Subsequence (LCS) is solved effectively using:**
- a) Two Pointers
- b) 2D Dynamic Programming
- c) Backtracking
- d) Min-Heap
> **Answer:** b
