# Challenge #12 - The Name Game! :open_hands:

All too often does the issue arise where I must have variable names with underscores and non capitalised letters in them (E.g total_fuel_counts, number_of_presents), that when I go to plot leaves me with having to type out the same name just in pleasant english.

**WELL NO MORE.** You, my minions shall fix my problem.

### Task:

Given a string with under scores and a variable containing a list of stop words, remove all the underscores, periods from the string, separate the words by spaces and capitalise the first word, and every word that isn't a stop word .

### Examples

1) 
```
   String = "Code_golf_victories_of_the_past"

   stopWords = ("and", "to", "of", "the")
   
   Result = "Code Golf Victories of the Past"
```

2) 
```
   String = "tHe_QUIcK_brOwn_FoX_jumps.over.THE_laZy_Dog"

   stopWords = ("is", "to", "of", "the")

   Result = "The Quick Brown Fox Jumps Over the Lazy Dog"
```

**OH GO ON** - we'll have a winner for shortest base language solution, and a shortest regular expression solution.
