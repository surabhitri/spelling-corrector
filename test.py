import re 
import numpy as np

corrupted = """Between Barton and Delaford, there was that constant
communication jhich strong family affection wold
naturally dictate;--and among the umerits and the happiness
of Elinor and Marianne, let it not be rfanke a the leat
considoerable, that though sisters, and living almost within
sight of each other, they could slive wthout disagreement
behtween themselves, or producing coolness betwenen their hunbands."""

string = corrupted.split()

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

print(string)



        
        
