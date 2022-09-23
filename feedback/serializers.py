from rest_framework import serializers
from feedback.models import Feedback
from django.contrib.auth.models import User, AnonymousUser
from rest_framework import exceptions


class FeedbackSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['created_by', 'good', 'bad', 'need_improvement', 'created_for']


class FeedbackSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['is_anonymous', 'good', 'bad', 'need_improvement', 'created_for']

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request is not None:
            if validated_data['is_anonymous']:
                instance = self.Meta.model.objects.create(**validated_data)
                instance.save()
                return instance
            if not validated_data['is_anonymous'] and isinstance(request.user, AnonymousUser):
                raise exceptions.PermissionDenied('Please Login if you are not posting as Anonymosly or select '
                                                  'Anonymous')
            elif not validated_data['is_anonymous'] and not isinstance(request.user, AnonymousUser):
                instance = self.Meta.model.objects.create(created_by=request.user, **validated_data)
                instance.save()
                return instance
        else:
            raise exceptions.bad_request('Something Went Wrong Please Try again')
