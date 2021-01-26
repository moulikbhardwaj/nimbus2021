from django.urls import path
from members.views import CoreTeamView, SponsorView

urlpatterns = [
    path('coreTeam/', CoreTeamView.as_view()),
    path('sponsors/', SponsorView.as_view()),
]
