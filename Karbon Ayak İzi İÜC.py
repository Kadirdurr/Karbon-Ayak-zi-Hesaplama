import matplotlib.pyplot as plt
elektrik_tüketimi = float(input("Evdeki elektrik kullanımınız aylık kaç kWh'dir? "))
araç_kullanımı = float(input("Araç kullanımınızda haftada ortalama kaç kilometre yol alıyorsunuz? "))
uçuş_sayısı = int(input("Yılda kaç kez uçakla seyahat ediyorsunuz? "))
su_tüketimi = float(input("Günlük su tüketiminiz nedir (litre)? "))
organik_tercih_oranı = float(input("Alışverişlerinizde hangi oranda organik veya yerel ürünleri tercih ediyorsunuz (% olarak)? "))
geri_dönüştürme_sıklığı = int(input("Geri dönüşüm kutularını haftada kaç kez dolduruyorsunuz? "))
ısıtma_enerji_kaynağı = float(input("Evdeki ısınma ihtiyacının ne kadarını doğalgaz ile sağlıyorsunuz? (% olarak)? "))
aydınlatma_verimliliği = float(input("Evdeki aydınlatma sistemlerinin kaçta kaçı enerji tasarruflu veya LED lamba içeriyor (% olarak)? "))
cihaz_kullanım_süresi = float(input("Evdeki cihazları ne kadar süreyle açık bırakıyorsunuz (günlük saat olarak)? "))
su_ısıtıcısı_kullanım_süresi = float(input("Evdeki su ısıtıcısını günde kaç saat kullanıyorsunuz? "))
fast_food_tercih_sıklığı = int(input("Haftada kaç kez fast-food veya hazır yemek tüketiyorsunuz? "))
tek_kullanımlık_ürün_sayısı = int(input("Alışveriş yaparken kullan-at ürünleri kaç adet alıyorsunuz haftada? "))
enerji_etiketli_alet_sayısı= int(input("Kaç tane enerji etiketine sahip A+++ ev aleti kullanıyorsunuz? "))
geri_dönüştürme_oranı = float(input("Evdeki çöplerin ne kadarını geri dönüştürüyorsunuz (% olarak)? "))
toplu_ulaşım_kullanım_sıklığı = int(input("Ulaşım için haftada kaç gün toplu taşıma araçlarını kullanıyorsunuz? "))
akıllı_ev_cihaz_sayısı = int(input("Evde kaç tane akıllı termostat veya enerji yönetim cihazı bulunuyor? "))
plastik_poşet_kullanım_limiti = int(input("Alışverişlerinizde plastik poşet kullanımını haftada kaç adetle sınırlıyorsunuz? "))
ağaç_bitki_sayısı = int(input("Evde kaç tane ağaç veya bitki bulunuyor? "))
yenilenebilir_enerji_cihaz_sayısı = int(input("Evde kaç tane enerji üreten (güneş paneli, rüzgar türbini, vb.) cihaz veya sistem bulunuyor? "))
yemek_pişirme_süresi = float(input("Yemek pişirme için kaç saat doğalgazlı ocak kullanıyorsunuz?"))
bahçe_balkon_kullanım_süresi = float(input("Evdeki bahçe veya balkonu kaç saat boyunca kullanıyorsunuz haftada? "))
telekominikasyon_sıklığı = int(input("Evde kaç kez telekonferans veya uzaktan çalışma yöntemini kullanıyorsunuz? "))
elektronik_alet_alışveriş_sayısı = int(input("Yılda kaç kez elektronik ekipman veya cihaz satın alıyorsunuz? "))
tek_kullanımlık_pil_sayısı = int(input("Evde kaç tane tek kullanımlık pil kullanıyorsunuz haftada? "))
doğa_aktiviteleri_saatleri = int(input("Ailece doğada geçirilen vakit haftada kaç saattir? "))
elektrik_katsayısı = 0.4
araç_kullanımı_katsayısı = 0.12
uçuş_katsayısı = 1.5
su_tüketimi_katsayısı = 0.015
organik_tercih_katsayısı = 3
geri_dönüştürme_katsayısı = 1.5
ısıtma_enerji_katsayısı = 0.25
aydınlatma_katsayısı = 0.15
cihaz_kullanım_katsayısı = 0.04
su_ısıtıcısı_katsayısı = 0.08
fast_food_katsayısı = 2.5
tek_kullanımlık_ürün_katsayısı = 0.08
enerji_etiket_katsayısı = 8
geri_dönüştürme_oran_katsayısı = 0.6
toplu_ulaşım_katsayısı = 4.5
akıllı_ev_cihaz_katsayısı = 6
plastik_poşet_kullanım_katsayısı = 0.03
ağaç_bitki_katsayısı = 18
yenilenebilir_enerji_cihaz_katsayısı = 12
yemek_pişirme_süresi_katsayısı = 0.18
bahçe_balkon_kullanım_süresi_katsayısı = 1.8
telekominikasyon_katsayısı = 4.5
elektronik_alet_alışveriş_katsayısı = 1.8
tek_kullanımlık_pil_katsayısı = 0.15
doğa_aktiviteleri_katsayısı = 8
karbon_ayak_izi = (
    elektrik_tüketimi * elektrik_katsayısı +
    araç_kullanımı * araç_kullanımı_katsayısı +
    uçuş_sayısı * uçuş_katsayısı +
    su_tüketimi * su_tüketimi_katsayısı +
    organik_tercih_oranı * organik_tercih_katsayısı +
    geri_dönüştürme_sıklığı * geri_dönüştürme_katsayısı +
    ısıtma_enerji_kaynağı * ısıtma_enerji_katsayısı +
    aydınlatma_verimliliği * aydınlatma_katsayısı +
    cihaz_kullanım_süresi * cihaz_kullanım_katsayısı +
    su_ısıtıcısı_kullanım_süresi * su_ısıtıcısı_katsayısı +
    fast_food_tercih_sıklığı * fast_food_katsayısı +
    tek_kullanımlık_ürün_sayısı * tek_kullanımlık_ürün_katsayısı +
    enerji_etiketli_alet_sayısı * enerji_etiket_katsayısı +
    geri_dönüştürme_oranı * geri_dönüştürme_oran_katsayısı +
    toplu_ulaşım_kullanım_sıklığı * toplu_ulaşım_katsayısı +
    akıllı_ev_cihaz_sayısı * akıllı_ev_cihaz_katsayısı +
    plastik_poşet_kullanım_limiti * plastik_poşet_kullanım_katsayısı +
    ağaç_bitki_sayısı * ağaç_bitki_katsayısı +
    yenilenebilir_enerji_cihaz_sayısı * yenilenebilir_enerji_cihaz_katsayısı +
    yemek_pişirme_süresi * yemek_pişirme_süresi_katsayısı +
    bahçe_balkon_kullanım_süresi * bahçe_balkon_kullanım_süresi_katsayısı +
    telekominikasyon_sıklığı * telekominikasyon_katsayısı +
    elektronik_alet_alışveriş_sayısı * elektronik_alet_alışveriş_katsayısı +
    tek_kullanımlık_pil_sayısı * tek_kullanımlık_pil_katsayısı +
    doğa_aktiviteleri_saatleri * doğa_aktiviteleri_katsayısı)
veriler = [
    elektrik_tüketimi,
    araç_kullanımı,
    uçuş_sayısı,
    su_tüketimi,
    organik_tercih_oranı,
    geri_dönüştürme_sıklığı,
    ısıtma_enerji_kaynağı,
    aydınlatma_verimliliği,
    cihaz_kullanım_süresi,
    su_ısıtıcısı_kullanım_süresi,
    fast_food_tercih_sıklığı,
    tek_kullanımlık_ürün_sayısı,
    enerji_etiketli_alet_sayısı,
    geri_dönüştürme_oranı,
    toplu_ulaşım_kullanım_sıklığı,
    akıllı_ev_cihaz_sayısı,
    plastik_poşet_kullanım_limiti,
    ağaç_bitki_sayısı,
    yenilenebilir_enerji_cihaz_sayısı,
    yemek_pişirme_süresi,
    bahçe_balkon_kullanım_süresi,
    telekominikasyon_sıklığı,
    elektronik_alet_alışveriş_sayısı,
    tek_kullanımlık_pil_sayısı,
    doğa_aktiviteleri_saatleri]
kategoriler = [
    "Elektrik Tüketimi",
    "Araç Kullanımı",
    "Uçuş Sayısı",
    "Su Tüketimi",
    "Organik Tercih Oranı",
    "Geri Dönüşüm Sıklığı",
    "Isıtma Enerji Kaynağı",
    "Aydınlatma Verimliliği",
    "Cihaz Kullanım Süresi",
    "Su Isıtıcısı Kullanım Süresi",
    "Fast-Food Tercih Sıklığı",
    "Tek Kullanımlık Ürün Sayısı",
    "Enerji Etiketli Alet Sayısı",
    "Geri Dönüşüm Oranı",
    "Toplu Ulaşım Kullanım Sıklığı",
    "Akıllı Ev Cihaz Sayısı",
    "Plastik Poşet Kullanım Limiti",
    "Ağaç Bitki Sayısı",
    "Yenilenebilir Enerji Cihaz Sayısı",
    "Yemek Pişirme Süresi",
    "Bahçe Balkon Kullanım Süresi",
    "Telekominikasyon Sıklığı",
    "Elektronik Alet Alışveriş Sayısı",
    "Tek Kullanımlık Pil Sayısı",
    "Doğa Aktiviteleri Saatleri"]
karbon_ayak_izi_verileri = [
    elektrik_tüketimi * elektrik_katsayısı,
    araç_kullanımı * araç_kullanımı_katsayısı,
    uçuş_sayısı * uçuş_katsayısı,
    su_tüketimi * su_tüketimi_katsayısı,
    organik_tercih_oranı * organik_tercih_katsayısı,
    geri_dönüştürme_sıklığı * geri_dönüştürme_katsayısı,
    ısıtma_enerji_kaynağı * ısıtma_enerji_katsayısı,
    aydınlatma_verimliliği * aydınlatma_katsayısı,
    cihaz_kullanım_süresi * cihaz_kullanım_katsayısı,
    su_ısıtıcısı_kullanım_süresi * su_ısıtıcısı_katsayısı,
    fast_food_tercih_sıklığı * fast_food_katsayısı,
    tek_kullanımlık_ürün_sayısı * tek_kullanımlık_ürün_katsayısı,
    enerji_etiketli_alet_sayısı * enerji_etiket_katsayısı,
    geri_dönüştürme_oranı * geri_dönüştürme_oran_katsayısı,
    toplu_ulaşım_kullanım_sıklığı * toplu_ulaşım_katsayısı,
    akıllı_ev_cihaz_sayısı * akıllı_ev_cihaz_katsayısı,
    plastik_poşet_kullanım_limiti * plastik_poşet_kullanım_katsayısı,
    ağaç_bitki_sayısı * ağaç_bitki_katsayısı,
    yenilenebilir_enerji_cihaz_sayısı * yenilenebilir_enerji_cihaz_katsayısı,
    yemek_pişirme_süresi * yemek_pişirme_süresi_katsayısı,
    bahçe_balkon_kullanım_süresi * bahçe_balkon_kullanım_süresi_katsayısı,
    telekominikasyon_sıklığı * telekominikasyon_katsayısı,
    elektronik_alet_alışveriş_sayısı * elektronik_alet_alışveriş_katsayısı,
    tek_kullanımlık_pil_sayısı * tek_kullanımlık_pil_katsayısı,
    doğa_aktiviteleri_saatleri * doğa_aktiviteleri_katsayısı]
plt.figure(figsize=(15, 8))
plt.barh(kategoriler, karbon_ayak_izi_verileri, color='skyblue')
plt.xlabel('Karbon Ayak İzi (CO2 Eşdeğeri)')
plt.title('Karbon Ayak İzi Kategorileri')
plt.grid(axis='x')
plt.show()
print(f"\nToplam karbon ayak iziniz: {karbon_ayak_izi} kg CO2e")
print(f"\nToplam karbon ayak iziniz: {sum(karbon_ayak_izi_verileri)} kg CO2e")


