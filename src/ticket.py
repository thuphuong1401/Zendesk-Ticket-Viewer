'''
Class representing a ticket with fields id, assignee_id, submitter_id, subject, description, url, 
status, created_at
'''

class Ticket:

    def __init__(self, ticket_json):
        self.id = ticket_json['id']
        self.assignee_id = ticket_json['assignee_id']
        self.submitter_id = ticket_json['submitter_id']
        self.subject = ticket_json['subject']
        self.description = ticket_json['description']
        self.url = ticket_json['url']
        self.status = ticket_json['status']
        self.created_at = ticket_json['created_at']

    def __str__(self):
        str_id = "Ticket ID: {}".format(self.id)
        str_assignee_id = "Assigned to: {}".format(self.assignee_id)
        str_submitter_id = "Submitted from: {}".format(self.submitter_id)
        str_subject = "Subject: {}".format(self.subject)
        str_description = "Description: {}".format(self.description)
        str_url = "URL: {}".format(self.url)
        str_status = "Status: {}".format(self.status)
        str_created_at = "Created at: {}".format(self.created_at)
        return "{} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n".format(str_id, str_assignee_id, str_submitter_id, str_subject, str_description, str_url, str_status, str_created_at)
        