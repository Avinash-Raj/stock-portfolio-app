import datetime
from typing import Dict, Optional, Tuple

import yfinance as yf
from mystocks.entities.classes import CURRENCIES, Amount, ConversionRate


def get_stock_info(stock_symbol: str) -> Dict:
    """
    Gets some basic information about a particular stock.
    """
    stock_ticker = yf.Ticker(stock_symbol)
    return stock_ticker.info


def get_stock_current_price(stock_symbol: str, target_currency_code: Optional[str] = None) -> Amount:
    """
    Gets the current price of a particular stock.

    Args:
        stock_symbol (str): Stock Symbol , ex: AAPL
        target_currency_code (str, optional): Current Price got converted to the target currency according
            to the latest exchange rate. Defaults to 'USD'.

    Returns:
        converted price
    """
    stock_info = get_stock_info(stock_symbol)

    current_price: float = stock_info["currentPrice"]
    original_currencry = CURRENCIES[stock_info["currency"]]
    original_amount: Amount = Amount(price=current_price, currency=original_currencry)

    if not target_currency_code:
        return original_amount

    if original_currencry.code == target_currency_code:
        # currency codes are same, so don't do currency conversion
        return original_amount
    # currency differs, so convert it
    converted_price = ConversionRate(original_currencry.code, target_currency_code).convert(current_price)
    return Amount(price=converted_price, currency=CURRENCIES[target_currency_code])


def get_stock_last_close_price(stock_symbol: str) -> Tuple[Amount, datetime.date]:
    """
    Get's the stock last close price along with date.

    Args:
        stock_symbol (str): Stock symbol

    Returns:
        Tuple[Amount, datetime.date]: _description_
    """
    stock_ticker = yf.Ticker(stock_symbol)
    data = stock_ticker.history(period="1d")
    last_quote = data["Close"].iloc[-1]
    # convert pandas timestamp to utc
    last_date = data.index[-1].tz_convert(tz="UTC").date()
    return Amount(price=last_quote), last_date
