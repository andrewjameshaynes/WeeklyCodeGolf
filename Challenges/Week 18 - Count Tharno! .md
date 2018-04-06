# Challenge #18 - Count Tharno :new_moon: :zap:

In honour of Theo’s last code golf day we shall be using __VAMPIRE NUMBERS__.

We are going to calculate whether a number is a vampire number or not and output them to look like faannngggsss.

A vampire number is a natural number with even number of digits N, that can be factored into two integers each with N/2 digits, where the two digits contain precisely all the values from the original number.

### Task:

Given a number as your input, your job is to write a macro, program function or datastep that not only checks whether a number is a vampire or not, but if it is a vampire, outputs it’s fangs. (Generic False if not a vampire)

Fangs look like the following (8 crosses, with the fangs hanging down from the first and last cross, on 2 new lines):

```
xxxxxxxx
1      6
7      9
```

### Examples:

1) Input: 73

   Output: False

2) Input: 1260 ( = 21 x 60)

   Output: True *because it can be split into 2 integers of size 2, and contains all the numbers from the 1260.*
  
```  
  xxxxxxxx
  2      6
  1      0
```

Other 4 digit examples of a True case: 1395, 1435, 2187
