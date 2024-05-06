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

    def __truediv__(self, b):
        # 분모의 제곱을 계산
        denominator = b.real ** 2 + b.imag ** 2
        # 분자의 실수부와 허수부 계산
        numerator_real = self.real * b.real + self.imag * b.imag
        numerator_imag = self.imag * b.real - self.real * b.imag
        return comax(numerator_real / denominator, numerator_imag / denominator)

# 사용자로부터 첫 번째 복소수 입력 받기
real_part1 = float(input("첫 번째 복소수의 실수부를 입력하세요: "))
imag_part1 = float(input("첫 번째 복소수의 허수부를 입력하세요: "))
z1 = comax(real_part1, imag_part1)

# 사용자로부터 두 번째 복소수 입력 받기
real_part2 = float(input("두 번째 복소수의 실수부를 입력하세요: "))
imag_part2 = float(input("두 번째 복소수의 허수부를 입력하세요: "))
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

# 나눗셈 연산 수행
div_result = z1 / z2
print("나눗셈 결과:", div_result.real, "+", div_result.imag, "i")
