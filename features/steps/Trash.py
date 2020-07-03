# HW 5
#
# $x("//div[@class='a-section']/*[contains(text(),'Regular')]")
#  or
# $x("//ul[@class="s-result-list s-col-3 wfm-desktop-list-font-unset s-height-equalized"]//*[contains(text(),'Regular')]")

"""
Create a function that will take a string as an input and return the 1st non-unique letter of a string.
“Google” => “l”
“Amazon” => “m”
If there are no unique letters, return an empty string: “xoxoxo” => “”.
How would you test it? How would you handle edge cases?

"""


# def return_uniq_letter(n):
#     n = str(n)
#     b = []
#     for i in n:
#         if i == b:
#             continue
#         else:
#             b.append(i)
#             break
#     return b
#
#
# print(return_uniq_letter("googl"))

# def return_uniq_letter(n):
#     n = str(n)
#     b = []
#     # c = []
#     for i in n:
#         if i not in b:
#             b.append(i)
#
#     return b[1]
# print(return_uniq_letter("googl"))

# def return_uniq_letter(n):
#     n = str(n)
#     b = []
#     for i in range(len(n)):
#         if i == :
#             continue
#         else:
#             b.append(i)
#             break
#     return b




#
# print(return_uniq_letter("googl"))
