# Zendesk-Ticket-Viewer
Author: Phuong Vu
Email: pvu3@u.rochester.edu

This is my solution to the Zendesk's Software Engineering Intern Coding challenge. This application is a CLI one.

# Features Implemented 
- Connect to the Zendesk API
- Request all the tickets for your account
- Display them in a list
- Display individual ticket details
- Page through tickets when more than 25 are returned

# Dependencies
python 3.8.5
requests 2.22.0

# Installation and Running Instruction
1. Clone this repository into your local machine
`git clone https://github.com/thuphuong1401/Zendesk-Ticket-Viewer` 

2. Change directory to where `main.py` is located
`cd Zendesk-Ticket-Viewer/src`

3. Run the CLI application. There will be instructions displayed when the application is running.
`python main.py`

# Application flow
At the beginning, the application will display a menu that prompts you to enter 1 to view all tickets (at most 25 per page), 2 to view a single ticket, and "quit" to exit the application. 
- Press 1: the first page of tickets will be displayed, which consists of the first 25 tickets. You will also see a sub-menu which provides option to navigate the list of all tickets: 
    + Press 'n' to go to next page 
    + Press 'p' to go to previous page
    + Press 'l' to go to last page
    + Press 'f' to go to first page
    + Enter a number to go to a specific page (if the number is greater than the max page, the application will display the last page, and if the number is smaller than 1, the application will display the first page)
    + Press 'e' to quit view all tickets mode
    + Enter "quit" to exit the application.
- Press 2: you will be prompted to enter a ticket ID. If the ID corresponds to a ticket present in the database, that ticket will be displayed. Else the application will indicates that ticket with such ID does not exist.
- Enter "quit": exit the application 

# Testing Instruction
1. Change directory to Zendesk-Ticket-Viewer/test, and run the following command
`python test.py`

# Files included:
- In src folder:
    + main.py: entry point of the CLI application
    + ticket.py: ticket class which represents a ticket with different fields
    + ticket_API.py: class that manages connecting to the Zendesk API and get ticket or ticket page
    + ticket_display.py: class that manages displaying information to the user
- In test folder:
    + ticket_test.py: class that test various functions in the source code
    + tickets.json: json for sample tickets, uploaded to Zendesk account

# Examples
The folder example_images contains some example images of running this CLI application


