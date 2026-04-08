# python is case sensititve
# keyword--> reserved words which have special meaning in python
# identifier--> name given to a variable, function, class, module, etc

import keyword
print(keyword.kwlist)
# -->['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print(len(keyword.kwlist))
# -->35

# identifier namong rules-->
# 1.identifier can start with letter or underscore
# 2.identifier cannot start with number
# 3.identifier cannot contain special characters except underscore,or hifen "-"
# 4.identifier cannot be a keyword

