from bsddb3 import db
import  re

def dateless(date):
    print(date)

def queryType(query):
    dateLessQuery  = re.match('date<=(.*)',query)
    if dateLessQuery:
        dateless(dateLessQuery.group(1))

def main():
    adsDB = db.DB()
    termsDB = db.DB()
    pdatesDB = db.DB()
    pricesDB = db.DB()
    adsDB.open('ad.idx',None,db.DB_HASH,db.DB_CREATE)
    termsDB.open('te.idx',None,db.DB_BTREE,db.DB_CREATE)
    pdatesDB.open('da.idx',None,db.DB_BTREE,db.DB_CREATE)
    pricesDB.open('pr.idx',None,db.DB_BTREE,db.DB_CREATE)

    adCursor = adsDB.cursor()
    teCursor = termsDB.cursor()
    daCursor = pdatesDB.cursor()
    prCursor = pricesDB.cursor()

    while(True):
        query = input("Enter query: ")
        queryType(query)
    
    adsDB.close()
    termsDB.close()
    pdatesDB.close()
    priceDB.close()
    adCursor.close()
    teCursor.close()
    daCursor.close()
    prCursor.close()

if __name__ == "__main__":
    main()