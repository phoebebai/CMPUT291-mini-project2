import os
os.system("sort -u < terms.txt | ./break.pl | db_load -T -t btree te.idx")
os.system("sort -u < prices.txt | ./break.pl | db_load -T -t btree pr.idx")