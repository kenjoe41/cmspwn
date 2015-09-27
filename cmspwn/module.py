import os, sys

FOUND = False

if sys.version_info.major >= 3:
    iteritems = dict.items
    itervalues = dict.values
    iterkeys = dict.keys
else:
    iteritems = dict.iteritems
    itervalues = dict.itervalues
    iterkeys = dict.iterkeys

class Modules:

    def __init__(self):
        self.modules = {}

    def get_modules(self):
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        #print cur_dir; return
        modules_dir = os.path.join(cur_dir, 'modules')
        #print modules_dir;return
        for fn in os.listdir(modules_dir):
            if fn.endswith('.py') and not fn.startswith('_'):
                #save filepath without the extension
                self.modules[fn[:-3]] = os.path.join(modules_dir, fn)
        return self.modules

#def pwnfunc(func):
 #   """Decorator for functions that process html.
  #  """
   # def add_attribute(func):
    #    func.cms = True
     #   return function
#    return add_attribute

def pwnfunc(_cms=None):
    def wrapper(func):
        setattr(func, 'cms', True)
        return func
    #hack not to have a _cms arg
    if callable(_cms):
        return wrapper(_cms)
    return wrapper
