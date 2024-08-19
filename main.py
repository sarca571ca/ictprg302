'''
Introduction to data structures
list()
dict()
tuples()
'''
msg_list = list() # []

msg = "I am the best"

for c in msg:
    msg_list.append(c)

print(msg_list)

a_dict = {
    'a': 8,
    'b': 10,
    'c': 12,
}

for key in a_dict:
    print(key)
    print(a_dict[key])

letter_count = {}

alphabet = 'abcdefghijklmnopqrstuvwxyz'

counted_message = "I am the best. My name is Robert Macleod. My email address is 20136040@nmtafe.wa.edu.au"

count_dict = {}

for c in counted_message:
    if c in alphabet:
        count_dict[c] = count_dict[c] + 1

for key in count_dict:
    print(count_dict[key])

# for c in counted_message:
#     letter_count[c] =+ 1
#
# for key in counted_message:
#     print(key, ": ", letter_count[key])
