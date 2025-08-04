# 📄 LinkedIn Job Postings Dataset - Analysis & Insights

Dataset ini berisi kumpulan lowongan pekerjaan dari LinkedIn yang dikumpulkan secara berkala, dan digunakan dalam proyek ini untuk eksplorasi dan analisis tren pekerjaan, keterampilan, dan permintaan pasar tenaga kerja berdasarkan deskripsi lowongan.

---

## 📁 Dataset
- **Nama File**: `postings.csv`
- **Sumber**: [Kaggle - LinkedIn Job Postings by Arsh Konatam](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)
- **Ukuran**: ~500MB+ (dapat berubah tergantung update)
- **Lisensi**: Untuk penggunaan edukasi dan non-komersial (cek detail di halaman Kaggle)

---

## 🧾 Isi Dataset (Kolom Penting)
Beberapa kolom penting dalam `postings.csv` antara lain:
- `title` : Judul pekerjaan
- `company` : Nama perusahaan
- `location` : Lokasi pekerjaan
- `description` : Deskripsi pekerjaan (teks panjang)
- `extensions` : Metadata tambahan (misalnya jenis kerja, industri, dll.)
- `via` : Sumber pengiklanan
- `job_id` : ID unik setiap posting

---

## 🎯 Tujuan Proyek
Proyek ini bertujuan untuk:
- Menganalisis tren pasar tenaga kerja berdasarkan deskripsi dan metadata lowongan.
- Mengekstrak kata kunci populer dari job description (NLP & wordcloud).
- Memberikan rekomendasi **upskilling** untuk jobseeker muda berdasarkan keterampilan yang sering muncul.

---

## 📊 Analisis yang Direncanakan
- **Eksplorasi distribusi pekerjaan** berdasarkan lokasi dan perusahaan.
- **Text mining** pada kolom `description` untuk menemukan keterampilan yang sering diminta.
- **Wordcloud** & frekuensi kata untuk menampilkan keyword populer.
- Rekomendasi skill/upskilling berdasarkan hasil ekstraksi data.

---

## 📦 Cara Mengakses Dataset
Karena ukuran dataset melebihi batas GitHub (>100MB), kamu bisa mengunduh dataset manual di:
👉 [https://www.kaggle.com/datasets/arshkon/linkedin-job-postings](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)

Setelah itu, simpan file `postings.csv` di direktori `data/` proyek ini.

---

## ⚠️ Catatan
- Data ini dikumpulkan melalui scraping, jadi validitas dan keakuratannya tidak dijamin 100%.
- Gunakan data ini hanya untuk **keperluan riset, edukasi, dan eksplorasi data.**

---

## 📬 Kontak
Untuk pertanyaan, kolaborasi, atau diskusi, silakan hubungi melalui Issues atau [email](mailto:youremail@example.com).

