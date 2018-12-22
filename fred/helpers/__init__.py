from sys import version_info
if version_info[0] >= 3:
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen
    import ssl
else:
    from urllib import urlencode
    from urllib2 import Request, urlopen
    import ssl

import fred.config as c
from json import loads
from pandas import DataFrame

# consider putting this in ~/.fred or env var
_USE_JOBLIB_CACHE = True
_THROTTLE_REQUESTS = True

def _fetch(url, ssl_verify = True):
    """
    Helper funcation to fetch content from a given url.
    """
    req = Request(url)
    if ssl_verify:
        page = urlopen(req)
    else:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        page = urlopen(req, context=ctx)
    content = page.read().decode('utf-8')
    page.close()
    return content

def _url_builder(url_root,api_key,path,params):
    """
    Helper funcation to build a parameterized url.
    """
    params['api_key'] = api_key
    url_end = urlencode(params)
    url = "%s%s%s" % (url_root,path,url_end)
    return url

def _convert(frame):
    """
    Helper funcation to build a parameterized url.
    """
    frame = frame.convert_objects(convert_numeric=True)
    for column in frame:
        if column in c.dates:
            frame[column] = frame[column].astype('datetime64')
    return frame

def _dict(content):
    """
    Helper funcation that converts text-based get response
    to a python dictionary for additional manipulation.
    """
    response = _data_frame(content).to_dict(orient='records')
    return response

def _data_frame(content):
    """
    Helper funcation that converts text-based get response
    to a pandas dataframe for additional manipulation.
    """
    response = loads(content)
    key = [x for x in response.keys() if x in c.response_data][0]
    frame = DataFrame(response[key])
    final_frame = _convert(frame)
    return final_frame

def _csv(content):
    """
    Helper funcation that converts text-based get response
    to comma separated values for additional manipulation.
    """
    response = _data_frame(content).to_csv(index=False)
    return response

def _tab(content):
    """
    Helper funcation that converts text-based get response
    to tab separated values for additional manipulation.
    """
    response = _data_frame(content).to_csv(index=False,sep='\t')
    return response

def _pipe(content):
    """
    Helper funcation that converts text-based get response
    to pipe separated values for additional manipulation.
    """
    response = _data_frame(content).to_csv(index=False,sep='|')
    return response

def _numpy(content):
    """
    Helper funcation that converts text-based get response
    to comma separated values for additional manipulation.
    """
    response = _data_frame(content).values
    return response

def _json(content):
    """
    Pass response
    """
    return content

def _xml(content):
    """
    Pass response
    """
    return content

def _dispatch(response_type):
    dispatch = {'dict':_dict,'df':_data_frame,'json':_json,
                'xml':_xml,'csv':_csv,'numpy':_numpy,
                'tab': _tab, 'pipe': _pipe}
    return dispatch[response_type]

def _get_request(url_root,api_key,path,response_type,params, ssl_verify):
    """
    Helper funcation that requests a get response from FRED.
    """
    url = _url_builder(url_root,api_key,path,params)
    content = _fetch(url, ssl_verify)
    response = _dispatch(response_type)(content)
    return response

if _USE_JOBLIB_CACHE:
    import joblib
    one_gb = 1000000000
    location = '/tmp/joblib_cache'
    memory = joblib.Memory(location, verbose=1, bytes_limit=one_gb)
    if _THROTTLE_REQUESTS:
        from ratelimit import limits, sleep_and_retry
        period_seconds = 1
        calls_per_second = 20
        _get_request = memory.cache(sleep_and_retry(limits(calls=calls_per_second, period=period_seconds)(_get_request)))
    else:
        _get_request = memory.cache(_get_request)
