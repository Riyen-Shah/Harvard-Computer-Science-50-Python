MonthsList = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]

def Date():
    while True:
        MDY = input("Date: ").lower()
        if MDY.count("/") == 2:
            YMD = ShortDate(MDY)
            if YMD:
                return YMD
        elif MDY.count(" ") == 2:
            LongMonth = MDY.split()
            if LongMonth[0] in MonthsList and "," in MDY:
                YMD = LongDate(MDY)
                if YMD:
                    return YMD
            else:
                pass
        else:
            pass

def ShortDate(MDY):
    Factual = True
    Month, Day, Year = MDY.split("/")
    try:
        Month = int(Month)
        if Month > 12 or Month < 1:
            Factual = False
        Month = str(Month)
        Month = Month.rjust(2, "0")
    except ValueError:
        Factual = False
    else:
        Day = int(Day)
        if Day > 31 or Day < 1:
            Factual = False
        Day = str(Day)
        Day = Day.rjust(2, "0")

        Year = int(Year)
        if Year > 9999 or Year < 1000:
            Factual = False
        Year = str(Year)
        if Factual == False:
            YMD = False
        else:
            YMD = (f"{Year}-{Month}-{Day}")
        return YMD

def LongDate(MDY):
    Factual = True
    LongMonth, Day, Year = MDY.split()
    Day = Day[:-1]
    Day = int(Day)
    if Day > 31 or Day < 1:
        Factual = False
    Day = str(Day)
    Day = Day.rjust(2, "0")
    Month = MonthsList.index(LongMonth) + 1
    if Month > 12 or Month < 1:
        Factual = False
    Month = str(Month)
    Month = Month.rjust(2, "0")
    Year = int(Year)
    if Year > 9999 or Year < 1000:
        Factual = False
    Year = str(Year)
    if Factual == False:
        YMD = False
    else:
        YMD = (f"{Year}-{Month}-{Day}")
    return YMD

NewDate = Date()
print(NewDate)
