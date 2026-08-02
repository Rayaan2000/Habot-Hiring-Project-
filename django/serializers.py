from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student

        fields = "__all__"

    def validate_full_name(self, value):

        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Full name must contain at least 3 characters."
            )

        return value

    def validate_age(self, value):

        if value < 3 or value > 18:
            raise serializers.ValidationError(
                "Age must be between 3 and 18."
            )

        return value

    def validate_grade(self, value):

        if value < 1 or value > 12:
            raise serializers.ValidationError(
                "Grade must be between 1 and 12."
            )

        return value

    def validate_phone(self, value):

        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain digits only."
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must contain exactly 10 digits."
            )

        return value

    def validate_emergency_contact(self, value):

        if not value.isdigit():
            raise serializers.ValidationError(
                "Emergency contact must contain digits only."
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                "Emergency contact must contain exactly 10 digits."
            )

        return value

    def validate(self, data):

        if data["has_learning_difficulty"]:

            if not data.get("difficulty_type"):
                raise serializers.ValidationError(
                    {
                        "difficulty_type":
                        "This field is required."
                    }
                )

        if not data["consent"]:

            raise serializers.ValidationError(
                {
                    "consent":
                    "Parent consent is mandatory."
                }
            )

        return data