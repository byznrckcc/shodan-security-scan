import shodan
import time

def get_ip_details(api_key, ip_address):
    # Shodan API ile IP adresinin detaylarını çeker
    try:
        api = shodan.Shodan(api_key)  # Shodan nesnesini oluştur
        host = api.host(ip_address)   # Belirtilen IP'nin detaylarını al
        
        print(f"IP Adresi: {host['ip_str']}")
        print(f"Organizasyon: {host.get('org', 'Bilinmiyor')}")
        print(f"Ülke: {host.get('country_name', 'Bilinmiyor')}")
        print(f"Şehir: {host.get('city', 'Bilinmiyor')}")
        print(f"Enlem/Boylam: {host.get('latitude', 'Bilinmiyor')}, {host.get('longitude', 'Bilinmiyor')}")
        print("Açık Portlar:")
        for item in host['data']:
            print(f" - Port: {item['port']}, Servis: {item.get('product', 'Bilinmiyor')}")
    except shodan.APIError as e:
        print(f"❌ Shodan API Hatası: {e}")  # Hata durumunda mesaj yazdır

def main():
    # Kullanıcıdan API key'i al (GitHub'da görünmez)
    api_key = input("Lütfen Shodan API key'ini girin: ")
    IP_ADDRESS = "8.8.8.8"  # Test için Google DNS IP'si, değiştirebilirsin
    start_time = time.time()  # Taramanın başlangıç zamanını kaydet
    print(f"=== IP Detayları için Shodan Tarama Başladı (IP: {IP_ADDRESS}) ===")
    get_ip_details(api_key, IP_ADDRESS)
    end_time = time.time()  # Taramanın bitiş zamanını kaydet
    print(f"⏱ Toplam süre: {end_time - start_time:.2f} saniye")

if __name__ == "__main__":
    main()  # Kodu çalıştır
