
🎯Problem Explaination:

We have a string num representing non-negative integer and an integer k(k digits to remove from num).
We need to remove k digits from num such that it's the smallest possible integer after removing k digits from num.

🧠Thinking Behind the Solution:

If you see my approach or others's approaches to solutions for this problem, you will mostly find that most solutions use a greddy approach and stack to solve this problem. But why a greedy approach with a stack chosen for solving the "Remove K Digits" problem? The reason is:

Greedy Approach:

The problem requires us to minimize the resulting number by removing k digits from the given number num.
A greedy approach is suitable because at each step (processing each digit), we make a locally optimal choice (keeping the smallest possible digit) with the aim of achieving the overall optimal solution (smallest resulting number).

By prioritizing smaller digits for the most significant places (leftmost positions), we ensure that the resulting number is minimized.
Use of Stack:
A stack is employed to facilitate the greedy decision-making process:
We traverse each digit of num and compare it with the top of the stack (the most recent digit we've chosen to keep).
If the current digit is smaller than the top of the stack and we still have removals (k > 0) remaining, we pop digits from the stack until a suitable position for the current digit is found.
This stack-based approach allows us to maintain the order of digits while dynamically removing larger, less significant digits to form the smallest possible number.

✅Approach:

Initialize an empty stack.
Traverse each digit of num.
For each digit, while the stack is not empty and k is greater than zero, check if the current digit is smaller than the top of the stack. If so, pop from the stack (remove the top digit) and decrement k.
Push the current digit onto the stack.
After processing all digits, handle remaining k (if any) by popping from the stack.
Construct the resulting number from the stack and remove any leading zeros.
Return the smallest possible number as a string.
Let's walkthrough🚶🏻‍♂️ the implementation process with an example for better understanding🎯:
Let's walk through the code step by step with the input num = "1432219" and k = 3.

Initial Values:

k: 3
stack: []
Iteration 1 (digit = '1'):

digit: '1'
k: 3
stack: [1]
Iteration 2 (digit = '4'):

digit: '4'
k: 3
stack: [1, 4]
Iteration 3 (digit = '3'):

digit: '3'
k: 2 (Remove '4' from stack because '4' > '3')
stack: [1, 3] (Remove '4' from stack because '4' > '3')
Iteration 4 (digit = '2'):

digit: '2'
k: 1 (Remove '3' from stack because '3' > '2')
stack: [1, 2] (Remove '3' from stack because '3' > '2')
Iteration 5 (digit = '2'):

digit: '2'
k: 1
stack: [1, 2, 2] (No removal needed)
Iteration 6 (digit = '1'):

digit: '1'
k: 0 (Remove '2' from stack because '2' > '1')
stack: [1, 2, 1] ( (Remove '2' from stack because '2' > '1')
Iteration 7 (digit = '9'):

digit: '9'
k: 0
stack: [1, 2, 1, 9]
After Loop:
stack: [1, 2, 1, 9]
Post-processing:
stack = stack[:-k] (Remove last k elements from stack): [1, 2, 1, 9]
''.join(stack): '1219'
'1219'.lstrip('0'): '1219' (No leading zeros to strip)
result: '1219'
