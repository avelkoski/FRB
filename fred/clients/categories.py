
from fred.utils import NamespacedClient, query_params
from fred.helpers import _get_request

class CategoriesClient(NamespacedClient):
    """
    Class for working with FRED categories
    """
    @query_params()
    def details(self,category_id=None,response_type=None,params=None):
        """
        Function to request a particular category's high-level details
        `<https://research.stlouisfed.org/docs/api/fred/category.html>`_

        :arg int category_id: The id for a category. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg bool ssl_verify: To verify HTTPs.
        :arg dict proxy: Set proxy dictionary. 
        """
        path='/category?'
        params['category_id'] = category_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response

    @query_params('realtime_start','realtime_end')
    def children(self,category_id=None,response_type=None,params=None):
        """
        Function to request a particular category's children
        `<https://research.stlouisfed.org/docs/api/fred/category_children.html>`_

        :arg int category_id: The id for a category. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg bool ssl_verify: To verify HTTPs.
        :arg dict proxy: Set proxy dictionary. 
        """
        path='/category/children?'
        params['category_id'] = category_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response

    @query_params('realtime_start','realtime_end')
    def related(self,category_id=None,response_type=None,params=None):
        """
        Function to request a particular category's related categories.
        Related categories are A related category is a one-way relation between 2 categories
        that is not part of a parent-child category hierarchy.
        Most categories do not have related categories.
        `<https://research.stlouisfed.org/docs/api/fred/category_related.html>`_

        :arg int category_id: The id for a category. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg bool ssl_verify: To verify HTTPs.
        :arg dict proxy: Set proxy dictionary. 
        """
        path = '/category/related?'
        params['category_id'] = category_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response

    @query_params('realtime_start','realtime_end','limit','offset',
                  'order_by','sort_order','filter_variable', 'filter_value',
                  'tag_names','exclude_tag_names')
    def series(self,category_id=None,response_type=None,params=None):
        """
        Function to request a particular category's data series
        `<https://research.stlouisfed.org/docs/api/fred/category_series.html>`_

        :arg int category_id: The id for a category. Required.
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
        :arg str filter_variable: The attribute to filter results by. Options are  'frequency', 'units','seasonal_adjustment'
        :arg str filter_value: The value of the filter_variable attribute to filter results by.
        :arg str tag_names: Tag names used to match series. Separate with semicolon as in "income;bea"
        :arg str exclude_tag_names: Tag names used to exclude series. Separate with semicolon as in "income;bea"
        :arg bool ssl_verify: To verify HTTPs.
        :arg dict proxy: Set proxy dictionary. 
        """
        path = '/category/series?'
        params['category_id'] = category_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response

    @query_params('realtime_start','realtime_end','limit','offset',
                  'order_by','sort_order','tag_names','tag_group_id','search_text')
    def tags(self,category_id=None,response_type=None,params=None):
        """
        Function to request a particular category's FRED tags.
        FRED tags are attributes assigned to series.
        Series are assigned tags and categories. Indirectly through series,
        it is possible to get the tags for a category. No tags exist for a
        category that does not have series.
        `<https://research.stlouisfed.org/docs/api/fred/category_tags.html>`_

        :arg int category_id: The id for a category. Required.
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
        :arg str tag_names: Tag names to only include in the response. Separate with semicolon as in "income;bea"
        :arg str tag_group_id: Tag ID to filter tags by. Options are 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'
        :arg str search_text: The words to find matching tags with. For example 'mortgage rates'
        :arg bool ssl_verify: To verify HTTPs.
        :arg dict proxy: Set proxy dictionary. 
        """
        path = '/category/tags?'
        params['category_id'] = category_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response

    @query_params('realtime_start','realtime_end','limit','offset',
                  'order_by','sort_order','exclude_tag_names','tag_group_id','search_text')
    def related_tags(self,category_id=None,tag_names=None,response_type=None,params=None):
        """
        Function to request FRED related tags for a particular category.
        FRED tags are attributes assigned to series.
        Series are assigned tags and categories. Indirectly through series,
        it is possible to get the tags for a category. No tags exist for a
        category that does not have series.
        `<https://research.stlouisfed.org/docs/api/fred/category_tags.html>`_

        :arg int category_id: The id for a category. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str tag_names: Tag names that series match. Required. Separate with semicolon as in "income;bea"
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 1000
        :arg int offset: Data offset. Options >=0
        :arg str order_by: Order results by values of the specified attribute. Options are 'series_id',
                            'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end',
                            'last_updated', 'observation_start', 'observation_end', 'popularity'
        :arg str sort_order: Sort results for attribute values specified by order_by. Options are 'asc','desc'
        :arg str exclude_tag_names: Tag names to exclude. Separate with semicolon as in "income;bea"
        :arg str tag_group_id: Tag ID to filter tags by. Options are 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'
        :arg str search_text: The words to find matching tags with. For example 'mortgage rates'
        :arg bool ssl_verify: To verify HTTPs.
        :arg dict proxy: Set proxy dictionary. 
        """
        path='/category/related_tags?'
        params['category_id'], params['tag_names'] = category_id, tag_names
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response
