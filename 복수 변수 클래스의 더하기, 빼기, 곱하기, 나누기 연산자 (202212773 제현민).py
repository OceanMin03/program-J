class comax:
    def __init__(self, x, y):
        self.real = x
        self.imag = y
        
    def __add__(self, b):
        return comax(self.real + b.real, self.imag + b.imag)
        
    def __sub__(self, b):
        return comax(self.real - b.real, self.imag - b.imag)
        
    def __mul__(self, b):
        return comax(self.real * b.real - self.imag * b.imag, self.real * b.imag + self.imag * b.real)

# 사용자로부터 첫 번째 복소수 입력 받기
real_part1 = float(input("첫 번째 복소수의 실수를 입력하세요: "))
imag_part1 = float(input("첫 번째 복소수의 허수를 입력하세요: "))
z1 = comax(real_part1, imag_part1)

# 사용자로부터 두 번째 복소수 입력 받기
real_part2 = float(input("두 번째 복소수의 실수를 입력하세요: "))
imag_part2 = float(input("두 번째 복소수의 허수를 입력하세요: "))
z2 = comax(real_part2, imag_part2)

# 덧셈 연산 수행
add_result = z1 + z2
print("덧셈 결과:", add_result.real, "+", add_result.imag, "i")

# 뺄셈 연산 수행
sub_result = z1 - z2
print("뺄셈 결과:", sub_result.real, "+", sub_result.imag, "i")

# 곱셈 연산 수행
mul_result = z1 * z2
print("곱셈 결과:", mul_result.real, "+", mul_result.imag, "i")
