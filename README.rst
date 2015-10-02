Requests-awsv2-auth
===================

AWS v2 signing support for Python-Requests.

Installation::

    pip install requests-awsv2-auth

Usage:

.. code-block:: python

    import requests
    from awsv2_auth import AwsV2Auth

    auth = AwsV2Auth('my-key', 'my-secret')
    response = requests.get('https://sos.exo.io/my-bucket',
                            auth=auth)

This can be used to generate pre-signed URLs as well:

.. code-block:: python

    auth = AwsV2Auth('my-key', 'my-secret')
    url = auth.pre_sign('https://sos.exo.io/my-bucket/path/to/file.txt',
                        method='GET',
                        expires=int(time.time()) + 3600,
                        headers=None)
