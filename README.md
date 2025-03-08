# Analisis-Data-dengan-Pyhton

Project ini bertujuan untuk menganalisis data peminjaman sepeda dan membangun dashboard interaktif menggunakan Streamlit. Analisis data dilakukan untuk memahami pola peminjaman sepeda berdasarkan waktu serta pengaruh kondisi cuaca terhadap jumlah peminjaman.

Dataset

Dataset yang digunakan dalam prject ini berisi informasi mengenai peminjaman sepeda dengan berbagai macam variabel seperti berikut ini:
- Datetime: Waktu peminjaman
- Season: Musim saat peminjaman terjadi
- Holiday: Apakah hari tersebut hari libur atau bukan
- Workingday: Indikasi apakah hari tersebut merupakan hari kerja
- Weather Condition: Kondisi cuaca saat peminjaman
- Temperature: Suhu dalam skala Celsius
- Humidity: Tingkat kelembaban
- Windspeed: Kecepatan angin
- Casual Users: Jumlah peminjam yang tidak memiliki langganan
- Registered Users: Jumlah peminjam yang memiliki langganan
- Total Users: Total jumlah peminjam

Instalasi dan Cara Menjalankan Dashboard
1. Pastikan Python telah terinstal di komputer Anda.
2. nstal dependensi dengan menjalankan perintah: pip install -r requirements.txt
3. Jalankan Streamlit dengan perintah: streamlit run dashboard/dashboard.py
4. Buka browser dan akses `http://localhost:8501` untuk melihat dashboard.

Fitur Dashboard
1. Filter Data. Pengguna dapat memfilter data berdasarkan musim, kondisi cuaca, atau waktu tertentu.
2. Visualisasi Data. Menampilkan grafik tren peminjaman sepeda berdasarkan berbagai faktor.
3. Insight Interaktif. Menampilkan insight terkait pola peminjaman sepeda dalam berbagai kondisi.

Analisis yang Dilakukan
- Bagaimana pengaruh kondisi cuaca terhadap jumlah peminjaman sepeda?
- Bagaimana pola peminjaman sepeda berdasarkan waktu (jam, hari kerja, dan musim)?

Insight Utama
- Peminjaman sepeda meningkat saat cuaca cerah dan selama musim tertentu.
- Ada pola peminjaman yang lebih tinggi pada jam sibuk (pagi dan sore hari).
