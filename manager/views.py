from django.shortcuts import render, HttpResponse

from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACf05b05f4990b0afeebec70deab1963a9'
auth_token = ''
client = Client(account_sid, auth_token)


def initiate_contact(request):
    data= {}
    msg = 'Hello {}! You can find information about your visit, prescription, and other useful information at {}. Would you like to receive a reminder for your medication? Y/N?'.format(name, url)
    message = client.messages.create(
        from_='hospital_num',
        body=msg,
        to=phone_number
    )

    print(message.sid)

@csrf_exempt
def receive_from_twilio(request):
    from_user = request.POST.get('From', '')
    user_message = request.POST.get('Body', '')
    r = MessagingResponse()
    r.message('Hello {}!'.format(from_user))
    return HttpResponse(str(r), content_type='text/xml')

@csrf_exempt
def call_response(request):
    return HttpResponse('<?xml version="1.0" encoding="UTF-8"?><Response><Say voice="alice">Take your prescription bitch!</Say></Response>', content_type='text/xml')

@csrf_exempt
def start_call(request):
    call = client.calls.create(
        url='http://d91b0f91.ngrok.io/api/response',
        to='+17173953498',
        from_='+17178961982'
    )
    return HttpResponse()
