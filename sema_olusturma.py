# import matplotlib.pyplot as plt
# import networkx as nx

# # Blok şema diyagramı oluşturma
# hardware_flow = nx.DiGraph()

# # Bileşenleri ekleyelim (malzemeleri birleştirerek)
# hardware_flow.add_edges_from([
#     ("Deneyap Kartları", "Motor Kartı"),
#     ("Motor Kartı", "DC Motorlar"),
#     ("Deneyap Kartları", "Bluetooth Modülü"),
#     ("Bluetooth Modülü", "Joystickler"),
#     ("Deneyap Kartları", "Jumper Kablolar"),
#     ("Li-Po Piller", "Deneyap Kartları"),
#     ("Robot Şasisi", "DC Motorlar"),
# ])

# # Görselleştirme
# plt.figure(figsize=(12, 8))

# # Spring Layout kullanarak düzenleme
# pos = nx.spring_layout(hardware_flow, seed=42, k=0.8)  # k'yi artırarak düğümleri daha uzak yapıyoruz

# # Düğümleri ve kenarları çizme
# nx.draw(
#     hardware_flow, pos, with_labels=False, node_color='lightblue', edge_color='black',
#     node_size=6800, font_size=9, font_weight='bold',  # Yuvarlakları büyütmek için node_size arttırıldı
#     bbox=dict(facecolor="white", edgecolor='black', boxstyle='round,pad=0.3')  # Yazılar yuvarlak kutu içinde
# )

# # Etiketleri alt alta yazmak için düzenleme
# labels = {node: "\n".join(node.split()) for node in hardware_flow.nodes()}  # İki kelimeden oluşan yazıları alt alta yerleştirir
# nx.draw_networkx_labels(hardware_flow, pos, labels=labels, font_size=14, font_weight='bold')

# plt.title("Robot Donanım Blok Şeması", fontsize=14)
# plt.show()


import matplotlib.pyplot as plt

# years = [2020, 2021, 2022, 2023, 2024, 2025]
# usage_growth = [50, 75, 105, 130, 160, 200]  # Milyon Dolar Cinsinden

# plt.plot(years, usage_growth, marker='o', color='b', linestyle='-', linewidth=2)
# plt.title("AR Teknolojisinin Turizmde Kullanılma Hacmi (2020-2025)")
# plt.xlabel("Yıl")
# plt.ylabel("Pazar Hacmi (Milyon Dolar)")
# plt.grid(True)
# plt.show()

categories = ['Abonelikler', 'Bilet Satışları', 'Lisanslama', 'Özel Turlar']
income_potential = [35, 25, 30, 10]  # Yüzde olarak

plt.bar(categories, income_potential, color='green')
plt.title("ARtur Gelir Modeli")
plt.xlabel("Gelir Kaynağı")
plt.ylabel("Yüzde (%)")
plt.show()


import matplotlib.pyplot as plt

years = [2023, 2024, 2025, 2026, 2027, 2028]
market_size = [92.46, 123.45, 164.56, 219.87, 293.45, 397.86]  # Milyar Dolar Cinsinden

plt.plot(years, market_size, marker='o', color='b', linestyle='-', linewidth=2)
plt.title("Yapay Zekâ Destekli Seyahat Pazarının Büyümesi (2023-2028)")
plt.xlabel("Yıl")
plt.ylabel("Pazar Büyüklüğü (Milyar Dolar)")
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt

# Yıllar ve pazar büyüklüğü verileri
years = [2005, 2010, 2015, 2020, 2025]
market_size_ar = [0.03, 0.09, 0.25, 0.55, 2.0]  # Milyar dolar cinsinden artırılmış gerçeklik pazar büyüklüğü
market_size_ai = [0.1, 0.2, 0.5, 1.5, 3.0]  # Milyar dolar cinsinden yapay zeka destekli seyahat pazarı büyüklüğü

# AR Pazar Büyümesi Grafiği
plt.figure(figsize=(10, 6))
plt.plot(years, market_size_ar, marker='o', color='b', linestyle='-', linewidth=2, label="AR Teknolojisi")
plt.plot(years, market_size_ai, marker='o', color='g', linestyle='-', linewidth=2, label="AI Destekli Seyahat")
plt.title("AR ve AI Teknolojilerinin Turizmdeki Pazar Büyüklüğü (2005-2025)")
plt.xlabel("Yıl")
plt.ylabel("Pazar Büyüklüğü (Milyar Dolar)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Yıllar ve pazar büyüklüğü verileri
years = [2005, 2010, 2015, 2020, 2025]  # Tam sayılar
market_size_ar = [0.03, 0.09, 0.25, 0.55, 2.0]  # Milyar dolar cinsinden artırılmış gerçeklik pazar büyüklüğü
market_size_ai = [0.1, 0.2, 0.5, 1.5, 3.0]  # Milyar dolar cinsinden yapay zeka destekli seyahat pazarı büyüklüğü

# Yılları integer yapmak için
years = [int(year) for year in years]

# AR Pazar Büyümesi Grafiği
plt.figure(figsize=(10, 6))
plt.plot(years, market_size_ar, marker='o', color='b', linestyle='-', linewidth=2, label="AR Teknolojisi")
plt.plot(years, market_size_ai, marker='o', color='g', linestyle='-', linewidth=2, label="AI Destekli Seyahat")
plt.title("AR ve AI Teknolojilerinin Turizmdeki Pazar Büyüklüğü (2005-2025)")
plt.xlabel("Yıl")
plt.ylabel("Pazar Büyüklüğü (Milyar Dolar)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator  # Tam sayı gösterimi için

# Yıllar ve pazar büyüklüğü verileri
years = [2005, 2010, 2015, 2020, 2025]  # Tam sayılar
market_size_ar = [0.03, 0.09, 0.25, 0.55, 2.0]  # Milyar dolar cinsinden artırılmış gerçeklik pazar büyüklüğü
market_size_ai = [0.1, 0.2, 0.5, 1.5, 3.0]  # Milyar dolar cinsinden yapay zeka destekli seyahat pazarı büyüklüğü

# AR Pazar Büyümesi Grafiği
plt.figure(figsize=(10, 6))
plt.plot(years, market_size_ar, marker='o', color='b', linestyle='-', linewidth=2, label="AR Teknolojisi")
plt.plot(years, market_size_ai, marker='o', color='g', linestyle='-', linewidth=2, label="AI Destekli Seyahat")
plt.title("AR ve AI Teknolojilerinin Turizmdeki Pazar Büyüklüğü (2005-2025)")
plt.xlabel("Yıl")
plt.ylabel("Pazar Büyüklüğü (Milyar Dolar)")
plt.grid(True)

# X eksenindeki yılları tam sayı olarak göstermek için
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

plt.legend()
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import networkx as nx

# Grafik oluştur
G = nx.DiGraph()

# Düğümleri ekle
G.add_node("ARtur")
G.add_node("Müzeler")
G.add_node("Belediyeler")
G.add_node("Turizm Şirketleri")
G.add_node("Premium İçerik Abonelikleri")
G.add_node("Özel Turlar")
G.add_node("Lisanslama")
G.add_node("Dijital Arşivleme")
G.add_node("Sanal Turlar")

# Kenarları ekle
G.add_edges_from([
    ("ARtur", "Müzeler"),
    ("ARtur", "Belediyeler"),
    ("ARtur", "Turizm Şirketleri"),
    ("ARtur", "Premium İçerik Abonelikleri"),
    ("Müzeler", "Dijital Arşivleme"),
    ("Müzeler", "Sanal Turlar"),
    ("Belediyeler", "Özel Turlar"),
    ("Turizm Şirketleri", "Premium İçerik Abonelikleri"),
    ("Premium İçerik Abonelikleri", "Lisanslama"),
    ("Dijital Arşivleme", "Sanal Turlar"),
])

# Grafik özelliklerini ayarlama
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Düzenleme tipi (spring_layout daha estetik olabilir)

# Grafik çiz
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)

# Başlık ekleyelim
plt.title("ARtur Projesi Ekosistemi")

# Göster
plt.tight_layout()
plt.show()



import matplotlib.pyplot as plt
import pandas as pd

# İlişkiler
data = {
    "Kaynak": ["ARtur", "ARtur", "ARtur", "ARtur", "Müzeler", "Müzeler", "Belediyeler", 
               "Turizm Şirketleri", "Premium İçerik Abonelikleri", "Dijital Arşivleme"],
    "Hedef": ["Müzeler", "Belediyeler", "Turizm Şirketleri", "Premium İçerik Abonelikleri", 
              "Dijital Arşivleme", "Sanal Turlar", "Özel Turlar", 
              "Premium İçerik Abonelikleri", "Lisanslama", "Sanal Turlar"]
}

df = pd.DataFrame(data)

# Grafik oluştur
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('tight')
ax.axis('off')

# Tabloyu çiz
table_data = [df.columns.tolist()] + df.values.tolist()
ax.table(cellText=table_data, colLabels=None, loc='center', cellLoc='center')

plt.title("ARtur Projesi Akış Diyagramı", fontsize=14)
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Zaman serisi verileri
years = [2005, 2010, 2015, 2020, 2025]
market_size_ar = [0.03, 0.09, 0.25, 0.55, 2.0]
market_size_ai = [0.1, 0.2, 0.5, 1.5, 3.0]

# DataFrame oluştur
df = pd.DataFrame({
    'Yıl': years,
    'AR Teknolojisi Pazar Büyüklüğü (Milyar $)': market_size_ar,
    'AI Destekli Seyahat Pazar Büyüklüğü (Milyar $)': market_size_ai
})

# Grafik oluştur
df.set_index('Yıl').plot(kind='bar', figsize=(10, 6))

plt.title("AR ve AI Teknolojilerinin Pazar Büyüklüğü (2005-2025)")
plt.xlabel("Yıl")
plt.ylabel("Pazar Büyüklüğü (Milyar Dolar)")
plt.grid(True)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import networkx as nx

# Grafik oluştur
G = nx.DiGraph()

# Düğümleri ekle (iş ortaklıkları ve gelir yaratma yöntemleri)
G.add_node("ARtur", label="Proje Başlangıcı")  # Proje başlatıcı
G.add_node("Müzeler", label="Premium İçerik Abonelikleri")  # İçerik sağlayıcı
G.add_node("Belediyeler", label="Dijital Arşivleme ve Turlar")  # Kamu destekli projeler
G.add_node("Turizm Şirketleri", label="Turistik Paket ve Satış")  # Turizm satışı yapan firmalar
G.add_node("Sanal Turlar", label="Dijital Ürünler ve Abonelikler")  # Sanal turlar ile gelir
G.add_node("Premium İçerik Abonelikleri", label="Abonelik Geliri")  # Premium içerik abonelikleri
G.add_node("Özel Turlar", label="Özel Tur Gelirleri")  # Turlar ile gelir
G.add_node("Lisanslama", label="Lisanslama ve Telif Hakkı Geliri")  # Lisans anlaşmaları
G.add_node("Dijital Arşivleme", label="Dijital Arşiv Gelirleri")  # Arşivlerin dijital satışı

# Kenarları ekle (işbirlikleri ve ilişkiler)
G.add_edges_from([
    ("ARtur", "Müzeler"),
    ("ARtur", "Belediyeler"),
    ("ARtur", "Turizm Şirketleri"),
    ("ARtur", "Premium İçerik Abonelikleri"),
    ("Müzeler", "Dijital Arşivleme"),
    ("Müzeler", "Sanal Turlar"),
    ("Belediyeler", "Dijital Arşivleme"),
    ("Turizm Şirketleri", "Özel Turlar"),
    ("Premium İçerik Abonelikleri", "Lisanslama"),
    ("Dijital Arşivleme", "Sanal Turlar"),
])

# Grafik ayarları
pos = nx.spring_layout(G, seed=42)  # Yerleşim tipi
plt.figure(figsize=(12, 8))

# Ağı çiz
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')

# Gelir oluşturma etiketleri ekle
labels = nx.get_node_attributes(G, 'label')
for node, (x, y) in pos.items():
    plt.text(x, y + 0.05, labels[node], fontsize=8, ha='center')

# Başlık
plt.title("ARtur Projesi İş Ortaklıkları ve Gelir Modeli", fontsize=14)

plt.tight_layout()
plt.show()



import matplotlib.pyplot as plt

# Daireyi dilimlere ayırarak sürdürülebilirlik döngüsünü oluşturma

labels = ['Gelir Modeli', 'İş Ortaklıkları', 'Yenilikçi Teknoloji', 'Kullanıcı Deneyimi', 'Toplum ve Çevre', 'Veri ve Analiz']
sizes = [20, 20, 20, 20, 10, 10]  # Her dilim için eşit büyüklükler

# Renkler
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

# Daireyi çizme
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'black'})

# Dairenin merkezine "Sürdürülebilirlik Döngüsü" yazısı ekleme
plt.text(-0.1, 0, 'Sürdürülebilirlik\nDöngüsü', horizontalalignment='center', verticalalignment='center', fontsize=14, fontweight='bold')

# Grafiği göster
plt.title("Proje Sürdürülebilirlik Döngüsü", fontsize=16)
plt.axis('equal')  # Dairenin tam yuvarlak olmasını sağlar
plt.tight_layout()
plt.show()





import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Kanvas şablonu
fig, ax = plt.subplots(figsize=(16, 9))
ax.axis('off')

# Kutuların koordinat ve boyutları
boxes = [
    (0.02, 0.55, 0.18, 0.4, 'Müşteri Segmentleri', 'Yerli ve yabancı turistler\nKültürel miras meraklıları\nTarih ve arkeoloji araştırmacıları\nTurizm şirketleri\nBelediyeler ve müzeler'),
    (0.22, 0.55, 0.18, 0.4, 'Değer Önerisi', 'Katmanlı AR ile tarihi yapıların\nrekonstrüksiyonları\nAI rehber ile etkileşimli\nve kişiselleştirilmiş bilgi\nZamansal keşif imkanı'),
    (0.42, 0.55, 0.18, 0.4, 'Kanallar', 'Mobil uygulama (iOS, Android)\nAR gözlük entegrasyonu\nTurizm acenteleri\nMüzeler ve belediyeler ile\nortak projeler\nDijital pazarlama (web, sosyal medya)'),
    (0.62, 0.55, 0.18, 0.4, 'Müşteri İlişkileri', '7/24 AI tabanlı rehber\nKişisel asistan deneyimi\nGeribildirim mekanizması\nSadakat programları\nSosyal medya toplulukları'),
    (0.82, 0.55, 0.16, 0.4, 'Gelir Akışı', 'Kurumsal lisanslama\nTurizm şirketlerine satış\nUygulama içi premium\nözellikler\nÖzel turlar\nBilet entegrasyonu'),
    (0.02, 0.05, 0.3, 0.4, 'Temel Ortaklıklar', 'Müzeler ve kültürel miras\nkurumları\nBelediyeler ve kamu kurumları\nAR ve AI teknoloji sağlayıcıları\nTurizm firmaları\nÜniversiteler ve akademisyenler'),
    (0.34, 0.05, 0.3, 0.4, 'Temel Faaliyetler', 'AR tabanlı mobil uygulama\ngeliştirme\nAI rehber ve NLP modeli\nintegrasyonu\n3D modelleme ve AR\nkatman tasarımı\nSaha testleri ve kullanıcı\ngeribildirimleri\nTarihsel araştırmalar ve\nuzman görüşleri'),
    (0.66, 0.05, 0.16, 0.4, 'Temel Kaynaklar', 'Mobil uygulama\nGeliştirici ekibi\nAR/AI altyapısı\nTarihsel veri tabanı\nİş ortakları ve uzmanlar'),
    (0.84, 0.05, 0.14, 0.4, 'Maliyet Yapısı', 'AR/AI geliştirme maliyetleri\nPersonel giderleri\nLisanslama ve telif ücretleri\nReklam ve pazarlama\nSaha çalışmaları')
]

# Kutuları çiz ve başlık/metin ekle
for x, y, w, h, title, content in boxes:
    ax.add_patch(Rectangle((x, y), w, h, linewidth=2, edgecolor='black', facecolor='white'))
    ax.text(x + 0.01, y + h - 0.04, title, fontsize=12, fontweight='bold', ha='left', va='top', color='darkgreen')
    ax.text(x + 0.01, y + h - 0.08, content, fontsize=10, ha='left', va='top', wrap=True)

# Başlık
ax.text(0.5, 0.97, 'ARtur İş Modeli Kanvası', fontsize=20, fontweight='bold', ha='center', color='darkgreen')

plt.tight_layout()
plt.show()
