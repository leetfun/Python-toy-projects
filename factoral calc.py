
'''program to calculate factorals of a given value'''

def factorialcalc(origin_num):
    #number to calculate factorals of
    factoral_num = origin_num
    #value keeper
    factoral_value = factoral_num
    #calculates factoral with range and prints total
    for i in range ((factoral_num -1), 0, -1):
        factoral_value = factoral_value * i
    return factoral_value

x = int(input(""))
print(factorialcalc(x))



## better version
def factoralcalc(val):
    if val == 0:
        return 1
    return val * factoralcalc(val-1)

val = int(input())
print (factoralcalc(val))
