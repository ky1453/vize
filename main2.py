import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

yerçekimi = 9.8

def main():
    mermi_max_hizi = 1800
    mermi_min_hizi = 330
    atis_acisi = 30
    baslangic_yuksekligi = 6
    hedef_mesafesi = 20000 + (200 * np.random.randint(-10, 10))
    hedef_boyutu = 1000 + (100 * np.random.randint(-2, 2))
    atis_denemeleri = 0
    hedef_vuruldu = False

    while not hedef_vuruldu:
        mermi_hizi = (mermi_max_hizi + mermi_min_hizi) / 2
        
        x_ekseni_hizi = mermi_hizi * math.cos(math.radians(atis_acisi))
        y_ekseni_hizi = mermi_hizi * math.sin(math.radians(atis_acisi))

        mermi_uçuş_süresi = (2 * y_ekseni_hizi / yerçekimi) + 0.07
        mermi_uçuş_mesafesi = x_ekseni_hizi * mermi_uçuş_süresi

        if hedef_mesafesi <= mermi_uçuş_mesafesi <= hedef_mesafesi + hedef_boyutu:
            hedef_vuruldu = True
            print("Hedefe isabet!")
            print("Ateş edilen toplam mermi sayısı: ", atis_denemeleri)
            print("Mermi hızı: ", mermi_hizi)
            print("Mermi uçuş süresi: ", mermi_uçuş_süresi)
            print("Mermi uçuş mesafesi: ", mermi_uçuş_mesafesi)
            print("Hedef mesafesi: ", hedef_mesafesi)
            break
        else:
            if hedef_mesafesi >= mermi_uçuş_mesafesi:
                print("Mermi hedefin önüne düştü.")
                mermi_min_hizi = mermi_hizi
            elif mermi_uçuş_mesafesi >= hedef_mesafesi + hedef_boyutu:
                print("Mermi hedefin arkasına düştü.")
                mermi_max_hizi = mermi_hizi

            atis_denemeleri += 1

    t = np.linspace(0, mermi_uçuş_süresi, num=500)
    x_top = x_ekseni_hizi * t
    y_top = baslangic_yuksekligi + y_ekseni_hizi * t - 0.5 * yerçekimi * t ** 2
    
    fig, ax = plt.subplots()

    ax.plot([0, mermi_uçuş_mesafesi], [baslangic_yuksekligi, baslangic_yuksekligi], 'b-', label='Atış Yolu')

    
    ax.plot(mermi_uçuş_mesafesi, baslangic_yuksekligi, 'ro', label='İsabet Noktası')

   
    ax.plot(x_top, y_top, 'g--', label='Topun Yolu')

    plt.legend()
    plt.xticks(range(0, int(hedef_mesafesi + hedef_boyutu + 5000) + 1, 2500))
    plt.yticks(range(0, int(5000) + 1, 500))
    plt.title('Eğik Atış Hareketi Grafiği')
    plt.xlabel('Mesafe (metre)')
    plt.ylabel('Yükseklik (metre)')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    main()
