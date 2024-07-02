# This program will show how to read and write file

# To write contents in the file: funny.txt
# 'w' will overwrite the exisiting contents of file
f = open ("D://Data_Science//1_Python//DATA//funny.txt", "w") 
f.write("I love Python")
f.close()

# 'a' will not overwrite the exisiting contents of file and will add the contents
f = open ("D://Data_Science//1_Python//DATA//funny.txt", "a") 
f.write("\nI love javascript")
f.close()

# To read contents from the file: funny.txt
with open ("D://Data_Science//1_Python//DATA//funny.txt", "r") as f:
    file_contents = f.read()
    f.close()

# print(file_contents)

# To count number of words from the file: funny.txt and write into another file: funny_wc.txt

f = open("D://Data_Science//1_Python//DATA//funny.txt", "r")
fc = open("D://Data_Science//1_Python//DATA//funny_wc.txt", "w")

for line in f:
    # split() will split the string using input character and return a list (array) or words
    # strip() removes endline character
    token = line.split(' ')
    fc.write(f"{line.strip()}, word_count: {len(token)}.\n")
    
f.close()
fc.close()




