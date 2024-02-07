import numpy as np
marks=np.random.randint(80,100,size=(5,6))
print("original marks",marks)

students=len(marks)
subjects=len(marks[0])
for i in range(students):
    for j in range(subjects):
        marks[i][j]+=5
print(f"final marks {marks}")