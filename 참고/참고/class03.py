# class (FourCal)
#   pass

# # a 는 Cookie 클래스로 생성된 객체
# a = Cookie()
# b = Cookie()

# 사칙 연산을 위한 FourCal Class 정의
# 클래스는 속성(클래스에서 관리/처리하는 값), 속성을 사용하여, 특정한 기능을 수행하는 함수로 이루어져 있다.

class FourCal:
  def setdata(self, first, second):
    self.first = first
    self.second = second

def add(self):
  result = self.first + self.second
  return result

def mul(self):
  result = self.first * self.second
  return result

def sub(self):
  result = self.first - self.second
  return result

a = FourCal()
a.setdata(4, 2)

result1 = a.add()

print(result1)