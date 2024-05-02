class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        print(students)
        print(sandwiches)
        while count < len(students):
            if len(sandwiches) == 0:
                break
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                print(students)
                students.append(students.pop(0))
                count += 1
                
        return len(students)