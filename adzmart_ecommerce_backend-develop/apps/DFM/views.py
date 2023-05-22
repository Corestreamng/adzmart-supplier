from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import MediaAdvisory, MediaBrief, Support, MEDIA_TYPE
from .serializers import (
    MediaAdvisorySerializer, 
    MediaBriefSerializer, 
    SupportSerializer,
    MediaBriefListingsSerializer,
    MediaAdvisoryListingsSerializer,
    SupportListingsSerializer
)

class MediaBriefRequests(APIView):
    """
    Create, Retreive, Update and Delete a media brief listing for a done-for-me customer.
    """

    def get(self, request, format=None):
        # TODO ==> TOLA (Filter the object based on the customer)
        listings = MediaBrief.objects.all()
        serializer = MediaBriefListingsSerializer(listings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        req_data = request.data   
        serializer = MediaBriefSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        listing = get_object_or_404(MediaBrief, pk=pk)
        serializer = MediaBriefSerializer(listing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        listing = get_object_or_404(MediaBrief, pk=pk)
        listing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MediaAdvisoryRequests(APIView):
    """
    Create, Retreive, Update and Delete a media advisory listing for a done-for-me customer.
    """
      
    def get(self, request, format=None):
        # TODO ==> TOLA (Filter the object based on the customer)
        listings = MediaAdvisory.objects.all()
        serializer = MediaAdvisoryListingsSerializer(listings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        req_data = request.data
        serializer = MediaAdvisorySerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def put(self, request, pk, format=None):
        listing = get_object_or_404(MediaAdvisory, pk=pk)
        serializer = MediaAdvisorySerializer(listing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        listing = get_object_or_404(MediaAdvisory, pk=pk)
        listing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MediaSupportRequests(APIView):
    """
    Create, Retreive, Update and Delete a support listing for a done-for-me customer.
    """

    def get(self, request, format=None):
        # TODO ==> TOLA (Filter the object based on the customer)
        listings = Support.objects.all()
        serializer = SupportListingsSerializer(listings, many=True)
        return Response (
                serializer.data, status=status.HTTP_200_OK
            ) 

    def post(self, request, format=None):
        req_data = request.data
        serializer = SupportSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response (
                serializer.data, status=status.HTTP_201_CREATED
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        listing = get_object_or_404(Support, pk=pk)
        serializer = SupportSerializer(listing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        listing = get_object_or_404(Support, pk=pk)
        listing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
