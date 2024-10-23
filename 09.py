
"""
merge sort algoritması diziyi küçük parçalara ayırıp 
önce her bir parçayı ayırıp recursive yapıdaki fonksyionu tekrar çağırıp sıralar
sonrasında bu sıralı parçaları birleştirip tüm diziyi sıralar
"""

def merge_sort(arr):
    if len(arr) > 1:
        # dizinin ortası
        mid = len(arr) // 2  
        #sol yarısı
        left_half = arr[:mid]  
        # sağ yarısı
        right_half = arr[mid:]  

        merge_sort(left_half)  
        merge_sort(right_half)

        i = j = k = 0

        # alt dizileri birleştirirken karşılaştır
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # sol yarıda kalan elemanları ekler
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # sağ yarıda kalan elemanları ekle
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

print("merge sort algoritmasiyla siralamak istediginiz diziyi giriniz")
array_str = input("dizi: ")
# string olarak girilen dizi virgül ile ayrılıp float tipine çevirip listeye atar
array_list = [float(x) for x in array_str.split(",")]
# merge sort fonksiyonu çalışrır
sorted_array_list = merge_sort(array_list)
print(f"merge sort algoritmasiyla siralanmis dizi:{sorted_array_list}")

print("dizide aramak istediğiniz sayiyi giriniz")
num = int(input("sayi: "))

# liste içinde ara
count_n = sorted_array_list.count(num)

if count_n == 0:
    print(f"{num} degeri dizide bulunmamaktadır")
else:
    print(f"{num} degeri dizide bulunmaktadir")