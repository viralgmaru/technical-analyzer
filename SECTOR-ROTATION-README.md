# NSE Sector Rotation Scripts — Complete Delivery Package

## 📦 What You Have

### Pine Scripts (4 Total)

1. **sector-rotation-alert.pine** — Balanced, all-purpose (35/35/20/10 weighting)
2. **sector-rotation-conservative.pine** — Risk-averse (40/40/15/5 weighting)
3. **sector-rotation-aggressive.pine** — Momentum-focused (30/30/25/15 weighting)
4. **sector-rotation-multiframe.pine** — Multi-timeframe confluence (Daily/Weekly/Monthly blend)

### Documentation (3 Files)

- **PINE-IMPLEMENTATION-GUIDE.md** — Step-by-step setup, webhook config, validation
- **PINE-VARIANTS-GUIDE.md** — Detailed comparison, when to use each script, customization
- **SECTOR-ROTATION-README.md** (this file) — Quick navigation guide

---

## 🚀 Getting Started (5 Minutes)

### Quickest Path to Live Alerts

1. **Open TradingView** → New Chart → NIFTY_IT symbol
2. **Pine Editor** → Create new indicator → Copy **sector-rotation-alert.pine** → Save
3. **Add to Chart** → Full-screen indicator view
4. **Alert Setup**:
   - Click Alert Bell → New Alert
   - Select your chart + indicator
   - Condition: "Indicator crosses..."
   - Webhook: `https://yourendpoint.com/alerts` (POST)
5. **Wait for alerts** on next daily close

You'll get signals like:

- 🟢 **IT 7.8** — Rotation in, initiate position
- 🔴 **BANK 4.2** — Rotation out, reduce position

---

## 📊 Script Selector

**Choose ONE based on your style:**

| Your Trading Style | Use This Script | Why                                |
| ------------------ | --------------- | ---------------------------------- |
| Day trading        | Balanced        | Moderate signals, 3-10 day holds   |
| Swing trading      | Conservative    | Fewer false breaks, 2-4 week holds |
| Scalping/Intraday  | Aggressive      | Fast signals, 1-5 day holds        |
| Position trading   | Multi-Frame     | Institutional-grade confirmation   |
| Testing/Learning   | Balanced        | Best for understanding mechanics   |

**Recommendation**: Start with **Balanced**, then switch to your style after 2 weeks.

---

## 📖 Understanding the Signals

### What the Rating Score Means

```
9-10  → Sector very attractive (Strong BUY signal)
7-8   → Sector attractive (BUY signal)
5-6   → Sector neutral (HOLD)
3-4   → Sector weak (SELL signal)
0-2   → Sector very weak (Strong SELL signal)
```

### Example Trade from Green Alert

```
Alert received: 🟢 IT 7.8
20-day average was: 6.1
Signal strength: +1.7 points (above threshold)

Action:
1. Check daily chart for technical confirmation
2. Buy 2-3% of portfolio in IT sector/index
3. Set stop: Previous support or -5% loss
4. Target: Wait for opposite signal or +15% gain
```

### Example Trade from Red Alert

```
Alert received: 🔴 PHARMA 4.1
20-day average was: 5.2
Signal strength: -1.1 points (below threshold)

Action:
1. Exit or reduce pharma position
2. Move capital to green-alert sectors
3. Or hold if thesis still intact (ignore signal)
```

---

## 🛠️ Configuration Examples

### For NSE Intraday Traders

```
Use: sector-rotation-aggressive.pine
Threshold: 0.3 (fast entries)
Sectors: IT, Bank, Pharma, Auto
Hold: 1-5 days
Position Size: 1-2% per trade
```

### For FII Portfolio Managers

```
Use: sector-rotation-multiframe.pine
Threshold: 1.0 (confirmed signals)
Sectors: IT, Bank, Pharma (Nifty 50)
Hold: 10-30 days
Position Size: 3-5% per rotation
```

### For Retail Swing Traders

```
Use: sector-rotation-conservative.pine
Threshold: 1.5 (high confidence)
Sectors: IT, Bank, Pharma
Hold: 10-30 days
Position Size: 2-3% per trade
```

---

## 📋 Regulatory Adjustments

Each script includes pre-set regulatory parameters:

```
Pharma:  +1 (PLI scheme positive)
Auto:    -1 (EV transition headwind)
Metals:  -1 (Export duty negative)
Infra:   +1 (Govt capex positive)
Energy:  -1 (Rate hike negative)
Others:   0 (Neutral)
```

**To adjust for your market view:**

1. Add indicator to chart
2. Settings (gear icon) → Inputs
3. Find "[SECTOR] Reg" option
4. Change value from -5 to +5
5. Apply → Watch updated alerts

---

## 🔗 Webhook Integration

### Discord Example

```javascript
// POST to this endpoint on alert
POST /webhooks/1234567890/abcdef

{
  "content": "🟢 IT Rating: 7.8 (+1.6 above avg)"
}
```

### Slack Example

```json
{
  "text": "🟢 *IT Rotation IN*",
  "attachments": [
    {
      "color": "good",
      "text": "Rating: 7.8 | 20MA: 6.2 | Diff: +1.6"
    }
  ]
}
```

### Trading Bot Integration (Python)

```python
from flask import Flask
app = Flask(__name__)

@app.route('/alerts', methods=['POST'])
def alert_handler():
    signal = request.json  # {"sector": "IT", "rating": 7.8, ...}

    if signal['rating'] > 7.0:
        # Execute BUY
        trading_bot.buy_sector(signal['sector'], position_size=0.03)
    elif signal['rating'] < 5.0:
        # Execute SELL
        trading_bot.sell_sector(signal['sector'])

    return {'status': 'ok'}
```

---

## ❓ Common Questions

**Q: Why did I miss a signal?**
A: Alerts fire on daily bar close (~3:30 PM IST). Check if market was open.

**Q: The rating keeps going up but no alert fires?**
A: The threshold compares current rating against 20-bar AVERAGE, not previous close. Need bigger jump.

**Q: Can I use this on other timefr than daily?**
A: Conditional. Multi-Frame script requires daily. Others can work on 4H/1H but optimize thresholds.

**Q: Should I trade every alert?**
A: No. Use as confluence signal only. Combine with:

- Chart support/resistance
- Sector-specific news
- Macro backdrop
- Your position sizing rules

**Q: Which script makes the most money?**
A: No single winner. Depends on market regime:

- Bull market → Aggressive wins
- Range market → Conservative wins
- Trending market → Multi-TF wins

---

## 📈 Backtesting Checklist

Before live trading, validate on historical data:

1. **Open TradingView chart** with 500+ bars of history (2+ years)
2. **Add indicator** → Settings → Past trades visible?
3. **Manual backtest** last 20 signals:
   - Did alerts catch good rotations?
   - False signal rate acceptable (<30%)?
   - Win rate % satisfactory (>50%)?
4. **Check regulatory news** during those signals
5. **Adjust threshold/weighting** if needed
6. **Paper trade 2 weeks** before real capital

---

## 📞 Support/Debugging

### Script won't compile

→ Make sure `@version=5` at top
→ Paste ENTIRE script, don't edit out lines

### No alerts firing

→ Check TradingView profile → Alerts → Verify enabled
→ Confirm indicator is full-screen (alerts don't fire minimized)
→ Test webhook endpoint separately

### Alerts firing too frequently

→ Conservative script + raise threshold
→ Or increase moving average period from 20 → 30

### Conflicting signals (BUY + SELL same sector)

→ Use Multi-TF script for confirmation
→ Or ignore if different timeframes (daily vs weekly)

---

## 📦 File Structure

```
ai-agents/
├── scripts/
│   ├── sector-rotation-alert.pine           [Balanced]
│   ├── sector-rotation-conservative.pine    [Risk-averse]
│   ├── sector-rotation-aggressive.pine      [Momentum]
│   └── sector-rotation-multiframe.pine      [Multi-TF]
├── PINE-IMPLEMENTATION-GUIDE.md             [Setup, webhooks, validation]
├── PINE-VARIANTS-GUIDE.md                   [Detailed comparison & customization]
└── SECTOR-ROTATION-README.md                [This file]
```

---

## 🎯 Next Steps

### Immediate (Today)

- [ ] Choose 1 script based on your style
- [ ] Add to TradingView chart
- [ ] Configure 1 alert (test alert first)

### This Week

- [ ] Paper trade 5-10 signals
- [ ] Validate with chart + news
- [ ] Adjust regulatory parameters if biased

### Next Week

- [ ] Backtest on 2 years historical
- [ ] Adjust threshold/weighting for your market view
- [ ] Go live with small position size (1% portfolio)

### Ongoing

- [ ] Track P&L per sector
- [ ] Adjust regulatory inputs quarterly
- [ ] Consider switching scripts seasonally

---

## 🏆 Pro Tips

1. **Combine scripts**: Use Aggressive for entry ideas, then confirm with Multi-TF before scaling
2. **Diversify sectors**: Don't go all-in on 1 signal; rotate across 2-3 concurrent rotations
3. **Respect the 20-bar MA**: It smooths noise; trust the trend, not individual bars
4. **Check macro backdrop**: Sector rotations need tailwind (GDP growth, RBI stance, FII flows)
5. **Use stop losses**: Even good signals fail; never risk >2% per trade
6. **Track your adjustments**: Document why you changed thresholds; measure impact

---

## 📚 Learning Resources

- [TradingView Pine Script Docs](https://www.tradingview.com/pine-script-docs/en/v5/)
- [NSE Sector Indices](https://www.nseindia.com/)
- [Moneycontrol Sector Analysis](https://www.moneycontrol.com/)
- [ET Markets Sector Tracker](https://markets.economictimes.com/)

---

**Version:** 1.0
**Date:** 2026-Q1
**Status:** Production Ready
**Validation:** All scripts compile without errors on TradingView v5

Questions? Re-read PINE-VARIANTS-GUIDE.md for detailed explanations.
