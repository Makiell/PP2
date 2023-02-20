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


# 3

# s=str(input())
# pattern="[a-z]_[a-z]{1}"
# x=re.findall(pattern, s)
# print(x)


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

s=str(input())
x=re.sub('(.)(_)([a-z])', r'\1\3', s)
print(x)

# s=str(input())
# temp = s.split('_')
# res = temp[0] + ''.join(ele.capitalize() for ele in temp[1:])
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

# str = str(input())

# str1 = re.sub('(.)([A-Z])', r'\1_\2', str)
# print(str1.lower())



# result=''
# for i in str:
#     if i.isupper():
#         result=result+"_"+i.lower()
#     else:
#         result+=i

# print(result)
