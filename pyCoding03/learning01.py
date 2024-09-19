# 리스트
# tempList = ['안녕!',10,20,40,50]
# print(tempList[-1])

# tempList = [[10,20,30],[40,50,60]]
# print(tempList[1][1])

# tempList = [10,20,30]
# print('변경 전:',tempList)
# tempList[0] = 1
# tempList[1] = 2
# tempList[2] = 3
# print('변경후 :',tempList)

tempList = [10,20,30]
#추가
tempList.append(40)
print(tempList)
tempList.insert(2,25)
print(tempList)
#삭제
tempList.remove(40)
print(tempList)
del(tempList[2])
print(tempList)