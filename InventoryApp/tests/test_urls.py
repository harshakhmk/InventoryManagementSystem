from django.urls import reverse,resolve
from django.test import SimpleTestCase
from InventoryApp.views import *

class TestUrls(SimpleTestCase):

    def test_available_equipments_url(self):
        url=reverse('available-equipments')
        assert resolve(url).view_name == 'available-equipments' 
    def test_send_access_requests_url(self):
        url=reverse('SendAccessRequest',args=[1])
        assert resolve(url).view_name == 'SendAccessRequest'     

    def test_issues_and_return_url(self):
        url=reverse('IssuesAndReturn',args=[1])
        assert resolve(url).view_name == 'IssuesAndReturn'     

    def test_issued_equipments(self):
        url=reverse('issued-equipments') 
        return resolve(url).view_name == 'issued-equipments'
    def test_view_access_requests(self):
        url=reverse('view-access-requests')  
        return resolve(url).view_name == 'view-access-requests'