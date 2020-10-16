# Author: Dymea Schippers dxs5940@psu.edu

def getGradePoint(grade):
  gradep = 0.0
  if grade == "A":
    gradep = 4.0
  elif grade == "A-":
    gradep = 3.67
  elif grade == "B+":
    gradep = 3.33
  elif grade == "B":
    gradep = 3.0
  elif grade == "B-":
    gradep = 2.67
  elif grade == "C+":
    gradep = 2.33
  elif grade == "C":
    gradep = 2.0
  elif grade == "D":
    gradep = 1.0
  else:
    gradep = 0.0
  return gradep

# User input for courses 1, 2, 3
def run():
  gpa_total = 0.0
  credit_total = 0.0

  for i in range(1,4):
    grade = input (f"Enter your course {i} letter grade: ")
    gradep = getGradePoint(grade)
    credit = float(input(f"Enter your course {i} credit: "))
    print(f"Grade point for course {i} is: {gradep}")
    gpa = gradep * credit
    gpa_total += gpa
    credit_total += credit
  GPA = gpa_total / credit_total
  print(f"Your GPA is: {GPA}")


if __name__ == "__main__":
  run()
