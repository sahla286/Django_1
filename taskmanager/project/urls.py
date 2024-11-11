from django.urls import path
from .views import *


urlpatterns=[
    path('pdash',ProjectDashboardView.as_view(),name='pdash'),
    path('padd',ProjectAddView.as_view(),name='padd'),
    path('pdelete/<int:id>',DeleteProjectView.as_view(),name='pdelete'),
    path('pedit/<int:id>',EditProjectView.as_view(),name='pedit')
] 