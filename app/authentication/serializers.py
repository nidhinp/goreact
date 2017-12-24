from rest_framework import serializers

from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Member
        fields = ('id', 'email', 'phone', 'password')

    def create(self, validated_data):
        member = Member.objects.create(**validated_data)
        password = validated_data.get('password', None)
        if password:
            member.set_password(password)
            member.save()
        return member

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
            instance.save()
        return instance
