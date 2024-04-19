from rest_framework import serializers
from .models import User
from curium_api.organization.models import Organization

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    org = serializers.CharField()

    class Meta:
        model = User
        fields = ["fname", "lname", "email_id", "password", "password2", "org", "role"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

        def save(self):
            org_name = self.validated_data["org"]
            try:
                org = Organization.objects.get(org_name=org_name)
            except Organization.DoesNotExist:
                org = None

            if org is None:
                raise serializers.ValidationError({"org": "Organization does not exist."})

            user = User(
                fname=self.validated_data["fname"],
                lname=self.validated_data["lname"],
                email_id=self.validated_data["email_id"],
                username=self.validated_data["email_id"],
                org=org,
                role=self.validated_data["role"],
            )
            password = self.validated_data["password"]
            password2 = self.validated_data["password2"]

            if password != password2:
                raise serializers.ValidationError({"password": "Passwords must match."})
            user.set_password(password)
            user.save()
            return user



class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("email_id", "fname", "lname")
