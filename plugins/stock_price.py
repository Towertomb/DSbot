import yfinance as yf

def get_stock_price(name):
    res = yf.Ticker(name)
    stock_info = res.history(period="1d")
    latest_price = stock_info['Close'].iloc[0]
    return f"{name}最新股价：${latest_price:.2f}"

if __name__ == "__main__":
    nvidia = yf.Ticker("NVDA")

    # 获取最新的股价信息
    stock_info = nvidia.history(period="1d")
    latest_price = stock_info['Close'].iloc[0]

    print(f"英伟达最新股价：${latest_price:.2f}")