# PartialStreamsTypesStreamsModelCreate_

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_url** | **str** | Webhook URL where moralis will send the POST request. | [optional] 
**description** | **str** | A description for this stream | [optional] 
**tag** | **str** | A user-provided tag that will be send along the webhook, the user can use this tag to identify the specific stream if multiple streams are present | [optional] 
**token_address** | **str** | The token address of the contract, required if the type : log | [optional] 
**topic0** | **str** | The topic0 of the event in hex, required if the type : log | [optional] 
**include_native_txs** | **bool** | Include or not native transactions defaults to false (only applied when type:contract) | [optional] 
**abi** | **AllOfPartialStreamsTypesStreamsModelCreateAbi** |  | [optional] 
**filter** | **AllOfPartialStreamsTypesStreamsModelCreateFilter** |  | [optional] 
**address** | **str** | The wallet address of the user, required if the type : tx | [optional] 
**chain_ids** | **list[str]** | The ids of the chains for this stream in hex Ex: [\&quot;0x1\&quot;,\&quot;0x38\&quot;] | [optional] 
**type** | [**StreamsType**](StreamsType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

