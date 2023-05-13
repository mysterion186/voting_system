from django.db import models

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