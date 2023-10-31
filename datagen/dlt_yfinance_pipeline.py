import dlt
import yfinance as yf

def main():
    stocks = ["AAPL", "TSLA", "MSFT", "GOOG", "NVDA"]

    dataframes = [yf.Ticker(stock).history(period="2y").assign(symbol=stock) for stock in stocks]

    pipeline = dlt.pipeline(
            pipeline_name="yfinance", 
            destination="duckdb",
            dataset_name="raw"
        )

    load_info = pipeline.run(
                        dataframes,
                        write_disposition="merge",
                        primary_key=("symbol", "date"),
                        table_name="stock_history"
                )

    print(load_info)

if __name__ == "__main__":
    main()