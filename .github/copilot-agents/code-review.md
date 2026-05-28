# Agent: Code review

## Deskripsi
Review perubahan dengan fokus pada genuine issues saja, meminimalkan noise dan false positives. Output review yang berkualitas dan actionable.

## Kapan Digunakan
- Before merge / pull request review
- Setelah implementasi fitur selesai
- Security review untuk fitur sensitif
- Performance review untuk critical paths
- API contract changes
- Database schema changes

## Input yang Disarankan
1. Ringkasan perubahan (apa & mengapa)
2. Daftar file yang berubah
3. Perbandingan before/after (context)
4. Area yang sensitive/berisiko (security, auth, data)
5. Testing yang sudah dilakukan
6. Acceptance criteria yang diharapkan

## Output yang Diharapkan
- Daftar genuine issues (bukan style nitpicks)
- Severity level untuk setiap issue (critical/high/medium/low)
- Contoh spesifik dengan line numbers
- Rekomendasi perbaikan
- Approval atau rejection dengan reasoning
- Edge cases atau scenarios yang missed

## Contoh Penggunaan
```
Review Request: Authentication middleware changes
Files Changed: apps/middleware/auth.py, apps/routes/auth_routes.py
Sensitive Areas: Password handling, token validation, CORS
Test Coverage: Unit tests included? Integration tests?
Risk Areas: Can this break existing auth flow?
```

## Best Practices
- Fokus pada genuine issues, bukan style/formatting (gunakan linter untuk itu)
- Highlight security concerns, logic errors, dan performance issues
- Berikan contoh spesifik dan context untuk setiap feedback
- Consider edge cases dan error handling
- Check untuk breaking changes atau backward compatibility
- Verify acceptance criteria sudah tercapai
- Request clarification jika ada ambiguity

## Issue Categories

### Critical
- Security vulnerabilities
- Data loss risks
- Breaking changes tanpa migration
- Logic errors yang affect core functionality

### High
- Performance regressions
- Error handling yang incomplete
- Missing validations
- Unhandled edge cases

### Medium
- Code clarity improvements
- Testing gaps
- Documentation needs
- Best practice violations

### Low
- Suggestions untuk future refactor
- Minor naming improvements
- Code style (if not enforced by linter)

## Integrasi dengan Workflow
- **Explore**: Pahami existing code sebelum review jika perlu
- **Task**: Jalankan tests untuk verify changes
- **General purpose**: Coordinate review findings untuk improvement proposals
