import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# Load data
day_df = pd.read_csv("day.csv")
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df = pd.read_csv("hour.csv")

# Judul Dashboard
st.title("Dashboard Peminjaman Sepeda - Bike Sharing Dataset")

# Sidebar filter
st.sidebar.header("Filter Data")
selected_season = st.sidebar.multiselect("Pilih Musim", options=day_df['season'].unique(), default=day_df['season'].unique())
selected_workingday = st.sidebar.multiselect("Pilih Hari Kerja", options=day_df['workingday'].unique(), default=day_df['workingday'].unique())

# Filter data berdasarkan musim dan hari kerja
filtered_df = day_df[(day_df['season'].isin(selected_season)) & (day_df['workingday'].isin(selected_workingday))]

# Mapping label cuaca dan musim
filtered_df['kondisi_cuaca'] = filtered_df['weathersit'].map({1: 'Cerah', 2: 'Berawan', 3: 'Hujan/Snow', 4: 'Hujan Lebat'})
filtered_df['label_musim'] = filtered_df['season'].map({1: 'Semi', 2: 'Panas', 3: 'Gugur', 4: 'Dingin'})

# Pertanyaan 1: Pengaruh Kondisi Cuaca
st.subheader("Peminjaman Sepeda Berdasarkan Kondisi Cuaca")
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.boxplot(data=filtered_df, x='kondisi_cuaca', y='cnt', palette='coolwarm', ax=ax1)
ax1.set_xlabel("Kondisi Cuaca")
ax1.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig1)

# Pertanyaan 2: Pola Peminjaman Berdasarkan Jam
st.subheader("Rata-rata Peminjaman Sepeda per Jam")
fig2, ax2 = plt.subplots(figsize=(10, 4))
sns.lineplot(data=hour_df, x="hr", y="cnt", estimator="mean", ci=None, marker="o", ax=ax2)
ax2.set_xlabel("Jam")
ax2.set_ylabel("Rata-rata Peminjaman")
st.pyplot(fig2)

# Pertanyaan 2: Pola Peminjaman Berdasarkan Hari Kerja
st.subheader("Peminjaman Sepeda Berdasarkan Hari Kerja")
fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.boxplot(data=filtered_df, x="workingday", y="cnt", palette="viridis", ax=ax3)
ax3.set_xlabel("Hari Kerja (0=Libur, 1=Hari Kerja)")
ax3.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig3)

# Pertanyaan 2: Peminjaman Berdasarkan Musim
st.subheader("Peminjaman Sepeda Berdasarkan Musim")
fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.barplot(data=filtered_df, x="label_musim", y="cnt", ci=None, palette="magma", ax=ax4)
ax4.set_xlabel("Musim")
ax4.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig4)

# Insight Tambahan: Tren Harian dengan Moving Average
st.subheader("Tren Peminjaman Sepeda Harian dengan Moving Average")
filtered_df['cnt_MA7'] = filtered_df['cnt'].rolling(window=7).mean()
fig5, ax5 = plt.subplots(figsize=(10, 5))
ax5.plot(filtered_df['dteday'], filtered_df['cnt'], label="Harian", color='lightblue')
ax5.plot(filtered_df['dteday'], filtered_df['cnt_MA7'], label="Rata-rata 7 Hari", color='red')
ax5.xaxis.set_major_locator(mdates.MonthLocator())
ax5.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45)
ax5.set_title("Tren Peminjaman Sepeda Harian")
ax5.set_xlabel("Tanggal")
ax5.set_ylabel("Jumlah Peminjaman")
ax5.legend()
st.pyplot(fig5)