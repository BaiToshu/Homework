students_score={
    "Ivan":5.00,
    "Alex": 3.50,
    "Maria":5.50,
    "Georgy": 5.00
}

best_students_score={

}

for key, value in students_score.items():
    if value>4.00:
        best_students_score[key]=value

print(best_students_score)

#Second option with lists

student=["Ivan", "Alex", "Maria", "Georgy"]
score=[5.00, 3.50, 5.50, 5.00]

for x in range(0,len(student),1):
    if score[x]>4.00:
        best_students_score[student[x]]=score[x]

print(best_students_score)


