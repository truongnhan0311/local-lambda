from faker import Faker
import json

def lambda_handler(event, context):

    body = json.loads(event)
    msg_in = body["message"]
    print(f'Message received: {msg_in}')

    fake = Faker()
    msg_out = f'Hello {fake.name()}!'
    print(f'Message sent: {msg_out}')
    
    return {'message': msg_out}