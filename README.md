# VINIX7 Internship – Analisis Pengangguran & Kebutuhan Pasar Kerja

Repositori ini berisi hasil tugas selama 4 minggu dalam program **VINIX7 Summer Internship**, mencakup dua topik besar:

1. **Week 1–2**: Analisis pengangguran dan partisipasi angkatan kerja di Indonesia (data BPS)
2. **Week 3–4**: Ekstraksi skill dari deskripsi lowongan kerja LinkedIn (text mining)

---

## 🧩 Bagian I – Week 1 & 2: Pengangguran & Angkatan Kerja (Data BPS)

### 🎯 Fokus
Mengangkat isu strategis: **Tingkat Pengangguran Terbuka (TPT)** dan **Tingkat Partisipasi Angkatan Kerja (TPAK)**, serta dampaknya terhadap pertumbuhan ekonomi Indonesia menjelang 2050.

### 📊 Dataset
- **Sumber**: BPS 2023  
- **Tautan**: [TPT & TPAK per Provinsi](https://www.bps.go.id/id/statistics-table/3/V2pOVWJWcHJURGg0U2pONFJYaExhVXB0TUhacVFUMDkjMyMwMDAw/)
- **Kolom**: `Provinsi`, `TPT`, `TPAK`

### 🧹 Pembersihan
- Penyesuaian format numerik (koma → titik)
- Penghapusan duplikasi & nilai kosong
- Disimpan sebagai `tpt_tpak_2023.csv`

### 📈 Visualisasi (Week 2)
- Bar chart per provinsi
- Scatter plot: TPT vs TPAK
- Heatmap provinsi dengan risiko tinggi

### 📢 Insight Utama
- Terdapat hubungan negatif antara TPT dan TPAK
- Beberapa provinsi menunjukkan mismatch SDM
- Insight digunakan untuk menyarankan kebijakan intervensi tenaga kerja

---

## 🧠 Bagian II – Week 3 & 4: Analisis Lowongan LinkedIn (Text Mining)

### 🎯 Fokus
Melakukan **eksplorasi teks** dari deskripsi lowongan kerja online untuk mengidentifikasi **keterampilan yang paling sering dibutuhkan industri**.

### 📄 Dataset
- **Sumber**: Kaggle  
- **Tautan**: [LinkedIn Job Postings](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)
- **File utama**: `postings.csv`

### ⚙️ Proses
- Preprocessing: lowercase, hapus simbol, stopwords, dll.
- Pisahkan teks deskripsi kerja vs keterampilan
- Visualisasi menggunakan **2 WordCloud**:
  - Kata dominan dari `description`
  - Kata dominan dari `skills`

### 📢 Insight
- Industri banyak menuntut **kemampuan digital, komunikasi, dan analisis data**
- Hasil ini membuka peluang untuk menyusun program **upskilling berbasis demand pasar**

---
