import os
os.system("chmod u+x break.pl ")
os.system("sort -n < ads.txt  | db_load -T -t hash ad.idx")
os.system("sort -n < terms.txt | ./break.pl | db_load -T -t btree te.idx")
os.system("sort -n < pdates.txt | ./break.pl | db_load -T -t btree da.idx")
os.system("sort -n < prices.txt | ./break.pl | db_load -T -t btree pr.idx")