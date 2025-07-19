from gradio_client import Client

client = Client("kapilmonadi/first-mcp-sentiment-server")
result = client.predict(
		text="I'm feeling great!!",
		api_name="/predict"
)
print(result)