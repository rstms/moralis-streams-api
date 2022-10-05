# moralis_streams_api.HistoryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_history**](HistoryApi.md#get_history) | **GET** /history | 
[**replay_history**](HistoryApi.md#replay_history) | **POST** /history/replay/{id} | 

# **get_history**
> HistoryTypesHistoryResponse get_history(limit, cursor=cursor, exclude_payload=exclude_payload)



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
api_instance = moralis_streams_api.HistoryApi(moralis_streams_api.ApiClient(configuration))
limit = 1.2 # float | 
cursor = 'cursor_example' # str |  (optional)
exclude_payload = true # bool |  (optional)

try:
    api_response = api_instance.get_history(limit, cursor=cursor, exclude_payload=exclude_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryApi->get_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**|  | 
 **cursor** | **str**|  | [optional] 
 **exclude_payload** | **bool**|  | [optional] 

### Return type

[**HistoryTypesHistoryResponse**](HistoryTypesHistoryResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replay_history**
> HistoryTypesHistoryModel replay_history(id)



Replay a specific history.

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
api_instance = moralis_streams_api.HistoryApi(moralis_streams_api.ApiClient(configuration))
id = moralis_streams_api.HistoryTypesUUID() # HistoryTypesUUID | The id of the history to replay

try:
    api_response = api_instance.replay_history(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryApi->replay_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**HistoryTypesUUID**](.md)| The id of the history to replay | 

### Return type

[**HistoryTypesHistoryModel**](HistoryTypesHistoryModel.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

