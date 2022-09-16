from django.urls import path
from . import views

urlpatterns = [
    path('api/flomo', views.MenstrualList.as_view(), name='menstrual_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/flomo/<int:pk>', views.MenstrualDetail.as_view(), name='menstrual_detail'), # api/contacts will be routed to the ContactDetail view for handling
]