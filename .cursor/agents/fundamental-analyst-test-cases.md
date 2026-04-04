# Fundamental Analyst Agent - Validation Test Cases

## Purpose

Test cases to validate the Fundamental Analyst Agent's FA_Rating calculation, output format, and analytical accuracy.

---

## Test Case 1: High Quality Blue Chip Stock

### Input Data

**Company:** Reliance Industries Limited (RELIANCE)
**Current Price:** 2,850 INR
**Market Cap:** 18,50,000 Cr INR
**Shares Outstanding:** 65 Cr

**Financial Metrics (Latest FY):**

- Revenue: 7,85,000 Cr INR (+8% YoY)
- EBITDA: 1,42,000 Cr INR
- Net Income: 68,000 Cr INR (+11% YoY)
- EPS: 104.6 INR
- Operating Margin: 18.2%
- Net Margin: 8.7%
- Free Cash Flow: 72,000 Cr INR (positive + growing)

**Balance Sheet:**

- Total Debt: 1,20,000 Cr INR
- Total Equity: 4,50,000 Cr INR
- Current Assets: 2,80,000 Cr INR
- Current Liabilities: 2,15,000 Cr INR
- Interest Expense: 8,500 Cr INR

**Valuation Metrics:**

- P/E Ratio: 22x
- P/B Ratio: 2.1x
- P/FCF: 25.7x
- EV/EBITDA: 12.8x
- PEG Ratio: 1.2x

**Peer Comparison (Sector Average):**

- Peers: TCS, INFY, WIPRO (IT), HUL, ITC (FMCG), HDFC Bank, ICICI Bank
- Sector P/E Median: 24x
- Sector P/B Median: 2.4x
- Sector ROE: 11.2%
- Sector D/E: 0.50x
- Sector Rev CAGR (3yr): 7.5%
- Sector EPS CAGR (3yr): 9.2%

**Qualitative Factors:**

- Business Model: Diversified (energy, refining, petrochemicals, retail, telecom, digital)
- Competitive Advantage: Strong moat, integrated operations, scale
- Management: Experienced, track record of value creation
- Governance: Best-in-class, institutional investor favorite
- Industry Trends: Energy transition ongoing, refining margins cyclical

**Calculation Metrics:**

| Metric             | Value | Calculation                              |
| ------------------ | ----- | ---------------------------------------- |
| ROE                | 15.1% | Net Income / Avg Equity = 68000 / 450000 |
| ROA                | 8.2%  | Net Income / Avg Assets                  |
| ROCE               | 13.4% | EBIT / Invested Capital                  |
| Revenue CAGR (3yr) | 8.0%  | Blended growth                           |
| EPS CAGR (3yr)     | 11.0% | Earnings growth                          |
| Debt/Equity        | 0.27x | 120000 / 450000                          |
| Current Ratio      | 1.30x | 280000 / 215000                          |
| Interest Coverage  | 16.7x | EBIT / Interest = 118000 / 8500          |
| Accruals Ratio     | 0.05  | Low (good earnings quality)              |

---

### Expected Output

**[STOCK ANALYSIS] Stock: RELIANCE | FA_Rating: 8.2/10**

**Valuation: 8/10**

> P/E 22x (vs sector avg 24x) - slightly undervalued
> P/B 2.1x (vs peer avg 2.4x) - fair value
> PEG ratio 1.2x (vs historical 1.5x) - attractive
> EV/EBITDA 12.8x - in line with quality peers

**Profitability: 8/10**

> ROE 15.1% (vs sector 11.2%) - outperforming peers
> Operating margin 18.2% (stable 3+ years)
> Profit growth +11% YoY (consistent and sustainable)
> ROCE 13.4% (above cost of capital ~9%)

**Growth: 7/10**

> Revenue growth +8% YoY (steady but not accelerating)
> Earnings growth +11% YoY (CAGR 11% over 3yr)
> Market share in core businesses stable
> Refining capex moderating; telecom growth maturing

**Financial Health: 9/10**

> Debt/Equity 0.27x (low; vs sector 0.50x) - fortress balance sheet
> Current ratio 1.30x (healthy liquidity)
> Interest coverage 16.7x (very safe)
> FCF positive and growing (72000 Cr INR)
> No covenant risk; investment grade credit

**Composite FA_Rating: 8.2/10 [EXCELLENT]**

**Rationale:**

- Strong ROE and margin durability with scale advantages
- Low leverage and excellent cash generation ability
- Valuation modestly cheaper than peers on quality-adjusted basis
- Growth stable but not accelerating; refining/telecom maturing
- Best-in-class governance and management execution

**Red Flags:**

- Capex requirements rising for energy transition; monitor FCF impact
- Refining margins cyclical; geopolitical/crude price sensitivity
- Telecom competition intense; margin compression risk
- Earnings quality excellent but one-time items minimal (risk when needed)

**Recommended Actions:**

- Rating: HOLD for long-term investors
- Accumulate on 5-10% dips (target entry ~2500-2650)
- Monitor: Q1 results for capex guidance, refining margin trends

---

## Test Case 2: High Growth Mid-Cap with Valuation Risk

### Input Data

**Company:** Happiest Minds Technologies (HAPPSTMNDS)
**Current Price:** 850 INR
**Market Cap:** 28,900 Cr INR
**Shares Outstanding:** 3.4 Cr

**Financial Metrics (Latest FY):**

- Revenue: 2,450 Cr INR (+32% YoY)
- EBITDA: 380 Cr INR
- Net Income: 185 Cr INR (+48% YoY)
- EPS: 54.4 INR
- Operating Margin: 15.5%
- Net Margin: 7.6%
- Free Cash Flow: 120 Cr INR (positive but declining as % of revenue)

**Balance Sheet:**

- Total Debt: 0 Cr INR (debt-free)
- Total Equity: 920 Cr INR
- Current Assets: 780 Cr INR
- Current Liabilities: 520 Cr INR
- Interest Expense: 0 Cr INR

**Valuation Metrics:**

- P/E Ratio: 36.5x (vs LTM historical 28x)
- P/B Ratio: 4.2x
- P/FCF: 52.3x
- EV/EBITDA: 24.5x
- PEG Ratio: 1.7x

**Peer Comparison (IT Services/Tech Mid-cap Average):**

- Peers: HCL Tech, Mindtree, Wipro (comparables)
- Sector P/E Median: 24x
- Sector P/B Median: 2.8x
- Sector ROE: 12.5%
- Sector D/E: 0.05x (tech companies low leverage)
- Sector Rev CAGR (3yr): 12-14%
- Sector EPS CAGR (3yr): 15-18%

**Qualitative Factors:**

- Business Model: IT consulting, digital transformation (high growth niche)
- Competitive Advantage: Specialized offerings, strong client retention (92%)
- Management: Experienced but founder-led; execution risk
- Governance: Good disclosures, but some related-party transactions flagged
- Industry Trends: Digital transformation boom, strong demand for IT services

**Calculation Metrics:**

| Metric             | Value    | Calculation                         |
| ------------------ | -------- | ----------------------------------- |
| ROE                | 20.1%    | Net Income / Avg Equity = 185 / 920 |
| ROA                | 18.5%    | High asset efficiency               |
| ROCE               | 20.1%    | EBIT / Invested Capital (no debt)   |
| Revenue CAGR (3yr) | 28%      | Strong growth                       |
| EPS CAGR (3yr)     | 35%      | Even faster earnings growth         |
| Debt/Equity        | 0.0x     | Debt-free                           |
| Current Ratio      | 1.50x    | 780 / 520                           |
| Interest Coverage  | Infinity | No debt                             |
| Accruals Ratio     | 0.18     | Moderate (working capital growing)  |
| FCF/Revenue        | 4.9%     | Declining from 6-7% historically    |

---

### Expected Output

**[STOCK ANALYSIS] Stock: HAPPSTMNDS | FA_Rating: 6.8/10**

**Valuation: 4/10**

> P/E 36.5x (vs sector 24x) - significantly overvalued
> P/B 4.2x (vs peer avg 2.8x) - expensive on book value
> PEG ratio 1.7x (>1.0 threshold) - growth not justifying premium
> EV/EBITDA 24.5x (vs sector 18x) - stretched multiple

**Profitability: 9/10**

> ROE 20.1% (vs sector 12.5%) - strong capital efficiency
> Operating margin 15.5% (improving 3-yr trend)
> Profit growth +48% YoY (exceptional)
> ROCE 20.1% (well above cost of capital)

**Growth: 9/10**

> Revenue growth +32% YoY (CAGR 28% over 3yr)
> Earnings growth +48% YoY (CAGR 35% over 3yr)
> Market share expanding in digital services niche
> Talent retention strong (92% client retention)

**Financial Health: 8/10**

> Debt/Equity 0.0x (debt-free) - fortress balance sheet
> Current ratio 1.50x (healthy)
> No debt service risk
> FCF positive but declining as % of revenue (4.9% vs historical 6-7%)
> Working capital growing faster than FCF

**Composite FA_Rating: 6.8/10 [MODERATE]**

**Rationale:**

- Exceptional growth and profitability metrics; market leader in niche
- Debt-free balance sheet provides optionality and safety
- Valuation stretched significantly above peers despite growth premium
- FCF conversion declining; working capital expanding faster than cash generation
- Management execution strong but founder-led concentration risk

**Red Flags:**

- P/E 36.5x vs sector 24x - paying 50% premium for growth (risky if growth slows)
- PEG 1.7x indicates valuation not justified by growth alone at current prices
- FCF/Revenue declining (working capital strain) - monitor cash flow quality
- Founder-dependent; succession planning not transparent
- Related-party transactions flagged in governance audit (low risk but worth monitoring)
- High growth rates may not sustain; any miss could trigger sharp re-rating

**Recommended Actions:**

- Rating: HOLD (do not add at current levels)
- Consider on 20-25% correction (target entry ~640-680)
- Wait for Q1 results to assess FCF trajectory and capex plans
- Monitor: Founder/management changes, client concentration, margin trends

**Valuation Alert:**
Growth story is real, but price has likely run ahead of fundamentals. Asymmetric risk/reward favors waiting for better entry or proof of sustained growth + FCF improvement.

---

## Test Case 3: Value Trap / Deteriorating Quality Stock

### Input Data

**Company:** Yes Bank Limited (YESBANK)
**Current Price:** 19.5 INR
**Market Cap:** 15,000 Cr INR
**Shares Outstanding:** 77 Cr

**Financial Metrics (Latest FY, Post-Restructuring):**

- Revenue: 6,800 Cr INR (-15% YoY; recovering from stress)
- EBITDA: 1,200 Cr INR (depressed)
- Net Income: 450 Cr INR (turnaround yr; still below pre-crisis levels)
- EPS: 5.84 INR (highly volatile)
- Operating Margin: 17.6% (inflated; excluding stress provisions)
- Net Margin: 6.6% (below industry standards)
- Free Cash Flow: 120 Cr INR (restricted by regulatory capital requirements)

**Balance Sheet:**

- Total Debt (Total Liabilities): 95,000 Cr INR (deposits + borrowings)
- Total Equity: 20,000 Cr INR (capital raised post-reconstruction)
- Capital Ratio: 12.5% (regulatory minimum 10.5%; tight)
- Current Leverage (Deposits/Equity): 4.75x
- Stressed Assets: 3.2% of portfolio (reducing but still elevated)
- Provisions Coverage: 72% (vs industry 150%+)

**Valuation Metrics:**

- P/E Ratio: 25.2x (vs peer avg 18x)
- P/B Ratio: 0.75x (below 1.0 - distressed)
- Price/Deposits: 0.16x
- Price/Assets: 0.12x (significantly below book)
- PEG Ratio: N/A (earnings unstable, turnaround phase)

**Peer Comparison (Private Sector Banks):**

- Peers: HDFC Bank, ICICI Bank, Axis Bank, Kotak Bank
- Sector P/E Median: 18-20x
- Sector P/B Median: 3.5-4.0x
- Sector ROE: 17-20%
- Sector D/E: 4.0-5.0x
- Sector NPL Ratio: 1.0-1.5%
- Sector Provision Coverage: 150-180%

**Qualitative Factors:**

- Business Model: Retail banking + corporate (recovery post-near-collapse)
- Competitive Advantage: Damaged brand; customer trust rebuilding
- Management: New MD/CEO; restructuring underway
- Governance: Regulatory oversight tight; multiple compliance issues flagged
- Industry Trends: Rising rates favorable for NIM, but credit growth challenges

**Calculation Metrics:**

| Metric                    | Value   | Calculation                           |
| ------------------------- | ------- | ------------------------------------- |
| ROE                       | 2.3%    | Net Income / Avg Equity = 450 / 20000 |
| ROA                       | 0.48%   | Extremely low; capital trapped        |
| Cost of Deposits          | 5.2%    | Rising; NIM compression risk          |
| Deposit Growth            | +8% YoY | Improving but still volatile          |
| Stressed Assets           | 3.2%    | Declining from 6%+ but elevated       |
| Provision Coverage        | 72%     | Very low; regulatory concern          |
| Capital Ratio             | 12.5%   | Minimal buffer; dividend uncertain    |
| NIM (Net Interest Margin) | 3.8%    | Below pre-crisis 4.5%+ levels         |
| Accruals Ratio            | 0.35    | High (quality concerns)               |
| Forecast ROE (2yr)        | 8-10%   | Best case scenario                    |

---

### Expected Output

**[STOCK ANALYSIS] Stock: YESBANK | FA_Rating: 3.2/10**

**Valuation: 5/10**

> P/E 25.2x (vs sector 18x) - expensive despite distress
> P/B 0.75x (vs peer 3.5x) - below book but earnings unreliable
> Price/Deposits 0.16x (vs sector 0.35-0.40x) - suspicious low valuation
> Valuation appears cheap BUT earnings quality severely compromised

**Profitability: 2/10**

> ROE 2.3% (vs sector 18%) - abysmal returns on capital
> ROA 0.48% (vs sector 1.5%+) - capital trapped in distressed assets
> Operating margin 17.6% (artificial; excludes true credit costs)
> Profit highly volatile; turnaround timeline uncertain (3-5 years minimum)

**Growth: 2/10**

> Revenue -15% YoY (contraction due to customer exodus)
> EPS highly volatile; positive but not repeatable
> Deposit growth +8% YoY (improving but fragile)
> Loan growth negative; portfolio quality under pressure
> Earnings recovery dependent on stressed asset resolution (uncertain timeline)

**Financial Health: 2/10**

> Capital Ratio 12.5% (minimal; regulatory minimum 10.5%)
> Stressed Assets 3.2% (declining but still elevated; vs sector 1%)
> Provision Coverage 72% (critically low; vs sector 150%+)
> Leverage 4.75x deposits/equity (acceptable but fragile given distress)
> Dividend unlikely for 2-3 years (capital preservation critical)

**Composite FA_Rating: 3.2/10 [POOR - AVOID]**

**Rationale:**

- Bank emerged from near-collapse restructuring; recovery uncertain
- ROE/ROA severely depressed; capital productivity at crisis levels
- Stressed asset portfolio still large; resolution timeline multi-year
- Regulatory capital buffer minimal; dividend risk high
- Earnings quality poor due to one-time restructuring effects
- Valuation appears cheap but fundamentals justify it (value trap)

**Red Flags:**

- ROE 2.3% vs sector 18% - massive underperformance persists 5 years post-rescue
- Provision coverage 72% (vs sector 150%+) - additional provisions likely; earnings at risk
- Stressed Assets 3.2% - while improving, still 3x sector average
- Regulatory scrutiny continues; compliance issues ongoing
- Management credibility still rebuilding; execution risk remains
- Deposits fragile (high cost, potential outflows if sentiment deteriorates)
- Dividend sustainability at ZERO - likely 2-3 more years minimum before resumption
- Valuation appears cheap but is a classic value trap; cheap for fundamental reasons

**Recommended Actions:**

- Rating: AVOID / REDUCE
- Not suitable for fundamental value investors (not undervalued; value trap)
- Only for turnaround specialists with 5-10yr horizon and high risk tolerance
- Downside risk if stressed assets deteriorate further; upside limited until ROE reaches 10%+

**Key Monitoring Metrics:**

- Stressed asset resolution pace
- Provision coverage ratio (must reach 120%+ for safety)
- Deposit growth sustainability
- Capital ratio trends
- ROE trajectory (target: reach 10%+ by FY2028 for credible story)
- Regulatory forbearance withdrawal timeline

---

## Test Criteria Validation Checklist

### Test Case 1: RELIANCE (High Quality)

- [ ] FA_Rating emerges in 7.5-8.5 range (composite excellent)
- [ ] Valuation_Score: 7-9 (cheap vs quality)
- [ ] Profitability_Score: 8-9 (strong ROE, margins)
- [ ] Growth_Score: 6-7 (steady, not accelerating)
- [ ] FinHealth_Score: 8-9 (low leverage, strong FCF)
- [ ] Output includes peer comparison context
- [ ] Red flags are realistic and actionable
- [ ] Rationale balances positives and negatives

### Test Case 2: HAPPSTMNDS (High Growth, OV)

- [ ] FA_Rating emerges in 6.0-7.5 range (moderate; expensive)
- [ ] Valuation_Score: 3-5 (overvalued despite growth)
- [ ] Profitability_Score: 8-9 (excellent)
- [ ] Growth_Score: 8-9 (strong CAGR)
- [ ] FinHealth_Score: 7-8 (debt-free but FCF declining)
- [ ] PEG explicitly flagged as >1.0 (growth-not-justified signal)
- [ ] Working capital trend highlighted
- [ ] Recommends waiting for better entry

### Test Case 3: YESBANK (Value Trap)

- [ ] FA_Rating emerges in 2.5-3.5 range (poor; clearly avoid)
- [ ] Valuation_Score: 4-6 (cheap for wrong reasons)
- [ ] Profitability_Score: 1-3 (terrible ROE/ROA)
- [ ] Growth_Score: 1-3 (negative/volatile)
- [ ] FinHealth_Score: 1-3 (capital buffer thin, stressed assets high)
- [ ] Clearly labels as VALUE TRAP (cheap but deteriorating)
- [ ] Provision coverage ratio highlighted as critical
- [ ] Turnaround timeline candid (3-5 years minimum)
- [ ] Avoids false optimism; realistic risk assessment

---

## Acceptance Criteria for Agent Validation

Agent passes validation if:

1. **FA_Rating Formula** - Composite score correctly weighted (0.30+0.30+0.20+0.20)
2. **Component Scoring** - Each 0-10 score reflects input data accurately
3. **Output Format** - Matches Example Output structure (ratings, rationale, red flags, actions)
4. **Peer Context** - Always compares to sector medians; explains relative position
5. **Quality Signal** - ROE, margins, FCF quality explicitly assessed
6. **Red Flag Detection** - Deterioration signals, leverage, earnings quality caught
7. **Valuation Reasoning** - PEG, multiples relative to growth always explained
8. **Actionable Advice** - Holds/accumulates/reduces with target entry prices
9. **Realism** - Acknowledges turnarounds take years; tempers irrational exuberance
10. **Consistency** - Same metrics drive scores consistently across test cases

---

## Usage Instructions

### For QA/Testing:

1. Run Agent with Test Case 1 input → Verify output matches Expected Output (within 0.3 rating variance)
2. Run Agent with Test Case 2 input → Verify overvaluation flagged, PEG >1.0 surfaced
3. Run Agent with Test Case 3 input → Verify value trap identified, avoid recommendation given

### For Product Demo:

1. Present Test Case 1 to show agent's analytical capability on quality blue-chips
2. Present Test Case 2 to show overvaluation detection on high-growth names
3. Present Test Case 3 to show value trap avoidance on deteriorating quality

### For Continuous Monitoring:

- Rerun these test cases quarterly to ensure agent output consistency
- Track if agent flags emerging red flags before they become crises (e.g., YESBANK stress)
- Validate PEG calculations and component scoring logic
