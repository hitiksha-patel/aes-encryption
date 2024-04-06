from django.urls import path
from . import views

urlpatterns = [
    path('agent-list/',views.AgentListView.as_view(),name = 'agent-list'),
    path('agent-list-encrypted/',views.AgentListEncrypted.as_view(),name = 'agent-list-encrypted'),
    path('decrypt-agent-list/', views.DecryptAgentList.as_view(), name='decrypt-agent-list')
]