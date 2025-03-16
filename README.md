# Analisis-Data-dengan-Pyhton

Project ini bertujuan untuk menganalisis data peminjaman sepeda dan membangun Dashboard yang dikembangkan menggunakan Streamlit untuk menampilkan analisis interaktif mengenai data peminjaman sepeda. Data yang digunakan berasal dari dataset peminjaman sepeda harian dan per jam. Dashboard ini bertujuan untuk menjawab beberapa pertanyaan analisis utama terkait pola peminjaman sepeda berdasarkan faktor-faktor eksternal seperti kondisi cuaca, musim, jam, hari kerja, dan tren waktu.

fitur analisis pada Dashboard
1. peminjaman sepeda berdasarkan kondisi cuaca
   - Visualisasi menggunakan Boxplot
   - Menampilkan distribusi jumlah peminjaman berdasarkan kondisi cuaca (Cerah, Berawan, 
     Hujan/Snow).
2. peminjaman sepeda berdasarkan Hari kerja
   - Visualisasi menggunakan Boxplot
   - Membandingkan peminjaman antara hari kerja dan akhir pekan/libur.
3. Peminjaman Sepeda Berdasarkan Musim
   - Visualisasi menggunakan Barplot
   - Menampilkan total peminjaman di setiap musim (Semi, Panas, Gugur, Dingin).
4. Pola Peminjaman Sepeda Berdasarkan Jam
   - Visualisasi menggunakan Lineplot
   - Menunjukkan rata-rata peminjaman pada setiap jam dalam sehari.
5. Tren Harian Peminjaman Sepeda (Moving Average)
   - Visualisasi menggunakan Lineplot dengan perataan (7-day Moving Average)
   - Menunjukkan tren umum peminjaman dari waktu ke waktu.

Teknologi yang Digunakan
 - Python
 - Pandas
 - Matplotlib & Seaborn
 - Streamlit

Struktur File
- `Dashboard.py` : Script utama Streamlit untuk menjalankan dashboard.
- `day.csv` & `hour.csv` : Dataset peminjaman sepeda per hari dan per jam.
- `SUFI_BIKE.ipynb` : Notebook eksplorasi dan analisis awal sebelum membuat dashboard.


Cara Menjalankan Dashboard
1. Pastikan semua dependensi sudah terinstall:
"pip install streamlit pandas matplotlib seaborn"
2. Jalankan dashboard dengan perintah:
"streamlit run Dashboard.py"
3. Dashboard akan terbuka di browser Anda secara otomatis.

Fitur Dashboard
1. Filter Data. Pengguna dapat memfilter data berdasarkan musim, kondisi cuaca, atau waktu tertentu.
2. Visualisasi Data. Menampilkan grafik tren peminjaman sepeda berdasarkan berbagai faktor.
3. Insight Interaktif. Menampilkan insight terkait pola peminjaman sepeda dalam berbagai kondisi.

Analisis yang Dilakukan
1. Bagaimana pengaruh kondisi cuaca terhadap jumlah peminjaman sepeda?
2. Bagaimana pola peminjaman sepeda berdasarkan waktu (jam, hari kerja, dan musim)?

Insight Utama
- Peminjaman sepeda meningkat saat cuaca cerah dan selama musim tertentu.
- Ada pola peminjaman yang lebih tinggi pada jam sibuk (pagi dan sore hari).
