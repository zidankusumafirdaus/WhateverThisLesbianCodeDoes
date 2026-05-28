# Agent: General purpose

## Deskripsi
Handle tugas-tugas kompleks multi-step yang memerlukan full toolset dan reasoning berkualitas tinggi. Berjalan di context terpisah untuk keep main conversation tetap fokus.

## Kapan Digunakan
- Implementasi fitur baru yang kompleks
- Refactor kode besar atau cross-module
- Fix bug yang melibatkan multiple layers
- Optimization tasks
- Architecture decisions dan planning
- Troubleshooting issues yang melibatkan banyak komponen

## Input yang Disarankan
1. Deskripsi masalah atau fitur yang detail
2. Acceptance criteria / requirements
3. File atau modul yang terpengaruh
4. Constraints atau limitations
5. Acceptance tests atau validasi
6. Context atau background yang penting

## Output yang Diharapkan
- Solusi lengkap dengan kode siap pakai
- Penjelasan approach dan trade-offs
- Ringkasan perubahan file
- Testing strategy
- Known limitations atau future improvements
- Catatan untuk review

## Contoh Penggunaan
```
Tugas: Implementasi role-based access control (RBAC) di API
Acceptance Criteria:
- User hanya bisa akses resource sesuai role
- Admin bisa manage permissions
- Audit log untuk permission changes
File Target: apps/controllers/, apps/services/
Tests Expected: Unit tests + integration tests
```

## Best Practices
- Describe tugas dengan context lengkap
- Batasi scope agar execution cepat
- Provide acceptance criteria yang jelas
- Specify file/modul yang terpengaruh
- Request testing strategy
- Ask untuk summary of changes sebelum approval

## Kombinasi dengan Agent Lain
- **Explore**: Research sebelum dimulai untuk memahami existing code
- **Task**: Jalankan build/tests setelah implementasi selesai
- **Code review**: Review output dari general purpose agent
- **Research**: Deep-dive investigation sebelum complex tasks
