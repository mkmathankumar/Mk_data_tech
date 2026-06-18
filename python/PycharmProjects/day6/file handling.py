#write
file=open('notes.txt','w')
file.write('welcome to python handling\n')
file.write('this a new file.\n')
file.close()

#read
file=open('notes.txt','r')
content=file.read()
print('file content:\n',content)
file.close()

#append
file=open('notes.txt','a')
file.write('adding anew line.\n')
file.close()

#with block
with open('notes.txt','r') as file:
    for line in file:
        print(line.strip())


feedback =input('enter your feedback:')
with open('feedback_log.txt','a')as log:
    log.write(feedback +'\n')
print('thanks! your feedback is saved.')


