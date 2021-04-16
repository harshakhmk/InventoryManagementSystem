from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve

from InventoryApp.models import Equipment,AccessRequest

class TestViews(TestCase):
    @classmethod
    def setUp(self):
        Equipment.objects.create(id=1,name="test_name")
        self.client = Client()
        self.equipmentlist=reverse('available-equipments')
        self.equipmentdetails=reverse('SendAccessRequest',args=[1])
        
        self.issueandreturn=reverse('IssuesAndReturn',args=[1])
        self.access_request_list_view=reverse('view-access-requests')
        self.list_issued_elements=reverse('issued-equipments')

    def test_equipmentlistview(self):
        resp = self.client.get(self.equipmentlist)
        self.assertEquals(resp.status_code, 200)

    def test_equipmentdetailview(self):
        resp_get=self.client.get(self.equipmentdetails)
        resp_post=self.client.post(self.equipmentdetails)
        self.assertEquals(resp_get.status_code, 200)
        
        self.assertEquals(resp_post.status_code, 200)
        
    def test_issue_and_return(self):
        resp_get=self.client.get(self.issueandreturn)
        resp_post=self.client.post(self.issueandreturn)
        self.assertEquals(resp_get.status_code,200)
        
        self.assertEquals(resp_post.status_code, 401)
        
    def test_AccessRequestListView(self):
         resp_get=self.client.get(self.access_request_list_view)
         self.assertEquals(resp_get.status_code,200)

    def test_List_issued_elements(self):
        resp_get=self.client.get(self.list_issued_elements)
        self.assertEquals(resp_get.status_code,200)
            


