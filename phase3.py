from bsddb3 import db
import  re

def dateGreater(date,daCursor):
    result = daCursor.set(date.encode("utf-8"))
    if(result != None):
        print("Key: " + str(result[0].decode("utf-8")) + ", Value: " + str(result[1].decode("utf-8")))
        
        dup = daCursor.next_dup()
        while(dup != None):
            print("key: " + str(dup[0].decode("utf-8")) + ", Value: " + str(dup[1].decode("utf-8")))
            dup = daCursor.next_dup()
    else:
        print("No Entry Found.")

def dateless(date,daCursor):
    result = daCursor.set(date.encode("utf-8"))
    if(result != None):
        print("Key: " + str(result[0].decode("utf-8")) + ", Value: " + str(result[1].decode("utf-8")))
        
        dup = daCursor.next_dup()
        while(dup != None):
            print("key: " + str(dup[0].decode("utf-8")) + ", Value: " + str(dup[1].decode("utf-8")))
            dup = daCursor.next_dup()
    else:
        print("No Entry Found.")
    
def teQuery(keyword,teCursor):
    result = teCursor.set(keyword.encode("utf-8")) 
    if(result != None):
        print("Key: " + str(result[0].decode("utf-8")) + ", Value: " + str(result[1].decode("utf-8")))
        
        dup = teCursor.next_dup()
        while(dup != None):
            print("key: " + str(dup[0].decode("utf-8")) + ", Value: " + str(dup[1].decode("utf-8")))
            dup = teCursor.next_dup()
    else:
        print("No Entry Found.")

def queryType(query,teCursor,daCursor):
    dateLessQuery  = re.match('date<=(.*)',query)
    dateGreaterQuery = re.match('date>(.*)',query)
    if dateLessQuery:
        dateless(dateLessQuery.group(1),daCursor)
    elif dateGreaterQuery:
        dateGreater(dateGreaterQuery.group(1),daCursor)
    else:
        teQuery(query,teCursor)

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
        querys = input("Enter query: ")
        querys = querys.split()
        for query in querys:
            queryType(query,teCursor,daCursor)
    
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