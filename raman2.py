
class myclass():
    def __init__(self, apt, bpt) -> None:
        self._ap = apt
        self._bp = bpt
    
    @property
    def apt(self):
        print('aya')
        return self._ap
    
    @property
    def bpt(self):
        print('aya')
        return self._bp
    
    def some_meth(self):
        sum = self.apt + self.bpt
        print(sum)
        return sum


a = myclass(1, 2)
b = a.some_meth()
print('b = ', b)
    