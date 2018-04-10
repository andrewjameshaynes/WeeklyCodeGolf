# Challenge #14 - Workly Code Golf! :golf:

Work? in a code golf?! outrageous. This week is a couple of simple easy tasks that have and will appear in your daily lives as a data wizard.

### Task 1 - Dummy a column:

WITHOUT using built-in functions/procedures or packages, write me a function, macro, program or data step that will take a column of values and create dummy variables ready for modelling. Your program must also remove the original column, and have a separator option for naming the new columns.

### Examples

input: (test_col, "_")
```
   test_col
     setosa
     setosa
 versicolor
     setosa
  virginica
```
output:
```
test_col_setosa    test_col_versicolor    test_col_virginica
               1                   0                  0
               1                   0                  0
               0                   1                  0
               1                   0                  0
               0                   0                  1
```
