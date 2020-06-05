# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102) by replacing your series of print statements with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

programming_words ={'if':'whether verification', 'else':'otherwise do something', 'for':'an intentional loop with some condition','and':'true when all conditions are true', 'or':'When one or another or both conditions are true or operation return true.'}

for key, value in programming_words.items():
    print(key + ": " + value)