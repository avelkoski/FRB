
from fred.utils import NamespacedClient, query_params
from fred.helpers import _get_request

class TagsClient(NamespacedClient):
    """
    Class for working with FRED tags
    """
    @query_params('realtime_start','realtime_end','limit','offset',
                  'order_by','sort_order','exclude_tag_names')
    def series(self,tag_names=None,response_type=None,params=None):
        """
        Function to request series matching all tags in the tag_names parameter.
        `<https://research.stlouisfed.org/docs/api/fred/category_series.html>`_

        :arg str tag_names: Tag names that series match. Required. Separate with semicolon as in "income;bea"
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 1000
        :arg int offset: Data offset. Options >=0
        :arg str order_by: Order results by values of the specified attribute. Options are 'series_id',
                            'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end',
                            'last_updated', 'observation_start', 'observation_end', 'popularity'
        :arg str sort_order: Sort results for attribute values specified by order_by. Options are 'asc','desc'
        :arg str exclude_tag_names: Tag names used to exclude series. Separate with semicolon as in "income;bea"
        :arg bool ssl_verify: To verify HTTPs.
        :arg dict proxy: Set proxy dictionary. 
        """
        path = '/tags/series?'
        params['tag_names'] = tag_names
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response

    @query_params('realtime_start','realtime_end','limit','offset',
                  'order_by','sort_order','tag_names','tag_group_id','search_text')
    def tags(self,response_type=None,params=None):
        """
        Function to request FRED tags.
        FRED tags are attributes assigned to series.
        `<https://research.stlouisfed.org/docs/api/fred/tags.html>`_

        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 1000
        :arg int offset: Data offset. Options >=0
        :arg str order_by: Order results by values of the specified attribute. Options are 'series_count',
                            'popularity', 'created', 'name', 'group_id'
        :arg str sort_order: Sort results for attribute values specified by order_by. Options are 'asc','desc'
        :arg str tag_names: Tag names to only include in the response. Separate with semicolon as in "income;bea"
        :arg str tag_group_id: Tag ID to filter tags by. Options are 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'
        :arg str search_text: The words to find matching tags with. For example 'mortgage rates'
        :arg bool ssl_verify: To verify HTTPs.
        :arg dict proxy: Set proxy dictionary. 
        """
        path = '/tags?'
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response

    @query_params('realtime_start','realtime_end','limit','offset',
                  'order_by','sort_order','exclude_tag_names','tag_group_id','search_text')
    def related_tags(self,tag_names=None,response_type=None,params=None):
        """
        Function to request FRED related tags.
        FRED tags are attributes assigned to series.
        `<https://research.stlouisfed.org/docs/api/fred/related_tags.html>`_

        :arg str tag_names: Tag names that series match. Required. Separate with semicolon as in "income;bea"
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 1000
        :arg int offset: Data offset. Options >=0
        :arg str order_by: Order results by values of the specified attribute. Options are 'series_count',
                            'popularity', 'created', 'name', 'group_id'
        :arg str sort_order: Sort results for attribute values specified by order_by. Options are 'asc','desc'
        :arg str exclude_tag_names: Tag names to exclude. Separate with semicolon as in "income;bea"
        :arg str tag_group_id: Tag ID to filter tags by. Options are 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'
        :arg str search_text: The words to find matching tags with. For example 'mortgage rates'
        :arg bool ssl_verify: To verify HTTPs.
        :arg dict proxy: Set proxy dictionary. 
        """
        path='/related_tags?'
        params['tag_names'] = tag_names
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response
