from tabulate import tabulate

# Database pertanyaan dan jawaban (soal 1–19 lengkap)
qa_data = {
    "1": {
        "soal": "Identifikasi komponen elektronika pasif pada rangkaian",
        "jawaban": tabulate([
            ["1", "Resistor 10 K", "Fixed Resistor", "─[Ω]─", "Pull-up resistor untuk output DO"],
            ["2", "Resistor 10 K", "Fixed Resistor", "─[Ω]─", "Pembagi tegangan untuk AO"],
            ["3", "Resistor 1 K", "Fixed Resistor", "─[Ω]─", "Mengatur sensitivitas deteksi"],
            ["4", "Resistor 1 K", "Fixed Resistor", "─[Ω]─", "Melindungi arus deteksi/indikator"],
            ["5", "Kapasitor 0.1 µF", "Kapasitor Keramik", "─| |─", "Bypass dari noise supply IC"],
            ["6", "Kapasitor 0.1 µF", "Kapasitor Keramik", "─| |─", "Filter noise input komparator"],
            ["7", "Potensiometer 10 K", "Variabel Resistor", "─[Ω]←", "Pengatur ambang batas kelembapan"]
        ], headers=["No", "Nama", "Jenis", "Simbol", "Keterangan"], tablefmt="fancy_grid")
    },
    "2": {
        "soal": "Identifikasi komponen elektronika aktif pada rangkaian",
        "jawaban": tabulate([
            ["1", "LED 805", "SMD LED (Putih)", "→|─|", "LED Indikator Power"],
            ["2", "LED 805", "SMD LED (Putih)", "→|─|", "LED Indikator Status D0"],
            ["3", "LM393", "Dual Voltage Comparator", "[≶]", "Membandingkan tegangan sensor dan referensi"]
        ], headers=["No", "Nama", "Jenis", "Simbol", "Keterangan"], tablefmt="fancy_grid")
    },
    "3": {
        "soal": "Input, proses, dan output",
        "jawaban": tabulate([
            ["Resistor 10 K", "", ""],
            ["Pin Header", "", ""],
            ["Capacitor 0,1 µF", "", ""],
            ["Potensiometer 10 K", "", ""],
            ["Capacitor 0,1 µF", "LM393", "Resistor 10 K"],
            ["", "", "Resistor 1 K"],
            ["", "", "Resistor 1 K"],
            ["", "", "LED 805"],
            ["", "", "LED 805"],
            ["", "", "Pin Header"]
        ], headers=["INPUT", "PROSES", "OUTPUT"], tablefmt="fancy_grid")
    },
    "4": {
        "soal": "Permasalahan Pada Rangkaian",
        "jawaban": tabulate([
            ["LED Power tidak menyala", "Cek koneksi ke VCC & GND", "Periksa kabel/pin"],
            ["DO selalu HIGH/LOW", "Ubah kelembapan, lihat LED", "Atur potensiometer, cek sensor"],
            ["LED status tidak menyala", "Periksa DO pakai multimeter", "Cek LED/resistor/solderan"],
            ["AO tidak berubah", "Gunakan multimeter baca AO", "Bersihkan probe, cek resistor"]
        ], headers=["Permasalahan", "Cara Identifikasi", "Solusi"], tablefmt="fancy_grid")
    },
    "5": {
        "soal": "Identifikasi Perangkat K3",
        "jawaban": tabulate([
            ["Sarung tangan anti-statis", "Melindungi tangan dan komponen dari ESD"],
            ["Kacamata pelindung", "Melindungi mata dari percikan solder"],
            ["Alas kerja ESD", "Melindungi komponen dari ESD"],
            ["Kotak P3K", "Pertolongan pertama jika cedera ringan"],
            ["APAR", "Memadamkan kebakaran akibat korsleting"]
        ], headers=["Perangkat K3", "Kegunaan"], tablefmt="fancy_grid")
    },
    "6": {
        "soal": "Identifikasi Perangkat Ukur Elektronika",
        "jawaban": tabulate([
            ["Multimeter", "Mengukur tegangan, arus, hambatan"],
            ["Osiloskop", "Melihat bentuk sinyal"],
            ["Power Supply DC", "Memberi tegangan uji"],
            ["LCR Meter", "Mengukur induktansi, kapasitansi, resistansi"],
            ["Logic Analyzer", "Analisa sinyal digital dan debugging"]
        ], headers=["Perangkat", "Kegunaan"], tablefmt="fancy_grid")
    },
    "7": {
        "soal": "Reverse Engineering SOP",
        "jawaban": tabulate([
            ["1", "Matikan sumber daya", "Aman dari kejutan"],
            ["2", "Inspeksi visual", "Deteksi kerusakan fisik"],
            ["3", "Gunakan AVOMeter", "Verifikasi sambungan"],
            ["4", "Gunakan Oscilloscope", "Analisa sinyal"],
            ["5", "Gambar skematik", "Dokumentasi rangkaian"],
            ["6", "Bandingkan fungsi", "Cocokkan dengan realita"]
        ], headers=["No", "Langkah", "Penjelasan"], tablefmt="fancy_grid")
    },
"8": {
    "soal": "Mengapa penting untuk melakukan inspeksi rutin terhadap alat kerja dan fasilitas sebelum digunakan?",
    "keywords": ["inspeksi rutin", "cek alat", "pengecekan alat"],
    "jawaban": (
        "- Memastikan semua alat dalam kondisi aman dan layak pakai\n"
        "- Mencegah kecelakaan akibat alat rusak atau kabel terkelupas\n"
        "- Menjamin efisiensi dan kelancaran pekerjaan"
    )
},
"9": {
    "soal": "Apa yang harus dilakukan jika terjadi kebakaran akibat korsleting pada perangkat elektronik?",
    "keywords": ["kebakaran", "korsleting", "korslet"],
    "jawaban": (
        "- Matikan sumber listrik utama\n"
        "- Gunakan APAR (CO₂ atau dry chemical)\n"
        "- Evakuasi area jika api tidak terkendali\n"
        "- Hubungi petugas keamanan atau pemadam kebakaran"
    )
},
"10": {
    "soal": "Jelaskan cara menangani situasi saat seseorang terkena sengatan listrik!",
    "keywords": ["sengatan listrik", "kesetrum", "korban listrik"],
    "jawaban": (
        "- Jangan sentuh korban langsung\n"
        "- Matikan sumber listrik terlebih dahulu\n"
        "- Gunakan alat isolator untuk menjauhkan korban dari sumber\n"
        "- Periksa kondisi korban, lakukan CPR jika perlu\n"
        "- Hubungi tenaga medis dan jangan tinggalkan korban sendirian"
    )
},
"11": {
    "soal": "Jelaskan apa perbedaan fungsi antara AVOMeter, Oscilloscope, Function Generator, dan Logic Analyzer serta saat kondisi apa masing-masing alat digunakan?",
    "keywords": ["fungsi avometer", "logic analyzer", "osiloskop", "alat ukur elektronika"],
    "jawaban": (
        "- AVOMeter: mengukur tegangan, arus, hambatan. Digunakan saat ingin mengetahui nilai dasar dari parameter listrik, seperti memeriksa tegangan sumber atau arus pada suatu rangkaian.\n"
        "- Osiloskop: Menampilkan bentuk gelombang sinyal secara real-time (tegangan terhadap waktu). Digunakan saat ingin menganalisis bentuk sinyal analog atau digital, frekuensi, noise, atau perubahan sinyal terhadap waktu.\n"
        "- Function Generator: Menghasilkan sinyal sine, square, triangle, dll pada frekuensi tertentu. Digunakan untuk menginjeksikan sinyal ke rangkaian untuk pengujian respons sistem atau filter.\n"
        "- Logic Analyzer: Mengukur dan menganalisis sinyal digital (logika 0 dan 1) dari banyak kanal secara paralel. Cocok digunakan saat menganalisis protokol digital, seperti SPI, I2C, UART, atau sistem digital dengan banyak output."
    )
},
"12": {
    "soal": "Jelaskan cara mengukur tegangan DC, arus DC, dan circuit continuity pada suatu rangkaian menggunakan AVOMeter!",
    "keywords": ["ukur tegangan", "continuity", "avometer", "multimeter"],
    "jawaban": (
        "Tegangan DC:\n"
        "- Putar selector ke DC Voltage (VDC)\n"
        "- Probe merah ke positif, hitam ke negatif\n"
        "- Baca tegangan di layar\n\n"
        "Arus DC:\n"
        "- Pilih DC Ampere (ADC)\n"
        "- Putuskan jalur dan sambungkan probe secara seri\n"
        "- Baca nilai arus\n\n"
        "Continuity:\n"
        "- Pilih mode continuity (dioda/buzzer)\n"
        "- Hubungkan probe ke dua titik\n"
        "- Jika ada sambungan, akan terdengar bunyi"
    )
},
"13": {
    "soal": "Bagaimana cara mengatur Oscilloscope untuk mengukur sinyal gelombang DC",
    "keywords": ["atur osiloskop", "sinyal dc", "pengukuran dc"],
    "jawaban": (
        "- Hubungkan probe ke titik sinyal dan ground\n"
        "- Atur coupling ke DC\n"
        "- Sesuaikan skala volts/div untuk ketajaman sinyal\n"
        "- Atur time/div secukupnya\n"
        "- Sinyal DC ditampilkan sebagai garis datar"
    )
},
"14": {
    "soal": "Sebutkan alat pelindung diri (APD) yang wajib digunakan saat bekerja di area laboratorium elektronik!",
    "keywords": ["apd", "alat pelindung diri", "lab elektronika"],
    "jawaban": (
        "- Sarung tangan anti-statis\n"
        "- Gelang anti-statis\n"
        "- Alas kerja anti-statis (ESD mat)\n"
        "- Kacamata pelindung\n"
        "- Jas laboratorium atau pakaian anti-statis\n"
        "- Masker debu / asap solder\n"
        "- Sepatu dengan alas anti-statis"
    )
},
"15": {
    "soal": "Apa yang dimaksud dengan ESD (Electrostatic Discharge), dan bagaimana Anda meminimalkan dampaknya di lingkungan kerja",
    "keywords": ["esd", "electrostatic discharge"],
    "jawaban": (
        "ESD adalah pelepasan muatan listrik statis secara tiba-tiba yang bisa merusak komponen elektronik.\n"
        "Cara meminimalkan:\n"
        "- Gunakan peralatan anti-statis seperti wrist strap dan ESD mat\n"
        "- Hindari gesekan bahan sintetis\n"
        "- Jaga kelembaban ruangan\n"
        "- Gunakan pakaian dan sepatu anti-statis\n"
        "- Simpan komponen dalam kantong ESD"
    )
},
"16": {
    "soal": "Mengapa penting untuk menggunakan grounding strap atau anti-static wristband saat menangani komponen elektronik sensitif",
    "keywords": ["grounding strap", "wristband", "anti statis"],
    "jawaban": (
        "- Mencegah akumulasi muatan listrik statis pada tubuh\n"
        "- Melindungi IC, sensor, dan mikroprosesor dari kerusakan\n"
        "- Muatan akan dialirkan ke ground secara aman"
    )
},
"17": {
    "soal": "Pemrograman Protokol Komunikasi",
    "keywords": ["kode lcd", "lcd i2c", "komunikasi i2c", "lcd esp32"],
    "jawaban": (
        "#include <Wire.h>\n"
        "#include <LiquidCrystal_I2C.h>\n\n"
        "LiquidCrystal_I2C lcd(0x27, 16, 2);\n\n"
        "void setup() {\n"
        "  lcd.begin();\n"
        "  lcd.backlight();\n"
        "  lcd.setCursor(0, 0);\n"
        "  lcd.print(\"ID : FaisalFirdaus\");\n"
        "}\n\n"
        "void loop() {}"
    )
},
"18": {
    "soal": "Jelaskan mengapa penting bagi seorang Embedded System Engineer untuk memahami dan mengikuti SOP dalam proses pembuatan sistem tertanam, mulai dari perancangan sistem hingga proses implementasi sistem di lapangan!",
    "keywords": ["sop", "embedded system", "prosedur kerja"],
    "jawaban": (
        "Seorang Embedded System Engineer harus memahami dan mengikuti SOP (Standard Operating Procedure) karena SOP menjadi panduan standar dalam setiap tahapan pengembangan sistem, mulai dari perancangan, pengujian, hingga implementasi di lapangan. Mengikuti SOP membantu memastikan bahwa sistem dirancang dengan aman, efisien, dan sesuai standar industri, menghindari kesalahan fatal yang dapat menyebabkan kerusakan perangkat atau bahaya keselamatan. Selain itu, SOP juga penting untuk menjamin kualitas, memudahkan dokumentasi, mempermudah tim lain memahami proses, dan mendukung troubleshooting bila terjadi kegagalan sistem."
    )
},
"19": {
    "soal": "Seorang Engineer akan menggunakan perangkat bertegangan tinggi (relay, pompa, dan kipas) untuk memproduksi sistem kendali dan pemantauan agroteknologi. Apa saja langkah-langkah keselamatan kerja yang perlu diperhatikan sesuai SOP saat melakukan implementasi sistem tersebut?",
    "keywords": ["keselamatan", "relay", "tegangan tinggi", "pompa", "kipas"],
    "jawaban": (
        "- Pastikan sistem dalam keadaan OFF sebelum bekerja\n"
        "- Gunakan APD seperti sarung tangan isolasi dan pelindung mata\n"
        "- Periksa kabel dan isolasi\n"
        "- Beri label peringatan dan pembatasan akses\n"
        "- Uji sistem dengan tegangan rendah dulu\n"
        "- Selalu bekerja dalam tim atau diawasi\n"
        "- Pastikan ada grounding dan sekering"
    )
}

}

# Fungsi tanya jawab
def tanya_jawab():
    print("=Kode Salah=")
    while True:
        query = input("\nKetik Keluar atau Pertanyaan): ").lower()

        if query == "keluar":
            break

        matched = False
        for key, value in qa_data.items():
            soal = value["soal"] if isinstance(value, dict) else ""
            if key in query or soal.lower() in query:
                print("\nJawaban:")
                print(value["jawaban"] if isinstance(value, dict) else value)
                matched = True
                break

        if not matched:
            print("Pertanyaan tidak ditemukan. Silakan tanya soal dari 1–19.")

# Jalankan program
if __name__ == "__main__":
    tanya_jawab()
