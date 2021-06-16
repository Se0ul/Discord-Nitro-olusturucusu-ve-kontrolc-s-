LICNECE = """
Telif hakkı © 2021 Drillenissen#4268

İşbu belgeyle, bu yazılımın ve ilgili belge dosyalarının ("Yazılım") bir kopyasını edinen herhangi bir kişiye, kullanım, kopyalama, değiştirme, birleştirme hakları dahilinde ancak bunlarla sınırlı olmamak üzere, herhangi bir kısıtlama olmaksızın Yazılımla ilgilenme izni verilir. Yazılımın kopyalarını yayınlamak, dağıtmak, alt lisansını vermek ve/veya satmak ve Yazılımın sağlandığı kişilerin aşağıdaki koşullara tabi olarak bunu yapmasına izin vermek:

Yukarıdaki telif hakkı bildirimi ve bu izin bildirimi, Yazılımın tüm kopyalarına veya önemli bölümlerine dahil edilecektir.

YAZILIM, SATILABİLİRLİK, BELİRLİ BİR AMACA UYGUNLUK VE İHLAL ETMEME GARANTİLERİ DAHİLİNDE ANCAK BUNLARLA SINIRLI OLMAMAK ÜZERE, AÇIK VEYA ZIMNİ HERHANGİ BİR GARANTİ OLMAKSIZIN “OLDUĞU GİBİ” SAĞLANIR. YAZARLAR VE TELİF HAKKI SAHİPLERİ HİÇBİR DURUMDA HERHANGİ BİR DAVA, HAKSIZ FİİL YA DA  SÖZLEŞME V.B, BİR EYLEM, ZARAR VEYA DİĞER SORUMLULUKLARDAN , YAZILIMI KULLANAN SORUMLU OLACAKTIR.

"""

import time
import os

print(LICNECE)

time.sleep(7)
os.system('cls' if os.name == 'nt' else 'clear')

import random
import string
import ctypes

try: # Gereksinimlerin yüklenip yüklenmediğini kontrol eder
    from discord_webhook import DiscordWebhook # Discord_webhook'u içe aktarmayı dener
except ImportError: # Eğer kurulamazsa

    input(f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nPress enter to exit") # Kullanıcıya henüz yüklenmediğini ve nasıl kurulacağını söyleyin
    exit() # Programdan çıkış yap
try: # Hatayı yakalamak için tekrar ifadesini ayarlayın
    import requests # İstekleri içe aktarmayı deneyin
except ImportError: # Yüklü Değil ise
    input(f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")# Kullanıcıya henüz yüklenmediğini ve nasıl kurulacağını söyleyin
    exit() # Programdan çıkış yap


class NitroGen: # Nitrogen sınıfını başlat
    def __init__(self): # Başlatma işlevi
        self.fileName = "Nitro Codes.txt" # Kodların depolandığı dosya adıını ayarlayınız

    def main(self): # Ana işlev , en önemli kodu içerir
        os.system('cls' if os.name == 'nt' else 'clear') # Ekranı temizler
        if os.name == "nt": # Sisteminiz windows ise
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Nitro Üretici ve Kontrolcüsü - Yapımcı: Drillenissen#4268 Çeviri: Seoul#1126") # Değiştir
        else: # Ya da unix ise 
            print(f'\33]0;Nitro Üretici ve Kontrolcüsü - Yapımcı: Drillenissen#4268 Çeviri: Seoul#1126\a', end='', flush=True) # Komut isteminin başlığını güncelle


        print(""" █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗██╗  ██╗
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██║╚██╗██╔╝
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║██║ ╚███╔╝
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██║ ██╔██╗
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║██║██╔╝ ██╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
                                                        """) # Başlık kartını yaz
        time.sleep(3) # Bir kaç saniye bekle
        self.slowType("Yapımcı: Drillenissen#4268 && Benz#4947 Çeviri: Seoul#1126", .02) # Print who developed the code
        time.sleep(1) # Birazcık daha bekle
        self.slowType("\nKaç Kod Oluşturulacağını ve kontrol edileceğini girin: ", .02, newLine = False) # İlk soruyu yazar

        num = int(input('')) # Kullanıcıdan kod miktarını isteyin

        # Webhook url'sini yapıştırın kullanmak istemiyorsanız boş bırakın.
        self.slowType("\nWebhook url'sini yapıştırın kullanmak istemiyorsanız boş bırakın: ", .02, newLine = False)
        url = input('') # Cevabı al
        webhook = url if url != "" else None # URL boşsa, bunun yerine Yok yapın

        # print() # Kodların görülmesi için yeni bir satır yazdırın

        valid = [] # Geçerli kodlar
        invalid = 0 # Geçersiz kodlar

        for i in range(num): # Kontrol edilecek kontrol üzerine döngü yapınız
            try: # Oluşabilecek hataları yakalayın
                code = "".join(random.choices( # Hediye kodunu oluştur
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                url = f"https://discord.gift/{code}" # URL oluştur

                result = self.quickChecker(url, webhook) # Kodu kontrol et

                if result: # Kod geçerli olsaydı
                    valid.append(url) # Kod geçerli ise geçerli listesine ekle
                else: # Fakat geçerli değil ise geçersiz listesine ekle
                    invalid += 1 # Geçersiz sayacını 1 arttır
            except Exception as e: # İstek başarsız olursa 
                print(f" Error | {url} ") # Kullanıcıya hata oluştuğunu göster

            if os.name == "nt": # Sistem Windows ise
                ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Üretici ve Kontrolcüsü - {len(valid)} Geçerli | {invalid}  Geçersiz - Made by Drillenissen#4268 Çeviri:Seoul#1126") # Başlığı değiştir
                print("")
            else: # Sistem Unix ise
                print(f'\33]0;Nitro Üretici ve Kontrolcüsü - {len(valid)} Geçerli | {invalid} Geçersiz - Made by Drillenissen#4268 Çeviri:Seoul#1126\a', end='', flush=True) # Başlığı değiştir

        print(f"""
Sonuçlar:
 Geçerli: {len(valid)}
 Geçersiz: {invalid}
 Geçerli kodlar: {', '.join(valid )}""") # Geçerli çıkar ise Webhook sayesinde cevap verin.

        input("\nBitti! 5 kere enter tıklayarak çıkış yapabilirsiniz") # Kullanıcıya programın bittiğini söyleyin 
        [input(i) for i in range(4,0,-1)] # 5 kere enter tuşuna basınız


    def slowType(self, text, speed, newLine = True): # Metni Daha hızlı yazmak için.
        for i in text: # Mesajın üzerinden geç
            print(i, end = "", flush = True) # Bir karakteri yazdırın, python'u karakteri yazdırmaya zorlamak için flush kullanılır
            time.sleep(speed) # Bir sonrakinden önce biraz uyu
        if newLine: # newLine bağımsız değişkeninin True olarak ayarlanıp ayarlanmadığını kontrol edin
            print() # Normal bir yazdırma ifadesi gibi davranmasını sağlamak için son bir yeni satır yazdırın

    def generator(self, amount): # Nitro kodları oluşturmak ve ayrı bir dosyada saklamak için kullanılan işlev
        with open(self.fileName, "w", encoding="utf-8") as file: # Dosyayı yazma modunda yükleyin
            print("Wait, Generating for you") # Kullanıcının, kodları oluşturduğunu bilmesini sağlayın

            start = time.time() # Başlatma zamanını not edin

            for i in range(amount): # Oluşturulacak kod miktarını döngüye alın
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                )) # kod kimliğini oluştur

                file.write(f"https://discord.gift/{code}\n") # Kodu yaz

            # Kullanıcıya üretmenin bittiğini ve ne kadar sürdüğünü şöyle
            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n") #

    def fileChecker(self, notify = None): # Bir dosyadan nitro kodlarını kontrol etmek için kullanılan işlev
        valid = [] # Geçerli kodların listesi
        invalid = 0 # Geçersiz kodların listesi
        with open(self.fileName, "r", encoding="utf-8") as file: # Nitro kodlarını içeren dosyayı açın
            for line in file.readlines(): # Dosyadaki her satırın üzerinde döngü yapın
                nitro = line.strip("\n") # Nitro kodunun sonundaki yeni satırı kaldırın

                # Daha sonra kullanmak üzere istek url'sini oluşturun
                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) # URL'den yanıtı alın

                if response.status_code == 200: # Eğer cevap gelirse
                    print(f" Valid | {nitro} ") # Kullanıcıya kodun geçerli olduğunu bildir
                    valid.append(nitro) # Nitro kodunu geçerli kodların listesine ekleyin

                    if notify is not None: # ve Webhook eklenmiş ise
                        DiscordWebhook( # Kullanıcıya geçerli bir nitro kodu olduğunu bildiren bir discord mesajı gönderin
                            url = notify,
                            content = f"Gecerli Kod bulundu @everyone \n{nitro}"
                        ).execute()
                    else: # Bir discord webhook kurulumu yapılmadıysa, kodu durdurun
                        break # Geçerli Bir kod bulur ise döngüyü durdur

                else: # Yanıt yoksayılırsa veya geçersiz ise (örneğin, 404 veya 405 )
                    print(f" Invalid | {nitro} ") # Kullanıcıya bir kodu test ettiğini ve geçersiz olduğunu göster
                    invalid += 1 # Geçersiz sayacını 1 arttır

        return {"valid" : valid, "invalid" : invalid} # Sonuçların bir raporunu döndürür

    def quickChecker(self, nitro, notify = None): # Bir seferde tek bir kodu kontrol etmek için kullanılır
        # Generate the request url
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) # Discord'dan bir cevap alır
        
        if response.status_code == 200: # Eğer cevap geçerse
            print(f" Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") # Kullanıcıya kodun geçerli olduğunu bildirin
            with open("Nitro Codes.txt", "w") as file: # Yazılacak dosyayı aç
                file.write(nitro) # Nitro kodunu dosyaya yazar , otomatik olarak yeni bir satır ekleyecek

            if notify is not None: # Webhook ekli ise
                DiscordWebhook( # Kullanıcının geçerli bir nitro kodu olduğunu bilmesini sağlamak için mesajı discord'a gönderin
                    url = notify,
                    content = f"Gecerli Kod bulundu @everyone \n{nitro}"
                ).execute()

            return True # Kodun bulunduğunu ana işlevi söyle

        else: # Yanıt yoksayıldıysa veya geçersizse (404 veya 405 gibi)
            print(f" Invalid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") # Kullanıcıya bir kodu test ettiğini ve geçersiz olduğunu göster
            return False # Ana fonksiyona kod bulunamadığını söyleyin

if __name__ == '__main__':
    Gen = NitroGen() # Nitro üreteci nesnesini oluşturun
    Gen.main() # Ana kodu çalıştırın
