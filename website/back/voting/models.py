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

class Voters(models.Model):
    user = models.OneToOneField(User)
    wallet = models.ForeignKey(Wallet)


class Vote(models.Model):
    name = name
    payer = models.OneToOneField(User)
    type_of_votes = models.Charfield(option = "Commit" and reveal, Fully encrypted, or fully open
    encryption_distribution_method = voter_encryption_method ## Burner anonymous wallet/Mixnets wallet/Open wallet
    vote_encryption_method = encryption_method ## Homomorphism/Public key hashing user(commit and reveal)/Direct reveal
    list_of_voters = list_of_voters ## An array of TZ1 arrays
    start_date = model.Datefield() ## Timestamp
    end_date = self.start_date + self.vote_duration ## Timestamp + Timedelta = Timestamp
    voter_rules = weight_arrays ## An array of TZ1:Weight => With weight being by default 1
    notification_per_user = self.notification_per_user ## Integer
    notification_delay = self.vote_duration.self.notification_per_user ## Default = Open duration /Notification per user