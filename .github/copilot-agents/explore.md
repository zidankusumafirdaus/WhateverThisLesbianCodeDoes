# Agent: Explore

## Deskripsi
Melakukan analisis codebase cepat tanpa menambah context ke conversation utama. Ideal untuk Q&A tentang kode tanpa mengganggu flow kerja.

## Kapan Digunakan
- Memahami struktur kode atau modul tertentu
- Mencari file atau fungsi spesifik
- Membaca dokumentasi kode
- Q&A tentang perilaku eksisting
- Investigasi cepat tanpa deep-dive

## Input yang Disarankan
1. Pertanyaan spesifik tentang kode
2. Scope pencarian (file/folder target)
3. Tingkat detail yang diinginkan (quick/medium/thorough)
4. Konteks atau batasan pencarian

## Output yang Diharapkan
- Ringkasan findings dengan daftar lokasi file
- Penjelasan singkat tentang fungsionalitas
- Link atau referensi ke kode relevan
- Rekomendasi untuk deep-dive jika perlu

## Contoh Penggunaan
```
Pertanyaan: Bagaimana cara authentication flow bekerja di project ini?
Tingkat detail: medium
Target: apps/services/, apps/routes/
```

## Best Practices
- Gunakan untuk pencarian cepat dan explorasi awal
- Specify tingkat detail untuk hasil yang lebih relevan
- Combine dengan agent lain (Task, General purpose) untuk action items
- Simpan output penting ke notes atau dokumentasi
