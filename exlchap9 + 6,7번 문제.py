#9.1

#1
print((123).__add__(334))

#2
print((123).__sub__(334))

#3
print((123).__mul__(334))

#4
print((123).__truediv__(3))




#9.3
#pop 사용 불가능
#sort 사용 불가능
#append 사용 불가능
#upper 사용 가능
#insert 사용 불가능
#remove 사용 불가능




#9.5
a = 1
b = 1
c= 2
d = 3
e = 3

print('a와 b는 같은 객체인가?', id(a)==id(b))
print('b와 c는 같은 객체인가?', id(b)==id(c))
print('c와 d는 같은 객체인가?', id(c)==id(d))
print('d와 e는 같은 객체인가?', id(d)==id(e))




#9.7
class Dog:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def __str__(self):
    return "이름은 {}이고, 나이는 {}살입니다.".format(self.name,self.age)

my_dog = Dog('Mango', '3')

print(my_dog)




#9.9
class Counter:
  def __init__(self,number = 0):
    self.__number = number
  def __str__(self):
    return 'C({})'.format(self.__number)
  def set_number(self,number):
    if (number>100) or number <= -1:
      self.__number = 0
    else:
      self.__number = number
  def get_number(self):
    return self.__number
  def reset(self):
    return Counter(0)
  def inc(self):
    self.__number += 1
  def dec(self):
    self.__number -= 1
    return Counter(self.__number)
  def __add__(self,other):
    num = self.__number + other.__number
    return Counter(num)
  def __sub__(self,other):
    num = self.__number - other.__number
    return Counter(num)

c1 = Counter(10)
c2 = Counter(20)
c3 = c1 + c2
c4 = c1 - c2
print('c3 = ',c3)
print('c4 = ',c4)




#9.11
class Student:
    def __init__(self, name, student_id, korean_quiz=0, math_quiz=0, science_quiz=0, total_score=270, avg_score=100):
        self.__name = name
        self.__student_id = student_id
        self.__korean_quiz = korean_quiz
        self.__math_quiz = math_quiz
        self.__science_quiz = science_quiz
        self.__total_score = total_score
        self.__avg_score = avg_score

    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id

    def set_korean_quiz(self, korean_quiz):
        self.__korean_quiz = korean_quiz

    def get_korean_quiz(self):
        return self.__korean_quiz

    def set_math_quiz(self, math_quiz):
        self.__math_quiz = math_quiz

    def get_math_quiz(self):
        return self.__math_quiz

    def set_science_quiz(self, science_quiz):
        self.__science_quiz = science_quiz

    def get_science_quiz(self):
        return self.__science_quiz

    def get_total_score(self):
        return self.__korean_quiz + self.__math_quiz + self.__science_quiz

    def get_avg_score(self):
        return self.get_total_score() / 3

    def __str__(self):
        return '이름 : {}, 학번 : {}\n국어성적 : {}, 수학성적 : {}, 과학성적 : {}\n합계 : {}, 평균 : {}'.format(
            self.__name, self.__student_id, self.__korean_quiz, self.__math_quiz, self.__science_quiz, self.__total_score, self.get_total_score() / 3)

name = input('학생의 이름을 입력하시오 : ')
student_id = input('학생의 학번을 입력하세요 : ')

student = Student(name, student_id)

korean_quiz = int(input('학생의 국어 성적을 입력하세요 : '))
math_quiz = int(input('학생의 수학 성적을 입력하세요 : '))
science_quiz = int(input('학생의 과학 성적을 입력하세요 : '))

student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)
print(student)




#9.13
class Rectangle:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def __str__(self):
        return "Rectangle : (x = {}, y = {}, w = {}, h = {}), 면적 : {}".format(self.__x, self.__y, self.__width, self.__height, self.__width*self.__height)

    def contains(self, other):
        if self.__x <= other.__x and self.__y >= other.__y and self.__width >= other.__width and self.__height >= other.__height:
            return True
        else:
            return False

    def overlaps(self, other):
        if (self.__height+self.__y) > (other.__y) and (self.__x+self.__width) > (other.__x):
            return True
        else:
            return False

r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(0, -10, 10, 10)
r3 = Rectangle(-100, 0, 120, 100)

print('r1 =', r1)
print('r2 =', r2)
print('r3 =', r3)

print('r1 contains r2 :', r1.contains(r2))
print('r1 contains r3 :', r1.contains(r3))
print('r2 contains r1 :', r2.contains(r1))
print('r3 contains r1 :', r3.contains(r1))

print('r1 overlaps r2 :', r1.overlaps(r2))
print('r1 overlaps r3 :', r1.overlaps(r3))
print('r2 overlaps r1 :', r2.overlaps(r1))
print('r3 overlaps r1 :', r3.overlaps(r1))




#6번
class Car:
  def method(self):
    print("슈퍼 클래스")

class Sedan(Car):
  def method(self):
    print("서브 클래스")

myCar = Car()
mySedan = Sedan()
myCar.method()
mySedan.method()

#슈퍼 클래스 서브 클래스




#7번
class Car:
    speed = 0

    def upSpeed(self, value):
        self.speed = self.speed + value

class RVCar(Car):  # Car 클래스를 상속받는 RVCar 클래스 정의
    seatNum = 0

    def getSeatNum(self):
        return self.seatNum
