import pandas as pd
import re

print("metin dosyasinin yolunu giriniz")
path = input("path: ")

# her kelimenin ne kadar geçtiğini sayar
def count_word(w_list,w_dict):
    for x in w_list:
        w_dict[x] += 1						
    return w_dict

# x[1] sözlüğün 2. öğesini alır
# reverse sıralamnın azalan sırada olmasını sağlar
def sort_word(w_dict):
    return dict(sorted(w_dict.items(), key=lambda x: x[1], reverse=True))

def read_file(path):
    try:
        with open(path,"r",encoding="utf-8") as fileObject: #mod yazmaszak otomatik read modunda açar

            for lineText in fileObject: #for lineText in fileObject.readlines()
                #print(lineText, end="")
                lineText = re.sub(r'[^a-zA-Z0-9çÇğĞıİöÖşŞüÜ\s]', '', lineText)
                word_list = lineText.lower().split()
            return word_list
        
    except FileNotFoundError:
        print("Belirtilen dosya bulunamadi")
        return []
    
def write_file(sorted_words):
    with open("cikti.txt", "w", encoding="utf-8") as file:
        for (word, count) in sorted_words.items():
            file.write(f"{word}: {count}\n")


word_list = read_file(path)
word_dict = {y:0 for y in word_list}

new_word_dict = count_word(word_list,word_dict)
sorted_word_dict = sort_word(new_word_dict)
print(sorted_word_dict)
write_file(sorted_word_dict)