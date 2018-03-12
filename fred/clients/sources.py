
from fred.utils import NamespacedClient, query_params
from fred.helpers import _get_request

class SourcesClient(NamespacedClient):
    """
    Class for working with FRED sources
    """
    @query_params('realtime_start','realtime_end')
    def details(self,source_id=None,response_type=None,params=None):
        """
        Function to request a particular source of economic data.
        `<https://research.stlouisfed.org/docs/api/fred/source.html>`_

        :arg int source_id: The id for a source. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg bool ssl_verify: To verify HTTPs.
        """
        path='/source?'
        params['source_id'] = source_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify)
        return response

    @query_params('realtime_start','realtime_end','limit',
                  'offset','sort_order','order_by')
    def sources(self,response_type=None,params=None):
        """
        Function to request all sources of economic data.
        `<https://research.stlouisfed.org/docs/api/fred/sources.html>`_

        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 1000
        :arg int offset: Data offset. Options >=0
        :arg str order_by: Order results by values of the specified attribute. Options are 'source_id',
                            'name', 'realtime_start', 'realtime_end'
        :arg str sort_order: Sort results for attribute values specified by order_by. Options are 'asc','desc'
        :arg bool ssl_verify: To verify HTTPs.
        """
        path='/sources?'
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify)
        return response

    @query_params('realtime_start','realtime_end','limit','offset',
                  'order_by','sort_order')
    def releases(self,source_id=None,response_type=None,params=None):
        """
        Function to request all releases of economic data.
        `<https://research.stlouisfed.org/docs/api/fred/releases.html>`_

        :arg int source_id: The id for a source. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 1000
        :arg int offset: Data offset. Options >=0
        :arg str order_by: Order results by values of the specified attribute. Options are 'source_id',
                            'name', 'realtime_start', 'realtime_end'
        :arg str sort_order: Sort results for attribute values specified by order_by. Options are 'asc','desc'
        :arg bool ssl_verify: To verify HTTPs.
        """
        path='/source/releases?'
        params['source_id'] = source_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify)
        return response
