
import random
import string

rand=""
#for r in range (0,10):
#    rand+=random.choice(string.ascii_letters)
#
#print(rand)
#
test=['@','$',"+","*","/"]

for r in range (0,2):
    rand += random.choice(string.ascii_letters)
    rand += random.choice(test)
    rand += str(random.randint(1,8))
print(rand)