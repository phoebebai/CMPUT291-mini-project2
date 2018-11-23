import xml.etree.ElementTree as ET
import fileinput
import re

def write_price(price_dictionary,file_for_price):
    
    if "price" not in price_dictionary:
        return
    
    file_for_price.write("{}:{},{},{}\n".format(price_dictionary["price"],price_dictionary["aid"],price_dictionary["cat"],price_dictionary["loc"]))

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
    print(new_string)
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
        
        write_price(price_dictionary,file_for_price)
        write_term(term_dictionary,file_for_term)
        
    file_for_price.close()
    file_for_term.close()


main()