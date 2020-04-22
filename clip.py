book_list=[]
book_flag=0
with open('My Clippings.txt','r')as f:
    while 1 :
        line = f.readline().split('\n')[0]
            if book_flag==1:
                if line != " ":
                    print(line)
                book_flag=0
            if line == "==========":
                book_flag=1
            if line == "RealEnd":#defind the end of the file
                break