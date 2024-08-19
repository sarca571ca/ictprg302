msg = "I am the best. My name is Robert Macleod. My email address is 20136040@nmtafe.wa.edu.au"
alphabet = 'abcdefghijklmnopqrstuvwxyz'

msg = msg.lower()

msg_count = {}

# for letter in alphabet:
#     msg_count[letter] = 0

for c in msg:
    if c in alphabet:
        if c in msg_count:
            msg_count[c] += 1
        else:
            msg_count[c] = 1

for key in msg_count:
    print("Key: ", key, " Value: ", msg_count[key])
