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
    return d_aids

def dateLess(date,daCursor,adCursor,opt):
    result = daCursor.set_range(date.encode("utf-8"))
    d_aids = []
    if(result != None):
        prev = daCursor.prev()
        while(prev != None):
            if  pd_get_aid(str(prev[1].decode("utf-8"))) not in d_aids:
                d_aids.append(pd_get_aid(str(prev[1].decode("utf-8"))))
            prev = daCursor.prev()
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
    return d_aids

def dateLessEqual(date,daCursor,adCursor,opt):
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
        prev = daCursor.prev()
        while(prev != None):
            if  pd_get_aid(str(prev[1].decode("utf-8"))) not in d_aids:
                d_aids.append(pd_get_aid(str(prev[1].decode("utf-8"))))
            prev = daCursor.prev()
    else:
        top = daCursor.first()
        while(top != None):
            newdate = time.strptime(date, "%Y/%m/%d")
            othdate = time.strptime(str(top[0].decode("utf-8")), "%Y/%m/%d")
            if othdate > newdate:
                break
            else:
                if  pd_get_aid(str(top[1].decode("utf-8"))) not in d_aids:
                    d_aids.append(pd_get_aid(str(top[1].decode("utf-8"))))
            top = daCursor.next()
    return d_aids    

def priceLess(price,prCursor,adCursor,opt):
    stop_price = ("{:>20}".format(price))
    curs = prCursor.first()
    p_aids = []
    
    
    if(curs != None): 
        while( curs!= None):
            if curs[0].decode("utf-8") >= stop_price:
               break
            else:
                if  pd_get_aid(str(curs[1].decode("utf-8"))) not in p_aids:
                    p_aids.append(pd_get_aid(str(curs[1].decode("utf-8"))))
            curs = prCursor.next()
        return p_aids   

def priceGreater(price,prCursor,adCursor,opt):
    price = ("{:>20}".format(price))
    result = prCursor.set(price.encode("utf-8"))
    p_aids = []
    if(result != None):
        dup = prCursor.next_dup()
        while(dup != None):
            dup = prCursor.next_dup()
        other = prCursor.next()
        while(other != None):
            if  pd_get_aid(str(other[1].decode("utf-8"))) not in p_aids:
                p_aids.append(pd_get_aid(str(other[1].decode("utf-8"))))
            other = prCursor.next()
    else:
        top = prCursor.first()
        while(top != None):
            othprice = str(top[0].decode("utf-8"))
            if (othprice > price):
                break
            top = prCursor.next()
        while(top != None):
            if  pd_get_aid(str(top[1].decode("utf-8"))) not in p_aids:
                p_aids.append(pd_get_aid(str(top[1].decode("utf-8"))))
            top = prCursor.next()
    return p_aids

def priceEqual(price,prCursor,adCursor,opt):
    price = ("{:>20}".format(price))
    result = prCursor.set(price.encode("utf-8"))
    p_aids = []
    if(result != None):
        p_aids.append(pd_get_aid(str(result[1].decode("utf-8"))))
        dup = prCursor.next_dup()
        while(dup != None):
            if  pd_get_aid(str(dup[1].decode("utf-8"))) not in p_aids:
                p_aids.append(pd_get_aid(str(dup[1].decode("utf-8"))))
            dup = prCursor.next_dup()
        return p_aids   
    else:
       return p_aids

def priceGreaterEqual(price,prCursor,adCursor,opt):
    price = ("{:>20}".format(price))
    result = prCursor.set(price.encode("utf-8"))
    p_aids = []
    if(result != None):
        p_aids.append(pd_get_aid(str(result[1].decode("utf-8"))))
        dup = prCursor.next_dup()
        while(dup != None):
            if  pd_get_aid(str(dup[1].decode("utf-8"))) not in p_aids:
                p_aids.append(pd_get_aid(str(dup[1].decode("utf-8"))))
            dup = prCursor.next_dup()
        result = prCursor.set_range(price.encode("utf-8"))
        other = prCursor.next()
        while(other != None):
            if  pd_get_aid(str(other[1].decode("utf-8"))) not in p_aids:
                p_aids.append(pd_get_aid(str(other[1].decode("utf-8"))))
            other = prCursor.next()  
    else:
        top = prCursor.first()
        while(top != None):
            othprice = str(top[0].decode("utf-8"))
            if othprice > price:
                break
            top = prCursor.next()
        while(top != None):
            if  pd_get_aid(str(top[1].decode("utf-8"))) not in p_aids:
                p_aids.append(pd_get_aid(str(top[1].decode("utf-8"))))
            top = prCursor.next()
    return p_aids

def priceLessEqual(price,prCursor,adCursor,opt):
    
    price = ("{:>20}".format(price))
    result = prCursor.set(price.encode("utf-8"))
    
    p_aids = []
    if(result != None):
        p_aids.append(pd_get_aid(str(result[1].decode("utf-8"))))
        dup = prCursor.next_dup()
        while(dup != None):
            if  pd_get_aid(str(dup[1].decode("utf-8"))) not in p_aids:
                p_aids.append(pd_get_aid(str(dup[1].decode("utf-8"))))
            dup = prCursor.next_dup()
        result = prCursor.set_range(price.encode("utf-8"))
        prev = prCursor.prev()
        while(prev != None):
            if  pd_get_aid(str(prev[1].decode("utf-8"))) not in p_aids:
                p_aids.append(pd_get_aid(str(prev[1].decode("utf-8"))))
            prev = prCursor.prev()
    else:
        top = prCursor.first()
        while(top != None):
            othprice = ("{:>20}".format(str(top[0].decode("utf-8"))))
            if othprice > price:
                break
            else:
                if  pd_get_aid(str(top[1].decode("utf-8"))) not in p_aids:
                    p_aids.append(pd_get_aid(str(top[1].decode("utf-8"))))
            top = prCursor.next()
    return p_aids    

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
    return ca_aids

def part(pte,teCursor,adCursor,opt):
    pte = pte.lower()
    top = teCursor.first()
    pt_aids = []
    while (top != None):
        te = str(top[0].decode("utf-8"))
        pmatch = re.search(str(pte)+'(.*)',te)
        if pmatch:
            if  str(top[1].decode("utf-8")).split('\n')[0] not in pt_aids:
                pt_aids.append(str(top[1].decode("utf-8")).split('\n')[0])
        top = teCursor.next()
    return pt_aids


def queryType(query,teCursor,daCursor,adCursor,prCursor,opt):
    partQuery = re.match('(.*)%',query)
    dateGreaterEqualQuery = re.match('date>=(.*)',query)
    dateLessEqualQuery  = re.match('date<=(.*)',query)
    dateGreaterQuery = re.match('date>(.*)',query)
    dateEqualQuery = re.match('date=(.*)',query)
    dateLessQuery = re.match('date<(.*)',query)
    locationQuery = re.match('location=(.*)',query)
    catQuery = re.match('cat=(.*)',query)
    priceEqualQuery = re.match('price=(.*)',query)
    priceGreaterEqualQuery = re.match('price>=(.*)',query)
    priceLessEqualQuery  = re.match('price<=(.*)',query)
    priceGreaterQuery = re.match('price>(.*)',query)
    priceLessQuery = re.match('price<(.*)',query)
    
    if dateLessEqualQuery:
        return dateLessEqual(dateLessEqualQuery.group(1),daCursor,adCursor,opt)
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
        return priceEqual(priceEqualQuery.group(1),prCursor,adCursor,opt)
    elif priceGreaterEqualQuery:
        return priceGreaterEqual(priceGreaterEqualQuery.group(1),prCursor,adCursor,opt)
    elif priceLessEqualQuery:
        return priceLessEqual(priceLessEqualQuery.group(1),prCursor,adCursor,opt)
    elif priceGreaterQuery:
        return priceGreater(priceGreaterQuery.group(1),prCursor,adCursor,opt)
    elif priceLessQuery:
        return priceLess(priceLessQuery.group(1),prCursor,adCursor,opt)
    
    elif partQuery:
        return part(partQuery.group(1),teCursor,adCursor,opt)
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
                break
        else:
             querys = querys.split()
             entries = []
             tr = 0
             for query in querys:
                 query = query.lower()
                 if (queryType(query,teCursor,daCursor,adCursor,prCursor,opt) != []) and (queryType(query,teCursor,daCursor,adCursor,prCursor,opt) != None):
                    entries.append(queryType(query,teCursor,daCursor,adCursor,prCursor,opt))
                 else:
                    print("no matching entries")
                    tr = 1
                    break

             if tr == 0:
                if len(entries) != 0:
                   final_entries = []
                   for i in range(len(entries)):
                       for j in range(len(entries[i])):
                           ein = 1
                           for e in entries:
                               if entries[i][j] not in e:
                                  ein = 0
                                  break
                           if ein == 1:
                              if entries[i][j] not in final_entries:
                                 final_entries.append(entries[i][j])
                if opt == 0:
                    get_title(final_entries,adCursor)
                elif opt == 1:
                    get_ad(final_entries,adCursor)
                


    
    adsDB.close()
    termsDB.close()
    pdatesDB.close()
    pricesDB.close()
    adCursor.close()
    teCursor.close()
    daCursor.close()
    prCursor.close()

if __name__ == "__main__":
    main()
       
