
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)
    #     # Add custom claims to the token
    #     token['user_type'] = "test"
    #     print(type(token), user.wallet, user.user_type)
    #     return token
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["user_type"] = self.user.user_type
        data["wallet"] = self.user.wallet
        return data