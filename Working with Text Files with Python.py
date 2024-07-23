person = "Anna"

print(f"my name is {person}")

d = {'a' : 1234, 'b':456 }

print(f"my nimber is {d['a']}")

library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]

library

for book in library:
    print(f"Author is {book[0]}")

for author,topic,pages in library:
    print(f"{author:{10}} {topic:{30}} {pages:.>{10}}") #10 30 30 min spaces adds spaces

from datetime import datetime

today = datetime(year=2019,month=2,day=28)

print(f"{today:%B %d, %Y}") #strftime.org

today

#part two: read and write to text files with python
#creating text files
%%writefile test.txt
Hello, this is a quik test file.
This is the second line of the file.

myfile = open('test.txt')
myfile

#for checking location use 'pwd'
myfile.read() # is usefull for the smaller files you grab every thing and then save ot as an string
myfile.read()

#you can't read it twice. cursor. to solve this problem:
myfile.seek(0)  #0 reset the cursor position to 0 (the begining of the text  file) 
myfile.read()

myfile.seek(0)

content = myfile.read()
content
print(content)

#once you aed done working you should close the file
myfile.close()

# to read in separate line (read each line as a separate item in the list)
myfile = open('test.txt')
myfile.readlines()
myfile.seek(0)
mylines = myfile.readlines()
mylines

#you can iterate through that
for line in mylines:
    print(line[0])

for line in mylines:
    print(line.split()[0]) #the set of first character before the space

# writing to the file (w+ -> read and write into the file. it over write completely in original file)
myfile = open('test.txt', 'w+')
myfile.read()
myfile.write('MY BRAND NEW TEXT')
myfile.seek(0)
myfile.read()
myfile.close()

# append keep old info and add new info. if the file dosen't exist it creates a new one.
myfile = open('whoops.txt', 'a+')
myfile.write('MY FIRST LINE IN A+ OPENING')
myfile.close()
newfile = open('whoops.txt')
newfile.read()
newfile.close()
myfile = open('whoops.txt', mode='a+')
myfile.write('This ia an added line, because I used a+ mode')
myfile.seek(0)
myfile.read()

# if you want to add it to the new line
myfile.write('\nThis is a real new line, on the next line')
myfile.seek(0)
myfile.read()
myfile.seek(0)
print(myfile.read())

# context  manager to automatically close the file for you 
with open('whoops.txt', 'r') as mynewfile:
    myvariable = mynewfile.readlines()

myvariable