data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}
# No 1
print("--- SEMUA DATA ---")
for info_panen in data_panen.values():
     tempat = info_panen['nama_lokasi'] 
     panen = info_panen['hasil_panen']
     print(f"lokasi berikut dari{tempat}, hasil panennya adalah {panen}")

# No 2
print("\n--- AKSES SPESIFIK ---")
jumlah_jagung = data_panen ['lokasi2']['hasil_panen']['jagung']
print(f" ini adalah jumlah jagung di lokasi 2 {jumlah_jagung}")

# No 3
print("\n--- AKSES SPESIFIK No 3---")
nama_lokasi = data_panen ['lokasi3']['nama_lokasi']
print(f"ini adalah nama lokasi dari lokasi 3 adalah {nama_lokasi}")

# No 4
print("\n--- LOOP PADI & KEDELAI ---")
for lokasi, info_panen in data_panen.items():
     jumlah_padi = info_panen['hasil_panen']['padi']
     jumlah_kedelai = info_panen['hasil_panen']['kedelai']
     print(f"ini jumlah padi {jumlah_padi} dan ini jumlah kedelai {jumlah_kedelai}")

# No 5
print("\n--- LIST HASIL ---")
list_padi = []
list_kedelai = []
for lokasi, info_panen in data_panen.items():
     jumlah_padi = info_panen['hasil_panen']['padi']
     jumlah_kedelai = info_panen['hasil_panen']['kedelai']
     list_padi.append(jumlah_padi)
     list_kedelai.append(jumlah_kedelai)
print(list_padi)
print(list_kedelai)

# No 6
print("\n--- STATUS KEBUN ---")
for lokasi, info_panen in data_panen.items():
     jumlah_padi = info_panen['hasil_panen']['padi']
     jumlah_jagung = info_panen['hasil_panen']['jagung']
     if jumlah_padi > 1300 or jumlah_jagung > 800:
        print(f"{lokasi}:perlu perhatian khusus")
     else: 
        print(f"{lokasi}:kondisi baik") 
