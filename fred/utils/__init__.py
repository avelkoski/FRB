
from functools import wraps

def query_params(*frb_fred_params):
    """
    Decorator that pops all accepted parameters from method's kwargs and puts
    them in the params argument. Modeled after elasticsearch-py client utils strategy.
    See https://github.com/elastic/elasticsearch-py/blob/3400179153cc13b6ae2c26734337202569bdfd80/elasticsearch/client/utils.py
    """
    def _wrapper(func):
        @wraps(func)
        def _wrapped(*args, **kwargs):
            params = kwargs.pop('params', {})
            for p in frb_fred_params:
                if p in kwargs:
                    params[p] = kwargs.pop(p)
            return func(*args,params=params,**kwargs)
        return _wrapped
    return _wrapper

class NamespacedClient(object):
    """
    Class for working with FRED categories
    """
    def __init__(self,client,api_key,url_root,response_type,ssl_verify):
        self.client = client
        self.api_key = api_key
        self.url_root = url_root
        self.response_type = response_type
        self.ssl_verify = ssl_verify
