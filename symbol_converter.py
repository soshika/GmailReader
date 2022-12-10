
def find_symbols(input_str):
    split = input_str.split()

    for i in range(len(split)-1):
        if split[i] == 'alert' and split[i+1] == 'was':
            ln = len(split[i-1])
            if ln >= 6 and ln <= 8:
                print(split[i-1])

def converter(symbol):

    symbols = dict()

    symbols['BTCUSDT'] = 'BTC-USDT'
    symbols['MASKUSDT'] = 'MASK-USDT'
    symbols['ETHUSDT'] = 'ETH-USDT'

    return symbols[symbol]