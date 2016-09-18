"""This is the unit test class"""
class UnitTest(object):
        
    def __init__(self, func, args, kwargs, res):    # make test
        """ init the class

            Args:
                func: the function to test
                args: the args to the func
                kwargs: more args
                res: the expected value
            Return:
                pass on fail on test
        
        """
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

