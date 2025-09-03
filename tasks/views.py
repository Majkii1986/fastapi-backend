from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  # 👈 toto je dôležité, inak spadne na basename error
    serializer_class = TaskSerializer    

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user_id': user.id,
            'username': user.username,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        })

    return Response(serializer.errors, status=400)
