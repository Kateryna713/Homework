# vowels = ["a", "e", "i", "o", "u"]
# var_string = 'hApPyHalLOweEn!'
# print('Version of the string: ' + var_string)
# count = 0
# for letter in var_string:
#     letter1 = letter.lower()
#     if letter1 in vowels:
#         count += 1
# print('Total vowels in the string ', str(count), sep="= ")


vowels = ["a", "e", "i", "o", "u"]
var_string = input("Provide a string: ")
var_string1 = var_string.lower()
k = 0
count = 0
while k < len(var_string):
    if var_string1[k] in vowels:
        count += 1
    k = k + 1
print('Total vowels in the string ', str(count), sep="= ")
