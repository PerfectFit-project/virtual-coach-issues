from behave import *
import requests

RASA_URL = 'http://localhost:5005'
EXPECTED_RUNNING_DISTANCE_RESPONSE = 'you should run 40.0 kilometers this week'

@given('rasa bot is up and running')
def step_impl(context):
    r = requests.get(RASA_URL)
    assert r.status_code == 200
    r.raise_for_status()

@given('virtual coach db is up and running')
def step_impl(context):
    r = requests.get(RASA_URL)
    assert r.status_code == 200
    r.raise_for_status()

@when('we ask for the agenda')
def step_impl(context):
    webhookurl = RASA_URL + '/webhooks/rest/webhook'

    body = {
            "message": "Kan ik de agenda voor de week krijgen?",
            "sender":"user"
            }

    query_params = None
    headers = {"Accept": "application/json"}
    r = requests.post(webhookurl, json=body)
    r.raise_for_status()

    assert r.status_code == 200

    context.chat_responses = r.json()

@then('all messages are found to be addressed to the user')
def step_impl(context):
    for msg in context.chat_responses:
        assert 'recipient_id' in msg
        assert msg['recipient_id'] == 'user'


@then('advice on running distance is given')
def step_impl(context):
    for msg in context.chat_responses:
        assert 'text' in msg
        if EXPECTED_RUNNING_DISTANCE_RESPONSE in msg['text']:
            break
    else:
        assert False

