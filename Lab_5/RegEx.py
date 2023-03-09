import re
# 1

# s=str(input())

# x=re.findall("ab*", s)

# print(x)


# 2

# s=str(input())
# patterns = 'ab{2,3}'
# x=re.findall(patterns, s)
# print(x)


# # 3
# import string

s=str(input())

x=re.split('_', s)
print(x)
result=[]
for i in range(len(x)-1):
    if x[i].islower() and x[i+1].islower():
        result.append(f"{x[i]}_{x[i+1]}")
print(result)


# 4

# s=str(input())
# pattern="[A-Z][a-z]+"
# x=re.findall(pattern, s)
# print(x)


# 5

# s=str(input())
# pattern = 'a[^ b]*b'
# x=re.findall(pattern, s)
# print(x)


# 6

# s=str(input())
# x=re.sub("[ ,.]", ":",s)
# print(x)


# 7

# s=str(input())
# x=re.split('_', s)
# res=x[0]
# for i in range(1,len(x)):
#     res+=x[i].capitalize()

# print(res)


# 8

# s=str(input())
# x=re.findall('[A-Z][^A-Z]*', s)
# print(x)


# 9

# s=str(input())
# x=re.findall('[A-Z][^A-Z]*', s)
# for i in x:
#     print(i +" ", end='')


# 10

str = str(input())

str1 = re.sub('(.)([A-Z])', r'\1_\2', str)
print(str1.lower())



# result=''
# for i in str:
#     if i.isupper():
#         result=result+"_"+i.lower()
#     else:
#         result+=i

# print(result)




# num=str(input())
# pattern= r"[(][0-9]{3}[)] [0-9]{3}-[0-9]{2}-[0-9]{2}"

# x=re.findall(pattern, num)
# print(x)