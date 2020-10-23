'''
'''
import os

print(os.path.join('demo','exercise'))

myFiles=['accounts.txt','details.csv','invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\demo\\exercise',filename))