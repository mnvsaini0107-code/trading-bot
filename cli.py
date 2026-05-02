import argparse
import os
import logging
from dotenv import load_dotenv
from binance.client import Client
from bot.logging_config import setup_logging

# Load environment variables
load_dotenv()

# Setup logging
setup_logging()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    # Load API keys
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    # Check API keys
    if not api_key or not api_secret:
        print("API keys not found. Check your .env file")
        logging.error("API keys missing")
        return

    # Initialize client
    client = Client(api_key, api_secret, testnet=True)

    try:
        # Prepare order params
        params = {
            "symbol": args.symbol.upper(),
            "side": args.side.upper(),
            "type": args.type.upper(),
            "quantity": args.quantity,
        }

        # Handle LIMIT order
        if args.type.upper() == "LIMIT":
            if args.price is None:
                raise ValueError("Price required for LIMIT order")
            params["price"] = args.price
            params["timeInForce"] = "GTC"

        # Logging request
        logging.info(f"Sending order: {params}")
        print("\n Sending order...")

        # Place order
        response = client.futures_create_order(**params)

        # Logging response
        logging.info(f"Response: {response}")

        # Print success output
        print("\n Order Placed Successfully!\n")
        print("Symbol:", response.get("symbol"))
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice", "N/A"))

    except Exception as e:
        logging.error(str(e))
        print("\n Error:", e)


if __name__ == "__main__":
    main()