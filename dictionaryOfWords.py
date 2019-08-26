# You are going to build a Python Dictionary to represent an actual dictionary. Each key/value pair within the Dictionary will contain a single word as the key, and a definition as the value. Below is some starter code. You need to add a few more words and definitions to the dictionary.

# After you have added them, use square bracket notation to output the definition of two of the words to the console.

# Lastly, use the for in loop to iterate over the KeyValuePairs and display the entire dictionary to the console.

"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
    Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
# Define different keys in the dictionary.
word_definitions["Exciting"] = "It is exciting to learn a new language"
word_definitions["Challenging"] = "It is challenging to learn a new computer language"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
# Lookup the definition of each item in the dictionary.
definition_of_exciting = word_definitions["Exciting"]
definition_0f_challenging = word_definitions["Challenging"]


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for eachword in word_definitions:
    print(f'The definition of {eachword} is {word_definitions[eachword]}')
