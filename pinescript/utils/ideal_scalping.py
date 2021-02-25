from datetime import datetime

def findBestTrades(ticks, minGain=1, spread=0.3, maxStableBars=None, verbose=False):
    count   = len(ticks)
    skip    = 0
    best_open_times = []
    best_close_times = []

    for i in range(0, count):
        if i<= skip:
            continue
        
        value          = ticks[i].close
        highestTime    = None
        highestValue   = ticks[i].close
        highestN       = i

        for n in range(i+1, count):
            # lower point found
            if ticks[n].close <= value  or ticks[n].close <= highestValue*(1-(minGain/100)):
                break
            if maxStableBars is not None and highestN < n - maxStableBars:
                break

            if ticks[n].close > highestValue:
                highestN     = n
                highestTime  = ticks[n].time
                highestValue = ticks[n].close

        if highestTime is not None:
            gain = (highestValue-value)*100/value
            if gain >= minGain:
                best_open_times.append(ticks[i].time)
                best_close_times.append(highestTime)

                highestValue = highestValue*(1-(spread/200))
                value        = value*(1+(spread/200))
                gain         = (highestValue-value)*100/value
                skip         = highestN
                if verbose:
                    print("Could scalpe from=" + datetime.utcfromtimestamp(ticks[i].time).strftime('%Y-%m-%d %H:%M:%S'), " to=" + datetime.utcfromtimestamp(highestTime).strftime('%Y-%m-%d %H:%M:%S'), " gain=" + str(gain))

    # print("")
    # print(' '.join(best_open_times))
    return best_open_times, best_close_times