student = [['강호명','10100',36.6,67.1,55.4,'none'],   # [이름, 학번, 수학점수, 국어점수, 정보점수, 빈공간(삭제 필요)]
          ['이규래','10400',96.1,'none',75.2,87.3]] 
student[0].remove('none')
student[1].remove('none')

student.append([input('학생 이름 입력:'),input('학생 학번 입력:'),float(input('수학 점수 입력:')),float(input('국어 점수 입력:')),float(input('정보 점수 입력:'))])

# 합 추가

# student[0].append(student[0][2]+student[0][3]+student[0][4])
# student[1].append(student[1][2]+student[1][3]+student[1][4])
# student[2].append(student[2][2]+student[2][3]+student[2][4])

student[0].append(sum(student[0][2:5]))
student[1].append(sum(student[1][2:5]))
student[2].append(sum(student[2][2:5]))

# 평균
student[0].append(int(student[0][5]/3))
student[1].append(int(student[1][5]/3))
student[2].append(int(student[2][5]/3))

if student[0][2] < 30 or student[0][3] < 30 or student[0][4]<30:
 student[0].insert(2,'F')
elif student[0][6] >= 90:
  student[0].insert(2,'A')
elif student[0][6] >= 80:
  student[0].insert(2,'B')
else:
  student[0].insert(2,'C')
  
if student[1][2] < 30 or student[1][3] < 30 or student[1][4]<30:
 student[1].insert(2,'F')
elif student[1][6] >= 90:
  student[1].insert(2,'A')
elif student[1][6] >= 80:
  student[1].insert(2,'B')
else:
  student[1].insert(2,'C')


if student[2][2] < 30 or student[2][3] < 30 or student[2][4]<30:
 student[2].insert(2,'F')
elif student[2][6] >= 90:
  student[2].insert(2,'A')
elif student[2][6] >= 80:
  student[2].insert(2,'B')
else:
  student[2].insert(2,'C')
  
print(student[0])
print(student[1])
print(student[2])

print('수학평균:',int((student[0][3]+student[1][3]+student[2][3])/3),',국어평균:',int((student[0][4]+student[1][4]+student[2][4])/3),',정보평균:',int((student[0][5]+student[1][5]+student[2][5])/3))
