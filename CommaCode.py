#Beginner solution

# spam = ['apples', 'bananas', 'tofu', 'cats']
# name = ""
# for index,a in enumerate(spam):
#     if index == 0:
#         name = name + a
#     elif index != len(spam)-1:
#         name = name + ", " + a
#     else:
#         name = name + " and " + a
#
# print(name)

#Actual Solution

def list_to_string(lst):
    if len(lst) == 0:
        return ""
    elif len(lst) == 1:
        return lst[0]
    else:
        return ", ".join(lst[:-1]) + " and " + lst[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']
print(list_to_string(spam))