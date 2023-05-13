from django.urls import path
from voting import views

urlpatterns = [
    path("candidates", views.add_candidates, name="add-candidates"),
    path("get-candidates", views.list_candidates, name="list-candidates"),
    path("get-candidate/<str:election_id>", views.get_election_candidate, name="get-candidate"),
    path("get-voters", views.get_all_voters, name="get-all-voters"),
    path("voters", views.add_voter, name="add-voter"),
    path("get-voter/<str:voter_wallet>", views.get_one_voter, name="get-one-voter"),
]