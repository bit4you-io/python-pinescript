from .series import *
from contextvars import ContextVar

close = ContextVar("close")
# IntSerie([ 1, 2, 8, 4 ])
open = IntSerie([ 8, 1, 9, 3 ])
volume = IntSerie([ 8, 1, 9, 3 ])
low = IntSerie([ 8, 1, 9, 3 ])
high = IntSerie([ 8, 1, 9, 3 ])

class syminfo:
    basecurrency = ContextVar("basecurrency", default="USD")
    currency     = ContextVar("currency", default="USD")
    description  = ContextVar("description", default="")
    mintick      = ContextVar("mintick")
    pointvalue   = ContextVar("pointvalue")
    prefix       = ContextVar("prefix")
    root         = ContextVar("root")
    session      = ContextVar("session")
    ticker       = ContextVar("ticker")
    tickerid     = ContextVar("tickerid")
    timezone     = ContextVar("timezone")
    type         = ContextVar("type")

# accdist
# adjustment.dividends
# adjustment.none
# adjustment.splits
# bar_index
class barmerge:
    gaps_off = False
    gaps_on = True

    lookahead_off = False
    lookahead_on = False

# barstate.isconfirmed
# barstate.isfirst
# barstate.ishistory
# barstate.islast
# barstate.isnew
# barstate.isrealtime

class currency:
    AUD = "AUD"
    CAD = "CAD"
    CHF = "CHF"
    EUR = "EUR"
    GBP = "GBP"
    HKD = "HKD"
    JPY = "JPY"
    NOK = "NOK"
    NONE = None
    NZD = "NZD"
    RUB = "RUB"
    SEK = "SEK"
    SGD = "SGD"
    TRY = "TRY"
    USD = "USD"
    ZAR = "ZAR"

# dayofmonth
# dayofweek
# dayofweek.friday
# dayofweek.monday
# dayofweek.saturday
# dayofweek.sunday
# dayofweek.thursday
# dayofweek.tuesday
# dayofweek.wednesday

class display:
    all = 1
    none = 0

# extend.both
# extend.left
# extend.none
# extend.right

class format:
    inherit = "inherit"
    price = "price"
    volume = "volume"

# high
# hl2
# hlc3
# hline.style_dashed
# hline.style_dotted
# hline.style_solid
# hour
# iii
# input.bool
# input.color
# input.float
# input.integer
# input.resolution
# input.session
# input.source
# input.string
# input.symbol
# label.style_arrowdown
# label.style_arrowup
# label.style_circle
# label.style_cross
# label.style_diamond
# label.style_flag
# label.style_label_center
# label.style_label_down
# label.style_label_left
# label.style_label_lower_left
# label.style_label_lower_right
# label.style_label_right
# label.style_label_up
# label.style_label_upper_left
# label.style_label_upper_right
# label.style_none
# label.style_square
# label.style_triangledown
# label.style_triangleup
# label.style_xcross
# line.style_arrow_both
# line.style_arrow_left
# line.style_arrow_right
# line.style_dashed
# line.style_dotted
# line.style_solid
# location.abovebar
# location.absolute
# location.belowbar
# location.bottom
# location.top
# low
# minute
# month
# na
# nvi
# obv
# ohlc4
# open
# order.ascending
# order.descending
# pvi
# pvt
# scale.left
# scale.none
# scale.right
# second
# session.extended
# session.regular
# shape.arrowdown
# shape.arrowup
# shape.circle
# shape.cross
# shape.diamond
# shape.flag
# shape.labeldown
# shape.labelup
# shape.square
# shape.triangledown
# shape.triangleup
# shape.xcross
# size.auto
# size.huge
# size.large
# size.normal
# size.small
# size.tiny


# text.align_center
# text.align_left
# text.align_right
# time
# time_close
# timeframe.isdaily
# timeframe.isdwm
# timeframe.isintraday
# timeframe.isminutes
# timeframe.ismonthly
# timeframe.isseconds
# timeframe.isweekly
# timeframe.multiplier
# timeframe.period
# timenow
# tr
# volume
# vwap
# wad
# weekofyear
# wvad
# xloc.bar_index
# xloc.bar_time
# year
# yloc.abovebar
# yloc.belowbar
# yloc.price

class color:
    aqua = "#00BCD4"
    black = "#363A45"
    blue = "#2196F3"
    fuchsia = "#E040FB"
    gray = "#787B86"
    green = "#4CAF50"
    lime = "#00E676"
    maroon = "#880E4F"
    navy = "#311B92"
    olive = "#808000"
    orange = "#FF9800"
    purple = "#9C27B0"
    red = "#FF5252"
    silver = "#B2B5BE"
    teal = "#00897B"
    white = "#FFFFFF"
    yellow = "#FFEB3B"

    def new(color, transp=100):
        return color

    def __init__(self, color):
        self.hex = color

    def __str__(self):
        return self.hex