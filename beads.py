class beads:
    def __init__(self, SortID=0, r=0, g=0, b=0, trans=False, mixed=False, glow=False, qty=0):
        self._trans = trans
        self._SortID = SortID
        self._r = r
        self._g = g
        self._b = b
        self._trans = trans
        self._mixed = mixed
        self._glow = glow
        self._qty = qty
    
    def r(self, v=None):
        if v: self._r = v
        try: return self._r
        except AttributeError: return None
    
    def g(self, v=None):
        if v: self._g = v
        try: return self._g
        except AttributeError: return None

    def b(self, v=None):
        if v: self._b = v
        try: return self._b
        except AttributeError: return None

    def trans(self, v=None):
        if v: self._trans = v
        try: return self._trans
        except AttributeError: return None

    def mixed(self, v=None):
        if v: self._mixed = v
        try: return self._mixed
        except AttributeError: return None

    def glow(self, v=None):
        if v: self._glow = v
        try: return self._glow
        except AttributeError: return None

    def qty(self, v=None):
        if v: self._qty = v
        try: return self._qty
        except AttributeError: return None

    def stat(self):
        print("R = ", self._r)
        print("G = ", self._g)
        print("B = ", self._b)
        print("Trans = ", self._trans)
        print("Mixed = ", self._mixed)
        print("Glow = ", self._glow)
        print("Qty = ", self._qty)

    def increment(self):
        self._qty = self._qty + 1