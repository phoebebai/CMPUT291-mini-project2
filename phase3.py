from bsddb3 import db
import  re

def pd_get_aid(info):
    info = info.split(',')
    return info[0]

def get_title(aids,adCursor):
    for aid in aids:
        result = adCursor.set(aid.encode("utf-8"))
        if(result != None):
            ad = str(result[1].decode("utf-8"))
            titleSearch = re.search('<ti>(.*)</ti>',ad)
            title = titleSearch.group(1)
            print(str(result[0].decode("utf-8")) + ": " + title)


def dateGreater(date,daCursor,adCursor):
    result = daCursor.set_range(date.encode("utf-8"))
    d_aids = []
    if(result != None):
        d_aids.append(pd_get_aid(str(result[1].decode("utf-8"))))
        other = daCursor.next()
        while(other != None):
            if  pd_get_aid(str(other[1].decode("utf-8"))) not in d_aids:
                d_aids.append(pd_get_aid(str(other[1].decode("utf-8"))))
            other = daCursor.next()
        get_title(d_aids,adCursor)
    else:
        print("No Entry Found.")

def dateless(date,daCursor,adCursor):
    result = daCursor.set_range(date.encode("utf-8"))
    d_aids = []
    if(result != None):
        d_aids.append(pd_get_aid(str(result[1].decode("utf-8"))))
        dup = daCursor.next_dup()
        while(dup != None):
            if  pd_get_aid(str(dup[1].decode("utf-8"))) not in d_aids:
                d_aids.append(pd_get_aid(str(dup[1].decode("utf-8"))))
            dup = daCursor.next_dup()
        result = daCursor.set_range(date.encode("utf-8"))
        prev = daCursor.prev()
        while(prev != None):
            if  pd_get_aid(str(prev[1].decode("utf-8"))) not in d_aids:
                d_aids.append(pd_get_aid(str(prev[1].decode("utf-8"))))
            prev = daCursor.prev()
        get_title(d_aids,adCursor)
        return
    else:
        print("No Entry Found.")
    
def teQuery(keyword,teCursor,adCursor):
    result = teCursor.set(keyword.encode("utf-8")) 
    te_aids = []
    if(result != None):
        te_aids.append(str(result[1].decode("utf-8")).split('\n')[0])
        dup = teCursor.next_dup()
        while(dup != None):
            if  str(dup[1].decode("utf-8")).split('\n')[0] not in te_aids:
                te_aids.append(str(dup[1].decode("utf-8")).split('\n')[0])
            dup = teCursor.next_dup()
    else:
        print("No Entry Found.")
    get_title(te_aids,adCursor)


def queryType(query,teCursor,daCursor,adCursor):
    dateLessQuery  = re.match('date<=(.*)',query)
    dateGreaterQuery = re.match('date>(.*)',query)
    locationQuery = re.match('location=(.*)',query)
    if dateLessQuery:
        dateless(dateLessQuery.group(1),daCursor,adCursor)
    elif dateGreaterQuery:
        dateGreater(dateGreaterQuery.group(1),daCursor,adCursor)
    if locationQuery:
        location(locationQuery.group(1),daCursor,adCursor)
    else:
        teQuery(query,teCursor,adCursor)

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
            queryType(query,teCursor,daCursor,adCursor)
    
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
