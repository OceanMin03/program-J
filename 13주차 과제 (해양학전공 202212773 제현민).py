import numpy as np


def costf(w, x, y):
    yp = w.T @ x
    return (yp-y.T)@(yp-y.T).T

def gradJ(w, x, y):
    return np.array([8*w[0]+4*w[1]+4*w[2]-4,4*w[0]+4*w[1]+2*w[2]-4,4*w[0]+2*w[1]+4*w[2]-4])

def step_func(yvalue):

    y = yvalue>0

    return 2*y.astype(int)-1

xi = np.array([[1, 1, 1, 1], [0, 0, 1, 1], [0, 1, 0, 1]])  
yi = np.array([[-1], [1], [1], [1]])
wi = np.array([[0], [0], [0]])  


rho = 0.001


J = costf(wi, xi, yi)

max_iterations = 1000  # 최대 반복 횟수 설정

iteration = 0

while True:
    JP = J
    
    J = costf(wi, xi, yi)
    delW = gradJ(wi, xi, yi)
    wi = wi - rho * delW
    J = costf(wi, xi, yi)
    
    iteration += 1
    
    if np.abs((J - JP) / J) < 0.000001 or iteration >= max_iterations:
        break


print("Optimized weights:", wi)
print("Final cost:", J)
print(wi.T @ xi)

# 최적화된 가중치를 사용하여 예측 수행
predicted_y = np.dot(wi.T, xi)
# 예측된 값과 실제 값 간의 오차 계산
error = predicted_y - yi.T
# 정확도 계산
accuracy = np.mean(np.sign(predicted_y) == np.sign(yi.T))

print("Predicted values:", predicted_y)
print("Actual values:", yi.T)
print("Error:", error)
print("Accuracy:", accuracy)