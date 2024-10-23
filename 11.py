class OgrenciOtomasyonSistemi:

    def __init__(self):
        # öğrencileri tutacak olan liste
        self.ogrcler = []
    
    def ogrenci_ekle(self,ogrc):
        # append, öğrenciyi listeye ekler
        self.ogrcler.append(ogrc)
        print(f"{ogrc.numara} numaralı öğrenci eklendi")

    def ogrenci_sil(self,num):
        # numarası girilen öğrenciyi tespit etmek için
        # öğrenci listesinin her elemanına kontrol eder
        for ogrenci in self.ogrcler:
            if ogrenci.numara == num:
                # kayıtlı öğrenciyi listeden siler
                self.ogrcler.remove(ogrenci)
                print(f"{num} numarali öğrenci silindi")
            else:
                print(f"{num} numarali öğrenci bulunamadı")

    def ogrenci_guncelle(self,num, yeni_isim):
        for ogrenci in self.ogrcler:
            if ogrenci.numara == num:
                # öğrenci ismini değiştirir
                ogrenci.isim = yeni_isim
                print(f"{num} numaralı öğrencinin ismi {yeni_isim} olarak güncellendi")
                return
        print(f"{num} numaralı öğrenci bulunamadı")
    
    def ogrenci_bilgileri(self,num):
        for ogrenci in self.ogrcler:
            if ogrenci.numara == num:
                print(f"öğrenci no: {ogrenci.numara}, isim: {ogrenci.isim}, ortalama: {ogrenci.not_ort}")
                return ogrenci
        print(f"{num} numaralı öğrenci bulunamadı")
        return None
    
    def tum_ogrencileri_goster(self):
        # eğer öğrenci listesi boş değilse tüm öğrencilerin bilgilerini ekrana yazdırır
        if len(self.ogrcler) != 0:
            print("sistemdeki öğrenciler:")
            for ogrenci in self.ogrcler:
                print(f"öğrenci no: {ogrenci.numara}, isim: {ogrenci.isim}, ortalama: {ogrenci.not_ort}")
        else:
            print("sistemde kayıtlı öğrenci yoktur")


class Ogrenci:
    def __init__(self,numara,isim,not_ort):
        self.numara = numara
        self.isim = isim
        self.not_ort = not_ort
    

Sistem = OgrenciOtomasyonSistemi()

ogrnc1 = Ogrenci("01","A","3.1")
ogrenc2 = Ogrenci("02","B","3.2")
ogrenc3 = Ogrenci("03","C","3.3")

Sistem.ogrenci_ekle(ogrnc1)
Sistem.ogrenci_ekle(ogrenc2)
Sistem.ogrenci_ekle(ogrenc3)
Sistem.tum_ogrencileri_goster()
Sistem.ogrenci_guncelle("01","D")
Sistem.ogrenci_bilgileri("02")
Sistem.ogrenci_sil("03")
Sistem.tum_ogrencileri_goster()
