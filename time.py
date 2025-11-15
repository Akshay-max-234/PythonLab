class Time:
    def __init__(self, h, m, s):
        self.__h = h
        self.__m = m
        self.__s = s
    def __add__(self, other):
        s = self.__s + other.__s
        m = self.__m + other.__m
        h = self.__h + other.__h
        if s >= 60:
            m += s // 60
            s = s % 60
        if m >= 60:
            h += m // 60
            m = m % 60
        return Time(h, m, s)
    def display(self):
        print(self.__h, ":", self.__m, ":", self.__s)
t1 = Time(2, 45, 50)
t2 = Time(3, 30, 20)
t3 = t1 + t2
t3.display()
