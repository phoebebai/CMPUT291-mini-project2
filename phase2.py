import os
#os.system("sort -u < ads.txt | ./break.pl | db_load -T -t hash ad.idx")
os.system("sort -u < terms.txt | ./break.pl | db_load -T -t btree te.idx")
#os.system("sort -u < pdates.txt | ./break.pl | db_load -T -t btree da.idx")
os.system("sort -u < prices.txt | ./break.pl | db_load -T -t btree pr.idx")