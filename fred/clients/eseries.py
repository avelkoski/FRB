
from fred.utils import NamespacedClient, query_params
from fred.helpers import _get_request

class ESeriesClient(NamespacedClient):
    """
    Class for working with FRED series
    """

    @query_params('realtime_start','realtime_end')
    def details(self,series_id=None,response_type=None,params=None):
        """
        Function to request a series of economic data.
        `<https://research.stlouisfed.org/docs/api/fred/release.html>`_

        :arg int series_id: The id for a series. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                        'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg bool ssl_verify: To verify HTTPs.
        """
        path='/series?'
        params['series_id'] = series_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify)
        return response

    @query_params('realtime_start','realtime_end')
    def categories(self,series_id=None,response_type=None,params=None):
        """
        Function to request the categories for an economic data series.
        `<https://research.stlouisfed.org/docs/api/fred/release.html>`_

        :arg int series_id: The id for a series. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                        'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg bool ssl_verify: To verify HTTPs.
        """
        path='/series/categories?'
        params['series_id'] = series_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify)
        return response

    @query_params('realtime_start','realtime_end')
    def release(self,series_id=None,response_type=None,params=None):
        """
        Function to request the release for an economic data series.
        `<https://research.stlouisfed.org/docs/api/fred/series_release.html>`_

        :arg int series_id: The id for a series. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                        'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg bool ssl_verify: To verify HTTPs.
        """
        path='/series/release?'
        params['series_id'] = series_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify)
        return response

    @query_params('realtime_start','realtime_end',
                  'order_by','sort_order')
    def tags(self,series_id=None,response_type=None,params=None):
        """
        Function to request FRED tags for a particular series.
        FRED tags are attributes assigned to series.
        `<https://research.stlouisfed.org/docs/api/fred/series_tags.html>`_

        :arg int series_id: The id for a series. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                        'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg str order_by: Order results by values of the specified attribute. Options are 'series_count',
                            'popularity', 'created', 'name', 'group_id'
        :arg str sort_order: Sort results for attribute values specified by order_by. Options are 'asc','desc'
        :arg bool ssl_verify: To verify HTTPs.
        """
        path = '/series/tags?'
        params['series_id'] = series_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify)
        return response

    @query_params('realtime_start','realtime_end','limit',
                  'offset','filter_value')
    def updates(self,series_id=None,response_type=None,params=None):
        """
        Function to request economic data series sorted by when observations
        were updated on the FRED server (attribute last_updated). Results are
        limited to series updated within the last two weeks.
        `<https://research.stlouisfed.org/docs/api/fred/series_updates.html>`_

        :arg int series_id: The id for a series. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                        'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 1000
        :arg int offset: Data offset. Options >=0
        :arg str filter_value: Limit results by geographic type of economic data series. Options are 'macro',
                                'regional', and 'all'
        :arg bool ssl_verify: To verify HTTPs.
        """
        path = '/series/updates?'
        params['series_id'] = series_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify)
        return response

    @query_params('realtime_start','realtime_end','limit',
                  'offset','sort_order')
    def vintage_dates(self,series_id=None,response_type=None,params=None):
        """
        Function to request the dates in history when a series' data values were
        revised or new data values were released. Vintage dates are the release dates
        for a series excluding release dates when the data for the series did not change.
        `<https://research.stlouisfed.org/docs/api/fred/series_vintagedates.html>`_

        :arg int series_id: The id for a series. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                        'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 1000
        :arg int offset: Data offset. Options >=0
        :arg str sort_order: Sort results by vintage_date. Options are 'asc','desc'
        :arg bool ssl_verify: To verify HTTPs.
        """
        path = '/series/vintagedates?'
        params['series_id'] = series_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify)
        return response

    @query_params('realtime_start','realtime_end','limit',
                  'offset','sort_order','observation_start','observation_end',
                  'units','frequency','aggregation_method','output_type',
                  'vintage_dates')
    def observations(self,series_id=None,response_type=None,params=None):
        """
        Function to request the observations or data values for an economic data series.
        `<https://research.stlouisfed.org/docs/api/fred/series_observations.html>`_

        :arg int series_id: The id for a series. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                        'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 100000
        :arg int offset: Data offset. Options >=0
        :arg str sort_order: Sort results is ascending or descending observation_date order. Options are 'asc','desc'
        :arg str observation_start: The start of the observation period. Format "YYYY-MM-DD"
        :arg str observation_end: The end of the observation period. Format "YYYY-MM-DD"
        :arg str units: A key that indicates a data value transformation. Options are 'lin', 'chg', 'ch1', 'pch',
                        'pc1', 'pca', 'cch', 'cca', 'log'
        :arg str frequency: Indicates a lower frequency to aggregate values. Options are 'd', 'w',
                            'bw', 'm', 'q', 'sa', 'a', 'wef', 'weth', 'wew', 'wetu', 'wem',
                            'wesu', 'wesa', 'bwew', 'bwem'
        :arg str aggregation_method: Indicates the aggregation method used for frequency aggregation. Options are  'avg',
                            'sum', 'eop'
        :arg int output_type: Output type. Options are 1, 2, 3, 4
        :arg str vintage_dates: Date(s) in history. Format "YYYY-MM-DD". Example for multiple dates "2000-01-01,2005-02-24,..."
        :arg bool ssl_verify: To verify HTTPs.
        """
        path = '/series/observations?'
        params['series_id'] = series_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify)
        return response

    @query_params('search_type','realtime_start','realtime_end',
                  'limit','offset','order_by','sort_order','filter_variable',
                  'filter_value','tag_names','exclude_tag_names')
    def search(self,search_text=None,response_type=None,params=None):
        """
        Function to request economic data series that match search text.
        `<https://research.stlouisfed.org/docs/api/fred/series_search.html>`_

        :arg str search_text: The words to match against economic data series. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                        'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str search_type: Determines the type of search to perform. Options are 'full_text','series_id'
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 1000
        :arg int offset: Data offset. Options >=0
        :arg str order_by: Order results by values of the specified attribute. Options are 'search_rank',
                            'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start',
                            'realtime_end', 'last_updated', 'observation_start', 'observation_end', 'popularity'
        :arg str sort_order: Sort results for attribute values specified by order_by. Options are 'asc','desc'
        :arg str filter_variable: The attribute to filter results by. Options are  'frequency', 'units','seasonal_adjustment'
        :arg str filter_value: The value of the filter_variable attribute to filter results by.
        :arg str tag_names: Tag names used to match series. Separate with semicolon as in "income;bea"
        :arg str exclude_tag_names: Tag names used to exclude series. Separate with semicolon as in "income;bea"
        :arg bool ssl_verify: To verify HTTPs.
        """
        path = '/series/search?'
        params['search_text'] = search_text
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify)
        return response

    @query_params('realtime_start','realtime_end',
                      'limit','offset','order_by','sort_order','tag_names',
                      'tag_group_id','tag_search_text')
    def search_tags(self,series_search_text=None,response_type=None,params=None):
        """
        Function to request the FRED tags for a series search.
        `<https://research.stlouisfed.org/docs/api/fred/series_search_tags.html>`_

        :arg str series_search_text: The words to match against economic data series. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                        'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 1000
        :arg int offset: Data offset. Options >=0
        :arg str order_by: Order results by values of the specified attribute. Options are  'series_count',
                            'popularity', 'created', 'name', 'group_id'
        :arg str sort_order: Sort results for attribute values specified by order_by. Options are 'asc','desc'
        :arg str tag_names: Tag names that series match. Separate with semicolon as in "income;bea"
        :arg str tag_group_id: Tag ID to filter tags by. Options are 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'
        :arg str tag_search_text: The words to find matching tags with.
        :arg bool ssl_verify: To verify HTTPs.
        """
        path = '/series/search/tags?'
        params['series_search_text'] = series_search_text
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify)
        return response

    @query_params('realtime_start','realtime_end',
                      'limit','offset','order_by','sort_order',
                      'tag_group_id','tag_search_text','exclude_tag_names')
    def search_related_tags(self,series_search_text=None,tag_names=None,response_type=None,params=None):
        """
        Function to request the related FRED tags for one or more FRED tags matching a series search.
        `<https://research.stlouisfed.org/docs/api/fred/series_search_related_tags.html>`_

        :arg str series_search_text: The words to match against economic data series. Required.
        :arg str tag_names: Tag names that series match. Separate with semicolon as in "income;bea". Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                        'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 1000
        :arg int offset: Data offset. Options >=0
        :arg str order_by: Order results by values of the specified attribute. Options are  'series_count',
                            'popularity', 'created', 'name', 'group_id'
        :arg str sort_order: Sort results for attribute values specified by order_by. Options are 'asc','desc'
        :arg str tag_group_id: Tag ID to filter tags by. Options are 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'
        :arg str tag_search_text: The words to find matching tags with.
        :arg str exclude_tag_names: Tag names to exclude. Separate with semicolon as in "income;bea"
        :arg bool ssl_verify: To verify HTTPs.
        """
        path = '/series/search/related_tags?'
        params['series_search_text'], params['tag_names'] = series_search_text, tag_names
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify)
        return response
