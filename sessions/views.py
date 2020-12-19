from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from sessions.models import Session
from sessions.serializers import SessionSerializer


@csrf_exempt
def sessions_list(request):
    """
    List all sessions, or create a new session
    """
    if request.method == 'GET':
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SessionSerializer(data=data)

        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def session_detail(request, pk):
    """
    Retrieve, update or delete a session.
    """
    try:
        session = Session.objects.get(pk=pk)
    except Session.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SessionSerializer(session)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SessionSerializer(session, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        session.delete()
        return HttpResponse(status=204)
