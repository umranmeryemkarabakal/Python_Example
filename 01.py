
def calculate_exact_divisor(num):
    num_list = []
    # 1'den girilen sayıya kadar döngüyü çalıştırır
    for i in range(1,num+1):
        # sayının i'ye tam bölündüğünü kontrol eder 
        if num % i == 0 :
            # eğer sayıya tam bölünüyorsa listeye ekler
            num_list.append(i)
    return num_list

while True:
    print("tam bölenleri hesaplamak istediğiniz iki sayiyi giriniz, çikmak için q'u tuslayiniz")
    
    num1 = input("birinci sayi: ")
    
    # kullanıcı çıkmak için q tuşlarsa, döngü kırılır
    if num1.lower() == 'q':
        break
    
    num2 = input("ikinci sayi: ")
    
    if num2.lower() == 'q':
        break
    
    else:
        
        try:
            # sayıların tam bölenleri hesapla
            divisor_list1 = calculate_exact_divisor(int(num1))
            divisor_list2 = calculate_exact_divisor(int(num2))

            common_divisor = list(set(divisor_list1) & set(divisor_list2))

            print(f"{num1} sayisinin tam bolenleri: {divisor_list1}")
            print(f"{num2} sayisinin tam bolenleri: {divisor_list2}")
            print(f"{num1},{num2} sayilarinin ortak tam bolenleri: {common_divisor}")

        except ValueError:
            # Eğer kullanıcı sayı yerine geçersiz bir karakter (harf, sembol vb.) girerse hata yakalanır
            print("yanlis değer girdiniz, tam bir sayi giriniz")
