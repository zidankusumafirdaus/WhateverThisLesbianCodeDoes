# Copilot Agents Documentation

Folder ini berisi dokumentasi detail untuk setiap Copilot agent yang tersedia di project.

## Struktur File

- **explore.md** - Agent untuk quick codebase analysis dan Q&A
- **task.md** - Agent untuk eksekusi commands (tests, builds, automation)
- **general.md** - Agent untuk complex multi-step tasks
- **code-review.md** - Agent untuk code review dan quality gates
- **research.md** - Agent untuk deep research dan investigation
- **rubber-duck.md** - Agent untuk feedback konstruktif dan validation

## Perbandingan Cepat

| Agent | Use Case | Speed | Complexity | Context Impact |
|-------|----------|-------|-----------|-----------------|
| **Explore** | Understanding code | ⚡ Very fast | Low | Minimal |
| **Task** | Running commands | ⚡ Fast | Low-Medium | None |
| **General** | Implementation | 🚀 Medium | High | Full isolation |
| **Code review** | Review changes | 🚀 Medium | Medium | Focused |
| **Research** | Investigation | 🐢 Slow | High | Full isolation |
| **Rubber duck** | Feedback | 🚀 Medium | Medium | None |

## Workflow Patterns

### Feature Implementation
```
Explore → Research → Rubber duck → General → Task → Code review
```
1. Explore existing patterns
2. Research best practices
3. Get feedback on approach (rubber duck)
4. Implement solution (general)
5. Run tests/build (task)
6. Code review sebelum merge

### Bug Investigation
```
Explore → Research → Rubber duck → General → Task
```
1. Explore code yang affected
2. Research root cause
3. Validate fix approach
4. Implement fix
5. Run tests

### Quick Changes
```
Explore → Task → Code review
```
1. Understand context
2. Run tests
3. Review changes

### Architecture Decision
```
Research → Rubber duck → General
```
1. Research opsi dan trade-offs
2. Get feedback on approach
3. Implement atau prototype

## Tips & Best Practices

### Maximize Efficiency
- **Use Explore first** untuk understanding code sebelum action items
- **Batch related tasks** untuk agent yang sama
- **Leverage isolation** dari General dan Research agents untuk complex work
- **Document findings** untuk future reference

### Minimize Context Pollution
- General dan Research agents berjalan di isolated context
- Gunakan untuk complex tasks yang mungkin generate banyak intermediate steps
- Main conversation tetap clean dan focused

### Quality & Confidence
- Use Rubber duck untuk validate approach sebelum big investments
- Use Code review untuk catch issues sebelum merge
- Combine agents untuk comprehensive workflow
- Document decisions dan rationale

## Related Documentation

- **Main agents guide**: [../copilot-agents.md](../copilot-agents.md)
- **Project workflow**: Lihat project README untuk development workflow
