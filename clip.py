book_list=[]
book_flag=0
fl=None
wordlist=[]
def writeLine(linelist):
    """
    linelist[0]:booktitle
    linelist[1]:the msg of bookmark
    linelist[2:]:content
    """
    filename='output/'+linelist[0]+'.md'
    with open(filename,'a')as f:
        if '标注'in linelist[1]:
            f.write('>')
        for line in linelist[2:]:
            f.write(line)
        f.write('\n')
        f.write(linelist[1])
        # f.write('\n')
with open('My Clippings.txt','r')as f:
    while 1 :
        line = f.readline()
        if '-' in line:
            if '书签' in line:#exclude the msg which is only about bookmark
                wordlist=[]
                continue
        else:
            line=line.split('\n')[0]
        wordlist.append(line)
        if line == "==========":
            wordlist.pop()
            writeLine(wordlist)
            wordlist=[]
        if line == "RealEnd":#defind the end of the file
            break

