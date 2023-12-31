from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.profiles.models import Profile

from .models import Rating

User = get_user_model()


# create agent review
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_agent_review(request, profile_id):
    agent_profile = get_object_or_404(Profile, id=profile_id, is_agent=True)
    data = request.data
    profile_user = User.objects.get(pkid=agent_profile.user.pkid)  # type: ignore

    if profile_user.email == request.user.email:  # type: ignore
        formatted_response = {"message": "You can't rate yourself"}
        return Response(formatted_response, status=status.HTTP_403_FORBIDDEN)

    alreadyExists = agent_profile.agent_review.filter(  # type: ignore
        agent__pkid=profile_user.pkid  # type: ignore
    ).exists()

    if alreadyExists:
        formatted_response = {"detail": "Profile already reviewed"}
        return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)

    elif data["rating"] == 0:
        formatted_response = {"detail": "Please select a rating"}
        return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)

    else:
        Rating.objects.create(
            rate_user=request.user,
            agent=agent_profile,
            rating=data["rating"],
            comment=data["comment"],
        )
        reviews = agent_profile.agent_review.all()  # type: ignore
        agent_profile.num_reviews = len(reviews)

        total = 0
        for i in reviews:
            total += i.rating

        agent_profile.rating = round(total / len(reviews), 2)  # type: ignore
        agent_profile.save()
        return Response("Review Added")
