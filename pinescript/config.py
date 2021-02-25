from .utils.context import context
from .variables import *

def study(title="", shorttitle="", overlay=False, format="inherit", precision=1, scale="none", max_bars_back=None, resolution=None):
    context.set("title", title)
    context.set("shorttitle", shorttitle)
    context.set("overlay", overlay)
    context.set("format", format)
    context.set("precision", precision)
    context.set("scale", scale)
    context.set("max_bars_back", max_bars_back)
    context.set("resolution", resolution)

    print("Study created " + title)

def input(defval, title): #, type, minval, maxval, confirm, step, options):
    return defval

class strategy:
    # variables:
    cash="cash"
    # strategy.closedtrades
    class commission:
        cash_per_contract="cash_per_contract"
        cash_per_order="cash_per_order"
        percent="percent"

    # strategy.direction.all
    # strategy.direction.long
    # strategy.direction.short
    # strategy.equity
    # strategy.eventrades
    # strategy.fixed
    # strategy.grossloss
    # strategy.grossprofit
    # strategy.initial_capital
    # strategy.long
    # strategy.losstrades
    # strategy.max_contracts_held_all
    # strategy.max_contracts_held_long
    # strategy.max_contracts_held_short
    # strategy.max_drawdown
    # strategy.netprofit
    # strategy.oca.cancel
    # strategy.oca.none
    # strategy.oca.reduce
    # strategy.openprofit
    # strategy.opentrades
    # strategy.percent_of_equity
    # strategy.position_avg_price
    # strategy.position_entry_name
    # strategy.position_size
    # strategy.short
    # strategy.wintrades

    def __init__(self, title, shorttitle=None, overlay=False, format="inherit", precision="price", scale=None, pyramiding=0, calc_on_order_fills=False, calc_on_every_tick=False, max_bars_back=None, backtest_fill_limits_assumption=None, default_qty_type="fixed", default_qty_value=0, initial_capital=100000, currency="USD", slippage=None, commission_type=None, commission_value=0, process_orders_on_close=False, close_entries_rule="FIFO"):
        context.set("title", title)
        context.set("shorttitle", shorttitle)
        context.set("overlay", overlay)
        context.set("format", format)
        context.set("precision", precision)
        context.set("scale", scale)
        context.set("pyramiding", pyramiding)
        context.set("calc_on_order_fills", calc_on_order_fills)
        context.set("calc_on_every_tick", calc_on_every_tick)
        context.set("max_bars_back", max_bars_back)
        context.set("backtest_fill_limits_assumption", backtest_fill_limits_assumption)
        context.set("default_qty_type", default_qty_type)
        context.set("default_qty_value", default_qty_value)
        context.set("initial_capital", initial_capital)
        context.set("currency", currency)
        context.set("slippage", slippage)
        context.set("commission_type", commission_type)
        context.set("commission_value", commission_value)
        context.set("process_orders_on_close", process_orders_on_close)
        context.set("close_entries_rule", close_entries_rule)

        context.strategy.set(self)
        print("Strategy created", title)

    # strategy pinescript methods:

    def entry(id, long, qty=None, limit=None, stop=None, oca_name="", oca_type="", comment=None, when=None, alert_message=None):
        return ""

    def exit(id, from_entry, qty=None, qty_percent=None, profit=None, limit=None, loss=None, stop=None, trail_price=None, trail_points=None, trail_offset=None, oca_name=None, comment=None, when=None, alert_message=None):
        return ""

    # methods:
    # cancel
    # cancel_all
    # close
    # close_all
    # order
    # risk.allow_entry_in
    # risk.max_cons_loss_days
    # risk.max_drawdown
    # risk.max_intraday_filled_orders
    # risk.max_intraday_loss
    # risk.max_position_size


# switch security context
__securityContextes = {}
def security(symbol, resolution, expression, gaps=barmerge.gaps_off, lookahead=barmerge.lookahead_off):
    if isinstance(symbol, ContextVar):
        symbol = str(symbol.get())
    if isinstance(resolution, ContextVar):
        symbol = str(resolution.get())

    id = symbol + resolution
    ctx = None
    if id in __securityContextes:
        ctx = __securityContextes[id]
    else:
        ctx = context.copy()
        ctx.run(lambda: set_context(symbol, resolution))
        __securityContextes[id] = ctx

    return __context_var(expression, ctx)

# attach values to variabless
def set_context(iso, resolution, provider="bit4you", apikey=None, secret=None):
    syminfo.tickerid.set(iso)

    if resolution == "1":
        close.set(IntSerie([ 1, 2, 8, 4 ]))
    else:
        close.set(IntSerie([ 11, 12, 18, 14 ]))
        syminfo.tickerid.set(str(iso) + "5")
    # open = IntSerie([ 8, 1, 9, 3 ])
    # volume = IntSerie([ 8, 1, 9, 3 ])
    # low = IntSerie([ 8, 1, 9, 3 ])
    # high = IntSerie([ 8, 1, 9, 3 ])

# -----

# todo cache data to prevent context switching
class __context_var:
    def __init__(self, var, ctx=None):
        self.__var = var
        self.__ctx = ctx

    def __run(self, cb):
        if self.__ctx == None:
            return cb(self.__var)

        if isinstance(self.__var, ContextVar):
            def run():
                return cb(self.__var.get())

            return self.__ctx.run(run)

        return self.__ctx.run(cb, self.__var)

    def __value(item):
        if isinstance(item, ContextVar):
            return item.get()

        return item

    def __len__(self):
        return self.__run(lambda val: len(val))

    def __str__(self):
        return self.__run(lambda val: str(val))

    # def __and__(self):
    #     if isinstance(b, bool):
    #         res = []
    #         for x in self.values:
    #             res.append(x and b)

    #         return BoolSerie(res)

    #     # cross series
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] and b.getBool(i))

    #     return BoolSerie(res)

    # def __or__(self):
    #     if isinstance(b, bool):
    #         res = []
    #         for x in self.values:
    #             res.append(x or b)

    #         return BoolSerie(res)

    #     # cross series
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] or b.getBool(i))

    #     return BoolSerie(res)

    # def __eq__(self, b):
    #     if isinstance(b, bool):
    #         res = []
    #         for x in self.values:
    #             res.append(x == b)

    #         return BoolSerie(res)

    #     # cross series
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] == b.getBool(i))

    #     return BoolSerie(res)

    # def __ne__(self, b):
    #     if isinstance(b, bool):
    #         res = []
    #         for x in self.values:
    #             res.append(x != b)

    #         return BoolSerie(res)

    #     # cross series
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] != b.getBool(i))

    #     return BoolSerie(res)

    # def __le__(self, b):
    #     if isinstance(b, bool):
    #         res = []
    #         for x in self.values:
    #             res.append(x <= b)

    #         return BoolSerie(res)

    #     # cross series
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] <= b.getBool(i))

    #     return BoolSerie(res)

    # def __lt__(self, b):
    #     if isinstance(b, bool):
    #         res = []
    #         for x in self.values:
    #             res.append(x < b)

    #         return BoolSerie(res)

    #     # cross series
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] < b.getBool(i))

    #     return BoolSerie(res)

    # def __ge__(self, b):
    #     if isinstance(b, bool):
    #         res = []
    #         for x in self.values:
    #             res.append(x >= b)

    #         return BoolSerie(res)

    #     # cross series
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] >= b.getBool(i))

    #     return BoolSerie(res)

    # def __gt__(self, b):
    #     if isinstance(b, bool):
    #         res = []
    #         for x in self.values:
    #             res.append(x > b)

    #         return BoolSerie(res)

    #     # cross series
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] > b.getBool(i))

    #     return BoolSerie(res)

    # def __getitem__(self, offset):
    #     res = []
    #     for i in range(0, len(self.values)):
    #         if i >= offset:
    #             res.append(self.values[i])

    #     return BoolSerie(res)

    # def getBool(self, i):
    #     return self.values[i]

    # def __abs__(self):
    #     res = []
    #     for x in self.values:
    #         res.append(abs(x))

    #     return IntSerie(res)

    # def __neg__(self):
    #     res = []
    #     for x in self.values:
    #         res.append(-x)

    #     return IntSerie(res)

    # def __pos__(self):
    #     return []

    # def __pow__(self, b):
    #     # multiply int type
    #     if isinstance(b, int):
    #         res = []
    #         for x in self.values:
    #             res.append(pow(x, b))

    #         return IntSerie(res)

    #     # multiply with serie
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(pow(self.values[i], b.getInt(i)))

    #     return IntSerie(res)

    def __add__(self, b):
        return self.__run(lambda val: val + __context_var.__value(b))

    # def __sub__(self, b):
    #     # multiply int type
    #     if isinstance(b, int):
    #         res = []
    #         for x in self.values:
    #             res.append(x - b)

    #         return IntSerie(res)

    #     # multiply with serie
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] - b.getInt(i))

    #     return IntSerie(res)

    # def __mod__(self, b):
    #     # multiply int type
    #     if isinstance(b, int):
    #         res = []
    #         for x in self.values:
    #             res.append(x % b)

    #         return IntSerie(res)

    #     # multiply with serie
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] % b.getInt(i))

    #     return IntSerie(res)

    # def __mul__(self, b):
    #     # multiply int type
    #     if isinstance(b, int):
    #         res = []
    #         for x in self.values:
    #             res.append(x * b)

    #         return IntSerie(res)

    #     # multiply with serie
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] * b.getInt(i))

    #     return IntSerie(res)

    # def __and__(self):
    #     return []

    # def __or__(self):
    #     return []

    # def __bool__(self):
    #     return []

    # def __float__(self):
    #     return []

    # def __float__(self):
    #     return []

    # def __int__(self):
    #     return []

    # def __ceil__(self):
    #     return []

    # def __round__(self):
    #     return []

    # def __floordiv__(self):
    #     return []

    # def __eq__(self, b):
    #     # multiply int type
    #     if isinstance(b, int):
    #         res = []
    #         for x in self.values:
    #             res.append(x == b)

    #         return BoolSerie(res)

    #     # multiply with serie
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] == b.getInt(i))

    #     return BoolSerie(res)

    # def __ne__(self, b):
    #     # multiply int type
    #     if isinstance(b, int):
    #         res = []
    #         for x in self.values:
    #             res.append(x != b)

    #         return BoolSerie(res)

    #     # multiply with serie
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] != b.getInt(i))

    #     return BoolSerie(res)

    # def __le__(self, b):
    #     # multiply int type
    #     if isinstance(b, int):
    #         res = []
    #         for x in self.values:
    #             res.append(x <= b)

    #         return BoolSerie(res)

    #     # multiply with serie
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] <= b.getInt(i))

    #     return BoolSerie(res)

    # def __lt__(self, b):
    #     # multiply int type
    #     if isinstance(b, int):
    #         res = []
    #         for x in self.values:
    #             res.append(x < b)

    #         return BoolSerie(res)

    #     # multiply with serie
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] < b.getInt(i))

    #     return BoolSerie(res)

    # def __ge__(self, b):
    #     # multiply int type
    #     if isinstance(b, int):
    #         res = []
    #         for x in self.values:
    #             res.append(x >= b)

    #         return BoolSerie(res)

    #     # multiply with serie
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] >= b.getInt(i))

    #     return BoolSerie(res)

    # def __gt__(self, b):
    #     # multiply int type
    #     if isinstance(b, int):
    #         res = []
    #         for x in self.values:
    #             res.append(x > b)

    #         return BoolSerie(res)

    #     # multiply with serie
    #     res = []
    #     l = len(self.values)
    #     if len(b) < l:
    #         l  = len(b)

    #     for i in range(0, l):
    #         res.append(self.values[i] > b.getInt(i))

    #     return BoolSerie(res)

    # def __getitem__(self, offset):
    #     res = []
    #     for i in range(0, len(self.values)):
    #         if i >= offset:
    #             res.append(self.values[i])

    #     return IntSerie(res)