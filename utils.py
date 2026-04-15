import logging

# ---------------- LOGGING ----------------
def setup_logger():
    logging.basicConfig(
        filename="trading.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

# ---------------- VALIDATION ----------------
def validate_input(symbol, side, order_type, quantity, price):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")

# ---------------- ORDER ----------------
def place_order(client, symbol, side, order_type, quantity, price=None):
    logging.info(f"Placing order: {side} {symbol} {order_type} {quantity} {price}")

    if order_type == "MARKET":
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

    elif order_type == "LIMIT":
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

    logging.info(f"Response: {response}")
    return response