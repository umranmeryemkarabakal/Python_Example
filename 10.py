from math import sqrt

def calculate(operation, *numbers):
    try:
        """
        yapılması istenilen işlemi tespit etmek için if, elif string kontrollerini yapar
        eğer yanlış işlem adı girilirse else çalışır kullanıcıya hata mesajı döndürür
        if kontrolllerinin altında aritmetik operasyonları kullanarak işlem sonuçlarını döndürür
        ekstra 0'a bölünme mesajını kullanıcıya döndürür
        """

        numbers = numbers[0]
        # girilen numaraları float türe çevirir
        numbers = [float(num) for num in numbers]

        if operation == "topla":
            return sum(numbers)
        
        elif operation == "çıkar":
            return numbers[0] - numbers[1]
        
        elif operation == "çarp":
            result = 1
            for num in numbers:
                result *= num
            return result
        
        elif operation == "böl":
            if numbers[1] == 0:
                return "Hata: Sıfıra bölme işlemi yapılamaz."
            return numbers[0] / numbers[1]
        
        elif operation == "üs":
            return numbers[0] ** numbers[1]
        
        elif operation == "karekök":
            if numbers[0] < 0:
                return "Hata: Negatif sayının karekökü alınamaz."
            return sqrt(numbers[0])
        
        elif operation == "mod":
            return numbers[0] % numbers[1]
        
        else:
            return "Hata: Geçersiz işlem."
        
    except (ValueError, IndexError):
        return "Hata: Geçersiz sayı veya eksik parametre."

# kullanıcı çıkış komutunu girene kadar döngü çalışır
while True:
    input_text = input("İşlem girin (topla,çıkar,çarp,böl,üs,karekök,mod)(çıkış için 'çıkış' yazın): ")
    input_list = input_text.split()

    # çıkışi
    if input_list[0] == "çıkış":
        print("Program sonlandı.")
        break

    # en az girdi karekök işlemi için 1 numara ve operasyon komutu girilmelidir
    if len(input_list) >= 2 : 
        operation = input_list[0]
        nums = input_list[1:]
        result = calculate(operation,nums)
    else:
        result = "Hatalı giriş, lütfen tekrar deneyin."

    # Sonucun ekrana yazdırılması
    print(f"Sonuç: {result}")
