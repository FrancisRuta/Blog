import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer


def login(request):
    return render(request, "login.html")


@api_view(["GET"])
def home(request):
    # Lets pull some random blog posts from an API for viewing only
    api_url = "https://jsonfakery.com/blogs/random/3"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        external_blogs = response.json()

        serializer = PostSerializer(data=external_blogs, many=True)

        if serializer.is_valid():
            return render(request, "home.html", {"posts": serializer.data})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)


@api_view(["POST"])
def posts(request):
    return render(request, "posts.html")
