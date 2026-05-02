# Binance Futures Testnet Trading Bot

## Overview
This is a simple CLI-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

## Features
- Market Orders (BUY/SELL)
- Limit Orders (BUY/SELL)
- CLI-based input
- Logging of requests & responses
- Error handling

## Setup

1. Clone the repository

2. Install dependencies:
pip install -r requirements.txt

3. Add API keys in `.env`:
API_KEY=your_api_key
API_SECRET=your_api_secret

## Usage

### MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 78000

## Logs
All logs are stored in:
trading_bot.log

## Notes
- Uses Binance Futures Testnet
- No real money involved
