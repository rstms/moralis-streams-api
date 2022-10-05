# StreamsTypesStreamsModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_url** | **str** | Webhook URL where moralis will send the POST request. | 
**description** | **str** | A description for this stream | 
**tag** | **str** | A user-provided tag that will be send along the webhook, the user can use this tag to identify the specific stream if multiple streams are present | 
**token_address** | **str** | The token address of the contract, required if the type : log | [optional] 
**topic0** | **str** | The topic0 of the event in hex, required if the type : log | [optional] 
**include_native_txs** | **bool** | Include or not native transactions defaults to false (only applied when type:contract) | [optional] 
**abi** | **AllOfstreamsTypesStreamsModelAbi** |  | [optional] 
**filter** | **AllOfstreamsTypesStreamsModelFilter** |  | [optional] 
**address** | **str** | The wallet address of the user, required if the type : tx | [optional] 
**chain_ids** | **list[str]** | The ids of the chains for this stream in hex Ex: [\&quot;0x1\&quot;,\&quot;0x38\&quot;] | 
**type** | [**StreamsType**](StreamsType.md) |  | 
**id** | **str** |  | [optional] 
**status** | [**StreamsStatus**](StreamsStatus.md) |  | [optional] 
**status_message** | **str** | Description of current status of stream. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

