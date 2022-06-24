class numeros:
    def _init_ (self, Real, Imaginario):
        self.Real=Real
        self.Imaginario=Imaginario
    def suma (self, other):
        c=self.Real+other.Real
        d=self.Imaginario+other.Imaginario
        return c+d
    def resta (self, other):
        c=self.Real+other.Real
        d=self.Imaginario+other.Imaginario
        return c-d
    def cociente (self, other):
        a=self.Real
        b=self.Imaginario
        c=other.Real
        d=other.Imaginario
        j=-1*d
        e=a*c
        f=b*j
        g=c*c
        h=d*j
        k=e+f
        l=g+h
        return k/l
    def norma (self):
        a=self.Real
        b=self.Imaginario
        c=a*a
        d=b*b*-1
        e=c+d
        f=e**(1/2)
        return f
    def producto (self, other):
        a=self.Real
        b=self.Imaginario
        c=other.Real
        d=other.Imaginario
        e=(a*c)+(b*d)
        f=(a*d)+(b*c)
        return e+f
        
    