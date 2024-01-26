import json
from task import lambda_handler as task_lambda_handler
from default import lambda_handler as default_lambda_handler

def lambda_handler(event, context):

    function_name = eval(event["function_name"] + '_lambda_handler')
    print(function_name)
    return function_name(event, context)