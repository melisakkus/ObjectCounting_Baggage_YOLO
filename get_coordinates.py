import cv2

image_name="images/reference_line.png"
image = cv2.imread(image_name)
width , height = 1000,800
image = cv2.resize(image, (width, height))


def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Tıklanan Nokta: X={x} Y={y}")
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1) # Yeşil bir daire
        cv2.imshow("Görüntü", image)

if image is None:
    print("Resim yüklenemedi. Dosya yolunu kontrol edin.")
else:
    cv2.imshow("Görüntü", image)

    # Pencereye fare geri arama fonksiyonunu ata
    cv2.setMouseCallback("Görüntü", get_coordinates)

    cv2.waitKey(0) # Bir tuşa basılana kadar bekle
    cv2.destroyAllWindows()