def solve(students):
#    min_mark = min(x[1] for x in students)
#    students = [x for x in students if x[1] > min_mark]
   min2_mark = min(x[1] for x in students)
   students = sorted([x[0] for x in students if x[1] == min2_mark])
   for x in students:
      print(x)

students = [['Amal',37],['Bimal',37],['Tarun',36],['Akash',41],['Himadri',39]]
solve(students)