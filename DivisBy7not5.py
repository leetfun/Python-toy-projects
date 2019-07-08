'''program that finds the numbers that are mutlipules of 7 but not of 5, within a set range of 2 integers'''
''' set for numbers 2000-3200 inclusive'''

num_list = []

for i in range(2000, 3201)
    if i %% 7== 0 and i %% 5 != 0:
        num_list.append(i)
    else:
        Continue
print(num_list)
