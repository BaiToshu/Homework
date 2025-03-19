# ---------------------------------------------------------------------------- #
#                             Задачи върху списъци                             #
# ---------------------------------------------------------------------------- #

# --------------------------------- Задача 1. -------------------------------- #
# Напишете програма, която чете цели числа въведени от потребителя и ги
# съхранява в списък. Програма трябва да продължи да чете стойности, докато
# потребителят не въведе 0. След това тя трябва да покаже всички стойности, въведени от
# потребителя (с изключение на 0), подредени от най-малката до най-голямата стойност.
# Пример:
#     вход: 2,3,1,6,5,4,2,0
#     изход:1,2,2,3,4,5,6,





# numbers=[]
# num=1

# while num!=0:
#     num=input("Type a number:")
#     if int(num) == 0:
#         break
#     if int(num)!=0:
#         numbers.append(num)
    
# for y in range(0,len(numbers),1):
#     for x in range(0,len(numbers)-1,1):
#         if numbers[x]>numbers[x+1]:
#             flag=numbers[x]
#             numbers[x]=numbers[x+1]
#             numbers[x+1]=flag

# print(numbers)





# --------------------------------- Задача 2. -------------------------------- #
# Да се създаде програма, която чете думи като вход от клавиатурата, докато
# потребителят не въведе празен ред. След като потребителят въведе празен ред,
# програмата трябва да изведе всяка дума, въведена от потребителя точно веднъж.
# Думите трябва да се показват в същия ред, в който са били въведени.
# Пример:
#   вход: first; second; first; third; second
#   изход:first; second; third




# words=[]
# word="start"

# while word !="":
#     does_exist=False
#     word=input("Type a word:")
#     if word != "":
#         for x in range(0,len(words)-1,1):
#             if words[x] == word:
#                 does_exist=True
#     if does_exist == False and word!="":
#         words.append(word)

# print(words)






# --------------------------------- Задача 3. -------------------------------- #
# Да се създаде програма, която да чете цели числа въведени от потребителя,
# докато не бъде въведен празен ред. След като всичките числа са прочетени, програмата
# трябва да показва всички отрицателни числа, последвани от нули, последвани от всички
# положителни числа. Във всяка група номерата трябва да се показват в същия ред, в
# който са въведени от потребителя.
# Пример:
#   вход:   3, -4, 1, 0, -1, 0, -2
#   изход: -4, -1, -2, 0, 0, 3, 1



# negative_numbers=[]
# positive_numbers=[]
# zeros=[]
# numbers=[]
# num=" "

# while num !="":
#     num=input("Enter a number:")
#     if num=="":
#         break
#     if int(num)<0:
#         negative_numbers.append(num)
#     if int(num)>0:
#         positive_numbers.append(num)
#     if int(num)==0:
#         zeros.append(num)

# print(negative_numbers+zeros+positive_numbers)





# --------------------------------- Задача 4. -------------------------------- #
# Напишете програма на Python, която намира най-дългата последователност от
# еднакви елементи в списък. Ако има няколко такива редици с еднаква дължина,
# върнете първата срещната.
# Пример:
#     дадено: numbers=[2, 1, 1, 2, 3, 3, 2, 2, 2, 1],       изход:  [2, 2, 2]
#     дадено: numbers=[4, 4, 2, 2, 2, 3, 3, 1, 4, 4, 4],    изход:  [2, 2, 2]




# def longest_sequence(numbers):
#     if not numbers:
#         return []

#     max_length = 1
#     current_length = 1
#     max_element = numbers[0]
#     current_element = numbers[0]

#     for i in range(1, len(numbers)):
#         if numbers[i] == numbers[i - 1]:
#             current_length += 1
#         else:
#             if current_length > max_length:
#                 max_length = current_length
#                 max_element = current_element
#             current_length = 1
#             current_element = numbers[i]

#     if current_length > max_length:
#         max_length = current_length
#         max_element = current_element

#     return [max_element] * max_length


# numbers1 = [2, 1, 1, 2, 3, 3, 2, 2, 2, 1]
# numbers2 = [4, 4, 2, 2, 2, 3, 3, 1, 4, 4, 4]

# print(longest_sequence(numbers1))
# print(longest_sequence(numbers2))






# --------------------------------- Задача 5. -------------------------------- #
# Напишете програма, която създава следната квадратна матрица m(n*n), по
# зададен от потребителя размер (n).
# Пример:
#     вход: n=3
#     изход:
#         [1, 4, 7]
#         [2, 5, 8]
#         [3, 6, 9]

#     вход: n=4
#     изход:
#         [1, 5, 9, 13]
#         [2, 6, 10, 14]
#         [3, 7, 11, 15]
#         [4, 8, 12, 16]






# def create_matrix(n):
#     matrix = [[0 for _ in range(n)] for _ in range(n)]
    
#     for i in range(n):
#         for j in range(n):
#             matrix[j][i] = i * n + j + 1
    
#     return matrix

# n = int(input("Въведете размера на матрицата (n): "))

# result_matrix = create_matrix(n)

# for row in result_matrix:
#     print(row)







# --------------------------------- Задача 6. -------------------------------- #
# Напишете програма, която създава следната квадратна матрица (n*n), по
# зададен от потребителя размер (n).
# Пример:
#     вход: n=3
#     изход:
#         [1, 6, 7]
#         [2, 5, 8]
#         [3, 4, 9]

#     вход: n=4
#     изход:
#         [1, 8, 9, 16]
#         [2, 7, 10, 15]
#         [3, 6, 11, 14]
#         [4, 5, 12, 13]




# def create_matrix(n):
#     matrix = [[0 for _ in range(n)] for _ in range(n)]
    
#     for i in range(n):
#         for j in range(n):
#             if i%2!=0 and i!=0:
#                 matrix[j][i] = i * n + n -j
#             if i%2==0 or i==0:
#                 matrix[j][i] = i * n + j + 1
    
#     return matrix

# n = int(input("Въведете размера на матрицата (n): "))

# result_matrix = create_matrix(n)

# for row in result_matrix:
#     print(row)