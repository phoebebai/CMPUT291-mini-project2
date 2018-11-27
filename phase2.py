import os

os.system("sort  < ads.txt  | ./break.pl | db_load -c duplicates=1 -T -t hash ad.idx")
os.system("sort -u < terms.txt | ./break.pl | db_load -c duplicates=1 -T -t btree te.idx")
os.system("sort -u < pdates.txt | ./break.pl | db_load -c duplicates=1 -T -t btree da.idx")
os.system("sort < prices.txt | ./break.pl | db_load -c duplicates=1 -T -t btree pr.idx")
