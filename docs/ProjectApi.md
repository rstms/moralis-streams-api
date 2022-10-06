# moralis_streams_api.ProjectApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_settings**](ProjectApi.md#get_settings) | **GET** /settings | 
[**set_settings**](ProjectApi.md#set_settings) | **POST** /settings | 

# **get_settings**
> SettingsTypesSettingsModel get_settings()



Get the settings for the current project based on the project api-key.

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
api_instance = moralis_streams_api.ProjectApi(moralis_streams_api.ApiClient(configuration))

try:
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsTypesSettingsModel**](SettingsTypesSettingsModel.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_settings**
> SettingsTypesSettingsModel set_settings(body)



Set the settings for the current project based on the project api-key.

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
api_instance = moralis_streams_api.ProjectApi(moralis_streams_api.ApiClient(configuration))
body = moralis_streams_api.SettingsTypesSettingsModel() # SettingsTypesSettingsModel | 

try:
    api_response = api_instance.set_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsTypesSettingsModel**](SettingsTypesSettingsModel.md)|  | 

### Return type

[**SettingsTypesSettingsModel**](SettingsTypesSettingsModel.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

