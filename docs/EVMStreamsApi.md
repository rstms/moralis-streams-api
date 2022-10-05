# moralis_streams_api.EVMStreamsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_address_to_stream**](EVMStreamsApi.md#add_address_to_stream) | **POST** /streams/evm/{id}/address | 
[**create_stream**](EVMStreamsApi.md#create_stream) | **PUT** /streams/evm | 
[**delete_address_from_stream**](EVMStreamsApi.md#delete_address_from_stream) | **DELETE** /streams/evm/{id}/address | 
[**delete_stream**](EVMStreamsApi.md#delete_stream) | **DELETE** /streams/evm/{id} | 
[**get_addresses**](EVMStreamsApi.md#get_addresses) | **GET** /streams/evm/{id}/address | 
[**get_stream**](EVMStreamsApi.md#get_stream) | **GET** /streams/evm/{id} | 
[**get_streams**](EVMStreamsApi.md#get_streams) | **GET** /streams/evm | 
[**update_stream**](EVMStreamsApi.md#update_stream) | **POST** /streams/evm/{id} | 
[**update_stream_status**](EVMStreamsApi.md#update_stream_status) | **POST** /streams/evm/{id}/status | 

# **add_address_to_stream**
> AddressesTypesAddressResponse add_address_to_stream(body, id)



Adds an address to a Stream.

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
api_instance = moralis_streams_api.EVMStreamsApi(moralis_streams_api.ApiClient(configuration))
body = moralis_streams_api.AddressesTypesAddressesAdd() # AddressesTypesAddressesAdd | Provide a Address Model
id = moralis_streams_api.StreamsTypesUUID() # StreamsTypesUUID | The id of the stream to add the address to

try:
    api_response = api_instance.add_address_to_stream(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EVMStreamsApi->add_address_to_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddressesTypesAddressesAdd**](AddressesTypesAddressesAdd.md)| Provide a Address Model | 
 **id** | [**StreamsTypesUUID**](.md)| The id of the stream to add the address to | 

### Return type

[**AddressesTypesAddressResponse**](AddressesTypesAddressResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stream**
> StreamsTypesStreamsModel create_stream(body)



Creates a new evm stream.

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
api_instance = moralis_streams_api.EVMStreamsApi(moralis_streams_api.ApiClient(configuration))
body = moralis_streams_api.StreamsTypesStreamsModelCreate() # StreamsTypesStreamsModelCreate | Provide a Stream Model

try:
    api_response = api_instance.create_stream(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EVMStreamsApi->create_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StreamsTypesStreamsModelCreate**](StreamsTypesStreamsModelCreate.md)| Provide a Stream Model | 

### Return type

[**StreamsTypesStreamsModel**](StreamsTypesStreamsModel.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_address_from_stream**
> AddressesTypesDeleteAddressResponse delete_address_from_stream(body, id)



Deletes an address from a Stream.

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
api_instance = moralis_streams_api.EVMStreamsApi(moralis_streams_api.ApiClient(configuration))
body = moralis_streams_api.AddressesTypesAddressesRemove() # AddressesTypesAddressesRemove | Provide a Address Model
id = moralis_streams_api.StreamsTypesUUID() # StreamsTypesUUID | The id of the stream to delete the address from

try:
    api_response = api_instance.delete_address_from_stream(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EVMStreamsApi->delete_address_from_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddressesTypesAddressesRemove**](AddressesTypesAddressesRemove.md)| Provide a Address Model | 
 **id** | [**StreamsTypesUUID**](.md)| The id of the stream to delete the address from | 

### Return type

[**AddressesTypesDeleteAddressResponse**](AddressesTypesDeleteAddressResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stream**
> StreamsTypesStreamsModel delete_stream(id)



Delete a specific evm stream.

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
api_instance = moralis_streams_api.EVMStreamsApi(moralis_streams_api.ApiClient(configuration))
id = moralis_streams_api.StreamsTypesUUID() # StreamsTypesUUID | The id of the stream to delete

try:
    api_response = api_instance.delete_stream(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EVMStreamsApi->delete_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**StreamsTypesUUID**](.md)| The id of the stream to delete | 

### Return type

[**StreamsTypesStreamsModel**](StreamsTypesStreamsModel.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addresses**
> AddressesTypesAddressesResponse get_addresses(id, limit, cursor=cursor)



Get all addresses associated with a specific stream.

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
api_instance = moralis_streams_api.EVMStreamsApi(moralis_streams_api.ApiClient(configuration))
id = moralis_streams_api.AddressesTypesUUID() # AddressesTypesUUID | the id of the stream to get the addresses from
limit = 1.2 # float | Limit response results max value 100
cursor = 'cursor_example' # str | Cursor for fetching next page (optional)

try:
    api_response = api_instance.get_addresses(id, limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EVMStreamsApi->get_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**AddressesTypesUUID**](.md)| the id of the stream to get the addresses from | 
 **limit** | **float**| Limit response results max value 100 | 
 **cursor** | **str**| Cursor for fetching next page | [optional] 

### Return type

[**AddressesTypesAddressesResponse**](AddressesTypesAddressesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stream**
> StreamsTypesStreamsModel get_stream(id)



Get a specific evm stream.

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
api_instance = moralis_streams_api.EVMStreamsApi(moralis_streams_api.ApiClient(configuration))
id = moralis_streams_api.StreamsTypesUUID() # StreamsTypesUUID | The id of the stream to get

try:
    api_response = api_instance.get_stream(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EVMStreamsApi->get_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**StreamsTypesUUID**](.md)| The id of the stream to get | 

### Return type

[**StreamsTypesStreamsModel**](StreamsTypesStreamsModel.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_streams**
> StreamsTypesStreamsResponse get_streams(limit, cursor=cursor)



Get all the evm streams for the current project based on the project api-key.

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
api_instance = moralis_streams_api.EVMStreamsApi(moralis_streams_api.ApiClient(configuration))
limit = 1.2 # float | Limit response results max value 100
cursor = 'cursor_example' # str | Cursor for fetching next page (optional)

try:
    api_response = api_instance.get_streams(limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EVMStreamsApi->get_streams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Limit response results max value 100 | 
 **cursor** | **str**| Cursor for fetching next page | [optional] 

### Return type

[**StreamsTypesStreamsResponse**](StreamsTypesStreamsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stream**
> StreamsTypesStreamsModel update_stream(body, id)



Updates a specific evm stream.

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
api_instance = moralis_streams_api.EVMStreamsApi(moralis_streams_api.ApiClient(configuration))
body = moralis_streams_api.PartialStreamsTypesStreamsModelCreate_() # PartialStreamsTypesStreamsModelCreate_ | Provide a Stream Model
id = moralis_streams_api.StreamsTypesUUID() # StreamsTypesUUID | The id of the stream to update

try:
    api_response = api_instance.update_stream(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EVMStreamsApi->update_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PartialStreamsTypesStreamsModelCreate_**](PartialStreamsTypesStreamsModelCreate_.md)| Provide a Stream Model | 
 **id** | [**StreamsTypesUUID**](.md)| The id of the stream to update | 

### Return type

[**StreamsTypesStreamsModel**](StreamsTypesStreamsModel.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stream_status**
> StreamsTypesStreamsModel update_stream_status(body, id)



Updates the status of specific evm stream.

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
api_instance = moralis_streams_api.EVMStreamsApi(moralis_streams_api.ApiClient(configuration))
body = moralis_streams_api.StreamsTypesStreamsStatusUpdate() # StreamsTypesStreamsStatusUpdate | Provide a Stream Model
id = moralis_streams_api.StreamsTypesUUID() # StreamsTypesUUID | The id of the stream to update

try:
    api_response = api_instance.update_stream_status(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EVMStreamsApi->update_stream_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StreamsTypesStreamsStatusUpdate**](StreamsTypesStreamsStatusUpdate.md)| Provide a Stream Model | 
 **id** | [**StreamsTypesUUID**](.md)| The id of the stream to update | 

### Return type

[**StreamsTypesStreamsModel**](StreamsTypesStreamsModel.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

