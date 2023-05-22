import threading

class EmailThread(threading.Thread):
    """
    Email thread class to send email in background.
    
    """

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=False)
