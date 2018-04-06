# Challenge #16 - Who calls their baby Keith? :baby_bottle:

Back to our mathematical roots today. Another number chalenge, we’ve done happy numbers, prime numbers, perfect numbers - now the next step is clearly Keith numbers.

A Keith number is any number that appears in its own n-digit fibonnaci-like sequence.

Create a sequence starting with *n* digits of an integer of size *n* (significant digit first) then continue the sequence where each subsequent term is the sum of the previous *n* digits. If the original *n* digit number appears in the sequence, then that number is a Keith number.

__Don’t worry - there will be examples__

### Task:

Given an integer N > 0, create a function, macro, program or data step that will determine if that number is a Keith number or not. The output should be True/False or any other realistic truthy or falsey value (e.g 1 or 0)

This sequence is monotonically increasing so a false case should be that the sequence up to and including N does not contain N.

### Examples:

- Input: 197

  Sequence: *1*, *9*, *7*, 17, 33, 57, 107, *197*, 391…

  Output: True

- Input: 28

  Sequence: *2*, *8*, 10, 18, *28*, 46…

  Output: True

### Notes:

- Keith Numbers are computationally difficult to find, and are only found via brute force searches, only about 100 have ever been found.
- It is unknown if there are infinite many keith numbers
- https://en.wikipedia.org/wiki/Keith_number
