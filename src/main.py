from ticket_display import TicketDisplay
from ticket_API import TicketAPI


def main():
    auth = {"subdomain": "zccpvu3", "email": "pvu140100@gmail.com", "password": "Thuphuong1401*"}
    ticket_display = TicketDisplay(auth)
    ticket_display.home_page()


if __name__ == '__main__':
    main()


