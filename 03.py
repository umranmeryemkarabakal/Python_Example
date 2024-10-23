
import re

print("metin içinde aranacak kelimeyi giriniz")
text = input("metin: ")
word = input("aranan kelime: ")

def search_word(text,word):
    text = re.sub("'",'',text)
    # türkçe karakterler hariç noktalama işaretlerini boşlukla değiştirir
    text = re.sub(r"[^a-zA-Z0-9çÇğĞıİöÖşŞüÜ\s']", '', text) 
    # metindeki tüm karakterleri küçültür
    text = text.lower()
    word = word.lower()
    # metindeki kelimeleri listeler
    text_list = text.split()
    #print(text_list)
    
    # aranan kelimenin metin içinde kaç yerde görüldüğünü verir
    # metindeki her kelime için w değişkeni atanır
    # if yapısı w kelimesin listenin her elemanında geçtiğini kontrol eder
    count_word = 0
    for w in text_list:
        if word in w:
            count_word +=1 
    
    return count_word

print(f"'{word}' kelimesi metinde {search_word(text,word)} defa geçmektedir")

"""
Lorem Ipsu'm i's si'mply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
