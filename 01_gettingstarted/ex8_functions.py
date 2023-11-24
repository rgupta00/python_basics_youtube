# basics of function in python
def sum_of_two_numbers(x, y):
    return x + y


def sum_of_numbers_of_list(mylist):
    sum = 0
    for i in mylist:
        sum = sum + i
    return sum

#10
def sum_of_n(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

print(sum_of_n(10))

# mylist = [7, 7, 7]
# print(sum_of_numbers_of_list(mylist))
#
# print(sum_of_two_numbers(3, 5))

#passing a list
# passing dictionary