# class FloatSerie:
# class ColorSerie:
# class StringSerie:

class IntSerie:
    def __init__(self, list=[]):
        self.values = list

    def __len__(self):
        return len(self.values)

    def __abs__(self):
        res = []
        for x in self.values:
            res.append(abs(x))

        return IntSerie(res)

    def __neg__(self):
        res = []
        for x in self.values:
            res.append(-x)

        return IntSerie(res)

    # def __pos__(self):
    #     return []

    def __pow__(self, b):
        # multiply int type
        if isinstance(b, int):
            res = []
            for x in self.values:
                res.append(pow(x, b))

            return IntSerie(res)

        # multiply with serie
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(pow(self.values[i], b.getInt(i)))

        return IntSerie(res)

    def __add__(self, b):
        # multiply int type
        if isinstance(b, int):
            res = []
            for x in self.values:
                res.append(x + b)

            return IntSerie(res)

        # multiply with serie
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] + b.getInt(i))

        return IntSerie(res)

    def __sub__(self, b):
        # multiply int type
        if isinstance(b, int):
            res = []
            for x in self.values:
                res.append(x - b)

            return IntSerie(res)

        # multiply with serie
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] - b.getInt(i))

        return IntSerie(res)

    def __mod__(self, b):
        # multiply int type
        if isinstance(b, int):
            res = []
            for x in self.values:
                res.append(x % b)

            return IntSerie(res)

        # multiply with serie
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] % b.getInt(i))

        return IntSerie(res)

    def __mul__(self, b):
        # multiply int type
        if isinstance(b, int):
            res = []
            for x in self.values:
                res.append(x * b)

            return IntSerie(res)

        # multiply with serie
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] * b.getInt(i))

        return IntSerie(res)

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

    def __str__(self):
        return str(self.values)

    # def __ceil__(self):
    #     return []

    # def __round__(self):
    #     return []

    # def __floordiv__(self):
    #     return []

    def __eq__(self, b):
        # multiply int type
        if isinstance(b, int):
            res = []
            for x in self.values:
                res.append(x == b)

            return BoolSerie(res)

        # multiply with serie
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] == b.getInt(i))

        return BoolSerie(res)

    def __ne__(self, b):
        # multiply int type
        if isinstance(b, int):
            res = []
            for x in self.values:
                res.append(x != b)

            return BoolSerie(res)

        # multiply with serie
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] != b.getInt(i))

        return BoolSerie(res)

    def __le__(self, b):
        # multiply int type
        if isinstance(b, int):
            res = []
            for x in self.values:
                res.append(x <= b)

            return BoolSerie(res)

        # multiply with serie
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] <= b.getInt(i))

        return BoolSerie(res)

    def __lt__(self, b):
        # multiply int type
        if isinstance(b, int):
            res = []
            for x in self.values:
                res.append(x < b)

            return BoolSerie(res)

        # multiply with serie
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] < b.getInt(i))

        return BoolSerie(res)

    def __ge__(self, b):
        # multiply int type
        if isinstance(b, int):
            res = []
            for x in self.values:
                res.append(x >= b)

            return BoolSerie(res)

        # multiply with serie
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] >= b.getInt(i))

        return BoolSerie(res)

    def __gt__(self, b):
        # multiply int type
        if isinstance(b, int):
            res = []
            for x in self.values:
                res.append(x > b)

            return BoolSerie(res)

        # multiply with serie
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] > b.getInt(i))

        return BoolSerie(res)

    def __getitem__(self, offset):
        res = []
        for i in range(0, len(self.values)):
            if i >= offset:
                res.append(self.values[i])

        return IntSerie(res)

    def getInt(self, i):
        return self.values[i]

    # def getBool(self, i):
    #     return self.values[i]

#  '__index__', '__invert__', '__lshift__','__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

class BoolSerie:
    def __init__(self, list=[]):
        self.values = list

    def __len__(self):
        return len(self.values)

    def __str__(self):
        return str(self.values)

    def __and__(self):
        if isinstance(b, bool):
            res = []
            for x in self.values:
                res.append(x and b)

            return BoolSerie(res)

        # cross series
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] and b.getBool(i))

        return BoolSerie(res)

    def __or__(self):
        if isinstance(b, bool):
            res = []
            for x in self.values:
                res.append(x or b)

            return BoolSerie(res)

        # cross series
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] or b.getBool(i))

        return BoolSerie(res)

    def __eq__(self, b):
        if isinstance(b, bool):
            res = []
            for x in self.values:
                res.append(x == b)

            return BoolSerie(res)

        # cross series
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] == b.getBool(i))

        return BoolSerie(res)

    def __ne__(self, b):
        if isinstance(b, bool):
            res = []
            for x in self.values:
                res.append(x != b)

            return BoolSerie(res)

        # cross series
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] != b.getBool(i))

        return BoolSerie(res)

    def __le__(self, b):
        if isinstance(b, bool):
            res = []
            for x in self.values:
                res.append(x <= b)

            return BoolSerie(res)

        # cross series
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] <= b.getBool(i))

        return BoolSerie(res)

    def __lt__(self, b):
        if isinstance(b, bool):
            res = []
            for x in self.values:
                res.append(x < b)

            return BoolSerie(res)

        # cross series
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] < b.getBool(i))

        return BoolSerie(res)

    def __ge__(self, b):
        if isinstance(b, bool):
            res = []
            for x in self.values:
                res.append(x >= b)

            return BoolSerie(res)

        # cross series
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] >= b.getBool(i))

        return BoolSerie(res)

    def __gt__(self, b):
        if isinstance(b, bool):
            res = []
            for x in self.values:
                res.append(x > b)

            return BoolSerie(res)

        # cross series
        res = []
        l = len(self.values)
        if len(b) < l:
            l  = len(b)

        for i in range(0, l):
            res.append(self.values[i] > b.getBool(i))

        return BoolSerie(res)

    def __getitem__(self, offset):
        res = []
        for i in range(0, len(self.values)):
            if i >= offset:
                res.append(self.values[i])

        return BoolSerie(res)

    def getBool(self, i):
        return self.values[i]