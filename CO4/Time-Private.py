class Time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second

    def __add__(self,obj):
        self.__hour += obj.__hour
        self.__minute += obj.__minute
        self.__second += obj.__second

        if(self.__second>=60):
            extra_minute =  int(self.__second/60)
            self.__second = self.__second%60
            self.__minute += extra_minute

        if (self.__minute >= 60):
            extra_hour = int(self.__minute / 60)
            self.__minute = self.__minute % 60
            self.__hour += extra_hour

        return "Hour(s) : "+str(self.__hour)+" | Minute(s) : "+str(self.__minute)+" |  Second(s) : "+str(self.__second)

obj1 = Time(4,30,0)
obj2  = Time(5,70,10)

print(obj1+obj2)
