import re
import csv
import time

freq_list = [0 for i in range(1000)]

with open('find_words.txt',encoding='utf-8') as f:
    words = f.read().split('\n')
with open('t8.shakespeare.txt') as f:
    text = f.read().split('\n')
with open('french_dictionary.csv', mode='r',encoding='utf-8') as dic:
    reader = csv.reader(dic)
    dictionary = {rows[0]:rows[1] for rows in reader}

#convert to only words
def only_words(x):
    reg = re.sub(r'[^a-zA-Z]', '', x)
    return reg
only_text = lambda text:re.sub(r'[^a-zA-Z]', '', text)

def capsConversion(word,rep_word):
    if word[0].isupper() and word[1].islower(): 
        rep_word=rep_word.capitalize()
    if word.isupper(): 
        rep_word =rep_word.upper()
    return rep_word      

def convertWords(word):
    plural = False
    small_word = word.lower()
    copi = only_text(small_word) if not (word.isalpha() and len(small_word) != 0) else small_word
    if not copi in words:
        if copi[:-1] in words:
            copi = copi[:-1]
            pos = word.rfind("s")
            lst = list(word)
            del(lst[pos])
            del(lst[pos-1])
            word = ''.join(lst)
            plural = True 
    if copi in words:
        freq_list[(words.index(copi))]  = freq_list[(words.index(copi))] + 1
        rep_word = dictionary[copi]+("s") if plural else dictionary[copi]
        #print(len(word),word,len(copi),copi)
        if len(word) != len(copi) or plural:
            pos = small_word.index(copi[0])
            rep_word = capsConversion(word,rep_word)
            #print(rep_word)
            word = word.replace(word[pos:len(copi)],rep_word)
        else:
            word = capsConversion(word,rep_word)
    return word


def convert(line):
    line[:] = map(lambda x:convertWords(x),line)
    return ' '.join(line)

def my_func():
    text[:] = map(lambda x:convert(x.split()),text)
if __name__ == '__main__':
    my_func()






# write output file
with open("outfile.txt",encoding='utf-8', mode="w") as outfile:
    outfile.write("\n".join(text))
#print(freq_list)

#write the frequency

with open("french_dictionary.csv", "r") as read_obj,\
    open('frequency.csv', 'w',newline='') as write_obj:
    csv_reader = csv.reader(read_obj)
    csv_writer = csv.writer(write_obj)
    for i,row in enumerate(csv_reader):
        row.append(freq_list[i])
        csv_writer.writerow(row)

