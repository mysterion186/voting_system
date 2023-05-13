from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from voting.serializers import CandidateSerializer, VotersSerializer
from voting.models import Candidates, Voters


@api_view(["POST"])
def add_candidates(request): 
    """Add a candidate for the election.
    
    Args : 
    request (Http Request) : contains the user's request.

    Returns : 
    Http Response : the reponse according to the result for processing the data.
    """
    serializer = CandidateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def list_candidates(request):
    """Get the candidates for all the elections.
    
    Args : 
    request (Http Request) : contains the user's request.
    
    Returns :
    Http Response : the data requested by the user.
    """
    candidates = Candidates.objects.all()
    serializer = CandidateSerializer(candidates, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_election_candidate(request, election_id):
    """Get the candidate for a specific election.

    Args : 
    request (Http Request) : contains the user's request.
    election_id (str) : the id for an election.

    Returns : 
    Http Response : the data requested by the user.
    """
    candidates = Candidates.objects.filter(election_id=election_id)
    serializer = CandidateSerializer(candidates, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_all_voters(request):
    """Get all the voters.
    
    Args :
    request (Http Request) : contains user's request.

    Returns :
    Http Response : all the intel about all voters.
    """
    voters = Voters.objects.all()
    serializer = VotersSerializer(voters, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def add_voter(request):
    """Add an entry for the Voters.
    
    Args :
    request (Http Request) : contains user's request.

    Returns : 
    Http Response : the reponse according to the result for processing the data.
    """
    serializer = VotersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_one_voter(request, voter_wallet):
    """Get all details on a voter with the associated wallet.
    
    Args : 
    request (Http Request) : contains user's request.

    Returns : 
    Http Response : the data requested by the user.
    """
    voter = Voters.objects.filter(one_time_wallet=voter_wallet)
    serializer=VotersSerializer(voter, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)