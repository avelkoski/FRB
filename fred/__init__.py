from fred.clients.categories import CategoriesClient
from fred.clients.releases import ReleasesClient
from fred.clients.tags import TagsClient
from fred.clients.sources import SourcesClient
from fred.clients.eseries import ESeriesClient
import fred.config as c
import weakref

## Establish Federal Reserve Economic Data (Fred) wrapper for Python
class Fred(object):
    """
    Fred client. Provides a straightforward mapping from Python to FRED REST endpoints.
    The instance has attributes ``cateogry``, ``release``, ``series``, ``tag``
    and ``source`` that provide access to instances of
    :class:`fred.clients.categories.CategoriesClient`,
    :class:`fred.clients.releases.ReleasesClient`,
    :class:`fred.clients.eseries.ESeriesClient`,
    :class:`fred.clients.tags.TagsClient` and
    :class:`fred.clients.sources.SourcesClient` respectively. This is the
    preferred (and only supported) way to get access to those classes and their
    methods.

    :arg str api_key: 32 character alpha-numeric lowercase string. Required.
    :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
    :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
    :arg bool ssl_verify: To verify HTTPs.
    """
    def __init__(self,api_key=c.api_key,response_type=c.response_type, ssl_verify=c.ssl_verify):
        ## Set root URL
        self.url_root = 'https://api.stlouisfed.org/fred'
        ## Set default API key
        self.api_key = api_key if api_key else None
        ## Set default file type
        self.response_type = response_type if response_type else None
        ## Set SSL Verify
        self.ssl_verify = ssl_verify
        ## Initiate clients
        self.category = CategoriesClient(weakref.proxy(self),self.api_key,self.url_root,self.response_type,self.ssl_verify)
        self.release = ReleasesClient(weakref.proxy(self),self.api_key,self.url_root,self.response_type,self.ssl_verify)
        self.series = ESeriesClient(weakref.proxy(self),self.api_key,self.url_root,self.response_type,self.ssl_verify)
        self.tag = TagsClient(weakref.proxy(self),self.api_key,self.url_root,self.response_type,self.ssl_verify)
        self.source = SourcesClient(weakref.proxy(self),self.api_key,self.url_root,self.response_type,self.ssl_verify)
