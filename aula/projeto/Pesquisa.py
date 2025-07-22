import yfinance as yf
import locale

# Define a localidade brasileira para formatação
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def inverter_par(ticker):
    val = yf.Ticker(ticker).info.get("regularMarketPrice")
    if val and val != 0:
        return 1 / val
    return None

def obter_info(ticker):
    t = yf.Ticker(ticker)
    info = t.info
    atual = info.get("regularMarketPrice")
    anterior = info.get("regularMarketPreviousClose")
    if atual is None or anterior is None:
        return None, None, None
    variacao = ((atual - anterior) / anterior) * 100
    return atual, anterior, variacao

def formatar_valor(valor):
    if valor is None:
        return "Dados indisponíveis"
    return locale.format_string('%.2f', valor, grouping=True)

def formatar_variacao(variacao):
    if variacao is None:
        return ""
    sinal = "+" if variacao >= 0 else ""
    return f"({sinal}{variacao:.2f}%)"

# Captura dos dados
vix, _, vix_var = obter_info("^VIX")
dxy, _, dxy_var = obter_info("DX-Y.NYB")
sp500, _, sp500_var = obter_info("^GSPC")
nasdaq, _, nasdaq_var = obter_info("^NDX")
dowjones, _, dowjones_var = obter_info("^DJI")
russell2000, _, russell2000_var = obter_info("^RUT")
nikkei225, _, nikkei225_var = obter_info("^N225")
eurostoxx50, _, eurostoxx50_var = obter_info("^STOXX50E")
dax, _, dax_var = obter_info("^GDAXI")
brent, _, brent_var = obter_info("BZ=F")
wti, _, wti_var = obter_info("CL=F")
gold, _, gold_var = obter_info("GC=F")

# Pares cambiais (base USD)
usdeur_val = inverter_par("EURUSD=X")
usdgbp_val = inverter_par("GBPUSD=X")
usdjpy, _, usdjpy_var = obter_info("JPY=X")
usdcnh, _, usdcnh_var = obter_info("CNH=X")

# Para inverter a variação dos pares invertidos
def inverter_variacao(ticker):
    atual, anterior, variacao = obter_info(ticker)
    if variacao is None:
        return None
    return -variacao  # porque inverte a moeda

usdeur_var = inverter_variacao("EURUSD=X")
usdgbp_var = inverter_variacao("GBPUSD=X")

def classificar_sentimento(vix, dxy, sp500, nasdaq, dowjones, russell2000,
                          nikkei225, eurostoxx50, dax, brent, wti, gold,
                          usdeur, usdgbp, usdjpy, usdcnh):
    score = 0

    if vix < 15: score += 1
    elif vix > 20: score -= 1

    if dxy < 103: score += 1
    elif dxy > 105: score -= 1

    if sp500 > 5000: score += 1
    else: score -= 1

    if nasdaq > 19000: score += 1
    else: score -= 1

    if dowjones > 39000: score += 1
    else: score -= 1

    if russell2000 > 1900: score += 1
    else: score -= 1

    if nikkei225 > 32000: score += 1
    else: score -= 1

    if eurostoxx50 > 4200: score += 1
    else: score -= 1

    if dax > 16000: score += 1
    else: score -= 1

    if brent > 80: score += 1
    else: score -= 1

    if wti > 75: score += 1
    else: score -= 1

    if gold > 1800:
        score += 1
    else:
        score -= 1

    if usdeur and usdeur > 0.85:
        score += 1
    else:
        score -= 1

    if usdgbp and usdgbp > 0.7:
        score += 1
    else:
        score -= 1

    if usdjpy and usdjpy < 130:
        score += 1
    else:
        score -= 1

    if usdcnh and usdcnh < 7.5:
        score += 1
    else:
        score -= 1

    if score >= 0:
        return "😃 Otimista"
    else:
        return "😨 Pessimista"

sentimento = classificar_sentimento(
    vix, dxy, sp500, nasdaq, dowjones, russell2000,
    nikkei225, eurostoxx50, dax, brent, wti, gold,
    usdeur_val, usdgbp_val, usdjpy, usdcnh
)

print("📊 Indicador de Sentimento de Mercado (Tempo Real)")
print(f"VIX: {formatar_valor(vix)} {formatar_variacao(vix_var)}")
print(f"DXY: {formatar_valor(dxy)} {formatar_variacao(dxy_var)}")
print(f"S&P500: {formatar_valor(sp500)} {formatar_variacao(sp500_var)}")
print(f"Nasdaq 100: {formatar_valor(nasdaq)} {formatar_variacao(nasdaq_var)}")
print(f"Dow Jones: {formatar_valor(dowjones)} {formatar_variacao(dowjones_var)}")
print(f"Russell 2000: {formatar_valor(russell2000)} {formatar_variacao(russell2000_var)}")
print(f"Nikkei 225: {formatar_valor(nikkei225)} {formatar_variacao(nikkei225_var)}")
print(f"Euro Stoxx 50: {formatar_valor(eurostoxx50)} {formatar_variacao(eurostoxx50_var)}")
print(f"DAX: {formatar_valor(dax)} {formatar_variacao(dax_var)}")
print(f"Brent: {formatar_valor(brent)} {formatar_variacao(brent_var)}")
print(f"WTI: {formatar_valor(wti)} {formatar_variacao(wti_var)}")
print(f"Ouro (Gold): {formatar_valor(gold)} {formatar_variacao(gold_var)}")
print(f"USD/EUR: {formatar_valor(usdeur_val)} {formatar_variacao(usdeur_var)}")
print(f"USD/GBP: {formatar_valor(usdgbp_val)} {formatar_variacao(usdgbp_var)}")
print(f"USD/JPY: {formatar_valor(usdjpy)} {formatar_variacao(usdjpy_var)}")
print(f"USD/CNH: {formatar_valor(usdcnh)} {formatar_variacao(usdcnh_var)}")
print(f"🧭 Sentimento atual: {sentimento}")
