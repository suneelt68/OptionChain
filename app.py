from fastapi import FastAPI
from nsepythonserver import nse_quote_ltp

app = FastAPI()

data = {
    "23000": nse_quote_ltp("NIFTY", "30-Sep-2025", "PE", 23000),
    "25800": nse_quote_ltp("NIFTY", "30-Sep-2025", "CE", 25800)
}
print(data)
@app.get("/nse/quote_ltp")
def get_quote_ltp():
    return data
    
