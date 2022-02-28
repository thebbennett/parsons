import logging
from parsons.utilities import check_env

logger = logging.getLogger(__name__)


class YourConnectorName(object):
    """
    Instantiate Slack class.

       `Args:`
    """

    def __init__(self, api_key=None):
        self.api_key = check_env.check('YOURCONNECTORNAME_API_KEY', api_key)
