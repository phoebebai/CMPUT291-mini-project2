import xml.etree.ElementTree as ET
import fileinput
import re

def write_price(price_dictionary,file_for_price):
    
    if "price" not in price_dictionary:
        return
    
    file_for_price.write("{:>20}:{},{},{}\n".format(price_dictionary["price"],price_dictionary["aid"],price_dictionary["cat"],price_dictionary["loc"]))

def write_term(term_dictionary, file_for_term):
    
    pattern1 = re.compile(r'[0-9a-zA-Z_-]')
    pattern2 = re.compile(r'&#[0-9]+;')
    new_string = re.sub(pattern2,"",term_dictionary["ti"])
    
    alist = new_string.split()
    for iterm in alist:
        chars = list(iterm)
        for i,char in enumerate(chars):
            flag = re.match(pattern1,char)
            if flag == None:
                chars[i] = ','

        iterm = "".join(chars)
        outputs = iterm.split(",")
        for output in outputs:
            if len(output) <= 2:
                continue
            output = output.lower()
            file_for_term.write("{}:{}\n".format(output,term_dictionary["aid"]))

    
    new_string = re.sub(pattern2,"",term_dictionary["desc"])

    blist = new_string.split()
    for iterm in blist:
        chars = list(iterm)
        for i,char in enumerate(chars):
            flag = re.match(pattern1,char)
            if flag == None:
                chars[i] = ','
                
        iterm = "".join(chars)        
        outputs = iterm.split(",")
        for output in outputs:
            if len(output) <= 2:
                continue
            output = output.lower()
            file_for_term.write("{}:{}\n".format(output,term_dictionary["aid"]))


def write_pdate(pdate_dictionary,file_for_pdate):

    if "date" not in pdate_dictionary:
        return
    file_for_pdate.write("{}:{},{},{}\n".format(pdate_dictionary["date"],pdate_dictionary["aid"],pdate_dictionary["cat"],pdate_dictionary["loc"]))

def write_ad(ad_dictionary,file_for_ad):

    file_for_ad.write("{}:<ad><aid>{}</aid><date>{}</date><loc>{}</loc><cat>{}</cat><ti>{}</ti><desc>{}</desc><price>{}</price></ad>\n".format(ad_dictionary["aid"],
    ad_dictionary["aid"],ad_dictionary["date"],ad_dictionary["loc"],ad_dictionary["cat"],ad_dictionary["ti"],ad_dictionary["desc"],ad_dictionary["price"]))


def main():

    file_for_term = open("terms.txt","w")
    file_for_price = open("prices.txt","w")
    file_for_pdate = open("pdates.txt","w")
    file_for_ad = open("ads.txt","w")
    tags_for_price = ["aid","price","cat","loc"]
    tags_for_term = ["ti","desc","aid"]
    tags_for_pdate = [ "date","aid","cat","loc"]
    tags_for_ad = ["aid","date","loc","cat","ti","desc","price"]

    for line in fileinput.input():
        price_dictionary = {}
        term_dictionary = {}
        pdate_dictionary = {}
        ad_dictionary = {}

        if not line.startswith("<ad>"):
            continue 
            
        root = ET.fromstring(line)
    
        for child in root:
            if child.tag in tags_for_price:
                price_dictionary[child.tag] = child.text

            if child.tag in tags_for_term:
                term_dictionary[child.tag] = child.text
            
            if child.tag in tags_for_pdate:
                pdate_dictionary[child.tag] = child.text

            if child.tag in tags_for_ad:
                ad_dictionary[child.tag] = child.text
        
        write_price(price_dictionary,file_for_price)
        write_term(term_dictionary,file_for_term)
        write_pdate(pdate_dictionary,file_for_pdate)
        write_ad(ad_dictionary,file_for_ad)
        
    file_for_price.close()
    file_for_term.close()
    file_for_pdate.close()
    file_for_ad.close()


main()
