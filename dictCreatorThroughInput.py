'''function when given a number creates a dictionary from 1 to given value as
"key":and assigns a value of "key"*"key"'''

def dictKeyMultiply (given_val):
    listy = {}
    for i in range(1,given_val+1):
        listy[i] = i*i
    return listy
    

input_val = int(input())
print(dictKeyMultiply(input_val))
