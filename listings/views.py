from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def listings_list(request):
    """
    List all travel listings (placeholder endpoint for Swagger testing)
    """
    return Response({
        'message': 'Listings endpoint is working!',
        'data': []
    }, status=status.HTTP_200_OK)