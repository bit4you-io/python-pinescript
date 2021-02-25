import matplotlib.pyplot as plt

class plot:
    style_area = 0
    style_areabr = 0
    style_circles = 0
    style_columns = 0
    style_cross = 0
    style_histogram = 0
    style_line = 0
    style_linebr = 0
    style_stepline = 0

    def __init__(self, series, title="", color="#000", linewidth=1, style=None, trackprice=False, transp=100, histbase=0.0, offset=0, join=False, editable=True, show_last=None, display=1):
        if offset > 0:
            series = series[offset]

        plt.plot(series.values)

def showPlot():
    plt.show()

# plotarrow
# plotbar
# plotcandle
# plotchar
# plotshape
# bgcolor
# barcolor
# fill

# line
# line.delete
# line.get_price
# line.get_x1
# line.get_x2
# line.get_y1
# line.get_y2
# line.new
# line.set_color
# line.set_extend
# line.set_style
# line.set_width
# line.set_x1
# line.set_x2
# line.set_xloc
# line.set_xy1
# line.set_xy2
# line.set_y1
# line.set_y2

# label
# label.delete
# label.get_text
# label.get_x
# label.get_y
# label.new
# label.set_color
# label.set_size
# label.set_style
# label.set_text
# label.set_textalign
# label.set_textcolor
# label.set_tooltip
# label.set_x
# label.set_xloc
# label.set_xy
# label.set_y
# label.set_yloc