#반복문
# i = 0
# while True:
#   print(i)
#   i = i+1

# for i in range(0,3,1):
#   print(i)
  
# a = [50,40,10,20,30]
# for i in  a:
#   print(i)

# i = 0
# while i < 3:
#   print(i)
#   j = 0
#   while j < 3:
#     print(i,j)
#     j = j+1
#   i = i+1
  
# for i in range(2,10,1):
#   print(i,'단')
#   for j in range(1,10,1):
#     print(i,'*',j,'=',i*j)
    
a = ['바나나','사과','배','딸기']
for i in a:
  print(i)
  if i == '배':
    print('배 찾음')
    break