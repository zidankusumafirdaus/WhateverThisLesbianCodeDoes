# Agent: Research

## Deskripsi
Melakukan deep research mendalam di codebase, repository relevan, dan web. Menghasilkan laporan detail dengan citations dan referensi.

## Kapan Digunakan
- Investigasi teknologi atau architectural decisions
- Benchmark dan perbandingan opsi tools/libraries
- Root cause analysis untuk bugs kompleks
- Best practices research untuk use case spesifik
- Performance optimization investigation
- Security vulnerability research
- Cost/benefit analysis untuk major changes

## Input yang Disarankan
1. Pertanyaan riset yang jelas dan spesifik
2. Scope penelitian (codebase, external, web)
3. Kriteria evaluasi / concerns utama
4. Constraints atau limitasi (teknologi, biaya, waktu)
5. Context bisnis atau technical background
6. Tingkat kedalaman yang diharapkan

## Output yang Diharapkan
- Ringkasan executive summary
- Detailed findings dengan breakdown
- Perbandingan opsi (pros/cons)
- Citations dan referensi ke sumber
- Rekomendasi berdasarkan findings
- Action items atau next steps
- Links ke dokumentasi atau resources

## Contoh Penggunaan
```
Research Topic: Optimal caching strategy untuk API
Concerns: Performance, memory usage, staleness tolerance
Scope: Codebase patterns + industry best practices
Constraints: Must work dengan existing database
Deliverable: Recommendation dengan implementation approach
```

## Best Practices
- Berikan context yang cukup untuk research yang targeted
- Specify constraints yang penting (teknologi, budget, timeline)
- Ask untuk perbandingan trade-offs, bukan hanya opsi
- Request citations untuk klaim penting
- Combine dengan Task agent untuk proof-of-concept jika diperlukan
- Document research findings untuk referensi mendatang

## Research Domains
- Architecture & Design Patterns
- Performance & Optimization
- Security & Compliance
- Tools & Libraries Evaluation
- Cost & Scalability Analysis
- Best Practices & Standards
- Troubleshooting & Root Cause Analysis

## Integrasi dengan Workflow
- **Explore**: Gathering existing code patterns sebagai baseline
- **General purpose**: Input untuk architectural decisions
- **Task**: Implement proof-of-concept atau prototype
- **Code review**: Validate research recommendations dalam code
