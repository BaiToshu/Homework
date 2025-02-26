text = """apple and banana one apple one banana
          a red apple and a green apple"""

words=text.split()
words_unique=list(set(words))

for word in range(0,len(words_unique),1):
    print(f"{words_unique[word]} - {words.count(words_unique[word])}")