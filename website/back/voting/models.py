from django.db import models
from back.settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL


# Create your models here.
class Voters(models.Model):
    """Class that contains the One Time Wallet with the private/public key for encryption/decryption."""
    
    one_time_wallet = models.CharField(max_length=150, primary_key=True)
    public_key = models.CharField(max_length=150)
    private_key = models.CharField(max_length=150)
    nonce = models.IntegerField()

class Candidates(models.Model):
    """Class that contains the Candidates for the specific election."""

    election_id = models.CharField(max_length=50, primary_key=True)
    list_of_candidates = models.JSONField()

class Campaign(models.Model):
    """Class that contains all the intel about an election."""

    voting_type = models.CharField(max_length=100)
    voting_method = models.CharField(max_length=150)
    voting_delay = models.CharField(max_length=150)
