#4.1
def my_greet():
  print('환영합니다.')

my_greet()
my_greet()




#4.3
def max2(m, n):
  if m>n:
    return print(m, '과', n, '중 큰 수는 : ', m)
  else:
    return print(m, '과', n, '중 큰 수는 : ', n)

def min2(m, n):
  if m>n:
    return print(m, '과', n, '중 작은 수는 : ', n)
  else:
    return print(m, '과', n, '중 작은 수는 : ', m)

max2(100, 200)
min2(100, 200)




#4.5
def inch2cm(inch):
  for inch in range(1, inch):
    cm = inch*2.54
    print(inch, '인치 = ', cm, '센티미터')

inch2cm(6)




#4,7
a, b, c = input('세 수를 입력하시오 : ').split()
a = int(a)
b = int(b)
c = int(c)

def mean3(a, b, c):
  print(a, ',', b, ',', c, '의 평균값은', (a+b+c)/3)
def max3(a, b, c):
  print(a, ',', b, ',', c, '의 평균값은', max(a,b,c))
def min3(a, b, c):
  print(a, ',', b, ',', c, '의 평균값은', min(a,b,c))

mean3(a, b, c)
max3(a, b, c)
min3(a, b, c)




#4.9
nums = list(map(int,input('정수를 여러 개 입력하시오 : ').split()))

def mean_of_n(nums):
  print('평균값은', sum(nums)/len(nums))

def max_of_n(nums):
  print('최댓값은', max(nums))

def min_of_n(nums):
  print('최솟값은', min(nums))

mean_of_n(nums)
max_of_n(nums)
min_of_n(nums)




#4.11
x1 = int(input('x1 좌표를 입력하시오 : '))
y1 = int(input('y1 좌표를 입력하시오 : '))
x2 = int(input('x2 좌표를 입력하시오 : '))
y2 = int(input('y2 좌표를 입력하시오 : '))

def area(x1, y1, x2, y2):
  result = (x2-x1)*(y2-y1)*0.5
  print('직각삼각형의 면적은 : ', result)

area(x1, y1, x2, y2)




#4.13
def a1(s):
  print(s**3)
def b1(w, h, l):
  print(l*w*h)
def c1(r, h):
  print(3.14*(r**2)*h*(1/3))
def d1(r):
  print((4/3)*3.14*(r**3))
def e1(r, h):
  print(3.14*(r**2)*h)

a1(12) #모서리의 길이가 12인 정육면체 부피
a1(20) #모서리의 길이가 20인 정육면체 부피
b1(3, 5, 6) #가로, 세로, 길이가 각각 3, 5, 6인 직육면체의 부피
c1(20, 10) #반지름과 높이가 각각 20, 10인 원뿔의 부피
d1(15) #반지름이 15인 구의 부피
e1(20, 10) #반지름과 높이가 각각 20, 10인 원기둥의 부피




#4.15
def my_sort(*nums):
  print(sorted(nums))

my_sort(45, 3, 4, 56, 5)
my_sort(9, 8, 7, 6, 5, 4, 3)




#4.17
def sum_range(n1,n2):
  a=0
  for i in range(n1,n2+1):
    a += i
  return a

print('{0:2d}에서 {1:3d}까지의 정수의 합 : {2:4d}'.format(10,20,sum_range(10,20)))
print('{0:2d}에서 {1:3d}까지의 정수의 합 : {2:4d}'.format(40,100,sum_range(40,100)))




#4.19
def fibo(n):
  if n<=1:
    return 1
  else:
    return(fibo(n-1)+fibo(n-2))

n = int(input("fibo(n)의 n을 입력하세요 : "))
print('fibo(',n,') = ', fibo(n))




#4.21
birth = input('주민등록번호 첫 6숫자 형식 입력: ')
birth = int(birth)
n = 0

a1 = birth // 10000
b = birth // 100%100
c = birth % 100

if birth >= 500000:
  a2 = 1900 + a1
  print('{}년 {}월 {}일'.format(a2, b, c))
else:
  a3 = 2000+a1
  print('{}년 {}월 {}일'.format(a3, b, c))




#4.23
def area_and_circumference(r):
  while True:
    r = int(input('반지름을 입력하시오 : '))
    if r <=0:
      print('프로그램을 종료합니다.')
      break
    print('넓이 : ', r**2*3.14, ', 둘레 :', r*2*3.14)

r = 0
area_and_circumference(r)




#4.25
s1 = 'Kand Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'

print(s1, '(은)는', s1.replace(' ', '').upper(), '(으)로 수정됨')
print(s2, '(은)는', s2.replace(' ', '').replace('Young-Min', 'YoungMin').upper(),'(으)로 수정됨')
print(s3, '(은)는', s3.replace(' ', '').upper(), '(으)로 수정됨')
print(s4, '(은)는', s4.replace(' ', '').replace('Dong-Yun', 'DongYun').upper(),'(으)로 수정됨')
print('KANGYOUNGMIN : ', 'KANGYOUNGMIN'.count('N'), '개의 N이 나타남')
print('KANGYOUNGMIN : ', 'KANGYOUNGMIN'.count('N'), '개의 N이 나타남')
print('PARKDONGMIN : ', 'PARKDONGMIN'.count('N'), '개의 N이 나타남')
print('PARKDONGMIN : ', 'PARKDONGMIN'.count('N'), '개의 N이 나타남')




#4.27
def unit_fraction(frac):
    denom = int(1 / frac)  #1/0.27의 경우 3.703..를 반환하므로 이를 정수로 변환

    d1 = frac - 1 / (denom + 1) # frac - 1/(분모 + 1) 값 d1하고
    d2 = 1 / denom - frac       # 1/(분모)- frac 값 d2를 구하기
    if d1 < d2:                 # d1과 d2 중에서 더 작은 값이 해
        return denom + 1
    else:
        return denom

f_val = float(input("1보다 작고 0보다 큰 소수를 입력하세요: "))

if f_val <= 0.0 or f_val >= 1.0:
    print('입력 오류입니다.')
else:
    denom = unit_fraction(f_val)
    print('가장 가까운 단위 분수는 1/{0}이며, 이 값은 {1:.50f}입니다.'.format(denom, f_val))
