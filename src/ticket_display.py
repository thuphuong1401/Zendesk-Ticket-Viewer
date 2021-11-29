from ticket_API import TicketAPI

class TicketDisplay:
    
    def __init__(self, auth, page_length):
        self.subdomain = auth["subdomain"]
        self.ticket_API = TicketAPI(auth)
        self.current_page = 1
        self.page_length = page_length
        self.max_page = self.ticket_API.get_max_page(page_length)
        self.total_ticket = self.ticket_API.get_total_ticket()


    def display_unavailable_API(self):
        print("Error: the Zendesk ticket API is unavailable at the moment!")

    def display_menu(self):
        print("\n")
        print("--------------------------------------------")
        print("Select view options: \n")
        print("* Press 1 to view all tickets \n")
        print("* Press 2 to view a ticket \n")
        print("* Type '\quit\' to exit")
        print("--------------------------------------------")
    
    def display_ticket_page_menu(self):
        print("View all ticket options: \n")
        print("* Press n to go to next page \n")
        print("* Press p to go to previous page \n")
        print("* Press l to go to last page \n")
        print("* Press f to go to first page \n")
        print("* Enter a number to go to a specific page \n")
        print("* Press e to exit view all ticket mode and return to main menu\n")
        print("* Type '\quit\' to exit the application\n")

    def display_page(self):
        ticket_page = self.ticket_API.get_ticket_page(self.page_length, self.current_page)
        if ticket_page is None:
            self.display_no_ticket()
        else:
            for t in ticket_page:
                print(t)
                print("******************************************")


    def display_ticket_with_id(self, id):
        ticket_with_id = self.ticket_API.get_ticket_with_id(id)
        if ticket_with_id is None: 
            self.display_invalid_ticket_id(id)
        else: 
            print(ticket_with_id)

    def display_no_ticket(self):
        print("There is no ticket in the database \n")

    def display_ending(self):
        print("Thank you for using Zendesk Ticket Viewer Application by Phuong Vu!\nHave a nice day ^^")
    
    def display_welcome(self):
        print("Welcome to Zendesk Ticket Viewer Application!\nThis application will display tickets at subdomain {}.zendesk.com".format(self.subdomain))

    def display_invalid_ticket_id(self, id):
        print("Ticket with ID {} does not exist".format(id))

    def display_invalid_input(self):
        print("Invalid input! Please try again\n")

    def prompt_id(self):
        print("What ticket ID would you like to display? (Enter a number from 1-{})".format(self.total_ticket))

    def increment_current_page(self):
        self.current_page += 1
        if self.current_page > self.max_page:
            self.current_page = self.max_page

    def decrement_current_page(self):
        self.current_page -= 1 
        if self.current_page < 1:
            self.current_page = 1
    
    def process_page_number(self, page_number):
        if page_number > self.max_page:
            page_number = self.max_page
        
        if page_number < 1:
            page_number = 1

        return page_number


    '''
    The menu in the home page will have the following options:

    1: show all tickets (max 25 per page)
        - p: prev page
        - n: next page
        - l: last page
        - f: first page
        - a number: go to that page number
        - e: exit view all mode
        - quit: quit the program

    2: show individual ticket

    quit: quit the program

    else: invalid option
    '''
    def display_home_page(self):
        
        response = self.ticket_API.connect_to_server()
        if response is None:
            self.display_unavailable_API()
            return
        if response["tickets"] is None:
            self.display_no_ticket()
            return 

        self.display_welcome()
        
        while True:
            self.display_menu()
            option = input()

            if option == "1":
                self.display_ticket_page_menu()
                self.display_page()

                while True:
                    self.display_ticket_page_menu()
                    sub_option = input()
                    if sub_option == "n":
                        self.increment_current_page()
                        self.display_page()
                    elif sub_option == "p":
                        self.decrement_current_page()
                        self.display_page()
                    elif sub_option == "f":
                        self.current_page = 1
                        self.display_page()
                    elif sub_option == "l":
                        self.current_page = self.max_page
                        self.display_page()
                    elif sub_option.isnumeric():
                        self.current_page = self.process_page_number(int(sub_option))
                        self.display_page()
                    elif sub_option == "e":
                        break
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


