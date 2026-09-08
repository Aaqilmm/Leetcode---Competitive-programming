class Solution:
    def dayOfYear(self, date: str) -> int:
        month = date[5:7]
        day = date[8:10]
        year = date[0:4]
        year = int(year)
        month = int(month)
        day = int(day)
        flag = 0
        if year%400 == 0:
            flag = 1
        elif year % 4 ==0 and year %100 !=0:
            flag = 1
        else:
            flag =0
        for i in range(1, month):
            if i == 1:
                day = day + 31
            elif i ==2:
                if flag == 1:
                    day = day + 29
                else:
                    day = day + 28
            elif i == 3:
                day = day +31
            elif i == 4:
                day = day + 30
            elif i == 5:
                day = day +31
            elif i == 6:
                day = day + 30
            elif i == 7:
                day = day +31
            elif i == 8:
                day = day +31
            elif i == 9:
                day = day + 30
            elif i == 10:
                day = day +31
            elif i == 11:
                day = day + 30
            elif i == 12:
                day = day +31
        return day