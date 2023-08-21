import openai


class ResponseGenerator:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')

    def generate_response(self, email):
        # Generate a response based on the email content
        # ...
        response = 'This is a sample response.'

        # Generate a follow-up using GPT-3.5 Turbo
        follow_up = self.generate_follow_up(email)

        # Add the follow-up to the response
        response += '\n\nFollow-up: ' + follow_up

        return response

    def generate_follow_up(self, email):
        # Generate a follow-up using GPT-3.5 Turbo
        # ...
        follow_up = 'This is a sample follow-up.'

        return follow_up

    def generate_whisper_follow_up(self, email):
        # Generate a follow-up using OpenAI Whisper
        # ...
        whisper_follow_up = 'This is a sample Whisper follow-up.'

        return whisper_follow_up
