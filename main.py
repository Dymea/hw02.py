# Author: Dymea Schippers dxs5940@psu.edu

def getGradePoint(grade1, grade2, grade3):
  if grade1 or grade2 or grade3 == 'A':
    return 4.0
  elif grade1 or grade2 or grade3== 'A-':
    return 3.67
  elif grade1 or grade2 or grade3== 'B+':
    return 3.33
  elif grade1 or grade2 or grade3 == 'B':
    return 3.0
  elif grade1 or grade2 or grade3 == 'B-':
    return 2.67
  elif grade1 or grade2 or grade3 == 'C+':
    return 2.33
  elif grade1 or grade2 or grade3 == 'C':
    return 2.0
  elif grade1 or grade2 or grade3 == 'D':
    return 1.0
  elif grade1 or grade2 or grade3 == 'F':
    return 0.0
  else:
    return 0.0

# User input for courses 1, 2, 3
def run():
  grade1 = input("Enter your course 1 letter grade: ")
  credit1 = input("Enter your course 1 credit: ")
  credit1 = int(credit1)
  print("Grade point for course 1 is: " + getGradePoint(grade1, grade2, grade3))
  grade2 = input("Enter your course 2 letter grade: ")
  credit2 = input("Enter your course 2 credit: ")
  credit2 = int(credit2)
  print("Grade point for course 2 is: " + getGradePoint(grade1, grade2, grade3))
  grade3 = input("Enter your course 3 letter grade: ")
  credit3 = input("Enter your course 3 credit: ")
  credit3 = int(credit3)
  print("Grade point for course 3 is: " + getGradePoint(grade1, grade3))
  print(f"Your GPA is: {(grade1 * credit1 + grade2 * credit2 + grade3 * credit3) / (credit1 + credit2 + credit3)}")


if __name__ == "__main__":
  run()
