def tickers_to_dict(filename):
    resultaat = {}
    tickers_tekst = open(filename, 'r')

    ticker_lines = tickers_tekst.readlines()
    for line in ticker_lines:
        gesplitst = line.split(':')
        naam = gesplitst[0].strip()
        afkorting = gesplitst[1].strip()
        resultaat[naam] = afkorting

    tickers_tekst.close()
    return resultaat


def name_to_symbol(name, ticker_dict):
    if name not in ticker_dict.keys():
        return None

    return ticker_dict[name]


def symbol_to_name(symbol, ticker_dict):
    for key, value in ticker_dict.items():
        if symbol == value:
            return key

    return None


naam_afkorting = tickers_to_dict('8_4_tickers.txt')

print(name_to_symbol('bestaat_niet', naam_afkorting))
print(symbol_to_name('bestaat_niet', naam_afkorting))
print(name_to_symbol('YAHOO', naam_afkorting))
print(symbol_to_name('BUD', naam_afkorting))