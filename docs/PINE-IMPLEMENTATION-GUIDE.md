# Pine Script Implementation & Webhook Setup

## Step 1: Add Script to TradingView

1. Open TradingView → Pine Script Editor
2. Click "Create" → New Indicator Script
3. Copy entire content from `sector-rotation-alert.pine`
4. Click "Save" (name: "NSE Sector Rotation")
5. Click "Add to Chart"

## Step 2: Configure Alert Webhook

### TradingView -> Alerts Setup

1. Click 3-dots menu on chart
2. Create Alert → Select indicator "NSE Sector Rotation"
3. Condition: Default (any value change)
4. Webhook URL: `https://your-server.com/alerts`
5. Message: `{{close}}`
6. Once Per Bar Close: enabled

### Webhook Receiver Requirements

- Listen on endpoint: `/alerts`
- Accept POST with JSON body
- Extract alert message from TradingView
- Forward to Discord/Slack/Trading system

## Step 3: Run on Daily Timeframe

1. Set chart to Daily (1D)
2. Enable only 2-3 sectors initially (IT, Bank, Pharma)
3. Monitor for 5-10 bars (5-10 trading days)
4. Verify alerts trigger correctly

## Step 4: Validate with Historical Data

1. Chart back 500 bars (~2 years)
2. Identify past rotation IN signals
3. Cross-check with actual NSE sector performance
4. Calculate win rate: (Profitable signals) / (Total signals)
5. Target: >65% accuracy before live trading

## Configuration Reference

| Setting                   | Default         | Adjust For                       |
| ------------------------- | --------------- | -------------------------------- |
| RSI Period                | 14              | Slower=21, Faster=10             |
| Short MA                  | 20              | Faster trend=10, Slower=30       |
| Long MA                   | 200             | 1-year trend line (fixed)        |
| Rotation Threshold        | 1.0             | Conservative=1.5, Aggressive=0.5 |
| Regulatory Adj (-5 to +5) | Sector-specific | Update for policy news           |

## Sector Regulatory Adjustments (2026)

- **IT:** 0 (neutral)
- **Banking:** 0 (watching rate policy)
- **Pharma:** +1 (PLI scheme active)
- **Auto:** +1 (EV incentives)
- **Metals:** -1 (export tax headwind)
- **FMCG:** 0 (monsoon watchlist)
- **Infra:** +1 (govt capex push)
- **Realty:** 0 (monitoring Q4 pickup)
- **Energy:** -1 (rate hike pressure)
- **PSU:** 0 (RBI policy sensitive)

Update adjustments when:

- New policy announced (Budget, RBI MPC)
- Major sector news (strikes, regulations)
- Earnings trends shift significantly

## Alert Message Format

```
🟢 IT 7.8          (Green = Rotation IN, sector rating 7.8/10)
🔴 BANK 5.2        (Red = Rotation OUT, sector rating 5.2/10)
```

Rating Guide:

- 7.5+: HIGHLY ATTRACTIVE
- 6.5-7.5: ATTRACTIVE
- 5.5-6.5: MODERATE
- <5.5: AVOID
