from bs4 import BeautifulSoup
import csv
import os.path

inpath = 'input/'   
outpath = 'output/'

for filename in os.listdir(inpath):
    ifile = inpath+filename
    soup = BeautifulSoup(open(inpath+filename),"lxml")
    rows = soup.find_all("div",class_='row')
    result = [[]]
    result [0] = ['time','sender','message']
    
    for r in rows:
        message = r.find(class_="msg")
        if message is not None:
            message = message.get_text()
            message = message.replace("\n","").encode('utf-8')
        else: message = ""
        sender = r.find("span",attrs={'class':'sender'}, recursive = False)
        if sender is not None:
            sender = sender.get_text()
            sender = sender.replace("\n","").encode('utf-8')
            sender = sender[:-8]
        else: sender = ""
        time = r.find(class_="timestamp")
        if time is not None:
            time = time.get_text()
            time = time.replace("\n","").encode('utf-8')
        else: time = ""
        result.append([time,sender,message])
    
    ofile = (outpath+filename).replace("html","csv")
    ofile  = open(ofile, "wb")
    writer = csv.writer(ofile, dialect='excel')
    writer.writerows(result)
    ofile.close()


