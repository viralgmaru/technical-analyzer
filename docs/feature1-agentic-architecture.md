# Feature 1 — Indian Stock TA Tool: Agent Coverage & Agentic Architecture

**Scope:** First feature only (symbol(s) in → validated OHLCV → multi-timeframe TA → patterns → setups → entry/exit with risk framing).  
**Stack alignment:** Local-first on Windows 10; .NET/C#/PostgreSQL/Azure-friendly; optional Python for quant/backtest.

---

## 1. Agent inventory vs your Feature 1 needs

| Need | Primary agent(s) | Fit |
|------|------------------|-----|
| OHLCV validation, gaps, cross-source sanity | `data-quality` | Strong (NSE/TV/screener context) |
| Candlestick & chart patterns, indicators, R:R, entry/stop/target, swing/intraday/position framing | `stock-analyst` | Strong (broad TA + strategies + backtest *guidance*) |
| SEBI/data-source compliance for scraping & bots | `sebi-compliance` | Strong |
| Position sizing, leverage, concentration | `risk-manager` | Strong |
| System design, scraping options, Azure/local topology | `architect` | Strong |
| Implementation (.NET/Python), backtester code, pipelines | `senior-developer` | Strong |
| Custom agents, RAG, LangGraph-style workflows | `custom-ai` | Strong |
| **Not Feature 1 core:** FA, sector ranks, macro composite | `fundamental-analyst`, `sector-analyst`, `macro-analyst`, `orchestrator` | Useful *overlay* after TA; orchestrator weights are **FA-heavy**, not TA-first |
| Runtime SLOs for *your* APIs/jobs | `performance-monitor` | Relevant once you ship services |

**Verdict:** The set **covers most** of Feature 1 for *analysis and engineering guidance*. It does **not** replace: (a) **your own data pipeline** (NSE bhavcopy, broker API, paid vendor), (b) a **deterministic backtest engine** in code, (c) **legal clearance** for each site’s ToS.

---

## 2. Gaps — new agents, edits, or workflows

### 2.1 Missing or weak in current prompts

| Gap | Recommendation |
|-----|----------------|
| **Pine Script** | Extend `stock-analyst` (or add `pine-tradingview.agent.md`): Pine v5 syntax, `request.security`, limitations vs broker execution, repainting, strategy vs indicator. |
| **Pivot points** (classic/Fib/Camarilla) | Add explicit section to `stock-analyst` or tiny `pivot-levels` subsection: formulas + confluence with S/R. |
| **“70–80% win rate” claims** | Add **disclaimer block** to `stock-analyst`: pattern stats are regime- and sample-dependent; require **your** backtest/out-of-sample; forbid overfitted headline rates without methodology. |
| **Scraping implementation detail** | Optional `data-ingestion.agent.md`: NSE bhavcopy/archived candles, broker APIs, rate limits, robots.txt/ToS, fallback to CSV contract. |
| **Broken handoffs** | `data-quality` and `risk-manager` reference **`alert-engine`** — agent file **not present**. Add `alert-engine.agent.md` **or** repoint handoffs to `senior-developer` / remove until built. |

### 2.2 Orchestrator note

`orchestrator` composite = `0.40*FA + 0.30*Sector + 0.20*Macro + 0.10*Quality`. For Feature 1, use a **TA-first mini-orchestrator** in app logic or a short playbook:

`Data_Quality → Stock_Analyst → Risk_Manager → SEBI_Compliance` (optional: Macro for context only).

---

## 3. What agents cannot do by themselves

- **Scrape** TradingView/NSE/Screener/StockEdge/Trendlyne reliably without you handling auth, ToS, anti-bot, and maintenance.
- **Guarantee** win rates; only **your** labeled data + backtest + walk-forward can estimate edge.
- **Act as** a SEBI-registered analyst in the legal sense — they are **decision-support**, not regulated advice.

**Practical data path (recommended):** NSE historical/bhavcopy + corporate actions, or **broker/vendor API** → store in PostgreSQL → export CSV for ad-hoc tools → optional scrape only where allowed.

---

## 4. Token-efficient operations (all agents & sub-agents)

Use consistently:

1. **Structured I/O:** JSON schema or fixed tables for outputs (symbol, timeframe, pattern, entry, stop, targets, confidence, caveats).
2. **Phase 1 / Phase 2:** Compact default; long narrative only on request (already in several agents).
3. **Chunking:** Send last *N* candles + indicator *summary*, not raw 10y OHLCV in prompt.
4. **Tool-first for numbers:** Indicators, pattern detection, and backtests in **code** (C#/Python); LLM interprets **precomputed** features.
5. **Model routing:** Small/fast model for classification (“bullish/neutral/bearish”); larger model only for synthesis.
6. **Embeddings:** For docs (pattern catalog, SEBI notes, Pine reference), use RAG; don’t paste full manuals into context.

**Tokenizer (implementation):** For OpenAI-compatible APIs use **`tiktoken`** (count before send); for local Hugging Face models use the model’s **`tokenizer.encode`**; target **max input budget** per call (e.g. 4–8k tokens) and trim oldest bars first.

---

## 5. Step-by-step architecture (local Phase 1)

### Phase A — Data contract (week 1–2)

- Define **canonical CSV/Excel columns:** `symbol,date,open,high,low,close,volume,timeframe,source,adjusted?`
- Implement **ingestion + validation** (reuse rules mentally aligned with `data-quality`).
- Store in **PostgreSQL** (hypertable optional later).

### Phase B — Quant core (weeks 2–6)

- **Indicators:** TA-Lib / Pandas TA / custom C# — RSI, MACD, BB, SMA/EMA, ATR, pivots, Fib levels from swing highs/lows.
- **Patterns:** Start with **rule-based** candlestick + 5–10 chart patterns; log detected events to DB.
- **Backtester:** Event-driven or vectorized; fees, slippage, NSE session rules; walk-forward splits. Agents advise; **code owns truth**.

### Phase C — LLM / agent layer (parallel)

- **RAG corpus:** Your pattern notes, risk checklist, SEBI summary, Pine cheat sheet (after you add it).
- **Vector DB local:** Chroma, Qdrant, LanceDB, or pgvector in PostgreSQL.
- **Flow:** `features_json + last_k_bars_summary + user_question` → LLM → structured trade plan.
- **Local LLMs:** Ollama / LM Studio (e.g. Llama 3.x, Qwen, Mistral); Azure OpenAI later.

### Phase D — Product shell

- **CLI or minimal WPF/Blazor** “upload CSV → report PDF/Excel”.
- **Chrome extension (later):** Only if you have a **stable API** behind it; extension calls localhost or your backend, not heavy scraping in-page.

### Phase E — Governance

- Every automated “recommendation” log: data version, strategy version, disclaimer.
- Run **`sebi-compliance`** + **`risk-manager`** on templates before publishing user-facing text.

---

## 6. Suggested agentic workflows (copy-paste playbooks)

**Workflow 1 — Single stock deep dive**  
1. `data-quality`: validate series + score.  
2. If score &lt; 70: stop or fetch alternate source.  
3. `stock-analyst`: multi-timeframe setups, entry/stop/target, R:R.  
4. `risk-manager`: position size vs your capital.  
5. `sebi-compliance`: disclaimers, data-source notes.

**Workflow 2 — Strategy / backtest review**  
1. `senior-developer`: implement or review backtest code.  
2. `stock-analyst`: critique overfitting, suggest robustness tests.  
3. `sebi-compliance`: algo/disclosure if needed.

**Workflow 3 — System build**  
1. `architect`: local → Azure evolution, boundaries.  
2. `senior-developer`: repos, APIs, DB.  
3. `custom-ai`: agent prompts, RAG, evaluation.

---

## 7. Do you need to “create an LLM”?

**No** for your goals. Use **general-purpose** local or hosted LLMs + **your data and code** for fidelity. Train/fine-tune only if you later have **large labeled datasets** (e.g. pattern outcomes); start with **RAG + structured outputs**.

---

## 8. Checklist before scaling to cloud (Year 2+)

- [ ] Single source of truth for prices + corporate actions  
- [ ] Reproducible backtests (commit hash + data snapshot id)  
- [ ] Rate limits and secrets in Key Vault  
- [ ] Audit log for any user-facing recommendation  
- [ ] Fix or add `alert-engine` handoffs  

---

## 9. Document maintenance

Re-verify **NSE data policies**, **SEBI algo/circular updates**, and **vendor ToS** periodically; agents are static text — **legal and market rules change**.

---

*Generated for Feature 1 planning; Feature 2 (screeners, scheduled jobs, universe export) intentionally out of scope here.*
