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

class Wallet(models.Model):
    public_key = models.CharField(max_length=150)
    private_key = models.CharField(max_length=150)
    nonce = models.IntegerField()

class New_voters(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)


class Vote(models.Model):
    admin  = models.OneToOneField(User,on_delete=models.CASCADE)
    #payer = admin
    type_of_votes = models.CharField(max_length=100,choices = [("Commit","Commit"),("reveal","reveal"), ("Fully encrypted","Fully encrypted"),("fully open","fully open")])
    encryption_distribution_method = models.CharField(max_length=100,choices=[("voter_encryption_method","voter_encryption_method"), ("Burner anonymous wallet","Burner anonymous wallet"), ("Open wallet","Open wallet")])
    vote_encryption_method = models.CharField(max_length=100,choices=[("Homomorphism","Homomorphism"),("Public key hashing user(commit and reveal)","Public key hashing user(commit and reveal)"),("Direct reveal","Direct reveal")])
    list_of_voters = models.JSONField() ## An array of TZ1 arrays
    start_date = models.DateField() ## Timestamp
    duration = models.IntegerField()

class Candidates(models.Model):
    """Class that contains the Candidates for the specific election."""
    election_id = models.CharField(max_length=50, primary_key=True)
    vote = models.ForeignKey(Vote,on_delete=models.CASCADE,default=None)
    list_of_candidates = models.JSONField()

class Weight_arrays(models.Model):
    vote = models.ForeignKey(Vote,on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)
    weight = models.FloatField(default=1.0)