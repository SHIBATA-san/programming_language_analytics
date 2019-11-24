# 日時
from datetime import datetime
utc_from = []
utc_to = []
for year in range(2):
    for mon in range(12):
        utc_from.append(datetime(2018-year,12-mon,1,0,0))
        if (12-mon) == 2:
            utc_to.append(datetime(2018-year,12-mon,28,23,59))
        elif (12-mon) == 4 or (12-mon) == 6 or (12-mon) == 9 or (12-mon) == 11:
            utc_to.append(datetime(2018-year,12-mon,30,23,59))
        else:
            utc_to.append(datetime(2018-year,12-mon,31,23,59))

print(utc_from)
print(utc_to)