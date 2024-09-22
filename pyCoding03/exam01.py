student = [['강호명','10100',36.6,67.1,55.4,'none'],   # [이름, 학번, 수학점수, 국어점수, 정보점수, 빈공간(삭제 필요)]
          ['이규래','10400',96.1,'none',75.2,87.3]]    # [이름, 학번, 수학점수, 빈공간(삭제 필요), 국어점수, 정보점수]
student[0].remove('none')
student[1].remove('none')
student[0].append(student[0][2]+student[0][3]+student[0][4])
student[1].append(student[1][2]+student[1][3]+student[1][4])

student[0].append(int(student[0][5]/3))
student[1].append(int(student[1][5]/3))

if student[0][6] >= 90:
  student[0].insert(2,'A')
elif student[0][6] >= 80:
  student[0].insert(2,'B')
else:
  student[0].insert(2,'C')
  
if student[1][6] >= 90:
  student[1].insert(2,'A')
elif student[1][6] >= 80:
  student[1].insert(2,'B')
else:
  student[1].insert(2,'C')
  
print(student[0])
print(student[1])