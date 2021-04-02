import boto3

connection_handles = [
    "CONNECT",
    "DISCONNECT"
]

REQUEST_HANDLED = {"statusCode": 200}

# we need to populate this after CloudFormation 
SOCKETS_ENDPOINT = "wss://gudvhyl103.execute-api.us-east-1.amazonaws.com/latest"

def lambda_handler(event, context):
    if event["requestContext"]["eventType"] in connection_handles:
        return manage_connection(event,context)
    else:
        return handle_incoming_ws_message(event, context)
        
def manage_connection(event, context):
    return REQUEST_HANDLED

def handle_incoming_ws_message(event, context):
    return reflect_incoming(event["requestContext"].get("connectionId"),event.get("body", ""))
                                        

def reflect_incoming(connection,incoming):
    gatewayapi = boto3.client("apigatewaymanagementapi",
                              endpoint_url=SOCKETS_ENDPOINT)
    gatewayapi.post_to_connection(ConnectionId=connection,
                                         Data=incoming)
    return REQUEST_HANDLED     

        

