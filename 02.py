
def calculate_average(nums):
    total = 0
    # liste maxsimum indexi kadar döngüyü çalıştırır
    for i in range(0,len(nums)):
        # elemanı toplam değişkenin üzerine ekler
        total += nums[i]
    average = total/len(nums)
    # round virgülden sonra ilk iki basamağı alır
    return round(average,2)

while True:
    print("oralamasini hesaplamak istediginiz 3 sayiyi giriniz, çikmak için q tuşlayiniz")

    num1 = input("birinci sayi: ")
    # kullanıcı çıkmak için q tuşlarsa, döngü kırılır
    if num1.lower() == 'q':
        break
    num2 = input("ikinci sayi: ")
    if num2.lower() == 'q':
        break
    num3 = input("ucuncu sayi: ")
    if num3.lower() == 'q':
        break
    else:
        try: 
            num_list = [float(num1),float(num2),float(num3)]
            print(f"{num1},{num2},{num3} sayıların ortalaması: {calculate_average(num_list)}")

        except ValueError:
            # Eğer kullanıcı sayı yerine geçersiz bir karakter (harf, sembol vb.) girerse hata yakalanır
            print("yanlis değer girdiniz, bir sayi giriniz")