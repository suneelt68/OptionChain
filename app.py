from fastapi import FastAPI
from nsepythonserver import nse_quote_ltp

app = FastAPI()

def safe_nse_quote_ltp(symbol, expiry, option_type, strike):
    try:
        return nse_quote_ltp(symbol, expiry, option_type, strike)
    except KeyError:
        # Happens if response JSON structure is unexpected
        return None
    except Exception as e:
        # Catch-all for any other errors
        return None


@app.get("/nse/quote_ltp")
def get_quote_ltp():
    data = {
        "23000": safe_nse_quote_ltp("NIFTY", "30-Sep-2025", "PE", 23000),
        "25800": safe_nse_quote_ltp("NIFTY", "30-Sep-2025", "CE", 25800)
    }
    print(data)
    # Optionally filter out None values if you want
    filtered_data = {k: v for k, v in data.items() if v is not None}
    return filtered_data
