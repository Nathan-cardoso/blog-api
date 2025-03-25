from .serializers import CustomUserRegistration
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from ..models import CustomUser


class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRegistration
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'User created successfully',
                 'data': serializer.data},
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            {'message': 'Error',
             'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
        
