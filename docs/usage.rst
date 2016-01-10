.. _usage:

Quickstart Guide
================

If you're new to the Federal Reserve Economic Data (FRED) API,
or if you're new to using our client, this guide should provide
you with all you need to know to start requesting economic data.

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

FRED API Key
------------

Visit the `Federal Reserve Bank of St. Louis`_ to obtain
your personalized API Key.

  .. _Federal Reserve Bank of St. Louis: https://research.stlouisfed.org/docs/api/api_key.html

Configuration
-------------

Default parameters can be set within fred/config.py
or optionally when you instantiate ``Fred()``. These include
``api_key`` and  ``response_type``. In order to request data from FRED,
you must configure the client with your ``api_key``.

.. note::

  Economic data are revised from time-to-time. A real-time period marks
  when information was known to be true. In FRED, the real-time period
  defaults to the current date (e.g. the parameters ``realtime_start``
  and ``realtime_end``, which define the real-time period, are set to today's date).
  Data are interpreted as facts known to be true as of today (most recent figure or revision).
  The real-time period can be set as an optional parameter in most functions. See our
  discussion :ref:`FRED vs. ALFRED <fva-label>` for additional details.


Usage
-----
Instantiate FRED with your API key and preferred response format:

::

    from fred import Fred
    fr = Fred(api_key='abcdefghijklmnopqrstuvwxyz123456',response_type='df')

If you do not include ``response_type``, the default response is ``xml``.
Available response types include ``xml``, ``json``, ``dict``, ``df``, ``numpy``, ``csv``,
``tab``, and ``pipe``.


Categories
~~~~~~~~~~

Economic data categories represent classes of data series that
are regarded as having similar characteristics. Categories are
often made up of subcategories along with economic data series.

Details
^^^^^^^

To request category details, provide a category ID to the
details method of the category client:

::

    res = fr.category.details(1)
    print res

The response includes the category ID, name, and parent category ID
associated with the requested category. The parent category ID is 0 if
the category has no parents.

.. csv-table::
    :header: "id", "name", "parent_id"

    1,Production & Business Activity,0

Children
^^^^^^^^

Get the child categories for a specified parent category.

::

    res = fr.category.children(1)
    print res


The response includes the category ID, name, and parent category ID
associated with a given child category. The parent category ID is 1
because we requested its children.

.. csv-table::
      :header: "id", "name", "parent_id"

       32262,           Business Cycle Expansions & Contractions,          1
       32436,                                       Construction,          1
       33490,                                  Finance Companies,          1
       32216,                                   Health Insurance,          1
          97,                                            Housing,          1
           3,       Industrial Production & Capacity Utilization,          1
       32295,  Institute for Supply Management Report on Busi...,          1
       32429,                                      Manufacturing,          1
           6,                                       Retail Trade,          1
       33441,                                           Services,          1
       33492,                                         Technology,          1
       33202,                                     Transportation,          1
       33203,                                    Wholesale Trade,          1

Related
^^^^^^^

To request categories related to a given category, provide
the category ID to the related method of the category client:

::

   res = fr.category.related(32073)
   print res


The response includes the category ID, name, and parent category ID
associated with a given related category.

.. csv-table::
     :header: "id", "name", "parent_id"

       149,     Arkansas,      27281
       150,     Illinois,      27281
       151,      Indiana,      27281
       152,     Kentucky,      27281
       153,  Mississippi,      27281
       154,     Missouri,      27281
       193,    Tennessee,      27281


Series
^^^^^^

Get economic data series associated with a category. In this request,
we add optional parameters to help refine our response. We limit
the number of records to 5, request series with the tags trade
and goods, order the response by popularity (descending):

::

  params = {
           'limit':5,
           'tag_names':'trade;goods',
           'order_by':'popularity',
           'sort_order':'desc'
           }

  res = fr.category.series(125,params=params)
  print res


The response includes the series frequency, observation period,
and popularity, among other descriptive features.

.. csv-table::
    :header: frequency,frequency_short,id,last_updated,observation_end,observation_start,popularity,realtime_end,realtime_start,seasonal_adjustment,seasonal_adjustment_short,title,units,units_short

             Monthly,M,BOPGSTB,Timestamp('2016-01-07 16:46:02'),Timestamp('2015-11-01 00:00:00'), Timestamp('1992-01-01 00:00:00'), 61, Timestamp('2016-01-09 00:00:00'), Timestamp('2016-01-09 00:00:00'), Seasonally Adjusted, SA,"Trade Balance: Goods, and Services Balance of Payments Basis",Millions of Dollars, Mil. of $
             Monthly,M,BOPGTB,Timestamp('2016-01-07 16:46:02'),Timestamp('2015-11-01 00:00:00'), Timestamp('1992-01-01 00:00:00'),42, Timestamp('2016-01-09 00:00:00'),Timestamp('2016-01-09 00:00:00'), Seasonally Adjusted, SA,"Trade Balance: Goods, Balance of Payments Basis",Millions of Dollars, Mil. of $


Tags
^^^^

Get the FRED tags associated with a category.

::

  params = {
           'limit':10
           }

  res = fr.category.tags(125,params=params)
  print res


The response includes the tag group_id, name, and series_count
associated with a given category tag.

.. csv-table::
    :header: created,group_id,name,notes,popularity,series_count

      2012-02-27 16:18:19,      src,           bea,  US. Bureau of Economic Analysis,  86,           45
      2012-02-27 16:18:19,     geot,        nation,                    Country Level,   100 ,         45
      2012-02-27 16:18:19,      geo,           usa,         United States of America,   100 ,         45
      2012-02-27 16:18:19,      gen,       balance,                                 ,   63 ,          39
      2012-02-27 16:18:19,     seas,           nsa,          Not seasonally adjusted ,  97 ,          28
      2012-02-27 16:18:19,     freq,     quarterly,                                  ,  88 ,          28
      2012-02-27 16:18:19,      gen,  discontinued,                                   , 69 ,          21
      2012-02-27 16:18:19,     seas,            sa,              Seasonally adjusted  , 93 ,          17
      2012-02-27 16:18:19,     freq,        annual,                                   , 84 ,          14
      2012-02-27 16:18:19,      gen,      services,                                   , 71 ,          14

Related tags
^^^^^^^^^^^^

Get the related FRED tags for one or more FRED tags within a category.

::

    params = {
             'tag_group_id':'gen',
             'limit':10,
             'exclude_tag_names':'services',
             'sort_order':'asc'
             }

    res = fr.category.related_tags(125,tag_names='bea',params=params)
    print res


The response includes the tag group_id, name, and series_count
associated with a given category tag.

.. csv-table::
    :header: created,group_id,name,notes,popularity,series_count

    2012-02-27 16:18:19,      gen,       investment,             ,   66,   3
    2013-11-13 22:08:31,      gen,      merchandise,             ,   33,   3
    2012-02-27 16:18:19,      gen,          primary,             ,   54,   3
    2012-02-27 16:18:19,      gen,        secondary,             ,  29,   3
    2012-02-27 16:18:19,      gen,        transfers,             ,   48,   3
    2012-02-27 16:18:19,      gen,            goods,             ,   71,   4
    2012-02-27 16:18:19,      gen,            trade,             ,   59,   4
    2012-02-27 16:18:19,      gen,  capital account,             ,   47,   6
    2012-02-27 16:18:19,      gen,  current account,             ,   57,   6
    2012-02-27 16:18:19,      gen,              net,             ,   67,   6

Releases
~~~~~~~~

A release is a distribution of an economic data series.
Releases are often maintained by different parties, including
the Federal Reserve Bank, Bureau of Labor Statistics,
Bureau of Economic Analysis, and Census Bureau.


All releases
^^^^^^^^^^^^

Get all releases of economic data.

::

    params = {
             'limit':5,
             }

    res = fr.release.all_releases(params=params)
    print res

The response includes the release ID, name, and link (among other items)
associated with the requested release.

.. csv-table::
    :header: id, link, name, press_release, realtime_end,realtime_start

      9,               http://www.census.gov/retail/,         Advance Monthly Sales for Retail and Food Serv..., True ,    2016-01-09,     2016-01-09
      10,                      http://www.bls.gov/cpi/,       Consumer Price Index,          True,       2016-01-09,     2016-01-09
      11,                  http://www.bls.gov/ncs/ect/,       Employment Cost Index,          True,     2016-01-09,     2016-01-09
      13, http://www.federalreserve.gov/releases/g17/,        G.17 Industrial Production and Capacity Utiliz...,          True,    2016-01-09,     2016-01-09
      14,  http://www.federalreserve.gov/releases/g19/,       G.19 Consumer Credit,          True,    2016-01-09,     2016-01-09

All dates
^^^^^^^^^

Get release dates for all releases of economic data.

::

    params = {
             'limit':5,
             }

    res = fr.release.all_dates(params=params)
    print res

The response includes the date, release ID, name of the release:

.. csv-table::
    :header: date, release_id, release_name

       2016-01-08,         302,             Cleveland Financial Stress Index
       2016-01-08,          86,                             Commercial Paper
       2016-01-08,          72,  Daily Treasury Inflation-Indexed Securities
       2016-01-08,         279,                  Economic Policy Uncertainty
       2016-01-08,          50,                         Employment Situation




Details
^^^^^^^

To request release details, provide a release ID to the
details method of the release client:

::

    res = fr.release.details(51)
    print res

The response includes the release ID, name, and link (among other items)
associated with the requested release.

.. csv-table::
    :header: id, link, name, press_release, realtime_end,realtime_start

      51, http://www.bea.gov/newsreleases/international/..., U.S. International Trade in Goods and Services, True, 2016-01-09, 2016-01-09

Dates
^^^^^

Get release dates for a release of economic data:

::

    params = {
             'limit':5,
             }

    res = fr.release.dates(51,params=params)
    print res

The response includes the date of the release and the realease_id.

.. csv-table::
    :header: date , release_id


         1997-01-17,          51
         1997-02-19,          51
         1997-03-20,          51
         1997-04-17,          51
         1997-04-25,          51

Series
^^^^^^

Get the series on a release of economic data:

::

   params = {
            'limit':2,
            }

   res = fr.release.series(51,params=params)
   print res

The response includes the series frequency, observation period,
and popularity, among other descriptive features.

.. csv-table::
   :header: frequency,frequency_short,id,last_updated,notes,observation_end,observation_start,popularity,realtime_end,realtime_start,seasonal_adjustment,seasonal_adjustment_short,title,units,units_short

      Monthly, M, BOMTVLM133S, Timestamp('2016-01-07 16:46:01'),NaN,Timestamp('2015-11-01 00:00:00'),Timestamp('1992-01-01 00:00:00'), 0,Timestamp('2016-01-10 00:00:00'), Timestamp('2016-01-10 00:00:00'),Seasonally Adjusted, SA, U.S. Imports of Services - Travel, Million of Dollars,Mil. of $
      Monthly, M, BOMVGMM133S, Timestamp('2014-10-20 14:27:37'),"BEA has introduced new table presentations, including a new presentation of services, as part of a comprehensive restructuring of BEA\u2019s international economic accounts.For more information see http://www.bea.gov/international/revision-2014.htm.",Timestamp('2013-12-01 00:00:00'), Timestamp('1992-01-01 00:00:00'),7, Timestamp('2016-01-10 00:00:00'),Timestamp('2016-01-10 00:00:00'), Seasonally Adjusted, SA,U.S. Imports of Services: U.S. Government Miscellaneous Services (DISCONTINUED),Millions of Dollars, Mil. of $


Tags
^^^^

Get the FRED tags associated with a release.

::

  params = {
           'limit':10
           }

  res = fr.release.tags(51,params=params)
  print res


The response includes the tag group_id, name, and series_count
associated with a given release tag.

.. csv-table::
    :header: created,group_id,name,notes,popularity,series_count

      2012-02-27 16:18:19,      src,       bea,  US. Bureau of Economic Analysis,     86,            57
      2012-02-27 16:18:19,      src,    census,         US. Bureau of the Census,    79,            57
      2012-02-27 16:18:19,     freq,   monthly,                                 ,    94,            57
      2012-02-27 16:18:19,     geot,    nation,                    Country Level,    100,            57
      2012-02-27 16:18:19,      geo,       usa,         United States of America,    100,            57
      2012-02-27 16:18:19,     seas,        sa,              Seasonally adjusted,     93,            41
      2012-02-27 16:18:19,      gen,  services,                                 ,     71,            38
      2012-02-27 16:18:19,      gen,   exports,                                 ,     63,            27
      2012-02-27 16:18:19,      gen,   imports,                                 ,     61,            27
      2012-02-27 16:18:19,      gen,     goods,                                 ,     71,            24


Related tags
^^^^^^^^^^^^

Get the related FRED tags for one or more FRED tags within a release.

::

    params = {
             'tag_group_id':'gen',
             'limit':10,
             'exclude_tag_names':'services',
             'sort_order':'asc'
             }

    res = fr.release.related_tags(51,tag_names='bea',params=params)
    print res


The response includes the tag group_id, name, and series_count
associated with a given release tag.

.. csv-table::
    :header: created,group_id,name,notes,popularity,series_count

        2012-02-27 16:18:19,      gen,  balance,                         ,      63,   1
        2012-02-27 16:18:19,      gen,    trade,                         ,      59,   1
        2013-01-28 20:10:13,      gen,      bop,  Balance of Payments    ,      56,  3
        2012-02-27 16:18:19,      gen,  exports,                         ,      63,   9
        2012-02-27 16:18:19,      gen,  imports,                         ,      61,  9
        2012-02-27 16:18:19,      gen,    goods,                         ,      71,  19

Series
~~~~~~

Economic data series are quantitative measures used
to describe various components of the economy. Series
consist of data measured over a time interval.

Details
^^^^^^^

To request series details, provide a series ID to the
details method of the series client:

::

  res = fr.series.details('GNPCA')
  print res

The response includes the series frequency, observation period,
and popularity, among other descriptive features.

.. csv-table::
  :header: frequency, frequency_short, id, last_updated, notes, observation_end, observation_start, popularity, realtime_end, realtime_start, seasonal_adjustment, seasonal_adjustment_short, title, units, units_short

      Annual, A, GNPCA, Timestamp('2015-07-30 14:03:15'),  BEA Account Code: A001RX1, Timestamp('2014-01-01 00:00:00'),  Timestamp('1929-01-01 00:00:00'), 28,  Timestamp('2016-01-10 00:00:00'), Timestamp('2016-01-10 00:00:00'),  Not Seasonally Adjusted, NSA, Real Gross National Product,Billions of Chained 2009 Dollars, Bil. of Chn. 2009 $

Categories
^^^^^^^^^^

Get the categories for an economic data series:

::

  res = fr.series.categories('GNPCA')
  print res

The response includes category ID, name, and parent ID:

.. csv-table::
  :header: id, name, parent_id

      106, GDP/GNP, 18

Release
^^^^^^^

Get the release for an economic data series:

::

  res = fr.series.release('GNPCA')
  print res

The response includes the release ID, name, and a link to the release:

.. csv-table::
  :header: id, link, name, press_release, realtime_end, realtime_start

      53, http://www.bea.gov/national/index.htm,Gross Domestic Product, True, Timestamp('2016-01-10 00:00:00'),Timestamp('2016-01-10 00:00:00')

Observations
^^^^^^^^^^^^

Get the observations or data values for an economic data series:

::

    params = {
             'limit':5,
             'output_type':1
             }

    res = fr.series.observations('GNPCA',params=params)
    print res

The response includes the date, real-time period, and value of the observation:

.. csv-table::
  :header: date, realtime_end, realtime_start, value

      1929-01-01,   2016-01-10,     2016-01-10,  1066.8
      1930-01-01,   2016-01-10,     2016-01-10,   976.3
      1931-01-01,   2016-01-10,     2016-01-10,   912.9
      1932-01-01,   2016-01-10,     2016-01-10,   794.8
      1933-01-01,   2016-01-10,     2016-01-10,   784.0


Tags
^^^^

Get the tags for an economic data series:

::

    res = fr.series.tags('GNPCA')
    print res

The response includes the tag group_id, name, and series_count
associated with a given series search.

.. csv-table::
  :header:  created,group_id,name,notes,popularity,series_count

      2012-02-27 16:18:19,seas,nsa,Not seasonally adjusted,97,326950
      2012-02-27 16:18:19,geo,usa,United States of America,100,248427
      2012-02-27 16:18:19,freq,annual,,84,222080
      2012-02-27 16:18:19,geot,nation,Country Level,100,163584
      2012-02-27 16:18:19,src,bea,US. Bureau of Economic Analysis,86,22902
      2012-08-16 20:21:17,rls,nipa,National Income and Product Accounts,83,11765
      2012-02-27 16:18:19,gen,real,Inflation Adjusted Data,82,9282
      2012-02-27 16:18:19,gen,gnp,Gross National Product,57,437

Updates
^^^^^^^

Get economic data series sorted by when observations were updated on the FRED server:

::

    params = {
             'limit':2,
             }

    res = fr.series.updates('GNPCA',params=params)
    print res

The response includes the tag group_id, name, and series_count
associated with a given series search.

.. csv-table::
  :header:  frequency,frequency_short,id,last_updated,notes,observation_end,observation_start,popularity,realtime_end,realtime_start,seasonal_adjustment,seasonal_adjustment_short,title,units,units_short


      Daily,D,RUTOP200TR,2016-01-09 01:56:42,"The Russell Top 200Â® Index measures the performance of the largest cap segment of the U.S. equity universe. The Russell Top 200Â® Index is a subset of the Russell 3000Â® Index. It includes approximately 200 of the largest securities based on a combination of their market cap and current index membership and represents approximately 68% of the U.S. market. The Russell Top 200Â® Index is constructed to provide a comprehensive and unbiased barometer for this very large cap segment and is completely reconstituted annually to ensure new and growing equities are reflected.

      This series is a total market index, which assumes that all cash distributions are reinvested, in addition to tracking the price movements.

      For more information, go to the source at: http://www.russell.com/indexes/americas/indexes/default.page?",2016-01-08 00:00:00,1978-12-31 00:00:00,23,2016-01-10 00:00:00,2016-01-10 00:00:00,Not Seasonally Adjusted,NSA,Russell Top 200Â® Total Market Index,Index,Index
      Daily,D,RUTOP200PR,2016-01-09 01:56:41,"The Russell Top 200Â® Index measures the performance of the largest cap segment of the U.S. equity universe. The Russell Top 200Â® Index is a subset of the Russell 3000Â® Index. It includes approximately 200 of the largest securities based on a combination of their market cap and current index membership and represents approximately 68% of the U.S. market. The Russell Top 200Â® Index is constructed to provide a comprehensive and unbiased barometer for this very large cap segment and is completely reconstituted annually to ensure new and growing equities are reflected.

      For more information, go to the source at: http://www.russell.com/indexes/americas/indexes/default.page?",2016-01-08 00:00:00,1978-12-31 00:00:00,16,2016-01-10 00:00:00,2016-01-10 00:00:00,Not Seasonally Adjusted,NSA,Russell Top 200Â® Price Index,Index,Index

Vintage dates
^^^^^^^^^^^^^

Get the dates in history when a series' data values were revised or new data values were released:

::

    params = {
             'limit':10,
             'sort_order':'desc'
             }

    res = fr.series.vintage_dates('GNPCA',params=params)
    print res

The response includes vintage_dates:

.. csv-table::
  :header:  0

      2015-07-30
      2015-03-27
      2014-07-30
      2014-03-27
      2013-07-31
      2013-03-28
      2012-07-27
      2012-03-29
      2011-07-29
      2011-03-25


Search
^^^^^^

Get economic data series that match keywords:

::

    params = {
             'limit':2,
             }

    res = fr.series.search('money service index',params=params)
    print res

The response includes the series frequency, observation period,
and popularity, among other descriptive features.

.. csv-table::
  :header: frequency, frequency_short, id, last_updated, notes, observation_end, observation_start, popularity, realtime_end, realtime_start, seasonal_adjustment, seasonal_adjustment_short, title, units, units_short

      Monthly, M, MSIM1P, Timestamp('2014-01-17 13:16:45'),"The MSI measure the flow of monetary services received each period by households and firms from their holdings of monetary assets (levels of the indexes are sometimes referred to as Divisia monetary aggregates).",Timestamp('2013-12-01 00:00:00'), Timestamp('1967-01-01 00:00:00'),30, Timestamp('2016-01-10 00:00:00'),Timestamp('2016-01-10 00:00:00'), Seasonally Adjusted, SA,Monetary Services Index: M1 (preferred), Billions of Dollars,Bil. of $
      Monthly, M, MSIMZMP, Timestamp('2014-01-17 13:16:42'),"The MSI measure the flow of monetary services received each period by households and firms from their holdings of monetary assets (levels of the indexes are sometimes referred to as Divisia monetary aggregates).\r\nPreferred benchmark rate equals 100 basis points plus the largest rate in the set of rates. \r\nAlternative benchmark rate equals the larger of the preferred benchmark rate and the Baa corporate bond yield.",Timestamp('2013-12-01 00:00:00'), Timestamp('1967-01-01 00:00:00'),24, Timestamp('2016-01-10 00:00:00'),Timestamp('2016-01-10 00:00:00'), Seasonally Adjusted, SA,Monetary Services Index: MZM (preferred),Billions of Dollars, Bil. of $

Search tags
^^^^^^^^^^^

Get the tags for a series search:

::

    params = {
             'limit':5
             }

    res = fr.series.search_tags('money service index',params=params)
    print res

The response includes the tag group_id, name, and series_count
associated with a given series search.

.. csv-table::
  :header:  created,group_id,name,notes,popularity,series_count

      2012-08-29 15:22:19,gen,academic data,"Time series data created mainly by academia to address growing demand in understanding specific concerns in the economy that are not well modeled by ordinary statistical agencies.",62,25
      2013-06-21 15:22:49,src,anderson & jones,Richard Anderson and Barry Jones,35,25
      2014-11-17 19:34:12,src,"anderson, richard g.",,37,25
      2012-02-27 16:18:19,gen,divisia,Monetary Services Indexes,35,25
      2012-02-27 16:18:19,src,frb stl,Federal Reserve Bank of St. Louis (source),83,25

Search releated tags
^^^^^^^^^^^^^^^^^^^^

Get the related tags for a series search:

::

    params = {
             'limit':5,
             'order_by':'popularity',
             'sort_order':'desc'
             }

    res = fr.series.search_related_tags('mortgage rate','30-year;frb',params=params)

The response includes the tag group_id, name, and series_count
associated with a given series search.

.. csv-table::
  :header:  created,group_id,name,notes,popularity,series_count

      2012-02-27 16:18:19,geot,nation,Country Level,100,3
      2012-02-27 16:18:19,geo,usa,United States of America,100,3
      2012-02-27 16:18:19,seas,nsa,Not seasonally adjusted,97,3
      2012-02-27 16:18:19,freq,monthly,,94,1
      2012-05-29 15:14:19,gen,interest rate,,91,3


Sources
~~~~~~~

Economic data series derive from a variety
of sources,including the Federal Reserve Bank,
Bureau of Labor Statistics,Bureau of Economic Analysis,
and Census Bureau.

All sources
^^^^^^^^^^^

Get all sources:

::

    params = {
             'limit':10
             }

    res = fr.source.sources(params=params)
    print res

The response includes source ID, name, and link to the source:

.. csv-table::
  :header: id,link,name,realtime_end,realtime_start

      1,http://www.federalreserve.gov/,Board of Governors of the Federal Reserve System (US),2016-01-10 00:00:00,2016-01-10 00:00:00
      3,http://www.philadelphiafed.org/,Federal Reserve Bank of Philadelphia,2016-01-10 00:00:00,2016-01-10 00:00:00
      4,http://www.stlouisfed.org/,Federal Reserve Bank of St. Louis,2016-01-10 00:00:00,2016-01-10 00:00:00
      6,http://www.ffiec.gov/,Federal Financial Institutions Examination Council (US),2016-01-10 00:00:00,2016-01-10 00:00:00
      11,http://www.dowjones.com,Dow Jones & Company,2016-01-10 00:00:00,2016-01-10 00:00:00
      13,http://www.ism.ws/,Institute for Supply Management,2016-01-10 00:00:00,2016-01-10 00:00:00
      14,https://www.umich.edu/,University of Michigan,2016-01-10 00:00:00,2016-01-10 00:00:00
      15,http://www.whitehouse.gov/cea/,Council of Economic Advisers (US),2016-01-10 00:00:00,2016-01-10 00:00:00
      16,http://www.whitehouse.gov/omb/,US. Office of Management and Budget,2016-01-10 00:00:00,2016-01-10 00:00:00
      17,http://www.cbo.gov/,US. Congressional Budget Office,2016-01-10 00:00:00,2016-01-10 00:00:00

Details
^^^^^^^

To request source details, provide a source ID to the
details method of the source client:

::

    res = fr.source.details(1)
    print res

The response includes the series frequency, observation period,
and popularity, among other descriptive features.

.. csv-table::
  :header: id, link,name, realtime_end, realtime_start

      1,http://www.federalreserve.gov/,Board of Governors of the Federal Reserve System (US),2016-01-10 00:00:00,2016-01-10 00:00:00


Releases
^^^^^^^^

To request source details, provide a source ID to the
details method of the source client:

::

    params = {
             'limit':10
             }

    res = fr.source.releases(1,params=params)
    print res

The response includes the source ID, name, and a link to the source:

.. csv-table::
  :header: id,link,name,notes,press_release,realtime_end,realtime_start

      13,http://www.federalreserve.gov/releases/g17/,G.17 Industrial Production and Capacity Utilization,,True,2016-01-10 00:00:00,2016-01-10 00:00:00
      14,http://www.federalreserve.gov/releases/g19/,G.19 Consumer Credit,,True,2016-01-10 00:00:00,2016-01-10 00:00:00
      15,http://www.federalreserve.gov/releases/g5/,G.5 Foreign Exchange Rates,,True,2016-01-10 00:00:00,2016-01-10 00:00:00
      17,http://www.federalreserve.gov/releases/h10/,H.10 Foreign Exchange Rates,,True,2016-01-10 00:00:00,2016-01-10 00:00:00
      18,http://www.federalreserve.gov/releases/h15/,H.15 Selected Interest Rates,,True,2016-01-10 00:00:00,2016-01-10 00:00:00
      19,http://www.federalreserve.gov/releases/h3/,H.3 Aggregate Reserves of Depository Institutions and the Monetary Base,,True,2016-01-10 00:00:00,2016-01-10 00:00:00
      20,http://www.federalreserve.gov/releases/h41/,H.4.1 Factors Affecting Reserve Balances,,True,2016-01-10 00:00:00,2016-01-10 00:00:00
      21,http://www.federalreserve.gov/releases/h6/,H.6 Money Stock Measures,,True,2016-01-10 00:00:00,2016-01-10 00:00:00
      22,http://www.federalreserve.gov/releases/h8/,H.8 Assets and Liabilities of Commercial Banks in the United States,,True,2016-01-10 00:00:00,2016-01-10 00:00:00
      52,http://www.federalreserve.gov/releases/z1/,Z.1 Financial Accounts of the United States,"The Financial Accounts (formerly known as the Flow of Funds accounts)  are a set of financial accounts used to track the sources and uses of funds by sector. They are a component of a system of macroeconomic accounts including the National Income and Product accounts (NIPA) and balance of payments accounts, all of which serve as a comprehensive set of information on the economyâs performance.(1) Some important inferences that can be drawn from the Financial accounts are the financial strength of a given sector, new economic trends, changes in the composition of wealth, and development of new financial instruments over time.(1)
      Sectors are compiled into three categories: households, nonfinancial businesses, and banks. The sources of funds for a sector are its internal funds (savings from income after consumption) and external funds (loans from banks and other financial intermediaries). (1) Funds for a given sector are used for its investments in physical and financial assets. Dividing sources and uses of funds into two categories helps the staff of the Federal Reserve System pay particular attention to external sources of funds and financial uses of funds.(2) One example is whether households are borrowing more from banksâor in other words, whether household debt is rising. Another example might be whether banks are using more of their funds to provide loans to consumers. Transactions within a sector are not shown in the accounts; however, transactions between sectors are.(2) Monitoring the external flows of funds provides insights into a sectorâs health and the performance of the economy as a whole.
      Data for the Financial accounts are compiled from a large number of reports and publications, including regulatory reports such as those submitted by banks, tax filings, and surveys conducted by the Federal Reserve System.(2) The Financial accounts are published quarterly as a set of tables in the Federal Reserveâs Z.1 statistical release.
      (1)	Teplin, Albert M. âThe U.S. Flow of Funds Accounts and Their Uses.â Federal Reserve Bulletin, July 2001; http://www.federalreserve.gov/pubs/bulletin/2001/0701lead.pdf.
      (2)	Board of Governors of the Federal Reserve System. âGuide to the Flow of Funds Accounts.â 2000, http://www.federalreserve.gov/apps/fof/.",True,2016-01-10 00:00:00,2016-01-10 00:00:00


Tags
~~~~

Economic data series derive from a variety
of sources,including the Federal Reserve Bank,
Bureau of Labor Statistics,Bureau of Economic Analysis,
and Census Bureau.

All tags
^^^^^^^^

Get all tags:

::

      params = {
               'limit':10
               }

      res = fr.tag.tags(params=params)
      print res

The response includes the group ID, name, and popularity:

.. csv-table::
  :header: created,group_id,name,notes,popularity,series_count

        2012-02-27 16:18:19,seas,nsa,Not seasonally adjusted,97,326950
        2012-02-27 16:18:19,geo,usa,United States of America,100,248427
        2012-02-27 16:18:19,freq,annual,,84,222080
        2012-02-27 16:18:19,geot,nation,Country Level,100,163584
        2012-02-27 16:18:19,src,census,US. Bureau of the Census,79,121069
        2012-02-27 16:18:19,geot,county,"County, Parish, or Borough Level",68,100793
        2012-02-27 16:18:19,src,bls,US. Bureau of Labor Statistics,86,100575
        2012-02-27 16:18:19,freq,monthly,,94,94751
        2012-02-27 16:18:19,gen,employment,,77,88557
        2015-12-30 19:26:34,rls,saipe,Small Area Income and Poverty Estimates (SAIPE),50,80957

Series
^^^^^^

Get series associated with tags:

::

    params = {
             'limit':2
             }

    res = fr.tag.series('slovenia;food',params=params)
    print res

The response includes the series details:

.. csv-table::
  :header: frequency,frequency_short,id,last_updated,notes,observation_end,observation_start,popularity,realtime_end,realtime_start,seasonal_adjustment,seasonal_adjustment_short,title,units,units_short

      Monthly,M,00XEFDSIM086NEST,2015-12-16 16:08:23,"The Harmonized Index of Consumer Prices category ""Overall Index Excluding Energy, Food, Alcohol, and Tobacco (00XEFOOD)"" is a classification of nondurable goods, semi-durable goods, durable goods, and services that includes Clothing Materials (03.1.1), Garments (03.1.2), Other Articles of Clothing and Clothing Accessories (03.1.3), Cleaning, Repair, and Hire of Clothing (03.1.4), Shoes and Other Footwear including Repair and Hire of Footwear (03.2.1/2), Actual Rentals Paid by Tenants including Other Actual Rentals (04.1.1/2), Materials for the Maintenance and Repair of the Dwelling (04.3.1), Services for the Maintenance and Repair of the Dwelling (04.3.2), Water Supply (04.4.1), Refuse Collection (04.4.2), Sewerage Collection (04.4.3), Other Services Relating to the Dwelling, Not Elsewhere Classified (04.4.4), Furniture and Furnishings (05.1.1), Carpets and Other Floor Coverings (05.1.2), Repair of Furniture, Furnishings, and Floor Coverings (05.1.3), Household Textiles (05.2), Major Household Appliances whether Electric or not and Small Electric Household Appliances (05.3.1/2), Repair of Household Appliances (05.3.3), Glassware, Tableware, and Household Utensils (05.4), Major Tools and Equipment and Small Tools and Miscellaneous Accessories (05.5.1/2), Nondurable Household Goods (05.6.1), Domestic Services and Household Services (05.6.2), Pharmaceutical Products (06.1.1), Other Medical Products, Therapeutic Appliances and Equipment (06.1.2/3), Medical and Paramedical Services (06.2.1/3), Dental Services (06.2.2), Hospital Services (06.3), Motor Cars (07.1.1), Motor Cycles, Bicycles, and Animal Drawn Vehicles (07.1.2/3/4), Spare Parts and Accessories for Personal Transport Equipment (07.2.1), Maintenance and Repair of Personal Transport Equipment (07.2.3), Other Services in respect of Personal Transport Equipment (07.2.4), Passenger Transport by Railway (07.3.1), Passenger Transport by Road (07.3.2), Passenger Transport by Air (07.3.3), Passenger Transport by Sea and Inland Waterway (07.3.4), Combined Passenger Transport (07.3.5), Other Purchased Transport Services (07.3.6), Postal Services (08.1), Telephone and Telefax Equipment and Telephone and Telefax Services (08.2/3), Equipment for the Reception, Recording, and Reproduction of Sound and Pictures (09.1.1), Photographic and Cinematographic Equipment and Optical Instruments (09.1.2), Information Processing Equipment (09.1.3), Recording Media (09.1.4), Repair of Audio-Visual, Photographic and Information Processing Equipment (09.1.5), Major Durables for Indoor and Outdoor Recreation including Musical Instruments (09.2.1/2), Maintenance and Repair of Other Major Durables for Recreation and Culture (09.2.3), Games, Toys, and Hobbies (09.3.1), Equipment for Sport, Camping, and Open-Air Recreation (09.3.2), Gardens, Plants, and Flowers (09.3.3), Pets and Related Products including Veterinary and Other Services for Pets (09.3.4/5), Recreational and Sporting Services (09.4.1), Cultural Services (09.4.2), Books (09.5.1), Newspapers and Periodicals (09.5.2), Miscellaneous Printed Matter, Stationery, and Drawing Materials (09.5.3/4), Package Holidays (09.6), Pre-Primary and Primary, Secondary, Post-Secondary Non-Tertiary, Tertiary Education, and Education not definable by Level (10.X), Restaurants, cafÃ©s, and the Like (11.1.1), Canteens (11.1.2), Accommodation Services (11.2), Hairdressing Salons and Personal Grooming Establishments (12.1.1), Electric Appliances for Personal Care and Other Appliances, Articles, and Products for Personal Care (12.1.2/3), Jewelry, Clocks, and Watches (12.3.1), Other Personal Effects (12.3.2), Social Protection (12.4), Insurance connected with the Dwelling (12.5.2), Insurance connected with Health (12.5.3), Insurance connected with Transport (12.5.4), Other Insurance (12.5.5) Other Financial Services , Not Elsewhere Classified (12.6.2), and Other Services, Not Elsewhere Classified (12.7).

      Information provided in the notes pertaining to Special Aggregates HICP classifications can be found from the source at: http://ec.europa.eu/eurostat/ramon/nomenclatures/index.cfm?TargetUrl=ACT_OTH_CLS_DLD&StrNom=HICP_2000&StrFormat=HTML&StrLanguageCode=EN&IntKey=22476519.

      Copyright, European Union, 1995-2014, http://epp.eurostat.ec.europa.eu/portal/page/portal/about_eurostat/policies/copyright_licence_policy.",2015-11-01 00:00:00,1999-12-01 00:00:00,0,2016-01-10 00:00:00,2016-01-10 00:00:00,Not Seasonally Adjusted,NSA,"Harmonized Index of Consumer Prices: Overall Index Excluding Energy, Food, Alcohol, and Tobacco for SloveniaÂ©",Index 2005=100,Index 2005=100
      Monthly,M,00XESESIM086NEST,2015-12-16 16:08:16,"The Harmonized Index of Consumer Prices category ""Overall Index Excluding Energy and Seasonal Food (00XESEAS)"" is a classification of nondurable goods, semi-durable goods, durable goods, and services that includes Bread and Cereals (01.1.1), Meat (01.1.2), Milk, Cheese, and Eggs (01.1.4), Oils and Fats (01.1.5), Sugar, Jam, Honey, Chocolate, and Confectionery (01.1.8), Food Products, Not Elsewhere Classified (01.1.9), Coffee, Tea, and Cocoa (01.2.1), Mineral Waters, Soft Drinks, and Fruit and Vegetable Juices (01.2.2), Spirits (02.1.1), Wine (02.1.2), Beer (02.1.3), Tobacco (02.2), Clothing Materials (03.1.1), Garments (03.1.2), Other Articles of Clothing and Clothing Accessories (03.1.3), Cleaning, Repair, and Hire of Clothing (03.1.4), Shoes and Other Footwear including Repair and Hire of Footwear (03.2.1/2), Actual Rentals Paid by Tenants including Other Actual Rentals (04.1.1/2), Materials for the Maintenance and Repair of the Dwelling (04.3.1), Services for the Maintenance and Repair of the Dwelling (04.3.2), Water Supply (04.4.1), Refuse Collection (04.4.2), Sewerage Collection (04.4.3), Other Services Relating to the Dwelling, Not Elsewhere Classified (04.4.4), Furniture and Furnishings (05.1.1), Carpets and Other Floor Coverings (05.1.2), Repair of Furniture, Furnishings, and Floor Coverings (05.1.3), Household Textiles (05.2), Major Household Appliances whether Electric or not and Small Electric Household Appliances (05.3.1/2), Repair of Household Appliances (05.3.3), Glassware, Tableware, and Household Utensils (05.4), Major Tools and Equipment and Small Tools and Miscellaneous Accessories (05.5.1/2), Nondurable Household Goods (05.6.1), Domestic Services and Household Services (05.6.2), Pharmaceutical Products (06.1.1), Other Medical Products, Therapeutic Appliances and Equipment (06.1.2/3), Medical and Paramedical Services (06.2.1/3), Dental Services (06.2.2), Hospital Services (06.3), Motor Cars (07.1.1), Motor Cycles, Bicycles, and Animal Drawn Vehicles (07.1.2/3/4), Spare Parts and Accessories for Personal Transport Equipment (07.2.1), Maintenance and Repair of Personal Transport Equipment (07.2.3), Other Services in respect of Personal Transport Equipment (07.2.4), Passenger Transport by Railway (07.3.1), Passenger Transport by Road (07.3.2), Passenger Transport by Air (07.3.3), Passenger Transport by Sea and Inland Waterway (07.3.4), Combined Passenger Transport (07.3.5), Other Purchased Transport Services (07.3.6), Postal Services (08.1), Telephone and Telefax Equipment and Telephone and Telefax Services (08.2/3), Equipment for the Reception, Recording, and Reproduction of Sound and Pictures (09.1.1), Photographic and Cinematographic Equipment and Optical Instruments (09.1.2), Information Processing Equipment (09.1.3), Recording Media (09.1.4), Repair of Audio-Visual, Photographic and Information Processing Equipment (09.1.5), Major Durables for Indoor and Outdoor Recreation including Musical Instruments (09.2.1/2), Maintenance and Repair of Other Major Durables for Recreation and Culture (09.2.3), Games, Toys, and Hobbies (09.3.1), Equipment for Sport, Camping, and Open-Air Recreation (09.3.2), Gardens, Plants, and Flowers (09.3.3), Pets and Related Products including Veterinary and Other Services for Pets (09.3.4/5), Recreational and Sporting Services (09.4.1), Cultural Services (09.4.2), Books (09.5.1), Newspapers and Periodicals (09.5.2), Miscellaneous Printed Matter, Stationery, and Drawing Materials (09.5.3/4), Package Holidays (09.6), Pre-Primary and Primary, Secondary, Post-Secondary Non-Tertiary, Tertiary Education, and Education not definable by Level (10.X), Restaurants, cafÃ©s, and the Like (11.1.1), Canteens (11.1.2), Accommodation Services (11.2), Hairdressing Salons and Personal Grooming Establishments (12.1.1), Electric Appliances for Personal Care and Other Appliances, Articles, and Products for Personal Care (12.1.2/3), Jewelry, Clocks, and Watches (12.3.1), Other Personal Effects (12.3.2), Social Protection (12.4), Insurance connected with the Dwelling (12.5.2), Insurance connected with Health (12.5.3), Insurance connected with Transport (12.5.4), Other Insurance (12.5.5) Other Financial Services , Not Elsewhere Classified (12.6.2), and Other Services, Not Elsewhere Classified (12.7).

      Information provided in the notes pertaining to Special Aggregates HICP classifications can be found from the source at: http://ec.europa.eu/eurostat/ramon/nomenclatures/index.cfm?TargetUrl=ACT_OTH_CLS_DLD&StrNom=HICP_2000&StrFormat=HTML&StrLanguageCode=EN&IntKey=22476519.

      Copyright, European Union, 1995-2014, http://epp.eurostat.ec.europa.eu/portal/page/portal/about_eurostat/policies/copyright_licence_policy.",2015-11-01 00:00:00,1999-12-01 00:00:00,0,2016-01-10 00:00:00,2016-01-10 00:00:00,Not Seasonally Adjusted,NSA,Harmonized Index of Consumer Prices: Overall Index Excluding Energy and Seasonal Food for SloveniaÂ©,Index 2005=100,Index 2005=100


Related tags
^^^^^^^^^^^^

Get related tags:

::

    params = {
             'limit':5,
             'exclude_tag_names':'goods',
             'sort_order':'desc'
             }

    res = fr.tag.related_tags('services;quarterly',params=params)
    print res

The response includes the group ID, name, and popularity:

.. csv-table::
  :header: created,group_id,name,notes,popularity,series_count

        2012-02-27 16:18:19,geot,nation,Country Level,100,1752
        2012-02-27 16:18:19,seas,nsa,Not seasonally adjusted,97,1230
        2012-02-27 16:18:19,geo,usa,United States of America,100,1200
        2012-08-16 20:21:17,rls,mei,Main Economic Indicators,77,1172
        2012-02-27 16:18:19,src,oecd,Organisation for Economic Co-operation and Development,77,1172
