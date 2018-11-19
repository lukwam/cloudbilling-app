"""Module with helper classes and functions."""

from apiclient.discovery import build
# from google.auth import default

class Google(object):
    """Google class."""

    def __init__(self, scopes=None, verbose=False):
        """Initialize an object instance."""
        # self.credentials, self.project_id = default(scopes)

    def get_billing_accounts(self):
        """Return a list of Google Billing Accounts."""
        billing = build('cloudbilling', 'v1', credentials=self.credentials)
        billingAccounts = billing.billingAccounts()
        request = billingAccounts.list()
        return self.get_list_items(billingAccounts, request, 'billingAccounts')

    def get_list_items(self, method, request, name):
        """Return the items from a Google list/list_next cycle."""
        items = []
        while request is not None:
            response = request.execute()
            items += response.get(name, [])
            request = method.list_next(request, response)
        return items
