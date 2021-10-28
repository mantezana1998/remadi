import requests, os
from dotenv import load_dotenv
import pprint
load_dotenv()
apikey = os.getenv("TICKET_MASTER")
def single_event(event_id):
    response = requests.get(f'https://app.ticketmaster.com/discovery/v2/events/{event_id}?apikey={apikey}')
    json = response.json()
    def grab_what_we_need(event):
            return {
            'ticket_master_id': event['id'],
            'name': event['name'],
            'location': event['_embedded']['venues'][0]['name'],
            'time': event['dates']['start']['localTime'],
            'dates': event['dates']['start']['localDate'],
            # 'price': event['priceRanges'],        
            }
    return grab_what_we_need(json)

def ticket_master_events():
    try:
        def grab_what_we_need(event):
            return {
              
            'ticket_master_id': event['id'],
            'name': event['name'],
            'location': event['_embedded']['venues'][0]['name'],
            'time': event['dates']['start']['localTime'],
            'dates': event['dates']['start']['localDate'],
            # 'price': event['priceRanges'],        
            }
        apikey = os.getenv("TICKET_MASTER")
        response = requests.get(f'https://app.ticketmaster.com/discovery/v2/events.json?size=10&apikey={apikey}')
        event = response.json()
        # print(event,'<------------------------------------------------------------Events')
        if event == None:
            raise Exception('couldnt catch')
        results = event['_embedded']['events']
        return list(map(grab_what_we_need, results))
    except: 
        print(str(Exception))
        return 'couldnt catch'