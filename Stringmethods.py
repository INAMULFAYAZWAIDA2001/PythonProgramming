a = "Inaam"

print(len(a))
print(a.count("Inaam")) # The `count` method is used to count the number of occurrences of a specific substring within
# a string. In this case, `a.count("Inaam")` is counting how many times the substring "Inaam"
# appears in the string `a`.
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Inaam", "Inam"))
print(a.split(" "))


# heading = "welcome to Python"
# print(heading.capitalize())

# str1 = "Welcome to the dashboard !!!"
# print(len(str1))
# print(str1.center(50))

# print(str1.endswith("!!!"))
# print(str1.endswith(","))

# str1 = "hello world"
# print(str1.islower())


str1 = "Welcome"
print(str1.isalpha())
# The `print(str1.isalpha())` statement is using the `isalpha()` method to check if all the characters
# in the string `str1` are alphabetic. It will return `True` if all characters are alphabetic
# (letters) and there is at least one character, otherwise it will return `False`.




print(str1.isalnum())
# The `print(str1.isalnum())` statement is using the `isalnum()` method to check if all the characters
# in the string `str1` are alphanumeric. It will return `True` if all characters are either alphabetic
# (letters) or numeric (digits) and there is at least one character, otherwise it will return `False`.








# print(str1.find("oard"))
# The `print(str1.find("oard"))` statement is using the `find` method to search for the substring
# "oard" within the string `str1`. If the substring is found, it will return the index of the first
# occurrence of the substring within the string. If the substring is not found, it will return -1.




# print(str1.index("oard"))
# The `print(str1.index("oard"))` statement is using the `index` method to search for the substring
# "oard" within the string `str1`. If the substring is found, it will return the index of the first
# occurrence of the substring within the string. If the substring is not found, it will raise a
# `ValueError`.

str1 = "World Health Organization"
# The `print(str1.istitle())` statement is using the `istitle()` method to check if the string `str1`
# follows the rules of a title-cased string.
print(str1.istitle())
print(str1.startswith("World"))


print(str1.swapcase())
# The `print(str1.swapcase())` statement is using the `swapcase()` method to swap the case of each
# character in the string `str1`. This means that all uppercase letters will be converted to
# lowercase, and all lowercase letters will be converted to uppercase. The result will be printed to
# the console.



print(str1.title())
# The `print(str1.title())` statement is using the `title()` method to convert the string `str1` into
# title case. In title case, the first letter of each word is capitalized while all other letters are
# in lowercase. The resulting string is then printed to the console.



str2 = "To Kill a Mockingbird"


print(str2.isprintable())
# The `print(str2.isprintable())` statement is using the `isprintable()` method to check if all the
# characters in the string `str2` are printable or not.


str3 = "         " #using spacebar
print(str3.isspace())

str4 = "    " #using Tab
print(str4.isspace())