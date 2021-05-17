class checker(object):
    
    def __init__(self):
        self.viewers = []
    
    def record(self, viewer_info):
        if not viewer_info in self.viewers:
            self.viewers.append(viewer_info)
    
    def unrecord(self, viewer_info):
        if viewer_info in self.viewers:
            self.viewers.remove(viewer_info)
    
    def unrecord_all(self):
        if self.viewers:
            del self.viewers[:]
            
    def refresh_viewers(self, *m, **n):
        for viewer_info in self.viewers:
            viewer_info.refresh(*m, **n)

# abstract viewer_info class
class viewer(object):
    
    def refresh(self, *m, **n):
        pass

# concrete viewer_info subclasses
class stock_pl(viewer):
    def refresh(self, *m, **n):
        print('Poland received: {0}\n{1}'.format(m, n))

class stcok_rw(viewer):
    def refresh(self, *m, **n):
        print('Rwanda received: {0}\n{1}'.format(m, n))

if __name__ == '__main__':
    the_biggest = checker()
    pl_viewer = stock_pl()
    rw_viewer = stcok_rw()
    
    the_biggest.record(pl_viewer)
    the_biggest.record(rw_viewer)
    the_biggest.refresh_viewers('it is urgent please refresh', msg='please go to board meeting')
