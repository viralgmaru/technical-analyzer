---
name: token-efficiency-quick-start
description: "Use when: Creating a new agent or skill in the repository; need to understand how to apply token-efficiency rules quickly; implementing Phase 1/Phase 2 pattern for the first time."
---

# Token-Efficiency Quick Start Guide

## One-Page Summary

| What                     | Rule                               | Example                                                                          |
| ------------------------ | ---------------------------------- | -------------------------------------------------------------------------------- |
| **Default Response**     | 300–500 tokens (Phase 1)           | Executive summary + matrix + checklist + next steps                              |
| **Extended Content**     | Only on explicit request (Phase 2) | "Would you like: Detailed ADR? / Threat model? / Implementation guide?"          |
| **Options Presentation** | Always use a table                 | 3-column matrix: option \| pros \| cons \| effort \| cost \| risk                |
| **Acceptance Criteria**  | Checklist format, not prose        | `- [ ] Functional: ...` / `- [ ] Non-functional: ...`                            |
| **Commentary**           | Minimal; rationale in parentheses  | "Use Redis. (1M ops/sec; team expertise.)" not "Redis is widely used because..." |
| **Abbreviations**        | Consistent across repo             | P99, SLO, MTTR, → instead of writing them out                                    |
| **Next Steps**           | With ownership & criteria          | `1. Owner: Team — Task (Acceptance criteria)`                                    |
| **Diagrams**             | 1-line captions max                | "Architecture: Multi-tier with canary deployment"                                |

---

## Checklist: Using These Rules

### When Creating a New Agent

```yaml
---
description: "[Agent purpose] — Implements token-efficient output skill"
model: Claude Haiku 4.5
tools: [read, edit, search, web, todo]
constraints:
  - "Phase 1 default: 300–500 tokens, no preamble"
  - "Use tables/matrices instead of prose for options"
  - "Ask before generating extended content (ADRs, runbooks)"
  - "Abbreviate: P99, SLO, MTTR, → (see .github/copilot-instructions.md)"
  - "Acceptance criteria in checklist format"
---
```

### When Creating a New Skill

```yaml
---
name: my-skill-name
description: "Use when: [specific task]; follows token-efficient-output pattern. Phase 1 (compact, 300–500 tokens) default; Phase 2 (extended docs) on explicit request."
constraints:
  - "Compact output always (300–500 tokens)"
  - "Decision matrices for all options"
  - "Ask before generating Phase 2 content"
---
```

### When Responding (Any Agent/Skill)

1. **Lead with Executive Summary** (1–3 sentences)

   ```
   Topic: [Recommendation]. (Key rationale: [trade-off or driver].)
   ```

2. **Present Options in a Table** (if 2+ options)

   ```markdown
   | Option | Pros | Cons | Effort | Risk   |
   | ------ | ---- | ---- | ------ | ------ |
   | A      | ...  | ...  | 2w     | Low    |
   | B      | ...  | ...  | 4w     | Medium |
   ```

3. **List Acceptance Criteria** (Checklist)

   ```markdown
   **Acceptance Criteria:**

   - [ ] Functional: ...
   - [ ] Non-functional: ...
   - [ ] Testing: ...
   ```

4. **Assign Next Steps** (With Owners)

   ```markdown
   **Next Steps:**

   1. Owner: [Team] — [Task] ([Criteria])
   ```

5. **Ask for Phase 2** (Optional)
   ```
   Would you like: [Option A? / Option B? / Option C?]
   ```

---

## Abbreviations Reference

Copy/paste this for consistent usage across all agents:

```
P99/P95/P50 = Percentile latency
SLO/SLI = Service Level Objective/Indicator
MTTR = Mean Time To Recover
→ = Direction or arrow (use in timelines)
↑ = Increase (capacity, performance)
↓ = Decrease (latency, cost)
$ = Cost or price
2w/4w/8w = Weeks of effort
CRUD = Create/Read/Update/Delete
API = Application Programming Interface
HA = High Availability
MVP = Minimum Viable Product
```

---

## Real-World Examples

### Example 1: Architecture Decision

**Good (Compact)**

```markdown
## Caching Layer

**Executive Summary:**
Deploy Redis cluster. (Reduces P99 from 500ms → 50ms; supports 1M ops/sec; team has expertise.)

| Option    | Pros            | Cons                 | Effort | Risk   |
| --------- | --------------- | -------------------- | ------ | ------ |
| In-Memory | Fast, simple    | Single node, no HA   | 1w     | High   |
| Redis     | HA, scalable    | Ops overhead         | 3w     | Medium |
| CDN       | Global, managed | Complex invalidation | 2w     | Low    |

**Acceptance Criteria:**

- [ ] Functional: Cache hit rate >80%
- [ ] Non-functional: P99 <50ms
- [ ] Non-functional: Failover <5s
- [ ] Testing: Load test with 100K keys

**Next Steps:**

1. Owner: Infra — Deploy Redis cluster (Staging validation, prod backup tested)
2. Owner: Backend — Integrate cache-aside logic (Unit + integration tests)
3. Owner: QA — Verify cache coherence (Concurrent read/write validation)

---

**Would you like:** Cost breakdown? / Scaling playbook? / Failover runbook?
```

**Bad (Verbose)**

```markdown
## Caching Strategy Recommendation

Hello! I've analyzed your requirements and have some thoughts on caching strategies.
As you probably know, caching is a critical component of modern distributed systems...

Option 1: In-Memory Caching
This approach uses an in-memory cache on each application server. The benefit is that
it's very fast because data is stored in RAM. However, it has some limitations...
```

### Example 2: Decision Matrix (3 Options)

**Good:**
| Option | Agility | Ops Cost | Complexity | Team Fit | Effort |
|--------|---------|----------|------------|----------|--------|
| Monolith | Low | Low | Low | Easy ramp | 4w |
| Services | High | Medium | Medium | Moderate | 8w |
| Serverless | Very high | Medium | High | Advanced | 12w |

**Bad:**
"Monolith is simple but lacks agility. Services provide good balance but require ops knowledge. Serverless is modern but has a steep learning curve..."

---

## When to Ask for Phase 2

### Good Triggers

- "Can you elaborate on [topic]?"
- "I need the detailed implementation"
- "Show me the ADR for this decision"
- "How do we handle the failover scenario?"
- "Create a runbook for this"

### Agent Response Template

```
**Would you like:**
- Detailed ADR with full context & consequences?
- Implementation guide with code samples & CI/CD?
- Threat model & security audit checklist?
- Cost projections & ROI analysis?
- Migration & rollback playbooks?
```

---

## Validation: Before Submitting

- [ ] Response is under 500 tokens (Phase 1)
- [ ] No preamble ("Here's my answer", "I will now")
- [ ] Decision matrix used for 2+ options (not paragraphs)
- [ ] All options visible in one table
- [ ] Acceptance criteria in `- [ ]` checklist format
- [ ] Next steps have owners assigned
- [ ] Abbreviations used (P99, SLO, MTTR, →)
- [ ] Diagram captions are 1 line max
- [ ] Rationale in parentheses (not separate paragraphs)
- [ ] Phase 2 prompt included ("Would you like...?")

---

## Files to Reference

- **Repository rules:** [.github/copilot-instructions.md](../copilot-instructions.md)
- **Full skill guide:** [.github/skills/token-efficient-output/SKILL.md](../skills/token-efficient-output/SKILL.md)
- **Example agent:** [.github/agents/custom-ai.agent.md](../agents/custom-ai.agent.md)

---

## Support

If you're creating a new agent or skill:

1. Copy the constraints section from this guide into your frontmatter
2. Follow the output template structure (exec summary → matrix → criteria → next steps)
3. Test Phase 1 response: Should be <500 tokens
4. Test Phase 2 request: "Would you like X?" triggers extended content
5. Validate checklist above before committing

For questions, refer to the full rules in `.github/copilot-instructions.md`.
