# moralis_streams_api.BetaApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stats**](BetaApi.md#get_stats) | **GET** /beta/stats | 

# **get_stats**
> StatsTypesStatsModel get_stats()



Get the stats for the current project based on the project api-key (Beta - This endpoint could be replaced or removed).

### Example
```python
from __future__ import print_function
import time
import moralis_streams_api
from moralis_streams_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = moralis_streams_api.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = moralis_streams_api.BetaApi(moralis_streams_api.ApiClient(configuration))

try:
    api_response = api_instance.get_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatsTypesStatsModel**](StatsTypesStatsModel.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

