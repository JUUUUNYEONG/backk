class Service:
    secret = "영구"
    def __init__(self,name):
        self.name=name

    def sum(self,a,b):
        result=a+b
        print("%s님, %s + %s = %s 입니다"%(self.name,a,b,result))


class Cal:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def sum_cal(self):
        result = self.a + self.b
        print(result)
    def mul_cal(self):
        result = self.a * self.b
        print(result)

class Park:
    lastname="박"
    def __init__(self,name):
        self.fullname = self.lastname + name
    def travel(self,place):
        print("{0}, {1}여행을 가다".format(self.fullname,place))


a=Park("준영")
print(a.fullname)
a.travel("부산")