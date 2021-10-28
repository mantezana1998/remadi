import requests, os
from dotenv import load_dotenv
import pprint
load_dotenv()

def ticket_master_events():
    try:
        def grab_what_we_need(event):
            return {
            # 'ticket_master_id': event['id*'],
            'name': event['name'],
            'location': event['_embedded']['venues'][0]['name'],
            'time': event['dates']['start']['localTime'],
            'dates': event['dates']['start']['localDate'],
            # 'price': float(event['priceRanges']),        
            }
        apikey = os.getenv("TICKET_MASTER")
        response = requests.get(f'https://app.ticketmaster.com/discovery/v2/events.json?size=1&apikey={apikey}')
        event = response.json()
        # print(event,'<------------------------------------------------------------Events')
        if event == None:
            raise Exception('couldnt catch')
        results = event['_embedded']['events']
        return list(map(grab_what_we_need, results))
    except: 
        return 'couldnt catch'