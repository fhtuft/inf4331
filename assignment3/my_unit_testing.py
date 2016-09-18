class UnitTest(object):
        
    def __init__(self, func, args, kwargs, res):    # make test
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.res = res

    def __call__(self):                             # run test

        try:
            if self.func(self.args[0],self.args[1],self.kwargs['num_rechecks']) == self.res:
                return True
            else: 
                return False
        except Exception:
            return False

