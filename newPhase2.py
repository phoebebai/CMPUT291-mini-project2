from bsddb3 import db
import os

# ad.idx
DB_File = "ad.idx"
database = db.DB()
database.set_flags(db.DB_DUP)
database.open(DB_File,None, db.DB_HASH, db.DB_CREATE)       
curs = database.cursor()
os.system("sort -u <ads.txt >ads_sorted.txt")

ads = open("ads_sorted.txt", 'r')
adList = []
for entry in ads:
    ad = entry.split(":")  
    adList.append(ad) 
for m in range(1, (len(adList))):
    adKey = adList[m][0]
    adVal = adList[m][1]
    m += 1  
    database.put(bytes(adKey, "utf 8"), bytes(adVal, "utf-8"))
ads.close()
curs.close()
database.close()  

# te.idx b-tree
DB_File = "te.idx"
database = db.DB()
database.set_flags(db.DB_DUP) 
database.open(DB_File,None, db.DB_BTREE, db.DB_CREATE)
curs = database.cursor()
os.system("sort -u <terms.txt >terms_sorted.txt")

terms = open("terms_sorted.txt", 'r')
termsList = []
for term in terms:
    ad = term.split(":")  
    termsList.append(ad)    
for m in range(len(termsList)):
    teKey = termsList[m][0]
    teEntry = termsList[m][1]
    m += 1
    database.put(bytes(teKey, "utf 8"), bytes(teEntry, "utf-8"))

terms.close()
curs.close()
database.close()    

# pr.idx b-tree
DB_File = "pr.idx"
database = db.DB()
database.set_flags(db.DB_DUP) 
database.open(DB_File,None, db.DB_BTREE, db.DB_CREATE)
curs = database.cursor()
os.system("sort -u <prices.txt >prices_sorted.txt")

prices = open("prices_sorted.txt", 'r')
priceList = []
for price in prices:
    ad = price.split(":")  
    priceList.append(ad)    
for m in range(len(priceList)):
    prKey = priceList[m][0]
    prEntry = priceList[m][1]
    m += 1
    database.put(bytes(prKey, "utf 8"), bytes(prEntry, "utf-8"))

prices.close()
curs.close()
database.close()    

# da.idx b-tree
DB_File = "da.idx"
database = db.DB()
database.set_flags(db.DB_DUP) 
database.open(DB_File,None, db.DB_BTREE, db.DB_CREATE)
curs = database.cursor()
os.system("sort -u <pdates.txt >pdates_sorted.txt")

pdates = open("pdates_sorted.txt", 'r')
pdateList = []
for pdate in pdates:
    ad = pdate.split(":")  
    pdateList.append(ad)    
for m in range(len(pdateList)):
    daKey = pdateList[m][0]
    daEntry = pdateList[m][1]
    m += 1
    database.put(bytes(daKey, "utf 8"), bytes(daEntry, "utf-8"))

pdates.close()
curs.close()
database.close()    