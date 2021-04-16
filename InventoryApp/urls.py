from django.urls import path,include
from .views import *
from django.conf.urls import   url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    
    path('employee/available-equipments/',EquipmentListView.as_view(),name='available-equipments'),
    path('employee/send-access-requests/<int:id>',EquipmentDetailView.as_view(),name="SendAccessRequest"),
    path('employee/issues-and-return/<int:id>',IssueandReturn.as_view(),name="IssuesAndReturn"),
 #  path('employee/equipment-details/<int:id>',EquipmentDetailView.as_view(),name='EquipmentDetails'),
    path('manager/available-equipments/',EquipmentListView.as_view(),name='available-equipments'),
    path('manager/issued-equipments',List_issued_elements.as_view(),name='issued-equipments'),
    path('manager/view-access-requests',AccessRequestListView.as_view(),name='view-access-requests'),

]
urlpatterns = format_suffix_patterns(urlpatterns)
