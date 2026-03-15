---
name: stock-monitoring
description: Run the user's local stock monitoring and backtesting workflow for A-shares, Hong Kong stocks, and US stocks. Use when the user asks to start or manage stock monitoring, realtime trading signal checks, RSI/MACD/Bollinger analysis, buy/sell alerts, overbought/oversold warnings, or stock strategy backtests tied to the local `~/clawd/stock-assistant` and `~/clawd/quant-trading` setup.
---

# Stock Monitoring

Use the user's local workflow instead of searching for another tool when they ask to start stock monitoring or run the paired backtest.

## Realtime monitor

Start the monitor from a shell that activates the existing virtual environment first:

```bash
cd ~/clawd/stock-assistant && source venv/bin/activate
python3 ~/clawd/quant-trading/realtime_monitor.py
```

What this workflow is expected to cover:

- A-shares and Hong Kong stocks during workdays from 09:00 to 16:00
- US stocks from 20:30 to 05:00 next day
- Multi-indicator analysis using RSI, MACD, and Bollinger Bands
- Automatic push notifications for buy and sell signals
- Overbought and oversold alerts

## Trading-hours behavior

Respect the user's quiet-hours rule:

- Outside trading hours, prefer not to proactively notify
- If asked to run the monitor outside market hours, mention that it should stay silent automatically
- Do not treat silence outside trading hours as a failure unless logs show an actual error

## Backtest

Use the backtest command the user provided:

```bash
python3 clawhub install stock-strategy-backtester/scripts/backtest.py
```

If the user asks for results interpretation, summarize the important metrics and call out assumptions, date ranges, and obvious overfitting risks.

## Execution notes

- Prefer running these commands as given unless the user asks to modify the strategy
- If a command fails, inspect the Python environment, working directory, and file paths before changing anything
- Treat this as a local custom workflow, not a generic market-data skill
