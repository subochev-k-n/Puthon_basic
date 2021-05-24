
class Data:

    def __init__(self, date_by_str):
        self.date_by_str = date_by_str
        self.day, self.month, self.year = Data.date_unpack(date_by_str)

    @classmethod
    def date_unpack(cls, date_by_str):

        day = int(date_by_str[:2])
        month = int(date_by_str[3:5])
        year = int(date_by_str[6:11])
        if cls.date_check(day, month, year):
            return (day, month, year)
        print("Формат строки даты не соответствует условиям")
        return (0, 0, 0000)

    @staticmethod
    def date_check(day, month, year):
        isok = True
        if not 0 < int(day) < 32:
            return False
        elif not 0 < int(month) < 13:
            return False
        elif not 0 < year < 10000:
            return False
        return True


date_str = "22-12-2021"
date_str1 = "35-12-2021"
date_str2 = "00-11-2020"

first_date = Data(date_str)
second_date = Data(date_str2)

print(first_date.day, second_date.month)
print(Data.date_unpack("13-04-2077"))
Data("04-00-1987")
