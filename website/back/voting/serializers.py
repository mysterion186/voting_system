from rest_framework import serializers
from voting.models import Voters, Candidates

class VotersSerializer(serializers.ModelSerializer):
    """Serializer for the voters model."""
    class Meta:
        model = Voters
        fields = ["one_time_wallet", "public_key", "private_key", "nonce"]


class CandidateSerializer(serializers.ModelSerializer):
    """Serializer for the candidates model."""
    class Meta:
        model = Candidates
        fields = ['election_id', 'list_of_candidates']
