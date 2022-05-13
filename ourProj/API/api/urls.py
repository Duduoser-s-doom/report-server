from django.urls import path

from API.api.views import ReportView

urlpatterns = [path('reports', ReportView.as_view())]
