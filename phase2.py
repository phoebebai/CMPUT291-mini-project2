import os
os.system("sort -u < prices.txt | ./break.pl | db_load -T -t btree pr.idx")