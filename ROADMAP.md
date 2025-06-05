# Shodan.io DevHunter Yol Haritası

Bu yol haritası, Shodan.io tabanlı gelişmiş bir yazılımcı dijital ayak izi keşif platformu olan Shodan.io DevHunter'ın planlanan geliştirme aşamalarını ve kilometre taşlarını özetlemektedir. Detaylı görevler, ilerleme güncellemeleri, riskler ve topluluk katkı fırsatlarını içerir.

---

## Geliştirme Aşamaları

### **1. Aşama: Temel Altyapı (Tahmini Tamamlanma - 2025 3. Çeyrek)**

* **Amaç:** Temel Shodan dork'lama, veri işleme ve çıktı formatlama yeteneklerini oluşturmak.
* **Kilometre Taşları:**
    * **Hedefli Shodan Sorguları:** Hedefli Shodan sorguları oluşturmak ve çalıştırmak için temel fonksiyonlar geliştirildi.
    * **Veri İşleme Modülü:** Shodan'dan alınan ham veriyi temizlemek ve yapılandırmak için veri işleme modülü oluşturuldu.
    * **Çıktı Formatlama:** Sonuçları okunabilir formatlarda (örn. JSON, CSV) sunmak için çıktı formatlama işlevleri uygulandı.
    * **Temel CLI:** Temel komut satırı arayüzü (CLI) oluşturuldu.
* **Karşılaşılan Riskler:** Shodan API sınırları nedeniyle sorgu hızı kısıtlamaları; daha verimli sorgu stratejileriyle çözüldü.

### **2. Aşama: YZ/ML Entegrasyonu (Tahmini Tamamlanma - 2025 4. Çeyrek)**

* **Amaç:** Geliştirici profillerini otomatik olarak analiz etmek ve güvenlik açıklarını önceliklendirmek için YZ/ML modellerini entegre etmek.
* **Kilometre Taşları:**
    * **Güvenlik Açığı Tespiti (ML):** Açıkta kalan Git depolarını, veritabanlarını ve diğer hassas bilgileri tespit etmek için makine öğrenimi modelleri eğitildi.
    * **Risk Sınıflandırma:** Bulunan güvenlik açıklarını risk seviyesine göre sınıflandırmak için bir puanlama sistemi uygulandı.
    * **Veri Görselleştirme:** Veri analizini görselleştirmek için temel grafikler ve panolar oluşturuldu.
* **Riskler ve Zorluklar:** YZ/ML modellerinin doğruluğunu ve performansını optimize etmek; daha fazla veri ve deney gerektiriyor.

### **3. Aşama: Genişletilmiş OSINT Entegrasyonu (Planlanan - 2026 1. Çeyrek)**

* **Amaç:** Geliştirici dijital ayak izlerini zenginleştirmek için diğer OSINT kaynaklarını (örn., GitHub, LinkedIn) entegre etmek.
* **Kilometre Taşları:**
    * **GitHub & LinkedIn Bağlayıcıları:** GitHub ve LinkedIn profillerinden veri çekmek ve Shodan sonuçlarıyla ilişkilendirmek için bağlayıcılar geliştirildi.
    * **Ek OSINT Kaynakları:** Ek OSINT kaynakları için (örn., Stack Overflow, Twitter) destek planlandı.
    * **Kapsamlı Profil Oluşturma:** Geliştirici becerilerini, projelerini ve iletişim bilgilerini özetleyen kapsamlı profiller oluşturmak için veri birleştirme algoritmaları uygulandı.
* **Öncelikler:** GitHub ve LinkedIn entegrasyonlarını tamamlamak ve diğer OSINT kaynakları için bir yol haritası oluşturmak.

### **4. Aşama: Topluluk ve Ölçeklenebilirlik (Planlanan - 2026 2. Çeyrek)**

* **Amaç:** Projeyi daha geniş bir topluluğa açmak ve büyük ölçekli dağıtımlar için mimariyi optimize etmek.
* **Kilometre Taşları:**
    * **Modüler Mimari:** Yeni Shodan filtreleri, OSINT kaynakları ve analiz modelleri eklemek için modüler bir mimari tasarlanacak.
    * **Dokümantasyon:** Topluluk katkılarını kolaylaştırmak için kapsamlı dokümantasyon ve örnekler oluşturulacak.
    * **Bulut Dağıtımı:** Büyük ağları izlemek için bulut dağıtım seçenekleri (örn., AWS, Google Cloud) araştırılacak.
    * **API Desteği:** Üçüncü taraf araçlarla (örn., SIEM sistemleri) entegrasyon için API desteği planlanacak.
* **Riskler ve Zorluklar:** Modüler mimarinin esnekliğini ve performansını korumak; topluluk katılımını teşvik etmek.

---

## Ana Kilometre Taşları

* **2025 3. Çeyrek:** Temel Shodan dork'lama ve veri işleme yetenekleri tamamlandı.
* **2025 4. Çeyrek:** YZ/ML modelleri entegre edildi ve temel güvenlik açığı analizi uygulandı.
* **2026 1. Çeyrek:** GitHub ve LinkedIn entegrasyonları tamamlandı.
* **2026 2. Çeyrek:** Ölçeklenebilir mimari tasarlandı ve topluluk katılımı için hazırlıklar yapıldı.

---

## Topluluk Katkıları

Gelişimi hızlandırmak için topluluk katılımını teşvik ediyoruz. Yardım edebileceğiniz alanlar:

* Yeni Shodan dork'ları ve OSINT kaynakları önerin.
* YZ/ML modellerini geliştirmek için veri kümeleri sağlayın veya algoritmalar geliştirin.
* Projenin farklı platformlarda (Linux, macOS, Windows) test edilmesine yardımcı olun.
* Dokümantasyonu iyileştirin veya yeni özellikler ekleyin.
* Projeyi farklı dillere çevirin.

---

## Notlar

* Zaman çizelgeleri, araştırma ilerlemesi, test sonuçları ve topluluk geri bildirimlerine bağlı olarak değişebilir.
* İlerlemeyi yansıtmak için bu yol haritası düzenli olarak güncellenecektir.
* En son güncellemeler için `ROADMAP.md` dosyasını kontrol edin.
 
