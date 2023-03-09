# 1

# list = [ input() for i in range(int(input()))]

# mult = '*'.join(i for i in list)

# print(eval(mult))



# 2

str = str(input())

lower=0
upper=0
for i in range(len(str)):
    if 65 <= ord(str[i]) <= 90:
        lower+=1
    else:
        upper+=1

print(lower, upper)



# 3

# str = str(input())


# str2=reversed(str)
# if list(str)==list(str2):
#     print("Palindrome")
# else:
#     print('Not palindrome')



# str2 = str[::-1]
# if (str)==(str2):
#     print("Palindrome")
# else:
#     print('Not palindrome')



# 4

# from time import sleep
# import math

# number = int(input())

# milliseconds = int(input())

# sleep(milliseconds/1000)

# print("Square root of {n} after {m} miliseconds is {sq}".format(n=number, m= milliseconds, sq = math.sqrt(number)))



# 5


# tuple = (True, True)

# print(all(tuple))

