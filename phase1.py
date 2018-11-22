import xml.etree.ElementTree as ET
import fileinput
import re

def write_price(price_dictionary,file_for_price):
    
    if "price" not in price_dictionary:
        return
    
    file_for_price.write("{}:{},{},{}\n".format(price_dictionary["price"],price_dictionary["aid"],price_dictionary["cat"],price_dictionary["loc"]))

def write_term(term_dictionary, file_for_term):

    alist = term_dictionary["ti"].split()
    pattern = re.compile(r'[0-9a-zA-Z_-]')
    

    for iterm in alist:
        if len(iterm) <= 2:
            continue
        
        chars = list(iterm)
        for char in chars:
            flag = re.match(pattern,char)
            if not flag:
                chars.pop(char)
        iterm = "".join(chars)
        iterm = iterm.lower()
        file_for_term.write("{}:{}\n".format(iterm,term_dictionary["aid"]))

    
    blist = term_dictionary["desc"].split()
    for iterm in blist:

        if len(iterm) <= 2:
            continue
        
        chars = list(iterm)
        for char in chars:
            flag = re.match(pattern,char)
            if not flag:
                chars.pop(char)
                
        iterm = "".join(chars)
        iterm = iterm.lower()
        file_for_term.write("{}:{}\n".format(iterm,term_dictionary["aid"]))

    



def main():

    file_for_term = open("terms.txt","w")
    file_for_price = open("prices.txt","w")
    tags_for_price = ["aid","price","cat","loc"]
    tags_for_term = ["ti","desc","aid"]

    for line in fileinput.input():
        price_dictionary = {}
        term_dictionary = {}

        if not line.startswith("<ad>"):
            continue 
            
        root = ET.fromstring(line)
    
        for child in root:
            if child.tag in tags_for_price:
                price_dictionary[child.tag] = child.text

            if child.tag in tags_for_term:
                term_dictionary[child.tag] = child.text
        
        #write_price(price_dictionary,file_for_price)
        write_term(term_dictionary,file_for_term)
        



main()