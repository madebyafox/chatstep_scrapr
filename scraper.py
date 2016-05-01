from bs4 import BeautifulSoup
import csv
import glob
import os.path

inpath = 'input/'   
outpath = 'output/'

for filename in os.listdir(inpath):
    ifile = inpath+filename
    soup = BeautifulSoup(open(inpath+filename),"lxml")
    rows = soup.find_all("div",class_='row')
    n = len(rows)
    result = [[]]
    result [0] = ['message', 'sender', 'time']
    
    for r in rows:
        message = r.find(class_="msg")
        if message is not None:
            message = message.get_text()
            message = message.replace("\n","")
        else: message = ""
        sender = r.find("span",attrs={'class':'sender'}, recursive = False)
        if sender is not None:
            sender = sender.get_text()
            sender = sender.replace("\n","")
            sender = sender[:-8]
        else: sender = ""
        time = r.find(class_="timestamp")
        if time is not None:
            time = time.get_text()
            time = time.replace("\n","")
        else: time = ""
        result.append([message,sender,time])
    
    ofile = (outpath+filename).replace("html","csv")
    ofile  = open(ofile, "wb")
    writer = csv.writer(ofile, dialect='excel')
    writer.writerows(result)
    ofile.close()
