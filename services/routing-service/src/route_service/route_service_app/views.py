from rest_framework.decorators import api_view
from rest_framework.response import Response
from .service import get_route

@api_view(['GET'])
def route(request):
    start = request.GET.get('start')
    end = request.GET.get('end')

    if not start or not end:
        return Response({'error': 'Start and end points are required.'}, status=400)

    map_html = get_route(start, end)

    return Response({'map': map_html})
