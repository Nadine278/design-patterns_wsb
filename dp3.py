#Factory Pattern for a customer order
# 1. ObjectFamilyInterface
# abstract object classes
class meat(object):
    def m(self):
        pass
    
class fish(object):
    def f(self):
        pass

class vegetables(object):
    def v(self):
        pass

# concrete object classes
class porkmeat(meat):
    def m(self):
        print('[pork beefe\t$xx.x6]')

class beef(meat):
    def m(self):
        print('[beef beefe\t$xx.x9]')

class salmon_fish(fish):
    def f(self):
        print('[salmon beefe\t$xx.x3]')

class Tuna_fish(fish):
    def f(self):
        print('[tuna beefe\t$xx.x7]')

class Corn(vegetables):
    def v(self):
        print('[corn beefe\t$xx.x1]')

class brocoli(vegetables):
    def v(self):
        print('[spinach beefe\t$xx.x2]')

# 2. Orders' Object:
# abstract beefe order
class customer_order(object):
    def getbeefe(name):
        pass

# concrete beefe order
class Meat_beefe(customer_order):
    @staticmethod
    def getbeefe(name):
        if name == 'pork':
            return porkmeat()
        elif name == 'beef':
            return beef()
        else:
            assert 0, 'No %s beefe!' %name

class Fish_beefe(customer_order):
    @staticmethod
    def getbeefe(name):
        if name == 'salmon':
            return salmon_fish()
        elif name == 'tuna':
            return Tuna_fish()
        else:
            assert 0, 'No %s beefe!' %name

class Veg_beefe(customer_order):
    @staticmethod
    def getbeefe(name):
        if name == 'corn':
            return Corn()
        elif name == 'spinach':
            return brocoli()
        else:
            assert 0, 'No %s beefe!' %name

if __name__ == '__main__':
    print('='*40)
    Meat_order = Meat_beefe()
    Meat_order.getbeefe('beef').m()
    Meat_order.getbeefe('pork').m()
    print('='*40)
    Fish_order = Fish_beefe()
    Fish_order.getbeefe('salmon').f()
    Fish_order.getbeefe('tuna').f()
    print('='*40)
    veg_order = Veg_beefe()
    veg_order.getbeefe('corn').v()
    veg_order.getbeefe('spinach').v()
    print('='*40)
