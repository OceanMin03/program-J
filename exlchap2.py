#AI프로그래밍및실습 #2장연습문제풀이 #홀수문항

#2.1
print(200, '+', 300,'+', 400, '=', 200+300+400)




#2.3
width =30
height = 60
print("사각형의 면적 : ", width*height)




#2.5
밑변 = int(input("정사각형의 밑변의 길이를 입력하시오 : "))
print('정사각형의 면적: ', 밑변*밑변)




#2.7
import math
print('10! = ', 1*2*3*4*5*6*7*8*9*10)




#2.9
import numpy as np

# 섭씨온도 배열 생성 (0도에서 50도까지 10도 단위)
celsius = np.arange(0, 51, 10).reshape(-1, 1)

# 화씨온도 계산
fahrenheit = (9/5) * celsius + 32

# 섭씨와 화씨를 열로 결합하여 행렬 생성
temperature_matrix = np.hstack((celsius, fahrenheit))

# 결과 출력
print("   섭씨  화씨")
for row in temperature_matrix:
    print(f"{row[0]:6.1f} {row[1]:6.1f}")




#2.11
# 화씨온도 입력받기
fahrenheit = float(input("화씨온도를 입력하세요: "))

# 섭씨온도 계산
celsius = (fahrenheit - 32) * 5/9

# 결과 출력
print(f"화씨 {fahrenheit}도는 섭씨 {celsius:.1f}도 입니다.")




#2.13
# 반지름 입력 받기
radius = float(input("원의 반지름을 입력하세요: "))

#파이 값 입력
PI = 3.141592

# 원의 둘레 계산
circumference = 2 * PI * radius

# 원의 면적 계산0
area = PI * radius**2

# 결과 출력
print(f"원의 둘레 = {circumference}, 원의 면적 = {area}")




#2.15
# 밑변과 높이 입력받기
a = float(input("밑변을 입력하세요: "))
b = float(input("높이를 입력하세요: "))

# 빗변 계산 (피타고라스의 정리 이용)
c = (a**2 + b**2)**0.5

# 결과 출력
print(f"빗변: {c}")




#2.17
# 2의 거듭제곱 수 10개 생성하여 출력
result = 1
for i in range(10):
    print(result, end=" ")
    result <<= 1




#2.19
# 사용자로부터 정수 입력 받기
n = int(input("정수를 입력하세요: "))

# 입력값이 0에서 100 사이의 짝수인지 판단하여 출력
result = 0 <= n <= 100 and n % 2 == 0
print(f"입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? {result}")




#2.21
# 사용자로부터 정수 입력 받기
n = int(input("정수를 입력하세요: "))

# 입력된 정수를 2진수로 출력
print("입력된 값 의 2진수 값:", bin(n))

# 입력된 정수에 대한 비트단위 부정 값 출력
bitwise_not = ~n
print("입력된 값 의 2진수 값에 대한 비트단위 부정값:", bitwise_not)




#2.23
# 사용자로부터 세 자리 정수 입력 받기
n = int(input("세 자리 정수를 입력하세요: "))

# 입력된 정수의 각 자리 십진수 값 계산
hundreds = n // 100
tens = (n % 100) // 10
units = n % 10

# 결과 출력
print(f"백의 자리: {hundreds}")
print(f"십의 자리: {tens}")
print(f"일의 자리: {units}")
