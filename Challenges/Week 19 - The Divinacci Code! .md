# Challenge #19 - The Divinacci Code :cop:

Crap crap crap crap. Totally forgot we do code golf (:golf:) on a thursday. Here’s a cool sequence you have to make using divisors and Fibonacci - the Divinacci sequence.

The Divinacci sequence is created the same way as the Fibonacci sequence {f(0) =0, f(1) = 1}, except that instead summing the previous 2 elements, you now sum the divisors of the previous two elements.

### Task:

Create a function, data step, macro or program that when given an integer N > 0 outputs the Divinacci sequence of length N.

### Example:

The first 10 numbers in the sequence are 0, 1, 1, 2, 4, 10, 25, 49, 88, 237.

4 = sum(1) + sum(1,2)

10 = sum(1,2) + sum(1,2,4) .. etc  

### Notes: 
- For this challenge we exclude 0 as a divisor
- Your program may take 0 or and empty vector as the initial, whatever your language prefers 
