---
name: token-efficient-output
description: "Use when: Responding to user queries or design requests; optimizing agent output for minimal token consumption while maintaining correctness. Enforces Phase 1 (compact, 300–500 tokens) by default, Phase 2 (extended content) only on explicit request. Use for all analysis, recommendations, and decision-making responses."
model: Claude Haiku 4.5
constraints:
  - "Compact default: 300–500 tokens, no preamble"
  - "Structured data > prose (tables, matrices, checklists)"
  - "Ask before Phase 2 content (ADRs, runbooks, threat models)"
  - "No extra commentary; abbreviate P99, SLO, MTTR, →"
  - "Acceptance criteria in checklist format"
---

# Token-Efficient Output Skill

## Overview

Implements **Phase 1 (Compact) ↔ Phase 2 (Extended)** pattern for consistent, cost-aware agent responses across the repository.

## When to Use

- User asks for a recommendation, analysis, or decision
- Need to present 3+ options (conservative/balanced/innovative)
- Designing agents, skills, or prompts
- Proposing architecture, design patterns, or trade-offs
- Any multi-step analysis or planning task

## Core Pattern

### Phase 1: Compact Output (Default, 300–500 tokens)

Always start with Phase 1. Provide:

1. **Executive Summary** (1–3 sentences max)
   - State the recommendation directly
   - One key trade-off or rationale in parentheses
   - No lengthy context restating

2. **Structured Recommendation**
   - Decision matrix (table: option | pros | cons | effort | cost | risk)
   - **OR** bullet breakdown if <3 options
   - **OR** acceptance criteria checklist
   - Choose the most compact format for the situation

3. **Acceptance Criteria** (Checklist Format)
   - Functional (API behavior, data consistency, feature completeness)
   - Non-functional (P99 latency, uptime SLO, cost, security)
   - Testing (unit test coverage, E2E validation)
   - Security (compliance, data governance)

   ```markdown
   **Acceptance Criteria:**

   - [ ] Functional: API returns 200 with valid JWT
   - [ ] Non-functional: P99 latency <100ms
   - [ ] Non-functional: 99.9% uptime SLO
   - [ ] Testing: Unit tests cover 80%+
   - [ ] Security: Secrets in vault, not source control
   ```

4. **Next Steps** (With Ownership)
   - List ordered tasks
   - Assign owner (e.g., "Backend team", "Infra team")
   - Include acceptance criteria in parentheses
   - No narrative descriptions

   ```markdown
   **Next Steps:**

   1. Owner: Backend team — Implement OAuth2 flow (Unit tests, E2E auth validation)
   2. Owner: Infra team — Set up key vault (Tested failover, rotation policy)
   3. Owner: QA team — Security audit (OWASP Top 10 coverage)
   ```

5. **Phase 2 Prompt** (Ask Before Extended Content)
   - End with: "Would you like: [Option A? / Option B? / Option C?]"
   - Examples:
     - "Would you like: Detailed ADR? / Cost breakdowm? / Migration playbook?"
     - "Would you like: Threat model? / Scaling roadmap? / Training materials?"
     - "Would you like: Full implementation guide? / API contract? / Load-test results?"
   - Let user decide what extended content is needed

### Phase 2: Extended Content (On Explicit Request Only)

When user asks for Phase 2 content:

- **ADRs** — Full context, decision, alternatives, consequences, acceptance criteria
- **Runbooks** — Step-by-step deployment, troubleshooting, incident response
- **Threat Models** — Security vectors, mitigations, audit checklists
- **Cost Projections** — Detailed pricing, ROI, scaling costs
- **Training Materials** — Team onboarding, code walkthroughs, best practices
- **Implementation Guides** — Code samples, CI/CD config, integration patterns
- **API Contracts** — OpenAPI specs, request/response examples, error codes

---

## Output Template

```markdown
## [Title]

**Executive Summary:**
[1–3 sentences. Recommendation + key trade-off or rationale in parentheses.]

| Option       | Pros | Cons | Effort | Cost | Risk   |
| ------------ | ---- | ---- | ------ | ---- | ------ |
| Conservative | ...  | ...  | 2w     | $X   | Low    |
| Balanced     | ...  | ...  | 4w     | $Y   | Medium |
| Innovative   | ...  | ...  | 8w     | $Z   | High   |

**Acceptance Criteria:**

- [ ] Functional: [requirement]
- [ ] Non-functional: [SLO/performance target]
- [ ] Testing: [coverage/validation requirement]
- [ ] Security: [compliance/governance requirement]

**Next Steps:**

1. Owner: [team name] — [Task] ([Acceptance criteria])
2. Owner: [team name] — [Task] ([Acceptance criteria])
3. Owner: [team name] — [Task] ([Acceptance criteria])

---

**Would you like:** [Phase 2 Option A? / Option B? / Option C?]
```

---

## Conventions & Abbreviations

### Abbreviations to Use Consistently

| Term                    | Abbr          | Usage                          |
| ----------------------- | ------------- | ------------------------------ |
| Effort/Timeline         | 2w, 4w, 8w    | "Effort: 4w"                   |
| Cost                    | $             | "Cost: $500/mo"                |
| Percentile              | P99, P95, P50 | "P99 latency < 100ms"          |
| Service Level Objective | SLO           | "99.9% uptime SLO"             |
| Service Level Indicator | SLI           | "Request latency SLI"          |
| Mean Time To Recover    | MTTR          | "MTTR < 5m"                    |
| Arrow/Direction         | →             | "Development → Staging → Prod" |
| Increase                | ↑             | "Capacity ↑ 2x"                |
| Decrease                | ↓             | "Latency ↓ 50%"                |

### Style Rules

- **No preamble:** Skip "Here's the answer:", "In today's world...", "I will now..."
- **No verbose closing:** Skip "I hope this helps!", "Feel free to reach out!"
- **Rationale in parentheses:** "Use Redis. (Scales to 100K ops/sec; existing expertise.)"
- **Diagram captions 1 line max:** "Architecture: Multi-tier service mesh with canary deployment"
- **No redundant explanations:** State decision once; rationale only in parentheses

### Example: Compact Rationale

```
BEFORE (verbose):
"Redis is a distributed in-memory data structure store that is widely used for caching.
It offers high availability through replication and clustering. The main advantage is its
performance, which can support millions of operations per second..."

AFTER (compact):
"Use Redis. (Supports 1M ops/sec; auto-scaling via clustering; team has experience.)"
```

---

## Decision Matrix Examples

### 2–3 Options (Use Table)

| Option        | Pros                                | Cons                    | Effort | Cost    |
| ------------- | ----------------------------------- | ----------------------- | ------ | ------- |
| API Gateway   | Centralized routing, rate limiting  | Single point of failure | 3w     | $200/mo |
| Service Mesh  | Distributed, observability built-in | Operational complexity  | 5w     | $500/mo |
| Load Balancer | Simple, proven                      | Limited intelligence    | 1w     | $50/mo  |

### Single Recommendation (Use Paragraph or Bullet)

If only recommending one option (no trade-off needed):

```markdown
**Recommendation:**
Use PostgreSQL with logical replication. (ACID guarantees; team expertise; managed backups in cloud.)

- Read replicas for analytics
- Automatic failover via patroni
- Full-text search via pg_trgm
```

---

## Acceptance Criteria Examples

### Full Stack (All Categories)

```markdown
**Acceptance Criteria:**

- [ ] Functional: API returns 200 with valid JWT
- [ ] Functional: User role-based access enforced
- [ ] Functional: Session timeout after 1h inactivity
- [ ] Non-functional: P99 latency <150ms
- [ ] Non-functional: 99.95% uptime SLO
- [ ] Non-functional: Cost <$10/user/mo
- [ ] Testing: Unit test coverage ≥80%
- [ ] Testing: E2E tests cover happy path + 3 error cases
- [ ] Testing: Load test: 1K concurrent users
- [ ] Security: Secrets stored in vault (not source control)
- [ ] Security: All endpoints require mTLS
- [ ] Security: Audit log for all privileged actions
```

### Minimal (Key Requirements Only)

```markdown
**Acceptance Criteria:**

- [ ] Functional: Cron job exports daily reports
- [ ] Non-functional: P99 export time <5m
- [ ] Testing: 95%+ data accuracy verified
```

---

## Phase 2 Request Examples

### When User Asks for Details

```
User: "How should we implement OAuth2?"

Phase 1 (default):
[Executive summary] [Decision matrix] [Acceptance criteria] [Next steps]

Would you like: Detailed implementation guide? / API contract? / Security audit checklist?

---

User: "Yes, detailed implementation guide"

Phase 2:
[Full code samples] [Step-by-step deployment] [CI/CD integration] [Testing strategy]
```

---

## Token Budget & Validation

### Phase 1 Token Budget

- Executive summary: 20–50 tokens
- Decision matrix: 100–200 tokens (3 options × 4–5 columns)
- Acceptance criteria: 50–100 tokens
- Next steps: 50–100 tokens
- Phase 2 prompt: 20–30 tokens
- **Total: 300–500 tokens max**

### Validation Checklist

Before submitting Phase 1 response:

- [ ] Executive summary is 1–3 sentences (no context restatement)
- [ ] Decision matrix or bullet list used (no prose comparison)
- [ ] All options visible in one table (no page breaks or scrolling)
- [ ] Acceptance criteria in checklist format (no prose bullets)
- [ ] Next steps have owners and acceptance criteria in parentheses
- [ ] No "I will" or "Here's" preamble
- [ ] No closing pleasantries or redundant explanations
- [ ] Abbreviations used (P99, SLO, MTTR, →, ↑, ↓)
- [ ] One-line diagram captions if diagrams present
- [ ] Response <500 tokens total

---

## Integration with Repository

This skill is referenced in `.github/copilot-instructions.md` and enforced across:

- `.github/agents/*` — All custom agents must implement Phase 1/Phase 2 pattern
- `.github/skills/*` — All skill descriptions must follow abbreviation & structure rules
- `.github/prompts/*` — All prompts must use compact decision matrices

For token-efficiency rules across the entire repository, see [copilot-instructions.md](../copilot-instructions.md).
