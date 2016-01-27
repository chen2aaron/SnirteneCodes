from raven import Client

client = Client('http://90d8cf4e3c3141f5b05e0913dccab853:373e7379a01947e1961bdaf83df1c2a5@sentry.morningchen.com/3')
client.captureMessage('Starting script')

for i in range(4):
    try:
        1 / 0
    except ZeroDivisionError:
        client.captureException()

client.captureMessage('End of script')
