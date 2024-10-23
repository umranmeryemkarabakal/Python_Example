def calculateFactorial(num):
    # girilen sayıdan 0 değerine kadar geriye kadar gelir
    # eğer girilen sayı 0 ise factoriyelini bir olarak hesaplar
    if num == 0:
        return 1
    else:
        # sayıyı bir azaltıp tekrar fonksiyonu çağırır
        factorial = num * calculateFactorial (num-1)
        return factorial
    
while True:
    print("faktöriyelini hesaplamak istediğiniz tam sayıyı giriniz, çıkmak için 'q' tuşlayınız")
    usr_input = input("tam sayı: ")

    if usr_input.lower() == "q":
        break
    
    try:
        number = int(usr_input)     
        numbers_factorial = calculateFactorial(number)
        print(f"{number} sayısının faktöriyeli: {numbers_factorial}")
    
    except ValueError:
        print("geçersiz değer girdiniz, lütfen integer bir sayı giriniz")
