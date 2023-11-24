# for and while

# counter = 1
# while counter <= 5:
#     print(counter)
#     counter=counter+1

# prime number
# x = 11
# is_prime = True
# i = 2
# while i < x / 2:
#     if x % i == 0:
#         is_prime = False
#         break
#     i = i + 1
# print('value is ' , is_prime)

# how to use loop with for loop
# for letter in 'programming':
#     print(letter, end=' ')

# mylist=[5,7,8,6,7]
# for letter in mylist:
#     print(letter, end=' ')

# for n in range(2, 60,3):
#     print(n,end=' ')

# how to print star patterns
num=int(input('enter no to generate star patterns'))
for i in range(1,num+1):
    for j in range(1, i+1):
        print('*', end=' ')
    print()