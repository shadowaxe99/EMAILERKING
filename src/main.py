import os
import time
from src.account_manager import AccountManager
from src.draft_manager import DraftManager
from src.email_manager import EmailManager
from src.response_generator import ResponseGenerator
from datetime import datetime, timedelta


class Main:
    def __init__(self):
        self.account_manager = AccountManager()
        self.draft_manager = DraftManager()
        self.email_manager = EmailManager()
        self.response_generator = ResponseGenerator()

    def run(self):
        # Main loop
        while True:
            # Check for new emails
            new_emails = self.email_manager.check_for_new_emails()

            # Process each email
            for email in new_emails:
                # Generate a response
                response = self.response_generator.generate_response(email)

                # Create a new draft
                self.draft_manager.create_draft(response)

                # Speak the response
                self.speak_response(response)

            # Wait for a while before checking for new emails again
            time.sleep(60)

    def speak_response(self, response):
        # Use text-to-speech library to speak the response
        # ...
        print('Speaking response:', response)


if __name__ == '__main__':
    main = Main()
    main.run()
