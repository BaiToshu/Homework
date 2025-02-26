students_score={
    "Ivan":5.00,
    "Alex": 3.50,
    "Maria":5.50,
    "Georgy": 5.00
}

scores=list(students_score.values())

highscore=scores[0]
lowscore=scores[0]

for high in range(0,len(scores),1):
    if highscore<scores[high]:
        highscore=scores[high]

for low in range(0,len(scores),1):

    if lowscore>scores[low]:
        lowscore=scores[low]

for key, value in students_score.items():
    if value == highscore:
        print(f'Highest score: {key} - {value}')
    if value == lowscore:
        print(f'Lowest score: {key} - {value}')
