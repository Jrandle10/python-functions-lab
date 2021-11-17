# Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

# For example:
# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0




def occurances(string, substr):
  stripped_string = string.replace(substr, '')
  return (len(string) - len(stripped_string)) // len(substr)

print(occurances('ja randle', 'a'))