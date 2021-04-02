import boto3

connection_handles = [
    "CONNECT",
    "DISCONNECT"
]

REQUEST_HANDLED = {"statusCode": 200}

# we need to populate this after CloudFormation 
SOCKETS_ENDPOINT = "https://gudvhyl103.execute-api.us-east-1.amazonaws.com/latest"

def lambda_handler(event, context):

    connection_id = event["requestContext"].get("connectionId")

    if event["requestContext"]["eventType"] in connection_handles:
        return manage_connection(event,context)
    else:
        return handle_incoming_ws_message(event, context)
        
def manage_connection(event, context):

    connection_id = event["requestContext"].get("connectionId")
    if event["requestContext"]["eventType"] == "CONNECT":
        print(f"connected: {connection_id}")
    else:
        print(f"disconnect: {connection_id}")

    return REQUEST_HANDLED

def handle_incoming_ws_message(event, context):
    connection_id = event["requestContext"].get("connectionId")
    gatewayapi = boto3.client("apigatewaymanagementapi",
                              endpoint_url=SOCKETS_ENDPOINT)
    print(f"SOCKETS_ENDPOINT {SOCKETS_ENDPOINT}")
    print(f"connection {connection_id}")
    print(f"body {event.get('body', '')}")
    gatewayapi.post_to_connection(ConnectionId=connection_id,
                                         Data=event.get("body", ""))
    return REQUEST_HANDLED                                         



        

