from rest_framework import serializers
from voting.models import Voters

class VotersSerializer(serializers.Serializer):
    """Serializer for the voters model."""
    class Meta:
        model = Voters
        fields = ["one_time_wallet", "public_key", "private_key", "nonce"]

