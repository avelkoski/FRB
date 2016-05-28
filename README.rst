Python Client for FRED® API
===========================
Python client for interfacing with the Federal Reserve Bank's
FRED API. Our goal is to provide a simple, well-documented
solution for FRED-related programming in Python.

.. note::

  This is a third-party client that is developed and maintained
  independently of the Federal Reserve Bank. As such, it is not
  affiliated with or supported by the institution.

Features
--------

This client was built to provide users with an intuitive
and effective framework for making requests to the FRED API
from within Python. As such, our main feature is the
ability to interact with the FRED web-service.

Comprehensive query support
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Request economic data from all 5 data groups available in FRED and ALFRED.
For reference, the data groups are included below.
See `Federal Reserve Bank of St. Louis`_  for additional documentation,
or click on a specific query to go directly to documentation for that query.

.. _Federal Reserve Bank of St. Louis: https://research.stlouisfed.org/docs/api/fred/

* **Categories**

  * `fred/category`_ - Get a category.
  * `fred/category/children`_ - Get the child categories for a specified parent category.
  * `fred/category/related`_ - Get the related categories for a category.
  * `fred/category/series`_ - Get the series in a category.
  * `fred/category/tags`_ - Get the tags for a category.
  * `fred/category/related_tags`_ - Get the related tags for a category.

.. _fred/category: https://research.stlouisfed.org/docs/api/fred/category.html
.. _fred/category/children: https://research.stlouisfed.org/docs/api/fred/category_children.html
.. _fred/category/related: https://research.stlouisfed.org/docs/api/fred/category_related.html
.. _fred/category/series: https://research.stlouisfed.org/docs/api/fred/category_series.html
.. _fred/category/tags: https://research.stlouisfed.org/docs/api/fred/category_tags.html
.. _fred/category/related_tags: https://research.stlouisfed.org/docs/api/fred/category_related_tags.html

* **Releases**

  * `fred/releases`_ - Get all releases of economic data.
  * `fred/releases/dates`_ - Get release dates for all releases of economic data.
  * `fred/release`_ - Get a release of economic data.
  * `fred/release/dates`_ - Get release dates for a release of economic data.
  * `fred/release/series`_ - Get the series on a release of economic data.
  * `fred/release/sources`_ - Get the sources for a release of economic data.
  * `fred/release/tags`_ - Get the tags for a release.
  * `fred/release/related_tags`_ - Get the related tags for a release.

.. _fred/releases: https://research.stlouisfed.org/docs/api/fred/releases.html
.. _fred/releases/dates: https://research.stlouisfed.org/docs/api/fred/releases_dates.html
.. _fred/release: https://research.stlouisfed.org/docs/api/fred/release.html
.. _fred/release/dates: https://research.stlouisfed.org/docs/api/fred/release_dates.html
.. _fred/release/series: https://research.stlouisfed.org/docs/api/fred/release_series.html
.. _fred/release/sources: https://research.stlouisfed.org/docs/api/fred/release_sources.html
.. _fred/release/tags: https://research.stlouisfed.org/docs/api/fred/release_tags.html
.. _fred/release/related_tags: https://research.stlouisfed.org/docs/api/fred/release_related_tags.html

* **Series**

  * `fred/series`_ - Get an economic data series.
  * `fred/series/categories`_ - Get the categories for an economic data series.
  * `fred/series/observations`_ - Get the observations or data values for an economic data series.
  * `fred/series/search`_ - Get economic data series that match keywords.
  * `fred/series/release`_ - Get the release for an economic data series.
  * `fred/series/search/tags`_ - Get the tags for a series search.
  * `fred/series/search/related_tags`_ - Get the related tags for a series search.
  * `fred/series/tags`_ - Get the tags for an economic data series.
  * `fred/series/updates`_ - Get economic data series sorted by when observations were updated on the FRED server.
  * `fred/series/vintagedates`_ - Get the dates in history when a series' data values were revised or new data values were released.

.. _fred/series: https://research.stlouisfed.org/docs/api/fred/series.html
.. _fred/series/categories: https://research.stlouisfed.org/docs/api/fred/series_categories.html
.. _fred/series/observations: https://research.stlouisfed.org/docs/api/fred/series_observations.html
.. _fred/series/release: https://research.stlouisfed.org/docs/api/fred/series_release.html
.. _fred/series/search:  https://research.stlouisfed.org/docs/api/fred/series_search.html
.. _fred/series/search/tags: https://research.stlouisfed.org/docs/api/fred/series_search_tags.html
.. _fred/series/search/related_tags: https://research.stlouisfed.org/docs/api/fred/series_search_related_tags.html
.. _fred/series/tags: https://research.stlouisfed.org/docs/api/fred/series_tags.html
.. _fred/series/updates: https://research.stlouisfed.org/docs/api/fred/series_updates.html
.. _fred/series/vintagedates: https://research.stlouisfed.org/docs/api/fred/series_vintagedates.html

* **Sources**

  * `fred/sources`_ - Get all sources of economic data.
  * `fred/source`_ - Get a source of economic data.
  * `fred/source/releases`_ - Get the releases for a source.

.. _fred/sources: https://research.stlouisfed.org/docs/api/fred/sources.html
.. _fred/source: https://research.stlouisfed.org/docs/api/fred/source.html
.. _fred/source/releases: https://research.stlouisfed.org/docs/api/fred/source_releases.html

* **Tags**

  * `fred/tags`_ - Get all tags, search for tags, or get tags by name.
  * `fred/related_tags`_ - Get the related tags for one or more tags.
  * `fred/tags/series`_ - Get the series matching tags.

.. _fred/tags: https://research.stlouisfed.org/docs/api/fred/tags.html
.. _fred/related_tags: https://research.stlouisfed.org/docs/api/fred/related_tags.html
.. _fred/tags/series: https://research.stlouisfed.org/docs/api/fred/tags_series.html

Popular response transformations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Transform data from http responses to your preferred format,
allowing you to focus more time on data integration and analysis
and less on response processing. If you prefer raw responses from FRED,
so that you can conduct your own response parsing, simply set ``response_type``
to *xml* or *json* (standard FRED responses). Otherwise, automatically
transform data into comma, tab, or pipe separated values,
python dictionaries, pandas dataframes, or numpy arrays.

For dictionary, dataframe, and array responses, an attempt is made to
convert data to more useful dtypes. For example, ``realtime_start``
and ``realtime_end`` response data are automatically converted
from a string to *datetime64* numpy dtype. Similarly, counts
and IDs (where appropriate) are converted to *int* while observation
measures are converted to *float*.


.. _fva-label:

Installation
------------

Install via ``pip``:

::

    pip install FRB


``Git`` clone from the command line:

::

    git clone http://github.com/avelkoski/FRB.git

Download directly from `Github`_.

  .. _Github: https://github.com/avelkoski/FRB/archive/master.zip


Basic usage
-------------
::

    from fred import Fred
    fr = Fred(api_key='abcdefghijklmnopqrstuvwxyz123456',response_type='dict')

    params = {
             'limit':2,
             'tag_names':'trade;goods'
             }

    res = fr.category.series(125,params=params)

    for record in res:
        print(record)


Read the Docs
-------------

For additional detail about this package, read our `documentation`_ .

  .. _documentation: http://frb.rtfd.org


License
-------

The MIT License (MIT)

Copyright (c) 2016 Aleksandar Velkoski https://github.com/avelkoski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Affiliation
-----------

The author is affiliated with the Data Science division of
the National Association of REALTORS.
