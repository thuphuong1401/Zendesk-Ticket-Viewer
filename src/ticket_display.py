from ticket_API import TicketAPI

class TicketDisplay:
    
    def __init__(self, auth):
        self.subdomain = auth["subdomain"]
        self.ticket_API = TicketAPI(auth["email"], auth["password"])
        self.current_page = 1


    def display_unavailable_API(self):
        print("Error: the Zendesk ticket API is unavailable at the moment!")

    def display_menu(self):
        print("Select view options: \n")
        print("* Press 1 to view all tickets \n")
        print("* Press 2 to view a ticket \n")
        print("* Type \'quit\' to exit")

    def display_page(self):
        pass

    def display_ticket_with_id(self):
        pass

    def display_ending(self):
        print("Thank you for using Zendesk Ticket Viewer Application by Phuong Vu! \n Have a nice day ^^")
    
    def display_welcome(self):
        print("Welcome to Zendesk Ticket Viewer Application! \n This application will display tickets at subdomain {}.zendesk.com".format(self.subdomain))

    def display_invalid_input(self):
        print("Invalid input! Please try again")

    def prompt_id(self):
        print("What ticket ID would you like to display? (Enter a number from 1-101)")



    '''
    The menu in the home page will have the following options:

    1: show all tickets (max 25 per page)
        - p: prev page
        - n: next page
        - m: menu
        - quit: quit the program

    2: show individual ticket

    quit: quit the program

    else: invalid option
    '''
    def home_page(self):
        ticket_API = TicketAPI()
        
        response = ticket_API.connect_to_server()
        if response['data'] is None:
            self.display_unavailable_API()
            return 

        self.display_welcome()
        
        while True:
            self.display_menu()
            option = input()

            if option == "1":
                while True:
                    self.display_menu()
                    sub_option = input()
                    if sub_option == "n":
                        self.display_page(self.current_page + 1)
                    elif sub_option == "p":
                        self.display_page(self.current_page - 1)
                    elif sub_option == "quit":
                        self.display_ending()
                        return
                    else:
                        self.display_invalid_input()
            
            elif option == "2":
                self.prompt_id()
                ticket_id = input()
                self.display_ticket_with_id(ticket_id)
            
            elif option == "quit":
                self.display_ending()
                return
            else: 
                self.display_invalid_input()


