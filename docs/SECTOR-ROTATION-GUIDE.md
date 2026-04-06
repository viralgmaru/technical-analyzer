# NSE Sector Rotation Alert System - Pine Script Guide

## Overview

This Pine Script implements the **Sector Analyst & Stock Analyst** framework in TradingView, monitoring 10 NSE sector indices for rotation signals. It calculates sector ratings and identifies rotation opportunities across sectors.

**Key Features:**

- ✅ Monitors 10 NSE sectors (IT, Banking, Pharma, Auto, Metals, FMCG, Infra, Realty, Energy, PSU)
- ✅ Dynamic sector rating calculation (Growth + Valuation + Flow + Regulatory)
- ✅ Real-time rotation signal alerts (Strong IN/OUT, Mild IN/OUT)
- ✅ Customizable regulatory adjustments for policy impact
- ✅ Historical tracking for 4-week rotation baseline

---

## How to Use

### Step 1: Add to TradingView

1. Go to TradingView Pine Script Editor
2. Copy the entire script from `sector-rotation-alert.pine`
3. Paste into a new indicator
4. Add to chart with default settings (or customize below)

### Step 2: Configure Sector Monitoring

**Available Sectors (Toggle On/Off):**

- Nifty IT (TCS, INFY, WIPRO, HCL)
- Nifty Bank (HDFC, ICICI, AXIS, Kotak)
- Nifty Pharma (Cipla, Dr. Reddy, Lupin)
- Nifty Auto (Maruti, Bajaj, TVS)
- Nifty Metals (Tata Steel, Vedanta, Hindalco)
- Nifty FMCG (HUL, ITC, Britannia)
- Nifty Infra (L&T, engineering firms)
- Nifty Realty (DLF, Oberoi, Godrej)
- Nifty Energy (Reliance, ONGC, Coal India)
- Nifty PSU Bank (State Bank, Bank of India)

**Example:** Toggle **Nifty IT** ON, disable others to focus on IT rotation.

### Step 3: Set Rotation Thresholds

**Default Settings:**

- **Strong Rotation Threshold:** 1.0 (rotation > +1.0 = Strong IN; < -1.0 = Strong OUT)
- **Mild Rotation Threshold:** 0.5 (rotation 0.5-1.0 = Mild IN; -1.0 to -0.5 = Mild OUT)

**Recommendation:**

- Conservative traders: Increase to 1.5 (wait for stronger confirmation)
- Aggressive traders: Decrease to 0.3 (catch earlier rotation)

### Step 4: Apply Regulatory Adjustments

**Why?** Fundamental policy changes affect sectors beyond technical signals.

**Current Pre-set Values (Based on 2026 Market Conditions):**

- **Pharma:** +1 (PLI scheme tailwind)
- **Auto:** +1 (EV incentive support)
- **Metals:** -1 (export tax headwind)
- **Infra:** +1 (govt capex push)
- **Energy:** -1 (rate hike pressure)
- Others: 0 (neutral)

**How to Adjust:**

1. Settings → Regulatory Adjustments group
2. Change sector adjustment from -5 to +5 based on:
   - **+3 to +5:** Strong policy support (better rating)
   - **0:** Neutral regulation
   - **-3 to -5:** Major policy headwind (lower rating)

**Example:** If RBI cuts rates → Add +1 to Banking sector

### Step 5: Enable Alerts

1. Settings → Alert Settings group
2. Toggle **Enable Alerts** ON
3. Check **Alert Strong Rotation (>1.0)** - for high-conviction signals
4. Check **Alert Mild Rotation** - for early trend confirmation

**Alert Format:**

```
🟢 STRONG ROTATION IN: IT | Rating: 7.2/10 | Rotation: +1.3
🔴 STRONG ROTATION OUT: Metals | Rating: 4.8/10 | Rotation: -1.6
🟡 MILD ROTATION IN: Pharma | Rating: 7.5/10
🟠 MILD ROTATION OUT: Energy | Rating: 5.2/10
```

---

## Sector Rating Calculation (Technical Proxies)

Since Pine Script cannot fetch fundamental data directly, the script uses **technical proxies** that correlate with sector health:

### Growth_Score (0-10)

- **Measures:** RSI momentum + ADX trend strength
- **Logic:**
  - RSI > 65 = Strong momentum (+4 pts)
  - ADX > 40 = Strong trend (+3 pts)
  - Max Score: 10

**Example:** IT sector (Nifty IT) with RSI=72 + ADX=42 → Growth_Score=7

### Valuation_Score (0-10)

- **Measures:** Price relative to 200-SMA (supports value rotation)
- **Logic:**
  - Price < 0.95 × 200-SMA = Deeply undervalued (score 9)
  - Price > 1.2 × 200-SMA = Significantly overvalued (score 1)

**Example:** Banking sector at 0.85× 200-SMA → Valuation_Score=7 (attractive)

### Flow_Score (0-10)

- **Measures:** Volume trend + OBV accumulation
- **Logic:**
  - Volume_Today > 1.2 × 20-day average = Strong flow (+3 pts)
  - OBV > OBV_MA20 = Accumulation phase (+2 pts)
  - Max Score: 10

**Example:** Pharma sector with volume surge + OBV rising → Flow_Score=6

### Regulatory_Score (0-10)

- **Measures:** Manual news-based policy adjustments
- **Logic:**
  - Base score = 5 (neutral)
  - Add/subtract adjustment from settings (-5 to +5)

**Example:** Infrastructure + +1 PLI adjustment → Regulatory_Score=6

### Composite Sector Rating Formula

```
Sector_Rating = (0.35 × Growth) + (0.35 × Valuation) + (0.20 × Flow) + (0.10 × Regulatory)

Range: 0-10
> 7.5 = HIGHLY ATTRACTIVE
6.5-7.5 = ATTRACTIVE (ACCUMULATE)
5.5-6.5 = MODERATE (HOLD)
4.5-5.5 = WEAK (AVOID)
< 4.5 = HIGHLY UNATTRACTIVE (REDUCE)
```

---

## Rotation Signal Interpretation

### Rotation = Current_Rating - 4-Week_Average_Rating

| Rotation Signal  | Interpretation                                    | Action                           |
| ---------------- | ------------------------------------------------- | -------------------------------- |
| **> +1.0**       | 🟢 **Strong IN** — Fundamentals improving rapidly | Consider sector rotation IN      |
| **+0.5 to +1.0** | 🟡 **Mild IN** — Early rotation signal            | Watch for confirmation next week |
| **-0.5 to +0.5** | ⚪ **Stable** — No major change                   | Hold current positions           |
| **-1.0 to -0.5** | 🟠 **Mild OUT** — Early deterioration             | Reduce exposure cautiously       |
| **< -1.0**       | 🔴 **Strong OUT** — Fundamentals declining        | Consider sector rotation OUT     |

**Example:** IT sector rating today = 7.2, 4-week avg = 6.5

- Rotation = 7.2 - 6.5 = +0.7 (Mild IN → watch for confirmation)

---

## Use Cases & Examples

### Use Case 1: Identify Top 2-3 Attractive Sectors for Stock Picking

**Scenario:** You want to trade individual stocks in the strongest sectors.

**Steps:**

1. Enable all 10 sectors
2. Disable alerts (only focus on rating visualization)
3. Look for sectors with ratings > 7.0
4. Use **Stock Analyst Agent** to find best trades within those sectors

**Example Output:**

```
Rating: IT (7.2/10), Pharma (7.5/10), Infra (7.0/10)
Decision: Screen for best stocks in IT & Pharma
```

### Use Case 2: Real-Time Rotation Alerts via Webhook

**Scenario:** You want automated Slack/Discord alerts when strong rotation signals trigger.

**Steps:**

1. Enable only **Alert Strong Rotation (>1.0)** - avoids noise
2. Create TradingView Alert on this indicator
3. Set webhook URL to Slack/Discord/custom receiver
4. Receive real-time notifications:
   ```
   🟢 STRONG ROTATION IN: Pharma | Rating: 7.8/10 | Rotation: +1.4
   ```

### Use Case 3: Monthly Sector Rebalancing Strategy

**Scenario:** You rebalance portfolio quarterly to favor strongest 3 sectors.

**Steps:**

1. Run analysis on 1-week timeframe
2. Identify top 3 sectors from ratings
3. Reduce exposure to bottom 2 sectors
4. Monitor rotation signals weekly for adjustment timing

**Example Decision Matrix:**

```
Week 1: Top 3 = IT (7.2), Pharma (7.5), Infra (7.0)
Week 3: Pharma rotation down (-1.2) → Reduce Pharma by 20%
Week 4: IT strong IN (+1.5) → Increase IT by 30%
```

### Use Case 4: Avoid Sector Traps with Policy News

**Scenario:** Rate hike announced → Banking sector fundamentals worse.

**Steps:**

1. Reduce banking sector adjustment by -2 (from 0 to -2)
2. Recalculate ratings on next day's bar
3. Watch for banking rotation OUT signal
4. Hedge banking exposure or rotate to less-sensitive sectors

---

## Technical Settings Deep Dive

### Indicator Periods

```
RSI Period: 14 (standard momentum measurement)
  - Lower (7-10): More sensitive to price changes
  - Higher (21+): Smoother, fewer false signals

Short MA: 20 (4-week trend line)
  - Identifies short-term direction

Long MA: 200 (1-year trend line)
  - Identifies long-term trend & valuation zone

ADX Period: 14 (trend strength)
  - > 25: Trending market
  - < 20: Ranging/choppy market
```

### Rotation Lookback

```
Default: 20 bars (4 trading weeks for daily chart)

For Intraday Analysis:
  - 5-min chart: Use 96 bars (4 trading weeks of intraday)
  - 15-min chart: Use 96 bars
  - 1-hour chart: Use 20 bars

For Swing Trading:
  - Daily chart: Use 20 bars (default)
  - Weekly chart: Use 13 bars (quarterly = ~3 months)
```

---

## Alert Integration Examples

### Slack Webhook Integration

```json
{
  "text": "🟢 STRONG ROTATION IN: Pharma | Rating: 7.8/10 | Rotation: +1.4"
}
```

### Discord Webhook Integration

```json
{
  "content": "🟢 **STRONG ROTATION IN:** Pharma | Rating: 7.8/10 | Rotation: +1.4"
}
```

### Custom HTTP Receiver (Python Flask)

```python
from flask import Flask, request

@app.route('/tradingview', methods=['POST'])
def receive_alert():
    msg = request.json['message']  # "STRONG ROTATION IN: IT ..."
    # Send to trading system, telegram, email, etc.
    trader.execute_rotation_strategy(msg)
    return 'OK'
```

---

## Known Limitations & Workarounds

| Limitation                                        | Workaround                                              |
| ------------------------------------------------- | ------------------------------------------------------- |
| **Can't fetch real institutional flow (FII/DII)** | Use volume & OBV as proxy; supplement with NSE website  |
| **No P/E or ROE data in Pine**                    | Use technical valuation proxy (price/200-MA ratio)      |
| **Regulatory score requires manual input**        | Check CNBC, ET, SEBI news daily; update settings        |
| **Multi-sector analysis on same chart cluttered** | Monitor 2-3 key sectors at a time; rotate focus         |
| **Missing earnings surprise data**                | Combine with Fundamental Analyst agent for top 5 stocks |

---

## Backtesting & Optimization

### Validate Before Live Trading

1. **Run on Past 1-2 Years of Data**
   - Set chart to Daily timeframe
   - Set back ~500 bars (2 years history)
   - Check if rotation signals aligned with actual sector performance

2. **Compare with Actual NSE Sector Index Returns**
   - When script signals Rotation IN +1.0 (IT), did Nifty IT outperform next month?
   - Measure win rate (% of signals profitable)
   - Target > 65% accuracy before live trading

3. **Optimize Settings**
   - Backtest with rotation threshold 0.7, 1.0, 1.3
   - Compare results; pick threshold with best win rate
   - Note: Higher thresholds = fewer but higher-confidence signals

### Example Backtest Checklist

```
✓ IT Strong IN signals: 7 total
  ├─ Profitable (Nifty IT up next 2 weeks): 5/7 = 71% win rate
  └─ All > +1.0 rotation threshold
✓ Banking Mild OUT signals: 12 total
  ├─ Profitable (avoided downside): 8/12 = 67% win rate
  └─ Threshold 0.5 too sensitive; recommend 0.7+
✓ Overall: 65% win rate → Ready for live trading
```

---

## Integration with Stock Analyst & Sector Analyst Agents

### Workflow: Identify Profitable Trades

```
1. Run Sector Rotation Alert
   ↓ (Identify attractive sectors)
2. Handoff to Sector Analyst Agent
   ↓ (Get detailed sector analysis & top stocks)
3. Handoff to Stock Analyst Agent
   ↓ (Get specific entry/exit setups in attractive sector)
4. Execute trade with Pine Script alerts (optional)
   ↓ (Monitor position via this script)
5. Rebalance on rotation signals
```

**Example:**

```
Script Output: Pharma strong IN (rating 7.8, rotation +1.4)
  ↓
Sector Analyst: Pharma top 3 stocks = Cipla, Dr. Reddy, Lupin
  ↓
Stock Analyst: Cipla setup ready – Support 1245, Target 1345, Risk/Reward 1:3.5
  ↓
Trade: Buy Cipla @ 1275, SL 1245, Target 1345
  ↓
Monitor: If Pharma rotation drops below 0.5, reduce position
```

---

## FAQ & Troubleshooting

**Q: Script shows no data / blank chart?**
A:

- Ensure sector symbols are correct (NIFTY_IT, NIFTY_BANK, etc.)
- Check TradingView has data for these indices
- Wait 5-10 bars for script to calculate (needs history)

**Q: Alerts not triggering?**
A:

1. Settings → Alert Settings → Enable Alerts = true
2. Create TradingView Alert on this indicator (not the indicator itself)
3. Check webhook URL if using external receiver

**Q: How to add custom sectors?**
A:

1. Uncomment a sector line (e.g., NIFTY_REALTY) and rename the function call
2. Add new input toggle and regulatory adjustment
3. Recompile script

**Q: What timeframe should I use?**
A:

- **Intraday traders:** 4-hour or hourly (hourly = more noise, better for day trades)
- **Swing traders:** Daily (default, best for 2-7 day holds)
- **Position traders:** Weekly (1-month rotation cycles)

**Q: Rotation signal keeps changing – how to filter noise?**
A: Increase rotation threshold to 1.5 or use **only Strong Rotation alerts**, ignore Mild.

---

## Next Steps

1. ✅ **Add script to TradingView** → Copy from `sector-rotation-alert.pine`
2. ✅ **Configure 2-3 key sectors** → Enable IT, Bank, Pharma; disable others
3. ✅ **Set alerts** → Strong rotation only (avoid noise)
4. ✅ **Backtest 1-2 years** → Validate win rate > 65%
5. ✅ **Live trade** → Start with 2% position size on strong rotation IN signals
6. ✅ **Monthly review** → Track performance, adjust regulatory scores

---

## Resources

- **Sector Analysis Framework:** See `sector-analyst.agent.md` for detailed methodology
- **Stock Picking in Sectors:** See `stock-analyst.agent.md` for trade setup rules
- **Pine Script Reference:** See `pine-tradingview.agent.md` for advanced customization
