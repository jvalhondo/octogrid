octogrid
========

    GitHub following network visualizer for Humans

.. image:: https://img.shields.io/pypi/v/octogrid.svg?style=flat-square
    :target: https://pypi.python.org/pypi/octogrid/
    :alt: Latest Version
    
.. image:: https://img.shields.io/badge/Python-2.6%2C%202.7-brightgreen.svg?style=flat-square
    :target: https://pypi.python.org/pypi/octogrid/
    :alt: Supported Python versions
    
.. image:: https://img.shields.io/pypi/l/octogrid.svg?style=flat-square
    :target: https://pypi.python.org/pypi/octogrid/
    :alt: License

.. image:: https://img.shields.io/pypi/dm/octogrid.svg?style=flat-square
    :target: https://pypi.python.org/pypi/octogrid/
    :alt: Downloads
    
octogrid in action
~~~~~~~~~~~~~~~~~~

`interactive version <https://plot.ly/~octogrid/4/github-network-for-pravj/>`_

.. figure:: https://github.com/pravj/gitpool/raw/master/octogrid/github-network.png
   :alt: Communities in GitHub Following Network for @pravj
    
Installation
~~~~~~~~~~~~
    pip install octogrid
    
If you are facing issues (on Linux) with 'python-igraph', you should consider installing required libraries first.

    apt-get install -y libigraph0-dev
    
How to
~~~~~~
- You need to `create an account <https://plot.ly/>`_ on Plotly to see your visualizations, it's free.
- Once you have an account there, execute the following in your terminal to setup your user credentials.

    python -c "import plotly; plotly.tools.set_credentials_file(username='USERNAME', api_key='APIKEY')"
    
- Your API key can be collected `from here <https://plot.ly/settings/api/>`_.
- All these steps aren't compulsory, though. If you leave them, *octogrid* will create plots via its own account.

Usage
~~~~~
- **octogrid generate [--reset] [--user=<username>]**

    Generate the GML file for user representing its GitHub following graph

- **octogrid publish [--reset] [--user=<username>]**

    Publish the user's GitHub community graph using Plotly
    
**--reset** (*optional*) flag is used to clear the cache storage for a given user

Powered By
~~~~~~~~~~

.. image:: https://github.com/pravj/gitpool/raw/master/octogrid/plotly-logo.png
    :alt: Plotly [Image Credit : Pensrulerstape - Own work, CC BY-SA 4.0, $3]

License
~~~~~~~~~~~~
    MIT © `Plotly <https://plot.ly>`_.
