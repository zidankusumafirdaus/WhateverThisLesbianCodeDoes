# Agent: Rubber duck

## Deskripsi
Bertindak sebagai kritikus konstruktif untuk memberikan feedback mendalam pada non-trivial tasks. Membantu validate approach, identify blind spots, dan improve quality sebelum execution.

## Kapan Digunakan
- Sebelum memulai implementasi kompleks
- Validate design atau architecture decisions
- Get feedback pada approach atau strategy
- Identify potential issues atau edge cases
- Improve clarity atau efficiency dari plan
- Sanity check sebelum major refactor
- Post-mortem atau lessons learned discussions

## Input yang Disarankan
1. Problem statement atau task description
2. Proposed approach atau solution outline
3. Concerns atau areas yang uncertain
4. Constraints atau requirements
5. Existing patterns atau precedents
6. Questions atau specific areas untuk feedback

## Output yang Diharapkan
- Critical feedback pada approach
- Identified gaps atau missing considerations
- Edge cases atau risks yang might be missed
- Suggestions untuk improvement
- Alternative approaches untuk consideration
- Clarity atau confidence assessment
- Confidence level dan reasoning

## Contoh Penggunaan
```
Konteks: Implementasi real-time notification system
Proposed Approach: WebSocket + message queue + database polling
Concerns: Scalability, duplicate handling, connection management
Specific Questions: 
- How handle reconnections?
- What's fallback untuk browser yang tidak support WebSocket?
- How ensure message delivery?
```

## Best Practices
- Be specific tentang approach atau plan
- Ask untuk critical feedback, bukan validation saja
- Include context tentang constraints dan requirements
- Mention concerns yang sudah teridentifikasi
- Be open untuk challenging feedback
- Follow up dengan implementation atau refinement
- Document decisions yang dihasilkan dari session ini

## Tipe Feedback yang Diharapkan
- **Logical soundness**: Apakah approach logically valid?
- **Completeness**: Apa yang missing atau overlooked?
- **Edge cases**: What boundary conditions atau scenarios belum covered?
- **Performance**: Concern tentang scalability atau efficiency?
- **Maintainability**: Apakah solution sustainable dan understandable?
- **Alternatives**: Ada approach lain yang worth considering?
- **Risk assessment**: What could go wrong? Mitigation strategy?

## Integrasi dengan Workflow
- **Research**: Input untuk informed decision making
- **Explore**: Understanding existing patterns sebelum feedback
- **General purpose**: Refinement sebelum full implementation
- **Code review**: Post-implementation review untuk lessons learned

## Automatic Invocation
Rubber duck agent dapat dipanggil automatically oleh Copilot CLI untuk certain operations. Manual invocation selalu tersedia untuk explicit feedback request.
