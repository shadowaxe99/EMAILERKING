import logging

logger = logging.getLogger(__name__)


class ErrorHandler:
    def handle_error(self, error):
        # Log the error
        logger.error(str(error))
        # Add your error handling logic here
        pass