# Challenge #6 - Show me the digits!

Practical task for you guys this week - I needed a function yesterday that floored a number to a certain number of digits, when I went to check it didn’t exist in R! I then checked SAS.. nothing. Python… nothing. SPSS.. I didn’t bother looking.

### Your Task:

Write me a *floor* or *ceiling* function or macro that takes 2 arguments, a value and the number of digits, and returns the floor or ceiling of that number to the specified number of significant digits.

### Rules
- The input value must work for decimals, and negatives and negative decimals as well as positive integers.

### Examples - for Floor  (Ceiling will just be the other way around)

```signif.floor(1234,1) -> 1000
signif.floor(1234,2) -> 1200

signif.floor(-1234,3) -> -1240

signif.floor(1.234,2) -> 1.2
signif.floor(-1.234,3)-> -1.24 
```
