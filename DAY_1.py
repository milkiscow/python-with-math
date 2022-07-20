x1, x2 = 1, 0
w1, w2 = 0.3, 0.7
result = x1*w1 + x2*w2
print(result)
d = 0.2
if result >= d:
    print(1)
else:
    print(0)
    
    
    
# 퍼셉트론 도식화
import matplotlib.pyplot as plt # 함수를 그려주는 pyplot 라이브러리 사용
import numpy as np

# 기본적인 점 (0.0)~(1,1) 구성
plt.plot([0,0,1,1],[0,1,0,1],'ro')

# 가중치와 임계값 입력
w1, w2, d = 0.3, 0.3, 0.5

x = np.array([0,1])
plt.plot(x, (d-w1*x)/w2) # x1w1 + x2w2 = d 를 그림

# d가 음수일 경우 아래 영역
plt.show()



# 퍼셉트론 함수로 구현하기
def pcep(x1, x2, w1, w2, d):
  result = 0
  if x1*w1 + x2*w2 > d:
    result = 1
  return(result)

# AND 구현하기
def AND(x1, x2):
    return(pcep(x1, x2, 0.3, 0.3, 0.5))
# OR 구현하기
def OR(x1, x2):
    return(pcep(x1, x2, 0.3, 0.3, 0.1))
# NAND 구현하기
def NAND(x1, x2):
    return(pcep(x1, x2, -0.3, -0.3, -0.5))
# XOR 구현하기
def XOR(x1, x2):
  return(AND(NAND(x1, x2), OR(x1, x2)))
# print(AND(0, 0))
# print(AND(0, 1))
# print(AND(1, 0))
# print(AND(1, 1))

# print(OR(0, 0))
# print(OR(0, 1))
# print(OR(1, 0))
# print(OR(1, 1))

# print(NAND(0, 0))
# print(NAND(0, 1))
# print(NAND(1, 0))
# print(NAND(1, 1))

# print(XOR(0, 0))
# print(XOR(0, 1))
# print(XOR(1, 0))
# print(XOR(1, 1))
           
# for i in range(0, 2):
#     for j in range(0, 2):
#         print(AND(OR(i, j), NAND(i, j)))