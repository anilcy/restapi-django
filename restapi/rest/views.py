from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import taskManager
from rest.api.serializer import restSerializer

class taskManagerView(APIView):
    def get(self, request):
        tasks = taskManager.objects.all()
        serializer = restSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

