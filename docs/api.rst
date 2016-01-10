.. _api:

API Documentation
=================

All API calls map the raw REST api as closely as possible, including the
distinction between required and optional arguments to the calls. This means
that the code makes distinction between positional and keyword arguments; we,
however, recommend that people **use keyword arguments for all calls for
consistency and safety**.

.. py:module:: fred

Fred
----

.. autoclass:: Fred
   :members:

.. py:module:: fred.clients.categories


Categories
----------

.. autoclass:: CategoriesClient
   :members:


.. py:module:: fred.clients.releases

Releases
--------

.. autoclass:: ReleasesClient
   :members:

.. py:module:: fred.clients.eseries

Series
------

.. autoclass:: ESeriesClient
   :members:

.. py:module:: fred.clients.sources

Sources
-------

.. autoclass:: SourcesClient
   :members:

.. py:module:: fred.clients.tags

Tags
----

.. autoclass:: TagsClient
   :members:
