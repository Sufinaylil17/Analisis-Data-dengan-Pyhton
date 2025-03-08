import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="Dashboard Bike Sharing", layout="wide")

# Load dataset
day_df = pd.read_csv("day.csv")

# Pastikan kolom 'dteday' dalam format datetime
day_df["dteday"] = pd.to_datetime(day_df["dteday"])

# Konversi nilai musim ke nama musim
season_mapping = {1: "Musim Semi", 2: "Musim Panas", 3: "Musim Gugur", 4: "Musim Dingin"}
day_df["season"] = day_df["season"].map(season_mapping)

# Konversi kondisi cuaca ke nama kategori
weather_mapping = {1: "Cerah", 2: "Berawan", 3: "Panas", 4: "Hujan"}
day_df["weathersit"] = day_df["weathersit"].map(weather_mapping)

# Judul dashboard
st.title("🚲 Dashboard Analisis Peminjaman Sepeda")

# --- Sidebar untuk filter ---
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim", ["All"] + list(day_df["season"].unique()))
selected_weather = st.sidebar.selectbox("Pilih Cuaca", ["All"] + list(day_df["weathersit"].unique()))

# Filter data berdasarkan pilihan pengguna
filtered_df = day_df.copy()
if selected_season != "All":
    filtered_df = filtered_df[filtered_df["season"] == selected_season]
if selected_weather != "All":
    filtered_df = filtered_df[filtered_df["weathersit"] == selected_weather]

# --- Visualisasi Data ---

# 1️⃣ **Jumlah peminjaman per bulan**
st.subheader("📊 Jumlah Peminjaman Sepeda per Bulan")
filtered_df["month"] = filtered_df["dteday"].dt.month
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=filtered_df["month"], y=filtered_df["cnt"], palette="coolwarm", ax=ax)
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_xticks(range(1, 13))
ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"])
st.pyplot(fig)

# 2️⃣ **Jumlah peminjaman berdasarkan musim**
st.subheader("🍂 Jumlah Peminjaman Sepeda berdasarkan Musim")
season_counts = filtered_df.groupby("season")["cnt"].sum().reset_index()
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x="season", y="cnt", data=season_counts, palette="viridis", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Peminjaman")
st.pyplot(fig)

# 3️⃣ **Pengaruh Cuaca terhadap Peminjaman**
st.subheader("🌦️ Pengaruh Cuaca terhadap Peminjaman Sepeda")
weather_counts = filtered_df.groupby("weathersit")["cnt"].sum().reset_index()
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x="weathersit", y="cnt", data=weather_counts, palette="magma", ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Total Peminjaman")
st.pyplot(fig)

# 4️⃣ **Tampilkan data yang sudah difilter**
st.subheader("📄 Data Peminjaman Sepeda (Filtered)")
st.dataframe(filtered_df)

# Footer
st.markdown("---")
st.caption("© 2025 Bike Sharing Analysis | Dibuat dengan ❤️ oleh Anda")
