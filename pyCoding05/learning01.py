# 함수 
def allSum(a,b):
  print(a+b)



def numInput():
  a = int(input('숫자를 입력:'))
  return a, 10

num1, num2 = numInput()
allSum(num1, num2)