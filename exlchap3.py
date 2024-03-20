#AI프로그래밍및실습 #3장연습문제풀이 #홀수문항

#3.1
print(100 > 200)
print(100 >= 200)
print(100 < 200)
print(100 <= 200)
print(100 == 200)
print(100 != 200)
print(200 == 200)
print(200 != 200)
print(True or True)
print(True or False)
print(True and False)
print(True and True)
print(True or True and False)
print(True and True or False)
print('Morning' < 'morning')
print('A' > 'B')




#3.3
age = int(input("나이를 입력하시오 : "))
height = int(input("키를 입력하시오(단위cm) : "))

if age >= 19 and height >= 150:
  print("입장할 수 있습니다")
else:
    print("입장할 수 없습니다")




#3.5
num1, num2 = map(int, input("두 개의 정수를 입력하세요: ").split())

if num1 < num2:
    print(num1, num2)
else:
    print(num2, num1)




#3.7
score = int(input("게임점수를 입력하시오 : "))

if score <= 1000:
  print("입문자입니다.")
else:
  print("고수입니다.")




#3.9
num = int(input("정수를 입력하시오: "))

divisible_by_2 = num % 2 == 0
divisible_by_3 = num % 3 == 0

if divisible_by_2:
    print("{}는(은) 2로 나누어집니다.".format(num))
else:
    print("{}는(은) 2로 나누어지지 않습니다.".format(num))

if divisible_by_3:
    print("{}는(은) 3로 나누어집니다.".format(num))
else:
    print("{}는(은) 3로 나누어지지 않습니다.".format(num))

if divisible_by_2 and divisible_by_3:
    print("{}는(은) 2와 3 모두로 나누어집니다.".format(num))
else:
    print("{}는(은) 2와 3 모두로 나누어지지 않습니다.".format(num))




#3.11

winning_numbers = [2, 3, 9]

user_numbers = list(map(int, input("세 복권번호를 입력하시오 : ").split()))

correct_count = sum(num in winning_numbers for num in user_numbers)

if correct_count == 3:
    print("1억 원")
elif correct_count == 2:
    print("1천만 원")
elif correct_count == 1:
    print("1만 원")
else:
    print("다음 기회에...")




#3.13
import math

center_x, center_y = 3, 4
radius = 10

x_str, y_str = input("점의 좌표 x와 y를 입력하세요 : ").split()
x, y = float(x_str), float(y_str)

distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)

if distance <= radius:
    print("원의 내부에 있음")
else:
    print("원의 외부에 있음")




#3.15
#1) for 문
for i in range(1, 10):
    print("2 *", i, "=", 2*i)

#2) while
i = 1
while i < 10:
    print("2 *", i, "=", 2*i)
    i += 1




#3.17
#(1)
for i in range(3):
  print('Python ')
  print('is ')
  print('FUN! ')

#(2)
for i in range(3):
  print('Python ')
  print('is ')
print('FUN! ')

#(3)
for i in range(3):
  print('Python ')
print('is ')
print('FUN! ')




#3.19
print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
print("- 햄버거(입력 b)")
print("- 치킨(입력 c)")
print("- 피자(입력 p)")

while True:
    choice = input("메뉴를 선택하세요(알파벳 b, c, p 입력) : ")
    if choice in ['b', 'c', 'p']:
        break
    else:
        print("메뉴를 다시 입력하세요(알파벳 b, c, p 입력) : ")

if choice == 'b':
    print("햄버거를 선택하였습니다.")
elif choice == 'c':
    print("치킨을 선택하였습니다.")
else:
    print("피자를 선택하였습니다.")




#3.21
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    else:

        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

num = int(input("숫자를 입력하세요: "))

if is_prime(num):
    print(f"{num}은(는) 소수입니다.")
else:
    print(f"{num}은(는) 소수가 아닙니다.")




#3.23
def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

num = int(input("숫자를 입력하세요: "))

result = sum_of_squares(num)
print(f"결과는 {result}입니다.")




#3.25
depth = 0
days = 0

while depth < 30:
  days = days + 1
  depth = depth + 7
  if days !=1:
    depth = depth - 5
  print('day : ', str(days),' 달팽이의 위치 : ', str(depth), '미터')
print('우물을 탈출하는 데 걸린 날은',str(days),'일 입니다.')






#3.27
def is_armstrong(num):
    # 각 자리수의 세제곱의 합 계산
    sum_of_cubes = sum(int(digit) ** 3 for digit in str(num))
    # 입력된 수와 세제곱의 합이 같으면 True 반환
    return num == sum_of_cubes

# 세 자리 정수 중에서 암스트롱 수 찾기
armstrong_numbers = [num for num in range(100, 1000) if is_armstrong(num)]

# 찾은 암스트롱 수 출력
print("세 자리의 암스트롱 수:", " ".join(map(str, armstrong_numbers)))




#3.29
fuel_level = 500

while True:
    action = input("충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오: ")

    if action.startswith('+'):
        fuel_added = int(action[1:])
        fuel_level += fuel_added
    elif action.startswith('-'):
        fuel_used = int(action[1:])
        fuel_level -= fuel_used

    print("현재 탱크양은 {}입니다.".format(fuel_level))

    if fuel_level < 50:
        print("경고: 연료가 10% 미만이니 충전하세요!")
        break




#3.31
def sum_of_divisors(n):
    divisor_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i
    return divisor_sum

def find_amicable_numbers(limit):
    amicable_pairs = []
    for num in range(2, limit + 1):
        partner = sum_of_divisors(num)
        if partner > num and sum_of_divisors(partner) == num:
            amicable_pairs.append((num, partner))
    return amicable_pairs

# 1에서 20,000 사이의 친화수를 찾음
limit = 20000
amicable_pairs = find_amicable_numbers(limit)

# 결과 출력
for pair in amicable_pairs:
    print("{}의 친화수 {}".format(pair[0], pair[1]))
    print("{}의 친화수 {}".format(pair[1], pair[0]))

