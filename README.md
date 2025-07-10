# YOLO ile Bagaj Sayma Sistemi

YOLO (You Only Look Once) nesne tespiti kullanarak bagaj karuselindeki bagaj eşyalarını sayan bir bilgisayar görüşü projesi. Bu sistem, gerçek zamanlı video akışlarında bavul ve diğer bagaj eşyalarını takip edebilir ve sayabilir.

## 🎯 Özellikler

- **Gerçek Zamanlı Nesne Tespiti**: Doğru bagaj tespiti için YOLOv11 kullanır
- **Nesne Takibi**: Video karelerinde bireysel bagaj eşyalarını takip eder
- **Referans Çizgi Sayımı**: Doğru sayım için referans çizgi sistemi uygular
- **Video İşleme**: MP4 video dosyası işlemeyi destekler

## 📋 Gereksinimler

### Bağımlılıklar
```bash
pip install ultralytics
pip install opencv-python
pip install imutils
pip install numpy
```

## 📁 Proje Yapısı

```
ObjectCounting_Baggage_YOLO/
├── models/
│   └── yolo11n.pt              # YOLO model dosyası
├── test_videos/
│   └── baggage_carousel.mp4    # Test video dosyası
├── object_counting.py          # Ana uygulama betiği
├── explainings.txt            # Proje açıklamaları
└── README.md                  # Bu dosya
```


### Tuş Kontrolleri
- **'q'**: Uygulamadan çıkış
- **ESC**: Video penceresini kapatma


## 🔧 Nasıl Çalışır

1. **Video Girişi**: Belirtilen yoldan video yükler
2. **Kare İşleme**: Kareleri yapılandırılmış boyutlara yeniden boyutlandırır
3. **Nesne Tespiti**: Her karede nesneleri tespit etmek için YOLO kullanır
4. **Nesne Takibi**: Benzersiz ID'ler kullanarak tespit edilen nesneleri kareler arasında takip eder
5. **Referans Çizgi**: Nesneleri saymak için referans çizgi çizer
6. **Sayım Mantığı**: Nesneler referans çizgiyi geçtiğinde sayar
7. **Görüntüleme**: Sınırlayıcı kutular ve sayım bilgisi ile işlenmiş videoyu gösterir

## 📊 Nesne Sınıfları

Sistem bavul tespiti için yapılandırılmıştır (COCO sınıf ID: 28), ancak `suitcase_id` parametresini değiştirerek diğer nesneleri tespit edecek şekilde değiştirilebilir.

## 🔍 Teknik Detaylar

### Algoritma Akışı
1. Video karesini oku
2. Kareyi yeniden boyutlandır
3. YOLO ile nesne tespiti yap
4. Tespit edilen nesneleri takip et
5. Referans çizgiyi kontrol et
6. Sayımı güncelle
7. Sonuçları görüntüle

