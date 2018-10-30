import requests


def send_put_request(my_body):

    result = requests.put('http://localhost:9000/processes/completetask/23945',
                          data=my_body)


def test_send_different_bodies():

    body1 = {"processProperties": {"objectId": ""},
             "objectData": {"statusCode": "agreedOriginator",
                            "actionType": "approve",
                            "approve": "true",
                            "agreed": "true"}}

    # Send PUT request with first body:
    send_put_request(body1)

    body2 = {"processProperties": {"objectId": ""},
             "objectData": {"statusCode": "agreedOriginator",
                            "actionType": "deny",
                            "approve": "false",
                            "agreed": "false"}}

    # Send PUT request with second body:
    send_put_request(body2)
