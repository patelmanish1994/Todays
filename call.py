from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "AC43abac4023402723816dc4c2508766a0"
AUTH_TOKEN = "c30395e313fdfc83b112c8b70a1127d5"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
call = client.calls.create(to="+918630046738", from_="+12675923022",
                           url="http://foo.com/call.xml")


REENA VISHWAKARMA
SHREYA VISHWAKARMA
DILIP VISHWAKARMA
09767218842