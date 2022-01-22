import re

import nltk.corpus
import numpy as np

text = nltk.corpus.gutenberg.raw("austen-sense.txt")

corrupted = ""

p_edit = 0.04

for char in text:
    if re.fullmatch("[a-zA-Z]", char) is not None and np.random.rand() < p_edit:
        edit = np.random.randint(3)
        if edit == 0:
            # insert
            if 97 <= ord(char) < 123:
                corrupted += chr(97 + np.random.randint(26))
            elif 65 <= ord(char) < 91:
                corrupted += chr(65 + np.random.randint(26))
            corrupted += char
        elif edit == 1:
            # delete
            pass
        else:
            # substitute
            if 97 <= ord(char) < 123:
                corrupted += chr(97 + np.random.randint(26))
            elif 65 <= ord(char) < 91:
                corrupted += chr(65 + np.random.randint(26))
    else:
        corrupted += char

with open("austen-sense-corrupted.txt", "w") as stream:
    stream.write(corrupted)

string = corrupted[:1000].split()

pattern = r"\w+[-]?\w+|\w+"


# c = re.findall(pattern, corrupted)

with open('dict.txt') as d:
    dict_list=[]
    for line in d:
        dict_list.append(line.strip())

def min_dis(target, source):
    target = '@' + target
    source = '@' + source
    lst_target = [k for k in target]
    lst_source = [k for k in source]
    arr = np.zeros((len(source), len(target)))
    arr[0] = [i for i in range(len(lst_target))]
    arr[:,0] = [j for j in range(len(lst_source))]
    
    if target[1] != source[1]:
        arr[1,1] = 1
    for col in range(1, len(target)):
        for row in range(1, len(source)):


            if target[col] != source[row]:
                arr[row, col] = min(arr[row-1,col],arr[row,col -1],arr[row-1,col-1]) + 1 

            else:
                arr[row, col] = arr[row-1, col-1]

    return int(arr[-1,-1])


for word in string:
    list_of_dist = []
    list_of_words = []
    if re.findall(pattern, word)[0] not in dict_list:
        for i in dict_list:
            dist = min_dis(i, re.findall(pattern, word)[0])
            list_of_words.append(i)
            list_of_dist.append(dist)
        index = list_of_dist.index(min(list_of_dist))
        replace_word = list_of_words[index]
        if word[-1] in [",", ".", "?", "!", ":", ";", ")"]:
            string[string.index(word)] = replace_word + word[-1]
        elif word[0] in ["("]:
            string[string.index(word)] = word[-1] + replace_word
        else:
            string[string.index(word)] = replace_word

final_str = ""
for j in string:
    final_str = final_str + j + " "
print(final_str)





