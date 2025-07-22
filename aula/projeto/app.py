from flask import Flask, jsonify, render_template
import yfinance as yf
import locale

# Formatação brasileira
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

app = Flask(__name__)

def obter_info(ticker):
    t = yf.Ticker(ticker)
    info = t.info
    atual = info.get("regularMarketPrice")
    anterior = info.get("regularMarketPreviousClose")
    maximo = info.get("dayHigh")
    minimo = info.get("dayLow")
    if atual is None or anterior is None:
        return None, None, None, None, None
    variacao = ((atual - anterior) / anterior) * 100
    return atual, anterior, variacao, maximo, minimo

def formatar_valor(valor):
    if valor is None:
        return "–"
    return locale.format_string('%.2f', valor, grouping=True)

def formatar_variacao(variacao):
    if variacao is None:
        return ""
    sinal = "+" if variacao >= 0 else ""
    return f"{sinal}{variacao:.2f}%"

def classificar_sentimento(vix, dxy, sp500, nasdaq, dowjones, russell2000,
                            nikkei225, eurostoxx50, dax, brent, wti, gold,
                            usdeur, usdgbp, usdjpy, usdcnh):
    score = 0

    if vix and vix < 15: score += 1
    elif vix and vix > 20: score -= 1

    if dxy and dxy < 103: score += 1
    elif dxy and dxy > 105: score -= 1

    if sp500 and sp500 > 5000: score += 1
    else: score -= 1

    if nasdaq and nasdaq > 19000: score += 1
    else: score -= 1

    if dowjones and dowjones > 39000: score += 1
    else: score -= 1

    if russell2000 and russell2000 > 1900: score += 1
    else: score -= 1

    if nikkei225 and nikkei225 > 32000: score += 1
    else: score -= 1

    if eurostoxx50 and eurostoxx50 > 4200: score += 1
    else: score -= 1

    if dax and dax > 16000: score += 1
    else: score -= 1

    if brent and brent > 80: score += 1
    else: score -= 1

    if wti and wti > 75: score += 1
    else: score -= 1

    if gold and gold > 1800: score += 1
    else: score -= 1

    if usdeur and usdeur > 0.85: score += 1
    else: score -= 1

    if usdgbp and usdgbp > 0.7: score += 1
    else: score -= 1

    if usdjpy and usdjpy < 130: score += 1
    else: score -= 1

    if usdcnh and usdcnh < 7.5: score += 1
    else: score -= 1

    return "😃 Otimista" if score >= 0 else "😨 Pessimista"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dados')
def dados():
    tickers = {
        "VIX": "^VIX",
        "DXY": "DX-Y.NYB",
        "S&P500": "^GSPC",
        "Nasdaq100": "^NDX",
        "DowJones": "^DJI",
        "Russell2000": "^RUT",
        "Nikkei225": "^N225",
        "EuroStoxx50": "^STOXX50E",
        "DAX": "^GDAXI",
        "Brent": "BZ=F",
        "WTI": "CL=F",
        "Gold": "GC=F",
        "USDJPY": "JPY=X",
        "USDCNH": "CNH=X",
    }

    data = {}
    valores_sentimento = {}

    for key, ticker in tickers.items():
        atual, anterior, variacao, maximo, minimo = obter_info(ticker)
        data[key] = {
            "valor": formatar_valor(atual),
            "variacao": formatar_variacao(variacao),
            "maximo": formatar_valor(maximo),
            "minimo": formatar_valor(minimo)
        }
        valores_sentimento[key] = atual

    # Câmbio invertido
    eurusd_atual, eurusd_anterior, eurusd_var, eurusd_max, eurusd_min = obter_info("EURUSD=X")
    gbpusd_atual, gbpusd_anterior, gbpusd_var, gbpusd_max, gbpusd_min = obter_info("GBPUSD=X")

    usd_eur_val = 1 / eurusd_atual if eurusd_atual else None
    usd_eur_var = -eurusd_var if eurusd_var is not None else None

    usd_gbp_val = 1 / gbpusd_atual if gbpusd_atual else None
    usd_gbp_var = -gbpusd_var if gbpusd_var is not None else None

    data["USDEUR"] = {
        "valor": formatar_valor(usd_eur_val),
        "variacao": formatar_variacao(usd_eur_var),
        "maximo": "–",
        "minimo": "–"
    }
    data["USDGBP"] = {
        "valor": formatar_valor(usd_gbp_val),
        "variacao": formatar_variacao(usd_gbp_var),
        "maximo": "–",
        "minimo": "–"
    }

    valores_sentimento["USDEUR"] = usd_eur_val
    valores_sentimento["USDGBP"] = usd_gbp_val

    sentimento = classificar_sentimento(
        valores_sentimento.get("VIX"),
        valores_sentimento.get("DXY"),
        valores_sentimento.get("S&P500"),
        valores_sentimento.get("Nasdaq100"),
        valores_sentimento.get("DowJones"),
        valores_sentimento.get("Russell2000"),
        valores_sentimento.get("Nikkei225"),
        valores_sentimento.get("EuroStoxx50"),
        valores_sentimento.get("DAX"),
        valores_sentimento.get("Brent"),
        valores_sentimento.get("WTI"),
        valores_sentimento.get("Gold"),
        valores_sentimento.get("USDEUR"),
        valores_sentimento.get("USDGBP"),
        valores_sentimento.get("USDJPY"),
        valores_sentimento.get("USDCNH"),
    )

    return jsonify({"dados": data, "sentimento": sentimento})

if __name__ == '__main__':
    app.run(debug=True)
