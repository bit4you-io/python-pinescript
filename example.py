from pinescript import *

set_context("USDT-BTC", "60", provider="bit4you", apikey="", secret="")

# @version=4
study("Bulk notification", overlay=True)

e = iff(close < close[1], -1, iff(close == close[1], 0, 1))
BCH = security("USDT-BCH", "60", e)
LTC = security("USDT-LTC", "60", e)

up = e == 1 and BCH == 1 and LTC == 1 and close / close[24] > 1.07
down = e == -1 and BCH == -1 and LTC == -1 and close / close[24] < 0.93

lastup = valuewhen(up, float(time), 1)
lastdown = valuewhen(down, float(time), 1)

# bgcolor(lastup < lastdown ? color.red : color.green, transp=60)

print(iff(lastup < lastdown, color.red , color.green))