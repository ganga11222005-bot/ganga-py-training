class StudentMarks:
    def __init__(self, marks):
        self.marks = marks
    def calculate(self):
        total = sum(self.marks)
        average = total / len(self.marks)
        passed = 0
        failed = 0
        for mark in self.marks:
            if mark >= 40:
                passed += 1
            else:
                failed += 1
        print("Total Marks:", total)
        print("Average Marks:", average)
        print("Passed Students:", passed)
        print("Failed Students:", failed)
# Main Program
marks_list = []
n = int(input("Enter number of students: "))
for i in range(n):
    mark = int(input("Enter mark: "))
    marks_list.append(mark)
ob = StudentMarks(marks_list)
ob.calculate()