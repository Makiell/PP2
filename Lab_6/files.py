import os


# 1

# path = 'D:\Git\PP2\\'

# print([name for name in os.listdir(path)])

# os.path.isdir(os.path.join(path, name))



# 2

# path = "D:\Git\PP2\Lab_6\\file.txt"

# if os.path.exists(path):
#     print("File exists")
#     print('Exists:', os.access(path, os.F_OK))
#     print('Readable:', os.access(path, os.R_OK))
#     print('Writable:', os.access(path, os.W_OK))
#     print('Executable:', os.access(path, os.X_OK))
# else:
#     print('File dont exists')



# 3

# print("Test a path exists or not:")

# path = 'D:\Git\PP2\Lab_6\\file.txt'
# if os.path.exists(path):
#     print("Path exists")
#     print("\nFile name of the path:")
#     print(os.path.basename(path))
#     print("\nDir name of the path:")
#     print(os.path.dirname(path))
# else:
#     print("Path dont exist")



# 4

# f = open("D:\Git\PP2\Lab_6\\file.txt", 'r')
# lines = len(f.readlines())
# print(lines)



# 5

# f=open("D:\Git\PP2\Lab_6\\file.txt", 'a')

# list = ['abc', 'aaa']

# for i in list:
#     f.write(i + "\n")

# f.close()

# f=open("D:\Git\PP2\Lab_6\\file.txt", 'r')

# print(f.read())



# 6

# import string

# if not os.path.exists("D:\Git\PP2\Lab_6\letters"):
#    os.makedirs("D:\Git\PP2\Lab_6\letters")

# for letter in string.ascii_uppercase:
#    with open('D:\\Git\\PP2\\Lab_6\\letters\\' + letter + ".txt", "w") as f:
#        f.writelines(letter)



# 7

# f=open('D:\Git\PP2\Lab_6\\file.txt', 'r')

# d=open("D:\Git\PP2\Lab_6\\file2.txt", 'w')

# for i in f:
#     d.write(i)

# f.close()
# d.close()



# 8

path = 'D:\Git\PP2\Lab_6\\file2.txt'

if os.path.exists(path):
    print("File exists")
    print('Exists:', os.access(path, os.F_OK))
    print('Readable:', os.access(path, os.R_OK))
    print('Writable:', os.access(path, os.W_OK))
    print('Executable:', os.access(path, os.X_OK))
    os.remove('D:\Git\PP2\Lab_6\\file2.txt')
else:
    print("File dont exist")
