import re

def getlen(doc):
    quan = 0
    for para in doc.paragraphs:
        if para.text.strip()[:3] == "ANS":
            quan += 1
    return quan


def getQues(doc, num):
    # ques = []
    # for para in doc.paragraphs:
    #     if para.text != "":
    #         try:
    #             if para.text.strip()[0].isdigit():
    #                 ques.append(para.text.strip())
    #         except:
    #             continue

    ques = []
    for para in doc.paragraphs:
        ques.append("".join(re.findall(r'^\d*.\s(.*)', para.text.strip()))) 
    ques = list(filter(None, ques))

    return ques[num]


def getQuesAns(doc, num):
    i = 0
    ans = []
    quesAns = []
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                quesAns.append(cell.text)
                i += 1
                if i == 8:
                    ans.append(quesAns[-8:])
                    i = 0
    return ans[num]


def getAns(doc, num):
    # letter = []
    # for para in doc.paragraphs:
    #     if para.text != "":
    #         if para.text.strip()[:3] == "ANS":
    #             letter.append(para.text.replace(" ", "")[5])

    letter = []
    for para in doc.paragraphs:
        letter.append("".join(re.findall(r'ANS:\s(.)', para.text.strip())))
    letter = list(filter(None, letter))

    return letter[num]


def printQues(doc, myDoc):
    for i in range(getlen(doc)):
        myDoc.add_paragraph(getQues(doc, i))

        eachAns = getQuesAns(doc, i)
        for j in range(8):
            if j % 2 == 0:
                myDoc.add_paragraph(eachAns[j] + " " + eachAns[j+1])
                j += 2
        
        myDoc.add_paragraph("ANSWER: " + getAns(doc, i))