# \t inserts a tab into a string
tabby_cat = "\tI'm tabbed in."

# \n inserts string onto a new line
persian_cat = "I'm split\non a line."

# \\ inserts a backslash into the string
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

escapes = """
\t* ASCII BEL \a
\t* ASCII BS \b
\t* ASCII Formfeed \f
\t* ASCII linefeed LF \n
\t* ASCII character named name \N{name}
\t* Carriage Return \r
\t* Horizontal Tab \t **
\t* Character with 16bit hex \u
\t* Character with 32bit hex \U
\t* ASCII vertical tab (VT) \vertical
\t* Character with octal value ooo \ooo

"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print escapes


print ""

