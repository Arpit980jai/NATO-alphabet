import pandas

data=pandas.read_csv("nato_phonetic_alphabet.csv")
dict={row.letter:row.code for (letter,row) in data.iterrows()}
print(dict)
word=input("What is your Name ? ").upper()
list=[dict[letter] for letter in word]
print(list)