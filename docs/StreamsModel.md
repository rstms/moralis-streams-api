# StreamsModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_url** | **str** | Webhook URL where moralis will send the POST request. | 
**description** | **str** | A description for this stream | 
**tag** | **str** | A user-provided tag that will be send along the webhook, the user can use this tag to identify the specific stream if multiple streams are present | 
**topic0** | **list[str]** | An Array of topic0&#x27;s in hex, required if the type : log | [optional] 
**all_addresses** | **bool** | Include events for all addresses (only applied when abi and topic0 is provided) | [optional] 
**include_native_txs** | **bool** | Include or not native transactions defaults to false (only applied when type:contract) | [optional] 
**include_contract_logs** | **bool** | Include or not logs of contract interactions defaults to false | [optional] 
**include_internal_txs** | **bool** | Include or not include internal transactions defaults to false | [optional] 
**abi** | [**list[AbiItem]**](AbiItem.md) |  | [optional] 
**advanced_options** | [**list[AdvancedOptions]**](AdvancedOptions.md) |  | [optional] 
**chain_ids** | **list[str]** | The ids of the chains for this stream in hex Ex: [\&quot;0x1\&quot;,\&quot;0x38\&quot;] | 
**id** | **str** |  | 
**status** | [**StreamsStatus**](StreamsStatus.md) |  | 
**status_message** | **str** | Description of current status of stream. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

