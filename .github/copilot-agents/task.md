# Agent: Task

## Deskripsi
Mengeksekusi perintah seperti tests, builds, dan automation tasks. Memberikan ringkasan hasil sukses dan output lengkap saat failure.

## Kapan Digunakan
- Menjalankan test suite
- Build project
- Deploy atau setup awal
- Automation tasks (lint, format, generate, etc)
- Validasi environment setup

## Input yang Disarankan
1. Perintah atau task yang ingin dijalankan
2. Direktori kerja / scope
3. Parameter atau flag khusus
4. Kriteria success/failure
5. Expected output atau behavior

## Output yang Diharapkan
- Ringkasan hasil sukses (singkat)
- Output lengkap saat failure
- Error messages dengan konteks
- Log atau report yang relevan
- Rekomendasi perbaikan jika diperlukan

## Contoh Penggunaan
```
Task: Jalankan unit tests untuk Backend
Command: pytest tests/ -v
Expected: Semua tests harus PASS
Scope: Backend/
```

## Best Practices
- Berikan perintah yang jelas dan lengkap
- Specify expected outcome untuk validasi
- Kumpulkan output failures untuk analysis
- Combine dengan Explore agent untuk debugging
- Dokumentasikan task kompleks untuk referensi mendatang

## Common Tasks
- `pytest tests/` - Run Python tests
- `npm test` - Run JavaScript tests
- `npm run build` - Build frontend
- `python -m pytest --cov` - Tests dengan coverage report
