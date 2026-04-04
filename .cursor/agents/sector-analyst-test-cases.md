# Sector Analyst Agent - Validation Test Cases

## Purpose

Test cases to validate the Sector Analyst Agent's Sector_Rating calculation, rotation signals, and analytical accuracy across NSE sectors.

---

## Test Case 1: Attractive Sector (IT - Rotation IN)

### Input Data

**Current Week (March 2026):**

| Metric                       | IT Sector | Nifty50 (Baseline) |
| ---------------------------- | --------- | ------------------ |
| YoY Earnings Growth          | +12%      | +8%                |
| P/E Ratio                    | 18x       | 24x                |
| P/B Ratio                    | 4.2x      | 3.0x               |
| FII Inflow (4-wk cumulative) | +2000 Cr  | Neutral            |
| DII Inflow (4-wk)            | Flat      | Flat               |

**4-Week Historical Baseline (Feb 2026):**

- Sector_Rating (4-wk avg): 6.5/10
- FII inflow (4-wk prior): -1500 Cr (selling)

**Regulatory Context:**

- PLI semiconductor scheme active (tailwind)
- RBI rate hikes ongoing (headwind)
- Data localization debate (minor headwind)

**Valuation History:**

- 6-month avg P/E: 20x
- 1-year high P/E: 22x
- 1-year low P/E: 16x
- Current 18x: 10% below 6-month avg

---

### Component Scoring

| Component        | Calculation                                               | Score |
| ---------------- | --------------------------------------------------------- | ----- |
| Growth_Score     | YoY 12% (+1 for forecast steady)                          | 7     |
| Valuation_Score  | P/E 18x vs 24x = 0.75x (75% of Nifty) + PEG favorable = 9 |
| Flow_Score       | FII +2000Cr = +3, DII flat = 0, momentum improving +1 = 7 |
| Regulatory_Score | PLI active (6-7) + rate headwind (-1) = 6                 |
| **Composite**    | (0.35*7)+(0.35*9)+(0.20*7)+(0.10*6) = **7.3/10**          |

---

### Expected Output

[SECTOR ANALYSIS] Sector: IT | Sector_Rating: 7.3/10

Growth: 7/10

> Sector growth: +12% YoY (vs Nifty50 +8%) - Outperforming
> Earnings growth: +14% YoY - Accelerating
> Forecast: +10% FY2027 (steady but slower)
> Headwind: Macro slowdown risk, client spending caution

Valuation: 9/10

> Sector P/E: 18x (vs Nifty50 24x) - 25% Undervalued
> P/B: 4.2x (vs sector hist avg 5.0x) - Attractive
> PEG ratio: 1.0x - Growth justifies valuation
> vs 6-month baseline: Trading 10% below avg (undervalued)

Fund Flows: 7/10

> FII inflow last 4 weeks: +2000 Cr - Strong reversal
> Prior 4 weeks: -1500 Cr (selling) -> Now +2000 Cr (buying)
> DII: Flat (no retail enthusiasm)
> Flow momentum: Improving significantly (rotation in signal)

Regulatory: 6/10

> PLI semiconductor scheme active - Tailwind for capex
> RBI rate hikes ongoing - Headwind (rate-sensitive sector)
> Data localization push - Minor headwind (offset by PLI)
> Policy signal: Net positive (PLI > rate headwind)

Composite Sector_Rating: 7.3/10 [ATTRACTIVE]

Rotation Signal: +0.8 (Mild rotation IN)

- Comparison: 4-week avg 6.5 vs current 7.3
- Interpretation: FII momentum reversing; institutional buyers re-entering
- Strength: New smart money accumulation after 8-week selling

Recommendation: ACCUMULATE

> Sector fundamentals improving; valuations attractive; FII positioning constructive
> Best picks in sector: TCS (quality, dividends), WIPRO (value), HCL (growth)
> Risk: Macro slowdown could derail client spending; guidance misses on margin pressure
> Monitor: FII flow consistency, client concentration, rupee movement

---

## Test Case 2: Deteriorating Sector (Metals - Rotation OUT)

### Input Data

**Current Week (March 2026):**

| Metric                       | Metals Sector | Nifty50 (Baseline) |
| ---------------------------- | ------------- | ------------------ |
| YoY Earnings Growth          | +2%           | +8%                |
| P/E Ratio                    | 6x            | 24x                |
| P/B Ratio                    | 0.8x          | 3.0x               |
| FII Inflow (4-wk cumulative) | -2000 Cr      | Neutral            |
| DII Inflow (4-wk)            | -500 Cr       | Neutral            |

**4-Week Historical Baseline (Feb 2026):**

- Sector_Rating (4-wk avg): 6.8/10
- FII inflow (prior period): -800 Cr (steady selling accelerating)

**Regulatory Context:**

- Export duty on steel/iron: 15% (headwind)
- Global steel prices declining (headwind)
- Domestic infrastructure spending moderating (headwind)

**Commodity Context:**

- Iron ore prices: Down 12% QoQ
- Global demand: China slowdown (weakness)
- Capacity utilization: 75% (below 80-85% optimal)

---

### Component Scoring

| Component        | Calculation                                                               | Score |
| ---------------- | ------------------------------------------------------------------------- | ----- |
| Growth_Score     | YoY 2% (very low growth) -> 1/10 - penalty for declining forecast = 0     |
| Valuation_Score  | P/E 6x vs 24x = 0.25x (only 25% of Nifty) BUT earnings questioned -> 8/10 |
| Flow_Score       | FII -2000Cr = -3, DII -500Cr = -1, momentum worsening -1 = 2/10           |
| Regulatory_Score | Export duty headwind (1-2) + global weakness (1-2) = 2/10                 |
| **Composite**    | (0.35*0)+(0.35*8)+(0.20*2)+(0.10*2) = **2.9/10**                          |

---

### Expected Output

[SECTOR ANALYSIS] Sector: Metals | Sector_Rating: 2.9/10 [AVOID]

Growth: 0/10

> Sector growth: +2% YoY (vs Nifty50 +8%) - Severe underperformance
> Earnings growth: Flat to negative (currency headwind)
> Forecast: -3% FY2027 (recession risk)
> Headwind: Global commodity cycle downturn, China weakness, domestic capex slowdown

Valuation: 8/10

> Sector P/E: 6x (vs Nifty50 24x) - Extremely cheap on paper
> P/B: 0.8x - Trading below book (distressed signal)
> BUT: Earnings likely to deteriorate further (value trap warning)
> Analysis: Valuation cheap for wrong reasons (earnings quality deteriorating)

Fund Flows: 2/10

> FII outflow last 4 weeks: -2000 Cr - Heavy selling
> Prior outflow: -800 Cr -> Accelerating to -2000 Cr
> DII also selling: -500 Cr (rare; indicates retail capitulation)
> Flow momentum: Deteriorating badly (rotation out signal)

Regulatory: 2/10

> Export duty 15% on steel: Direct margin pressure - Headwind
> Global steel prices declining 12% QoQ - Headwind
> Domestic infrastructure capex: Moderating after demand peak - Headwind
> Policy signal: Negative (multiple headwinds, no tailwind)

Composite Sector_Rating: 2.9/10 [AVOID]

Rotation Signal: -3.9 (Strong rotation OUT)

- Comparison: 4-week avg 6.8 vs current 2.9
- Interpretation: Sector fundamentals deteriorating; institutional exodus
- Strength of signal: Very strong; all indicators negative

Recommendation: AVOID / REDUCE

> Sector in downtrend; valuations cheap but deteriorating earnings
> This is a classic VALUE TRAP: cheap but getting cheaper
> Best action: Reduce exposure; wait for earnings stabilization (ETAs 6-9 months)
> Best picks if forced: Larsen & Toubro (engineering business cushion), NOT pure-play Tata Steel
> Risk: Further P/E compression likely if earnings miss; execution risk on cost cutting

Key Warning:
VALUE TRAP ALERT. Price reflects despair, but earnings cycle still deteriorating. Do NOT chase "cheap" valuations. Wait for growth inflection confirmation (positive guidance, commodity price bottom).

---

## Test Case 3: Balanced Sector (Pharma - Moderate Attraction)

### Input Data

**Current Week (March 2026):**

| Metric                       | Pharma Sector | Nifty50 (Baseline) |
| ---------------------------- | ------------- | ------------------ |
| YoY Earnings Growth          | +18%          | +8%                |
| P/E Ratio                    | 25x           | 24x                |
| P/B Ratio                    | 5.5x          | 3.0x               |
| FII Inflow (4-wk cumulative) | +800 Cr       | Neutral            |
| DII Inflow (4-wk)            | +400 Cr       | Neutral            |

**4-Week Historical Baseline (Feb 2026):**

- Sector_Rating (4-wk avg): 6.2/10
- FII inflow (prior): +200 Cr (steady but slow)

**Regulatory Context:**

- PLI scheme for pharma active (tailwind)
- USFDA approval pace: Accelerating (tailwind)
- Price controls on new drugs: Debate ongoing (neutral to minor headwind)
- Rupee depreciation: ~5% (strong tailwind for exports)

**Earnings Context:**

- Domestic demand: +8% YoY
- US export growth: +25% YoY (strong)
- Margin: Flat (offset by wage inflation & API cost)
- Guidance: Maintained for FY2027

---

### Component Scoring

| Component        | Calculation                                                           | Score |
| ---------------- | --------------------------------------------------------------------- | ----- |
| Growth_Score     | YoY 18% (strong)                                                      | 9/10  |
| Valuation_Score  | P/E 25x vs 24x = 1.04x BUT ROE high (6-7) + PEG 1.4 acceptable = 6/10 |
| Flow_Score       | FII +800Cr = +2, DII +400Cr = +1, momentum good (+1 momentum) = 6/10  |
| Regulatory_Score | PLI + USFDA (7-8) + price control risk (-1) = 7/10                    |
| **Composite**    | (0.35*9)+(0.35*6)+(0.20*6)+(0.10*7) = **6.85/10**                     |

---

### Expected Output

[SECTOR ANALYSIS] Sector: Pharma | Sector_Rating: 6.85/10 [MODERATE]

Growth: 9/10

> Sector growth: +18% YoY (vs Nifty50 +8%) - Strong outperformance
> Earnings growth: +20% YoY (US export strength)
> Forecast: +15% FY2027 (sustained strong growth)
> Tailwind: US demand robust, USFDA approvals accelerating, rupee weak

Valuation: 6/10

> Sector P/E: 25x (vs Nifty50 24x) - Marginally premium (104% of Nifty)
> P/B: 5.5x - Premium to Nifty (3.0x) but justified by 25% ROE vs 15% Nifty
> PEG: 1.4x (growth semi-premium but acceptable for pharma)
> vs historical: Trading near 5-year avg; not cheap but not expensive

Fund Flows: 6/10

> FII inflow last 4 weeks: +800 Cr - Steady accumulation
> Prior inflow: +200 Cr -> Acceleration to +800 Cr
> DII also involved: +400 Cr (retail + domestic HNI interest)
> Flow momentum: Improving steadily (no strong rotation but positive)

Regulatory: 7/10

> PLI scheme for pharma: Active, driving capex - Tailwind
> USFDA approvals accelerating: 12+ approvals FY2026 - Tailwind
> Price control debate: Potential headwind but low probability - Neutral to minor headwind
> Rupee depreciation (5%): Export margin boost - Tailwind
> Policy signal: Positive on PLI and USFDA; manageable on price controls

Composite Sector_Rating: 6.85/10 [MODERATE]

Rotation Signal: +0.65 (Mild rotation IN)

- Comparison: 4-week avg 6.2 vs current 6.85
- Interpretation: Growth story attractive; fund flows improving
- Strength: Balanced profile; low valuation risk despite premium multiple

Recommendation: HOLD / MODERATE ACCUMULATE

> Sector fundamentals strong but valuation requires growth confirmation
> Best picks: Cipla (value + dividend), Dr. Reddy (US strength), Biocon (margin expansion)
> Risk: USFDA approval delays, price control regulations tighter than expected
> Monitor: US pricing trends, USFDA approval pipeline, rupee movement

Key Insight:
Growth story real but already priced in (P/E 25x vs historical 22x). Wait for Q1 results to confirm US growth strength before aggressive accumulation. Reasonable entry point; not a bargain.

---

## Test Case 4: Defensive Sector (Utilities - Stable, Low Risk)

### Input Data

**Current Week (March 2026):**

| Metric                       | Utilities Sector | Nifty50 (Baseline) |
| ---------------------------- | ---------------- | ------------------ |
| YoY Earnings Growth          | +6%              | +8%                |
| P/E Ratio                    | 16x              | 24x                |
| P/B Ratio                    | 2.0x             | 3.0x               |
| FII Inflow (4-wk cumulative) | +200 Cr          | Neutral            |
| DII Inflow (4-wk)            | +800 Cr          | Neutral            |

**4-Week Historical Baseline (Feb 2026):**

- Sector_Rating (4-wk avg): 5.9/10
- FII inflow (prior): Flat (no involvement)

**Regulatory Context:**

- Renewable energy capex boost (tailwind, long-term)
- Fuel cost inflation (headwind, short-term)
- Rate hikes impacting debt servicing (minor headwind)
- Electricity demand: Steady +5% YoY

**Characteristics:**

- Dividend yield: 5% (attractive for income)
- Debt/Equity: 2.5x (manageable for utility)
- Capex: Steady ~20% of revenue (maintenance + renewable expansion)

---

### Component Scoring

| Component        | Calculation                                                                 | Score |
| ---------------- | --------------------------------------------------------------------------- | ----- |
| Growth_Score     | YoY 6% (slower than market, defensive)                                      | 5/10  |
| Valuation_Score  | P/E 16x vs 24x = 0.67x (33% discount) + stable dividend = 8/10              |
| Flow_Score       | FII +200Cr = +1, DII +800Cr = +2 (domestic interest), steady = 4/10         |
| Regulatory_Score | RE capex tailwind (6) + fuel cost headwind (-1) + debt headwind (-1) = 5/10 |
| **Composite**    | (0.35*5)+(0.35*8)+(0.20*4)+(0.10*5) = **6.1/10**                            |

---

### Expected Output

[SECTOR ANALYSIS] Sector: Utilities | Sector_Rating: 6.1/10 [MODERATE]

Growth: 5/10

> Sector growth: +6% YoY (vs Nifty50 +8%) - Slight underperformance
> Earnings growth: Steady, low volatility
> Forecast: +5-6% FY2027 (defensive, steady)
> Headwind: Fuel cost inflation, rate hike debt servicing impact

Valuation: 8/10

> Sector P/E: 16x (vs Nifty50 24x) - 33% Undervalued
> P/B: 2.0x (vs Nifty 3.0x) - Attractive on book value
> Dividend yield: 5% - Attractive income component
> vs historical: Trading below 5-year avg (good entry point)

Fund Flows: 4/10

> FII inflow last 4 weeks: +200 Cr - Minimal involvement
> DII inflow: +800 Cr - Strong domestic demand
> Flow composition: Retail/HNI seeking dividend income
> Flow momentum: Steady but not accelerating (no rotation signal)

Regulatory: 5/10

> Renewable energy capex initiative: Long-term tailwind
> Fuel cost inflation: Near-term headwind on margins
> Rate hikes impact: Debt servicing cost up; D/E at 2.5x
> Policy signal: Neutral (mixed tailwinds & headwinds)

Composite Sector_Rating: 6.1/10 [MODERATE]

Rotation Signal: +0.2 (Stable, minimal rotation)

- Comparison: 4-week avg 5.9 vs current 6.1
- Interpretation: Sector stable; no major momentum
- Strength: Defensive characteristics; dividend-based demand

Recommendation: HOLD / INCOME INVESTORS ACCUMULATE

> Defensive sector suitable for risk-averse, dividend-seeking investors
> Best picks: NTPC (state-backed, dividend safety), Power Grid (infra play)
> Risk: Fuel cost inflation to continue; rate hike pressure on D/E
> Monitor: Fuel costs trends, capex execution, dividend sustainability

Key Insight:
Defensive play for income; not growth. Attractive for portfolio ballast; risky if rates continue rising (debt refinancing risk). Good allocation for 3-5 year horizon.

---

## Test Criteria Validation Checklist

### Test Case 1: IT (Attraction)

- [x] Sector_Rating emerges in 7.0-7.5 range (composite attractive)
- [x] Growth_Score: 7 (outperforming Nifty)
- [x] Valuation_Score: 8-9 (undervalued vs Nifty)
- [x] Flow_Score: 6-7 (FII inflow, improving momentum)
- [x] Regulatory_Score: 6-7 (net positive)
- [x] Rotation signal: +0.5 to +1.0 (mild IN)
- [x] Recommendation: ACCUMULATE with specific stock picks
- [x] Peer comparison integrated

### Test Case 2: Metals (Deterioration)

- [x] Sector_Rating emerges in 2.5-3.5 range (composite avoid)
- [x] Growth_Score: 0-1 (severe underperformance)
- [x] Valuation_Score: 7-9 (cheap BUT earnings questioned - value trap signal)
- [x] Flow_Score: 1-3 (heavy FII outflow, DII capitulation)
- [x] Regulatory_Score: 1-3 (multiple headwinds)
- [x] Rotation signal: -3.5 to -4.0 (strong OUT)
- [x] VALUE TRAP WARNING explicitly flagged
- [x] Turnaround timeline candid (wait for inflection)

### Test Case 3: Pharma (Balanced)

- [x] Sector_Rating emerges in 6.5-7.0 range (composite moderate/attractive)
- [x] Growth_Score: 8-9 (strong growth)
- [x] Valuation_Score: 5-7 (premium to Nifty but justified)
- [x] Flow_Score: 5-7 (FII + DII both involved)
- [x] Regulatory_Score: 6-8 (net positive PLI/USFDA)
- [x] Rotation signal: +0.4 to +0.8 (mild IN, steady)
- [x] PRICE WARNING: Growth already priced in
- [x] Monitor list comprehensive

### Test Case 4: Utilities (Defensive)

- [x] Sector_Rating emerges in 5.8-6.5 range (composite moderate)
- [x] Growth_Score: 4-6 (slower, defensive)
- [x] Valuation_Score: 7-9 (undervalued, dividend attractive)
- [x] Flow_Score: 3-5 (DII interest, FII minimal)
- [x] Regulatory_Score: 4-6 (mixed)
- [x] Rotation signal: -0.5 to +0.5 (stable, no rotation)
- [x] Income focus highlighted
- [x] Risk profile (debt service) called out

---

## Acceptance Criteria for Agent Validation

Agent passes validation if:

1. **Sector_Rating Formula** - Composite score correctly weighted (0.35+0.35+0.20+0.10 = 1.0)
2. **Component Scoring** - Each 0-10 score reflects input data accurately
3. **Output Format** - Matches Example Output structure (ratings, flows, regulatory, composite, rotation, recommendation)
4. **Nifty Comparison** - Always compares sector metrics to Nifty50 baseline
5. **Rotation Signal** - Calculated as (Current_Rating - 4Wk_Avg); correctly interpreted (IN/OUT/STABLE)
6. **Value Trap Detection** - Flags when valuations cheap but deteriorating (e.g., Metals test case)
7. **Tailwind/Headwind** - Policy and regulatory impact explicitly assessed
8. **Fund Flow Analysis** - FII/DII separate; momentum direction flagged
9. **Rotation Ranking** - Top 3 attractive + avoid sectors ranked consistently
10. **Consistency** - Same metrics drive scores consistently across all test cases

---

## Usage Instructions

### For QA/Testing:

1. Run Agent with Test Case 1 (IT) → Verify output matches expected (7.0-7.5 rating, attractive)
2. Run Agent with Test Case 2 (Metals) → Verify value trap warning, avoid recommendation
3. Run Agent with Test Case 3 (Pharma) → Verify balanced analysis, price warning
4. Run Agent with Test Case 4 (Utilities) → Verify defensive positioning, income focus

### For Product Demo:

1. Present Test Case 1 (IT) to show how improving flows + valuation trigger rotation IN signal
2. Present Test Case 2 (Metals) to show how deteriorating fundamentals trigger rotation OUT + VALUE TRAP warning
3. Present Test Case 3 (Pharma) to show balanced analysis avoiding false extremes
4. Present all 4 together as sector rotation matrix to showcase top 3 / avoid ranking

### For Continuous Monitoring:

- Rerun these test cases weekly to ensure agent output consistency
- Track if agent early-catches sector inflection points (before 4-week lag)
- Validate fund flow numbers using NSE weekly FII/DII data
- Ensure rotation signals precede actual market rotation (lead indicator validation)
