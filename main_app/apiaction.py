import requests

response = requests.get('https://app.ticketmaster.com/discovery/v2/events.json?size=1&apikey=GQ3J1mWC3Y8d1xwK6HMbLo5QA6aSmIoI')
event = response.json()
print(event['_embedded']['events'])
