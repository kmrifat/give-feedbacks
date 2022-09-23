from django.shortcuts import render
from django.contrib.auth.models import User
from feedback.models import Feedback
from rest_framework import generics, status
from feedback.serializers import FeedbackSerializerGet, FeedbackSerializerPost


class FeedbackGetList(generics.ListAPIView):
    serializer_class = FeedbackSerializerGet
    queryset = Feedback.objects.all()


class FeedbackCreate(generics.CreateAPIView):
    serializer_class = FeedbackSerializerPost
    queryset = Feedback.objects.all()
