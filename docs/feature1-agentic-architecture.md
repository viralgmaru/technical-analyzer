# Feature 1 — Indian Stock TA: Agents & Workflow

**Scope:** Feature 1 only — symbols in → OHLCV (scrape/API/CSV) → D/W/M analysis → patterns → setups → entry/exit + risk framing.  
**Stack:** Local Win10; .NET/C#/PostgreSQL/Azure-friendly; Python optional for quant.

---

## 1. Agent map (re-verified)

| Your need | Agent | Notes |
|-----------|-------|--------|
| **Where to get OHLCV** (NSE, broker, CSV, ToS-aware scrape fallback) | **`data-ingestion`** | Canonical CSV contract; source matrix; hands off to quality |
| OHLCV validation | `data-quality` | Pre-TA gate; → `alert-engine` / **`data-ingestion`** if source bad |
| Full TA, setups, mean reversion, breakouts, pivots, Fib, seasonality | `stock-analyst` | SuperTrend, pivots, win-rate discipline |
| Pine v5, alerts, anti-repaint | `pine-tradingview` | Phase 1 token cap |
| SEBI, scraping ToS, algo | `sebi-compliance` | Use early if ingestion is scrape-heavy |
| Sizing, leverage, VaR | `risk-manager` | → `alert-engine` on breaches |
| Notifications spec | `alert-engine` | Dedupe, severity, channels |
| Build pipelines, backtester | `senior-developer` | Implements ingestion spec from `data-ingestion` |
| RAG, multi-agent design | `custom-ai` | |
| System topology | `architect` | |
| Macro/geo context | `macro-analyst` | Optional overlay |
| FA overlay (P/E etc.) | `fundamental-analyst` | Optional |
| Sector context | `sector-analyst` | Optional |
| FA+sector+macro rank | `orchestrator` | Not TA-first for Feature 1 |
| Service SLOs | `performance-monitor` | After APIs ship |

**Agents do not replace:** executable ETL, broker keys, or legal sign-off on each data source.

---

## 2. Feature 1 workflow (TA-first)

```
data-ingestion (source + CSV/API design) → ingest job (your code)
    → data-quality (≥70 score) → stock-analyst (D/W/M + pattern hypotheses)
    → risk-manager → sebi-compliance
Parallel: sebi-compliance on scrape/TV/screener/StockEdge/Trendlyne plans
Optional: pine-tradingview | macro-analyst
Alerts: alert-engine ← data-quality | risk-manager | ingestion failures
```

**Recovery loop:** `data-quality` rejects feed → handoff **`data-ingestion`** to pick NSE/broker/CSV path.

---

## 3. Repo agent changelog

| Change | Reason |
|--------|--------|
| `data-ingestion.agent.md` | Dedicated ingestion + CSV contract + source matrix |
| `data-quality` handoff | **Fix Ingestion Path** → `data-ingestion` |
| `alert-engine` | Alerts for quality/risk |
| `stock-analyst` | SuperTrend, Pine handoff, win-rate discipline |
| `pine-tradingview` | Token constraints, TV win % caveat |

---

## 4. Token efficiency (all agents)

1. Structured I/O: JSON or tables.  
2. Indicators/patterns in **code**; LLM gets summaries.  
3. `tiktoken` / HF tokenizer; cap context, trim old bars.  
4. RAG for long docs — not full paste.

---

## 5. Build steps (local)

| Phase | Deliverable |
|-------|-------------|
| A | **Canonical CSV** (see `data-ingestion` agent): symbol, date, OHLCV, timeframe, source, adjusted? |
| B | **Ingestion** per `data-ingestion` (NSE/broker/CSV first) |
| B′ | **Quality** checks aligned with `data-quality` |
| C | Indicators + pattern rules + backtester + WFO |
| D | LLM layer: `features_json` + RAG |
| E | UI/CLI; extension = client to your API |

---

## 6. LLM training?

**No** foundation training required v1. General LLM + RAG + structured outputs; fine-tune only with large labeled outcomes later.

---

*Feature 2 (screeners, scheduled universe export) out of scope here.*
