
from fred.utils import NamespacedClient, query_params
from fred.helpers import _get_request

class ReleasesClient(NamespacedClient):
    """
    Class for working with FRED releases
    """

    @query_params('realtime_start','realtime_end','limit','offset',
                  'order_by','sort_order')
    def all_releases(self,response_type=None,params=None):
        """
        Function to request all releases of economic data.
        `<https://research.stlouisfed.org/docs/api/fred/releases.html>`_

        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 1000
        :arg int offset: Data offset. Options >=0
        :arg str order_by: Order results by values of the specified attribute. Options are  'release_id',
                            'name', 'press_release', 'realtime_start', 'realtime_end'
        :arg str sort_order: Sort results for attribute values specified by order_by. Options are 'asc','desc'
        :arg bool ssl_verify: To verify HTTPs.
        :arg dict proxy: Set proxy dictionary. 
        """
        path='/releases?'
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response

    @query_params('realtime_start','realtime_end','limit','offset',
                  'order_by','sort_order','include_release_dates_with_no_data')
    def all_dates(self,response_type=None,params=None):
        """
        Function to request release dates for all releases of economic data.
        `<https://research.stlouisfed.org/docs/api/fred/releases_dates.html>`_

        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 1000
        :arg int offset: Data offset. Options >=0
        :arg str order_by: Order results by values of the specified attribute. Options are  'release_date',
                            'release_id', 'release_name'.
        :arg str sort_order: Sort results for attribute values specified by order_by. Options are 'asc','desc'
        :arg str include_release_dates_with_no_data: Determines whether release dates with no data available are returned.
                                    Options are 'true', 'false'
        :arg bool ssl_verify: To verify HTTPs.
        :arg dict proxy: Set proxy dictionary. 
        """
        path='/releases/dates?'
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response

    @query_params('realtime_start','realtime_end')
    def details(self,release_id=None,response_type=None,params=None):
        """
        Function to request the high-level details for a particular release of economic data..
        `<https://research.stlouisfed.org/docs/api/fred/release.html>`_

        :arg int release_id: The id for a release. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg bool ssl_verify: To verify HTTPs.
        :arg dict proxy: Set proxy dictionary. 
        """
        path='/release?'
        params['release_id'] = release_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response

    @query_params('realtime_start','realtime_end')
    def sources(self,release_id=None,response_type=None,params=None):
        """
        Function to request the sources for a particular release of economic data.
        `<https://research.stlouisfed.org/docs/api/fred/release.html>`_

        :arg int release_id: The id for a release. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg bool ssl_verify: To verify HTTPs.
        :arg dict proxy: Set proxy dictionary. 
        """
        path='/release/sources?'
        params['release_id'] = release_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response

    @query_params('realtime_start','realtime_end','limit','offset',
                  'sort_order','include_release_dates_with_no_data')
    def dates(self,release_id=None,response_type=None,params=None):
        """
        Function to request release dates for a particular release of economic data.
        Note that release dates are published by data sources and do not necessarily
        represent when data will be available on the FRED or ALFRED websites.
        `<https://research.stlouisfed.org/docs/api/fred/release_dates.html>`_

        :arg int release_id: The id for a release. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 1000
        :arg int offset: Data offset. Options >=0
        :arg str sort_order: Sort results is ascending or descending release date order. Options are 'asc','desc'
        :arg str include_release_dates_with_no_data: Determines whether release dates with no data available are returned.
                                    Options are 'true', 'false'
        :arg bool ssl_verify: To verify HTTPs.
        :arg dict proxy: Set proxy dictionary. 
        """
        path = '/release/dates?'
        params['release_id'] = release_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response

    @query_params('realtime_start','realtime_end','limit','offset',
                  'order_by','sort_order','filter_variable', 'filter_value',
                  'tag_names','exclude_tag_names')
    def series(self,release_id=None,response_type=None,params=None):
        """
        Function to request the series on a release of economic data.
        `<https://research.stlouisfed.org/docs/api/fred/release_series.html>`_

        :arg int release_id: The id for a release. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 1000
        :arg int offset: Data offset. Options >=0
        :arg str order_by: Order results by values of the specified attribute. Options are  'series_id', 'title', 'units', 'frequency',
                            'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated', 'observation_start',
                            'observation_end', 'popularity'
        :arg str sort_order: Sort results for attribute values specified by order_by. Options are 'asc','desc'
        :arg str filter_variable: The attribute to filter results by. Options are  'frequency', 'units','seasonal_adjustment'
        :arg str filter_value: The value of the filter_variable attribute to filter results by.
        :arg str tag_names: Tag names used to match series. Separate with semicolon as in "income;bea"
        :arg str exclude_tag_names: Tag names used to exclude series. Separate with semicolon as in "income;bea"
        :arg bool ssl_verify: To verify HTTPs.
        :arg dict proxy: Set proxy dictionary. 
        """
        path = '/release/series?'
        params['release_id'] = release_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response

    @query_params('realtime_start','realtime_end','limit','offset',
                  'order_by','sort_order','tag_names','tag_group_id','search_text')
    def tags(self,release_id=None,response_type=None,params=None):
        """
        Function to request FRED tags for a particular release.
        FRED tags are attributes assigned to series.
        Series are assigned tags and releases. Indirectly through series,
        it is possible to get the tags for a category. No tags exist for a
        release that does not have series.
        `<https://research.stlouisfed.org/docs/api/fred/release_tags.html>`_

        :arg int release_id: The id for a release. Required.
        :arg str response_type: File extension of response. Options are 'xml', 'json',
                            'dict','df','numpy','csv','tab,'pipe'. Required.
        :arg str realtime_start: The start of the real-time period. Format "YYYY-MM-DD"
        :arg str realtime_end: The end of the real-time period. Format "YYYY-MM-DD"
        :arg int limit: The maximum number of results to return. Options 1 to 1000
        :arg int offset: Data offset. Options >=0
        :arg str order_by: Order results by values of the specified attribute. Options are 'series_count',
                            'popularity', 'created', 'name', 'group_id'
        :arg str sort_order: Sort results for attribute values specified by order_by. Options are 'asc','desc'
        :arg str tag_names: Tag names that series match. Separate with semicolon as in "income;bea"
        :arg str tag_group_id: Tag ID to filter tags by. Options are 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'
        :arg str search_text: The words to find matching tags with. For example 'mortgage rates'
        :arg bool ssl_verify: To verify HTTPs.
        :arg dict proxy: Set proxy dictionary. 
        """
        path = '/release/tags?'
        params['release_id'] = release_id
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response

    @query_params('realtime_start','realtime_end','limit','offset',
                  'order_by','sort_order','exclude_tag_names','tag_group_id','search_text')
    def related_tags(self,release_id=None,tag_names=None,response_type=None,params=None):
        """
        Function to request FRED related tags for a particular release.
        FRED tags are attributes assigned to series.
        Series are assigned tags and releases. Indirectly through series,
        it is possible to get the tags for a category. No tags exist for a
        release that does not have series.
        `<https://research.stlouisfed.org/docs/api/fred/release_related_tags.html>`_

        :arg int release_id: The id for a release. Required.
        :arg str tag_names: Tag names that series match. Separate with semicolon as in "income;bea". Required
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
        path='/release/related_tags?'
        params['release_id'], params['tag_names'] = release_id, tag_names
        response_type = response_type if response_type else self.response_type
        if response_type != 'xml': params['file_type'] = 'json'
        response = _get_request(self.url_root,self.api_key,path,response_type,params,self.ssl_verify,self.proxy)
        return response
