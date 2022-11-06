# Reading File Lecture
# modem can be r(read), w(write), a(append), add b to each to open in binary mode
# you can also add + for bonus permission

# print("1")
# myfile = open('filename.txt', 'r+')
# text = myfile.read()
# print(text)
# myfile.close()
#
# print("2")
# myfile = open('filename.txt', 'r+')
# print(myfile.readlines())
# myfile.close()
#
# print("3")
# myfile = open('filename.txt', 'r+')
# for line in myfile:
#     print(line)
# myfile.close()

print("4")
try:
    myfile = open('filename.txt', 'w')  # if file is open in W format mode - the file will be created if isn't exist
    myfile.writelines("Hello World!\n")
except NameError:
    print("Something Wrong")
finally:
    myfile.close()

print("5")
myfile = open('filename.txt', 'a+')
myfile.writelines("New Text..\n")
myfile.close()

print("6")
with open('filename.txt', 'a+') as f:
    f.write("Some text...")
    f.close()

try:
    myfile = open('filename.txt', mode='r+')
    print(myfile.readlines())
except NameError:
    print(".......")
finally:
    myfile.close()
# myfile = open('filename.txt', 'r+')
# for line in myfile:
#     print(line)
# myfile.close()
