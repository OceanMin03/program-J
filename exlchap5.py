#5장 연습문제

#5.1
list_ex = [10, 20, 30, 40, 50, 60, 70]
high = 5
low = 3
print(list_ex[low])
print(list_ex[low+2])
print(list_ex[high-low])
print(list_ex[low-high])
print(list_ex[-1])
print(list_ex[-low])
print(list_ex[2*3])
print(list_ex[2]*3)
print(list_ex[5 % 4])
print(len(list_ex))




#5.3
list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]
for i in list1:
  for j in list2:
    print(i, '*', j, '=', i*j)




#5.5
list1 = ['I like', 'I love']
list2 = ['pancakes.', 'kiwi juice.', 'espresso.']

for i in list1:
    for j in list2:
        print(i, j)




#5,7
n_list = [10, 20, 30, 50, 60]
print("리스트 원소들 :", n_list)
total = 0
for i in n_list:
  total = total + i

print("리스트 원소들의 합: ", total)




#5.9
n_list = [10, 20, 30, 50, 60]
print("리스트 원소들 :", n_list)
max1 = 0
for i in n_list:
  if i>max1:
    max1 = i
print("리시트의 원소들 중 최댓값 :", max1)




#5.11
nums = list(map(int,input('5개의 수를 입력하세요 : ').split()))
print('합 :', sum(nums))
total = 0
for i in nums:
  total = total + i
average = total / len(nums)
print('평균 :', average)
print('최댓값 :', max(nums))
print('최솟값 :', min(nums))




#5.13
nums = list(map(int,input('10개의 수를 입력하세요 : ').split()))
print('합 :', sum(nums))
total = 0
for i in nums:
  total = total + i
average = total / len(nums)
print('평균 :', average)
nums_sigma = 0
for i in nums:
  nums_sigma += (i - average) ** 2
print('표준편자 : {: .2f}'.format((nums_sigma/len(nums))**0.5))




#5.15
greet = 'Have a beautiful day.'
print(greet[0:4])
print(greet[7:16])
print(greet[17:20])




#5.17
animals = ['dog', 'cat', 'tiger', 'lion']
print('animals =', animals)

animals.remove('dog')
animals.extend(['dog'])
print(animals)

for i in animals:
  print('I love',i,'.')




#5.19
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
print('s_list = ', s_list)
new_s_list = []
for i in range(0,len(s_list)):
  temp = s_list[i]
  if new_s_list.count(temp) == 0:
    new_s_list.append(temp)
print('new_s_list = ', new_s_list)




#5.21
src = 'a2b3c6a2c3f1g1'

for ch in src:
  if ch.isnumeric():
    for i in range(int(ch)):
      print(ch_old,end='')
  else:
    ch_old = ch




#5.23
#(1)
person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1+person2+person4

def how_many_people():
  n_people = len(person_list)/5
  n_people = int(n_people)
  print(str(n_people)+'명의 정보가 담겨있습니다')

how_many_people()




#(2)
person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1+person2+person3+person4

def count_males_females():
  n_males = person_list.count(1)
  n_females = person_list.count(0)
  print('리스트에는 남자가', n_males, '명, 여자가', n_females, '명 입니다.')

count_males_females()




#(3)
person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1+person2+person3+person4

def average_age():
  compute_average_age = sum(person_list[1:len(person_list):5])/(len(person_list)/5)
  print('평균 나이는', compute_average_age, '세 입니다.')

average_age()




#(4)
person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1+person2+person3+person4

def display_people(person_list):
  list1 = person_list[0:5]
  list2 = person_list[5:10]
  list3 = person_list[10:15]
  list4 = person_list[15:]
  print(list1)
  print(list2)
  print(list3)
  print(list4)

display_people(person_list)

