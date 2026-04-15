# Binance Futures Trading Bot

A command-line trading bot for Binance Futures (USDT-M) built with Python. Supports MARKET and LIMIT orders via the Binance Testnet API.

---

## Project Structure
binance-futures-trading-bot/
├── client.py # Binance client setup
├── cli.py # CLI entry point
├── utils.py # Validation, logging, order logic
├── .env # API keys (not committed)
├── trading.log # Auto-generated log file
└── requirements.txt

---

## Features

- Place MARKET and LIMIT futures orders via CLI  
- Input validation with clear error messages  
- Automatic symbol uppercasing  
- Order logging to `trading.log`  
- Testnet support for safe testing  

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/jaayysoni/binance-futures-trading-bot
cd binance-futures-trading-bot
2. Install dependencies
pip install python-binance python-dotenv
3. Create .env file
BINANCE_API_KEY=your_testnet_api_key
BINANCE_SECRET_KEY=your_testnet_secret_key
Get your testnet keys from:
https://testnet.binancefuture.com
Usage
MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000
Arguments
Argument	Required	Description
--symbol	Yes	Trading pair e.g. BTCUSDT
--side	Yes	BUY or SELL
--type	Yes	MARKET or LIMIT
--quantity	Yes	Order quantity (float)
--price	No	Required for LIMIT orders
Example Output
Order Summary:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

✅ Order placed successfully
Order ID: 13036803200
Status: NEW
Executed Qty: 0.0000
Avg Price: 0.00
Logging
All orders are automatically logged to trading.log:
2026-04-15 10:23:01 | INFO | Placing order: BUY BTCUSDT MARKET 0.001 None
2026-04-15 10:23:02 | INFO | Response: {'orderId': 13036803200, 'status': 'NEW', ...}
Validation Rules
--side must be BUY or SELL
--type must be MARKET or LIMIT
--quantity must be greater than 0
--price is required when --type is LIMIT
Notes
This bot runs on Binance Futures Testnet — no real money involved
Testnet orders may show Status: NEW instead of FILLED — this is normal testnet behavior
Do not commit your .env file — add it to .gitignore
Tech Stack
Python 3
https://github.com/sammchardy/python-binance
python-dotenv
Binance Futures Testnet API
Author
Jay Soni
GitHub: https://github.com/jaayysoni
LinkedIn: https://www.linkedin.com/in/jaayysoni