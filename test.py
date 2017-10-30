"""	Automating the boring stuff with python: 
	Practical Programming for Total Beginners 
								by Al Sweigart"""

""" Chap 6 String manipulation """
print("This is Tom's little hut\'")

#muitiline String, newline, tab
print('''This is a multiline
	string
	hope you \n\tcan enjoy it''')

#in and not in
print('ours in' in 'this time we put ours in the trunk')

#upper(), lower(), isupper(), islower()
print('shameful'.upper())

#input
print('please input your age')
#ins=input()
#print('your age is ' +ins)
#isX method: isalpa(), isalnum, isdecimal(), isspace(), istitle()
print('as ThisAOne'.isalpha())
print('is124'.isalnum())

#startswith(), endswith()

#join
temp = ','.join(['this','that','these','those'])
print(temp)
temp=' '.join(['this','that','these','those'])
temp='ABC'.join(['this','that','these','those'])
print(temp)

#split
temp='this is a good story'.split()
temp='thisABCisABCaABCgoodABCstory'.split('ABC')
temp='''a common use of split is
split a paragraph
along newline'''
print(temp.split('\n'))

#ljust(), rjust(), center()
def printItem(title, itemsDict, leftWidth, rightWidth):
  print(title.center(leftWidth+rightWidth,'-'))
  for k, v in itemsDict.items():
    print(k.ljust(leftWidth,'.')+str(v).rjust(rightWidth))
item={'apple':4,'juice':6,'sausage':6}
printItem('PICNIC ITEMS',item, 20, 5)
printItem('PARTY ITEMS',item,30,10)

#removing whitespace with strip(), rstrip(), lstrip()
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))

#copy and paste with pyperclip module. need to install the module
#import pyperclip
#paste=pyperclip.paste()
#print(paste)

## part II automating tasks

#chap8 reading and writing files

#working with file and directory
import os
print(os.path.join('Users','inspiron'))
print(os.getcwd())
#os.chdir('c:\\Users\\inspiron\\coding')
print(os.getcwd())
print(os.path.abspath('test.py'))
print(os.listdir())

print(os.path.isdir('c:\\Users\\inspiron'))
print(os.path.isfile('c:\\Users\\inspiron\\test.py'))
print(os.path.exists('c:\\Users\inspiron\\test.py'))

from sys import platform
print('distinguish os')
if platform == "linux" or platform == "linux2":
# linux
  print('os is linux')
elif platform == "darwin":
# OS X
  print('os is OSX')
elif platform == "win32":
# Windows...
  print('os is windows')
## file reading and writing
aFile=open(os.path.abspath('1.txt'))
#acontent=aFile.read()
acontent=aFile.readline() #read a line
bcontent=aFile.readlines()
print(bcontent)
print(len(bcontent))
aFile.close()
