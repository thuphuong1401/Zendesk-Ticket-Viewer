import requests
from ticket import Ticket

class TicketAPI:
    
    def __init__(self, auth):
        self.auth = auth
        self.session = requests.Session()
        self.session.auth = (self.auth["email"], self.auth["password"])

    '''
    Get total number of tickets in the database
    Params: none
    Return:
        - an integer which is the total number of tickets in the database
    '''
    def get_total_ticket(self):
        total_ticket_url = "https://zccpvu3.zendesk.com/api/v2/tickets/count.json"
        response = None
        try:
            response = self.session.get(total_ticket_url)
        except ConnectionError as ce:
            print(ce)

        if response:
            total_number_of_tickets = int(response.json()["count"]["value"])
            return total_number_of_tickets
        else:
            return 0


    '''
    Get total number of pages for the whole ticket database, given that at most page_length tickets is displayed
    Params: 
        - page_length: maximum number of tickets displayed per page. For this challenge, it is 25
    Returns: 
        - total number of pages
    '''
    def get_max_page(self, page_length):
        max_page_url = "https://zccpvu3.zendesk.com/api/v2/tickets/count.json"
        response = None
        try:
            response = self.session.get(max_page_url)
        except ConnectionError as ce:
            print(ce)

        if response:
            max_page_number = response.json()["count"]["value"] / page_length
            if int(max_page_number) == max_page_number:
                return int(max_page_number)
            else:
                return int(max_page_number) + 1
    
    
    '''
    Check whether the API is available for connection.
    Params: none
    Return: 
        - If the API is available, return all ticket data 
        - Else return None
    '''
    def connect_to_server(self):
        if self.auth is None:
            return 

        url = "https://zccpvu3.zendesk.com/api/v2/tickets.json"
        response = self.session.get(url)
        
        if response.status_code != 200:
            return 

        ticket_data = response.json()
        return ticket_data


    '''
    Display all tickets, at most page_length per page, with options to go to next page (press n) or go to previous page (press p)
    Params: 
        - page_length: maximum number of tickets displayed per page. For this challenge, it is 25
        - page_number: the page that the user wants to display
    Return: 
        - a list of ticket objects corresponding to all tickets on that page
    '''
    def get_ticket_page(self, page_length, page_number):
        ticket__page_url = "https://zccpvu3.zendesk.com/api/v2/tickets.json?per_page={}&page={}".format(page_length, page_number)
        response = None
        try:
            response = self.session.get(ticket__page_url)
        except ConnectionError as ce:
            print(ce)

        if response:
            ticket_page_json = response.json()["tickets"]
            ticket_page = []
            for ticket_json in ticket_page_json:
                ticket = Ticket(ticket_json)
                ticket_page.append(ticket)
            return ticket_page
        else: 
            return response
        

    '''
    Get a ticket with a specific ID
    Params: 
        - id: the ID of the ticket that the user wishes to view
    Return: 
        - an object of Ticket class, or None if invalid ticket ID
    '''
    def get_ticket_with_id(self, id):
        ticket_url = "https://zccpvu3.zendesk.com/api/v2/tickets/{}.json".format(str(id))
        response = None
        try:
            response = self.session.get(ticket_url)
        except ConnectionError as ce:
            print(ce)

        if response:
            ticket_json = response.json()["ticket"]
            ticket = Ticket(ticket_json)
            return ticket
        else: 
            return None

