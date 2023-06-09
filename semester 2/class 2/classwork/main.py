file = open('semester 2\\class 1\\grades.csv')
result = []
for line in file:
    arr = line.split(',')
    print(arr)
    result.append(arr)
 

sum_of_grades = sum(map(int, result[6][1:]))
print(sum_of_grades)

file.close()


print(result[4][2])

file.close()


def clear_file(file_path):
    with open(file_path, 'w') as file:
        file.write('')



with open('class 1\grades.csv', 'r') as file:
    a = file.read()
    a = a.replace('"','')
    clear_file('class 1\grades.csv')
    file.write(a)
    


with open('semester 2\\class 1\\grades.csv', 'r') as file:
    result = []
    sixth_student = result[6]
    list_of_grades = sixth_student[1:]
    print(list_of_grades)
    

        
