# Mamimu Currency Converter

Mamimu Currency Converter ini adalah sebuah aplikasi konverter mata uang yang dirancang agar memudahkan pengguna untuk mengkonversi antara mata uang yang berbeda menggunakan nilai tukar waktu nyata.

## Fitur Aplikasi

1. Mengkonversi antara beberapa mata uang yaitu USD, EURO, serta beberapa mata uang yang digunakan di Asia Tenggara
2. Mengambil nilai tukar waktu nyata dari API
3. Melihat mata uang yang tersedia
4. Lacak riwayat konversi
5. Antarmuka baris perintah yang ramah pengguna

## Persyaratan

- Python 3.6 atau lebih tinggi
- Pustaka requests untuk panggilan API

## Cara Instal

1. Pastikan sudah menginstal Python 3.6+
2. Instal paket-paket yang diperlukan:

bash
permintaan instalasi pip


## Cara Penggunaan

Jalankan aplikasi dari baris perintah:

bash
python main.py


## Struktur Program

Program ini mendemonstrasikan beberapa konsep pemrograman utama:

### 1. Struktur Kontrol

- Pernyataan kondisional (if/elif/else) untuk navigasi menu dan penanganan kesalahan
- Perulangan (while/for) untuk aliran program dan tampilan data
- Penanganan pengecualian (try/except) untuk manajemen kesalahan yang kuat

### 2. Struktur Data

- Kamus untuk menyimpan nilai tukar dan riwayat konversi
- Daftar untuk pilihan menu dan kode mata uang
- Objek data khusus (kelas) untuk mengatur fungsionalitas terkait

### 3. Library

- permintaan: Digunakan untuk mengambil nilai tukar mata uang dari API eksternal
- json: Digunakan untuk mengurai respons API dan menyimpan nilai tukar dalam cache
- os: Digunakan untuk membersihkan layar dan mendeteksi ukuran terminal
- time: Digunakan untuk mengatur waktu operasi dan melacak pembaruan nilai tukar
- datetime: Digunakan untuk menampilkan stempel waktu

## Cara Kerja

Program ini terdiri dari beberapa modul:

- main.py: Titik masuk utama dan antarmuka pengguna
- currency_converter.py: Berisi logika konversi inti
- currency_api.py: Menangani interaksi API untuk mengambil nilai tukar
- utils.py: Berisi fungsi utilitas untuk UI dan pemformatan

## Informasi API

Program ini menggunakan API nilai tukar mata uang gratis:
- API Utama: https://api.exchangerate-api.com/
- API cadangan: https://open.er-api.com/

Keduanya menyediakan data nilai tukar mata uang dasar tanpa memerlukan kunci API.
