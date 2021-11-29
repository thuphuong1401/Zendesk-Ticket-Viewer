import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))) + '/src')
from ticket_API import TicketAPI
from ticket_display import TicketDisplay
from ticket import Ticket
import unittest
import json


class Test(unittest.TestCase):

    '''
    Test function for connecting to server with correct authentication credentials
    '''

    def test_connect_to_server_correct_auth(self):
        correct_auth = {"email": "pvu140100@gmail.com",
                        "password": "Thuphuong1401*"}
        ticket_API = TicketAPI(correct_auth)
        response = ticket_API.connect_to_server()
        self.assertIsNotNone(
            response, 'Error: if successfully authenticated, the response from connect_to_server() should be other than none')

    '''
    Test function for connecting to server with wrong authentication credentials
    '''

    def test_connect_to_server_wrong_auth(self):
        wrong_auth = {"email": "pvu140100@gmail.com",
                      "password": "Thuphuongvu1401*"}
        ticket_API = TicketAPI(wrong_auth)
        response = ticket_API.connect_to_server()
        self.assertIsNone(
            response, 'Error: with wrong credentials, the response from connect_to_server() should be none')

    '''
    Test function for getting total number of tickets
    '''

    def test_get_total_ticket(self):
        correct_auth = {"email": "pvu140100@gmail.com",
                        "password": "Thuphuong1401*"}
        ticket_API = TicketAPI(correct_auth)
        total_tickets = ticket_API.get_total_ticket()
        self.assertEqual(
            total_tickets, 101, 'Error: function get_total_ticket() in ticket_API.py returns the wrong total number of tickets')

    '''
    Test function for getting total number of pages
    '''
    def test_get_max_page(self):
        correct_auth = {"email": "pvu140100@gmail.com",
                        "password": "Thuphuong1401*"}
        ticket_API = TicketAPI(correct_auth)
        max_page_4 = ticket_API.get_max_page(4)
        max_page_25 = ticket_API.get_max_page(25)
        self.assertEqual(
            max_page_4, 26, 'Error: function get_max_page() in ticket_API.py returns the wrong max number of pages')
        self.assertEqual(
            max_page_25, 5, 'Error: function get_max_page() in ticket_API.py returns the wrong max number of pages')

    '''
    Test function for getting a ticket with a correct ID
    '''
    def test_get_ticket_with_id(self):
        correct_auth = {"email": "pvu140100@gmail.com",
                        "password": "Thuphuong1401*"}
        ticket_API = TicketAPI(correct_auth)
        id = 101
        output = ticket_API.get_ticket_with_id(id)
        expected_json = {"id": 101, "assignee_id": 1902357847384, "submitter_id": 1902357847384, "subject": "in nostrud occaecat consectetur aliquip", "description": "Esse esse quis ut esse nisi tempor sunt. Proident officia incididunt cupidatat laborum ipsum duis. Labore qui labore elit consequat.\n\nDo id nisi qui et fugiat culpa veniam consequat ad amet ut nisi ipsum. Culpa exercitation consectetur adipisicing sunt reprehenderit. Deserunt consequat aliquip tempor anim officia elit proident commodo consequat aute. Magna enim esse tempor incididunt ipsum dolore Lorem cupidatat incididunt.", 
        "url": "https://zccpvu3.zendesk.com/api/v2/tickets/101.json", "status": "open", "created_at" : "2021-11-28T03:22:15Z"}
        expected = Ticket(expected_json)
        self.assertEqual(output, expected, 'Error: function get_ticket_with_id() in ticket_API.py returns the wrong ticket')


    '''
    Test function for getting a ticket with a wrong ID
    '''
    def test_get_ticket_with_wrong_id(self):
        correct_auth = {"email": "pvu140100@gmail.com",
                        "password": "Thuphuong1401*"}
        ticket_API = TicketAPI(correct_auth)
        id = 1000
        output = ticket_API.get_ticket_with_id(id)
        self.assertIsNone(output, 'Error: function get_ticket_with_id() in ticket_API.py should return None when the ticket ID is invalid')


if __name__ == '__main__':
    unittest.main()
