# Reading from Books.txt and writing in Catalog.txt

# Creating variables
dataFromFile = []
fileInput = []
fileOutput = ""
# read file
print("Executing of reading file...")
try:
    fileOutput = open('books.txt', 'r+', encoding="UTF-8")
    fileInput = fileOutput.readlines()
    for lines in fileInput:
        temp = lines[0] + str(len(lines))
        dataFromFile.append(temp)
except NameError:
    print("File Can't be Open!")
# Some Exceptions
finally:
    fileOutput.close()
# close File

# Getting information from 'dataFromFile' list and input in catalog.txt
with open('catalog.txt', mode='w+', encoding="UTF-8") as f:
    for item in dataFromFile:
        f.write("%s\n" % item)
    print("Write in File Successful!")
    f.close()

# showing result in Console
with open('catalog.txt', mode='r+', encoding="UTF-8") as f:
    print("Result from 'catalog.txt':")
    print(f.readlines())