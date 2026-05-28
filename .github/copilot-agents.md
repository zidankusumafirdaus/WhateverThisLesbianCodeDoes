# Panduan Peran Copilot

Dokumen ini membagi tugas ke beberapa peran Copilot agar pekerjaan lebih terstruktur, konsisten, dan mudah di-review.

## Ringkas Peran

| Peran | Fokus | Keluaran Utama |
| --- | --- | --- |
| **Coding** | Implementasi fitur/perbaikan bug | Kode siap digunakan + catatan perubahan |
| **Review** | Quality gate sebelum merge | Temuan bug/risiko + rekomendasi perbaikan |
| **Testing** | Validasi perilaku | Hasil tes + langkah reproduksi |
| **Docs** | Dokumentasi dan petunjuk | Doc yang update + contoh penggunaan |
| **Research** | Investigasi kebutuhan/opsi | Ringkasan temuan + referensi |

## Aturan Umum (Berlaku untuk semua peran)

1. Jelaskan tujuan singkat dan hasil yang diharapkan.
2. Berikan konteks file/endpoint/fitur yang relevan.
3. Batasi scope agar hasil cepat dan fokus.
4. Laporkan risiko, asumsi, dan batasan secara jelas.

## Copilot Coding

**Kapan digunakan**  
Saat perlu menambah fitur, memperbaiki bug, atau melakukan refactor terarah.

**Input yang disarankan**  
1. Tujuan fitur/perbaikan  
2. File atau folder target  
3. Kriteria penerimaan (acceptance criteria)  
4. Contoh request/response (jika API)

**Output yang diharapkan**  
Kodenya sudah disesuaikan, perilaku sesuai kriteria, dan ada ringkasan perubahan.

## Copilot Review

**Kapan digunakan**  
Setelah perubahan kode selesai, sebelum merge.

**Input yang disarankan**  
1. Ringkasan perubahan  
2. Daftar file yang berubah  
3. Area yang berisiko tinggi (auth, data, keamanan, performa)

**Output yang diharapkan**  
Temuan isu yang relevan (bug/logika/keamanan) beserta rekomendasi perbaikan.

## Copilot Testing

**Kapan digunakan**  
Untuk memastikan perubahan tidak merusak perilaku.

**Input yang disarankan**  
1. Skenario utama yang harus lulus  
2. Endpoint/fitur terkait  
3. Data uji yang diperlukan

**Output yang diharapkan**  
Hasil tes, langkah uji, dan daftar kegagalan (jika ada).

## Copilot Docs

**Kapan digunakan**  
Setelah fitur berubah atau ada cara pakai baru.

**Input yang disarankan**  
1. File dokumentasi target  
2. Perubahan perilaku/parameter/endpoint  
3. Contoh penggunaan baru

**Output yang diharapkan**  
Dokumentasi update, contoh request/response yang sesuai.

## Copilot Research

**Kapan digunakan**  
Saat butuh perbandingan opsi atau keputusan arsitektur.

**Input yang disarankan**  
1. Pertanyaan inti  
2. Batasan (waktu/teknologi/biaya)  
3. Kriteria keputusan

**Output yang diharapkan**  
Ringkasan temuan, opsi, dan rekomendasi singkat.

## Template Permintaan (Copy-Paste)

```
Peran: <Coding | Review | Testing | Docs | Research>
Tujuan:
Konteks:
Kriteria penerimaan:
File/Path target:
Contoh (opsional):
```
