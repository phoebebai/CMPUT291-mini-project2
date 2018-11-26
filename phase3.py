from bsddb3 import db
import  re
import time

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

def get_ad(aids,adCursor):
    for aid in aids:
        result = adCursor.set(aid.encode("utf-8"))
        if(result != None):
            ad = str(result[1].decode("utf-8"))
            print(str(result[0].decode("utf-8")) + ": " + ad)

def dateEqual(date,daCursor,adCursor,opt):
    result = daCursor.set(date.encode("utf-8"))
    d_aids = []
    if(result != None):
        d_aids.append(pd_get_aid(str(result[1].decode("utf-8"))))
        dup = daCursor.next_dup()
        while(dup != None):
            if  pd_get_aid(str(dup[1].decode("utf-8"))) not in d_aids:
                d_aids.append(pd_get_aid(str(dup[1].decode("utf-8"))))
            dup = daCursor.next_dup()
        if opt == 0:
            get_title(d_aids,adCursor)
        elif opt == 1:
            get_ad(d_aids,adCursor) 
        return d_aids   
    else:
        print("No Entry found")

def dateGreaterEqual(date,daCursor,adCursor,opt):
    result = daCursor.set(date.encode("utf-8"))
    d_aids = []
    if(result != None):
        d_aids.append(pd_get_aid(str(result[1].decode("utf-8"))))
        dup = daCursor.next_dup()
        while(dup != None):
            if  pd_get_aid(str(dup[1].decode("utf-8"))) not in d_aids:
                d_aids.append(pd_get_aid(str(dup[1].decode("utf-8"))))
            dup = daCursor.next_dup()
        result = daCursor.set_range(date.encode("utf-8"))
        other = daCursor.next()
        while(other != None):
            if  pd_get_aid(str(other[1].decode("utf-8"))) not in d_aids:
                d_aids.append(pd_get_aid(str(other[1].decode("utf-8"))))
            other = daCursor.next()
        if opt == 0:
            get_title(d_aids,adCursor)
        elif opt == 1:
            get_ad(d_aids,adCursor)   
        return d_aids    
    else:
        print("No Entry found")

def dateLess(date,daCursor,adCursor,opt):
    result = daCursor.set_range(date.encode("utf-8"))
    d_aids = []
    if(result != None):
        prev = daCursor.prev()
        while(prev != None):
            if  pd_get_aid(str(prev[1].decode("utf-8"))) not in d_aids:
                d_aids.append(pd_get_aid(str(prev[1].decode("utf-8"))))
            prev = daCursor.prev()
        if opt == 0:
            get_title(d_aids,adCursor)
        elif opt == 1:
            get_ad(d_aids,adCursor)
        return d_aids
    else:
        print("No Entry Found.")

def dateGreater(date,daCursor,adCursor,opt):
    result = daCursor.set(date.encode("utf-8"))
    d_aids = []
    if(result != None):
        dup = daCursor.next_dup()
        while(dup != None):
            dup = daCursor.next_dup()
        other = daCursor.next()
        while(other != None):
            if  pd_get_aid(str(other[1].decode("utf-8"))) not in d_aids:
                d_aids.append(pd_get_aid(str(other[1].decode("utf-8"))))
            other = daCursor.next()
    else:
        top = daCursor.first()
        while(top != None):
            newdate = time.strptime(date, "%Y/%m/%d")
            othdate = time.strptime(str(top[0].decode("utf-8")), "%Y/%m/%d")
            if othdate > newdate:
                break
            top = daCursor.next()
        while(top != None):
            if  pd_get_aid(str(top[1].decode("utf-8"))) not in d_aids:
                d_aids.append(pd_get_aid(str(top[1].decode("utf-8"))))
            top = daCursor.next()
    if opt == 0:
        get_title(d_aids,adCursor)
    elif opt == 1:
        get_ad(d_aids,adCursor)
    return d_aids

def datelessequal(date,daCursor,adCursor,opt):
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
        if opt == 0:
            get_title(d_aids,adCursor)
        elif opt == 1:
            get_ad(d_aids,adCursor)
        return d_aids
    else:
        print("No Entry Found.")

def priceless(price,curs,adCursor,opt):

    result = curs.set(price.encode("utf-8"))
    priceids = []
    if(result != None):
        prev = curs.prev()
        while prev != None:
            if  pd_get_aid(str(prev[1].decode("utf-8"))) not in priceids:
                priceids.append(pd_get_aid(str(prev[1].decode("utf-8"))))
            prev = curs.prev()
        if opt == 0:
            get_title(priceids,adCursor)
        elif opt == 1:
            get_ad(priceids,adCursor)
        return priceids
    else:
        print("No price was found")

def pricegreater(price,curs,adCursor,opt):

    result = curs.set_range(price.encode("utf-8"))
    priceids = []
    if(result != None):
        dup = curs.next_dup()
        while(dup != None):
            dup = curs.next_dup()
        result = curs.next()
        while(result != None):
            if  pd_get_aid(str(result[1].decode("utf-8"))) not in priceids:
                priceids.append(pd_get_aid(str(result[1].decode("utf-8"))))
            result = curs.next()
        if opt == 0:
            get_title(priceids,adCursor)
        elif opt == 1:
            get_ad(priceids,adCursor)
        return priceids
    else:
        print("No price was found")

def priceequal(price,prCursor,adCursor,opt):
    result = prCursor.set(price.encode("utf-8"))
    priceids = []
    if(result != None):
        priceids.append(pd_get_aid(str(result[1].decode("utf-8"))))
        dup = prCursor.next_dup()
        while(dup != None):
            if  pd_get_aid(str(dup[1].decode("utf-8"))) not in priceids:
                priceids.append(pd_get_aid(str(dup[1].decode("utf-8"))))
            dup = prCursor.next_dup()   
        if opt == 0:
            get_title(priceids,adCursor)
        elif opt == 1:
            get_ad(priceids,adCursor)
        return priceids
    else:
        print("No price was found")

def teQuery(keyword,teCursor,adCursor,opt):
    result = teCursor.set(keyword.encode("utf-8")) 
    te_aids = []
    if(result != None):
        te_aids.append(str(result[1].decode("utf-8")).split('\n')[0])
        dup = teCursor.next_dup()
        while(dup != None):
            if  str(dup[1].decode("utf-8")).split('\n')[0] not in te_aids:
                te_aids.append(str(dup[1].decode("utf-8")).split('\n')[0])
            dup = teCursor.next_dup()
        if opt == 0:
            get_title(te_aids,adCursor)
        elif opt == 1:
            get_ad(te_aids,adCursor)
        return te_aids
    else:
        print("No Entry Found.")

def location(loca,adCursor,opt):
    loca = loca.lower()
    top = adCursor.first()
    loc_aids = []
    while (top != None):
        ad = str(top[1].decode("utf-8"))
        locSearch = re.search('<loc>(.*)</loc>',ad)
        loc = locSearch.group(1)
        if (loc.lower() == loca):
            loc_aids.append(top[0].decode("utf-8"))
        top = adCursor.next()
    if opt == 0:
        get_title(loc_aids,adCursor)
    elif opt == 1:
        get_ad(loc_aids,adCursor)
    return loc_aids

def cat(ca,adCursor,opt):
    ca = ca.lower()
    top = adCursor.first()
    ca_aids = []
    while (top != None):
        ad = str(top[1].decode("utf-8"))
        catSearch = re.search('<cat>(.*)</cat>',ad)
        cat = catSearch.group(1)
        if (cat == ca):
            ca_aids.append(top[0].decode("utf-8"))
        top = adCursor.next()
    if opt == 0:
        get_title(ca_aids,adCursor)
    elif opt == 1:
        get_ad(ca_aids,adCursor)
    return ca_aids

def queryType(query,teCursor,daCursor,adCursor,prCursor,opt):
    dateGreaterEqualQuery = re.match('date>=(.*)',query)
    dateLessEqualQuery  = re.match('date<=(.*)',query)
    dateGreaterQuery = re.match('date>(.*)',query)
    dateEqualQuery = re.match('date=(.*)',query)
    dateLessQuery = re.match('date<(.*)',query)
    locationQuery = re.match('location=(.*)',query)
    catQuery = re.match('cat=(.*)',query)
    priceEqualQuery = re.match('price=(.*)',query)
    priceGreaterQuery = re.match('price>(.*)',query)
    priceLessQuery = re.match('price<(.*)',query)
    if dateLessEqualQuery:
        return datelessequal(dateLessEqualQuery.group(1),daCursor,adCursor,opt)
    elif dateEqualQuery:
        return dateEqual(dateEqualQuery.group(1),daCursor,adCursor,opt)
    elif dateGreaterEqualQuery:
        return dateGreaterEqual(dateGreaterEqualQuery.group(1),daCursor,adCursor,opt)
    elif dateLessQuery:
        return dateLess(dateLessQuery.group(1),daCursor,adCursor,opt)
    elif dateGreaterQuery:
        return dateGreater(dateGreaterQuery.group(1),daCursor,adCursor,opt)
    elif catQuery:
        return cat(catQuery.group(1),adCursor,opt)
    elif locationQuery:
        return location(locationQuery.group(1),adCursor,opt)
    elif priceEqualQuery:
        return priceequal(priceEqualQuery.group(1),prCursor,adCursor,opt)
    elif priceGreaterQuery:
        return pricegreater(priceGreaterQuery.group(1),prCursor,adCursor,opt)
    elif priceLessQuery:
        return priceless(priceLessQuery.group(1),prCursor,adCursor,opt)
    else:
        return teQuery(query,teCursor,adCursor,opt)

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

    opt = 0

    while(True):
        querys = input("Enter query: ")
        outSearch = re.search('output=(.*)',querys)
        if outSearch:
            option = outSearch.group(1)
            if option == "full":
                opt = 1
            elif option == "brief":
                opt = 0
            else:
                print("invalid option")
        else:
            querys = querys.split()
            entries = []
            for query in querys:
                entries.append(queryType(query,teCursor,daCursor,adCursor,prCursor,opt))
            final_entries = []
            for i in range(len(entries)):
                for j in range(len(entries[i])):
                    ein = 1
                    for e in entries:
                        if entries[i][j] not in e:
                            ein = 0
                            break
                    if ein == 1:
                        final_entries.append(entries[i][j])
            if opt == 0:
                get_title(final_entries,adCursor)
            elif opt == 1:
                get_ad(final_entries,adCursor)


    
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
