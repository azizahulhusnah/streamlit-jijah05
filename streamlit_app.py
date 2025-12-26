import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# TITLE
# =========================
st.title("Tugas Pertemuan 12 - Streamlit Web App")

# =========================
# HEADER
# =========================
st.header("Pengenalan Streamlit")

# =========================
# SUBHEADER
# =========================
st.subheader("Apa itu Streamlit?")

# =========================
# TEXT (PARAGRAF)
# =========================
st.text(
    "Streamlit adalah library Python yang digunakan untuk membuat aplikasi web "
    "interaktif dengan cepat, khususnya untuk data science dan machine learning. "
    "Dengan Streamlit, kita dapat menampilkan teks, tabel, grafik, dan berbagai "
    "komponen interaktif hanya dengan beberapa baris kode."
)

# =========================
# CAPTION
# =========================
st.caption("Contoh aplikasi sederhana menggunakan Streamlit")

# =========================
# CODE (POTONGAN CODE)
# =========================
st.subheader("Contoh Potongan Kode Streamlit")
st.code(
    """
import streamlit as st

st.title("Hello Streamlit")
st.write("Ini adalah contoh aplikasi Streamlit sederhana")
    """,
    language="python"
)

# =========================
# DATA DISPLAY - DATAFRAME
# =========================
st.subheader("Contoh Data Mahasiswa")

data = {
    "Nama": ["Andi", "Budi", "Citra", "Dewi", "Eka"],
    "Umur": [20, 21, 22, 20, 23],
    "Nilai": [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)

st.write("Tabel Data Mahasiswa:")
st.dataframe(df)

# =========================
# DATA DISPLAY - CHART
# =========================
st.subheader("Grafik Nilai Mahasiswa")

fig, ax = plt.subplots()
ax.bar(df["Nama"], df["Nilai"])
ax.set_xlabel("Nama")
ax.set_ylabel("Nilai")
ax.set_title("Grafik Nilai Mahasiswa")

st.pyplot(fig)
