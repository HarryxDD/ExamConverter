import docx
import os
import functions


path = 'source/'
data = os.listdir(path)

for file in range(len(data)):

    doc = docx.Document(f'{path}{data[file]}')
    myDoc = docx.Document()

    functions.printQues(doc, myDoc)
    myDoc.save(f'output/{data[file]}')

