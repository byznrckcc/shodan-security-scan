import shodan
import time

class ShodanScanner:
    """
    Shodan.io API kullanarak cihaz taraması yapan sınıf.
    """

    def __init__(self, api_key):
        self.api = shodan.Shodan(api_key)

    def search_devices(self, query="city:Istanbul", limit=5):
        """
        Verilen sorguya göre cihazları arar ve temel bilgileri döner.
        """
        results = self.api.search(query)
        output = []
        output.append(f"Toplam cihaz sayısı: {results['total']}\n")
        for result in results['matches'][:limit]:
            device_info = (
                f"IP: {result['ip_str']}\n"
                f"Port: {result['port']}\n"
                f"Servis: {result.get('product', 'Bilinmiyor')}\n"
                f"Organizasyon: {result.get('org', 'Yok')}\n"
                "------------------------------"
            )
            output.append(device_info)
        return output

def main():
    output_lines = []
    def print_and_log(line):
        print(line)
        output_lines.append(line)

    print_and_log("=== Shodan.io Tarayıcı Başladı ===")

    # 🔑  API Key'in burada
    API_KEY = "uM2qbeAk4WhV7JHDlDf0k5BEl65EQCkk"
    scanner = ShodanScanner(API_KEY)

    start_time = time.time()
    try:
        results = scanner.search_devices()
        for line in results:
            print_and_log(line)
    except shodan.APIError as e:
        print_and_log(f"❌ Shodan API Hatası: {e}")

    end_time = time.time()
    print_and_log(f"⏱ Toplam süre: {end_time - start_time:.2f} saniye")

    # Logları dosyaya kaydet
    with open("shodan_scan_results.txt", "w", encoding="utf-8") as f:
        for line in output_lines:
            f.write(line + "\n")

if __name__ == "__main__":
    main()

