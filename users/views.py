from .serializers import FormSerializer, CommentSerializer, UniversitySerializer
from rest_framework import generics
from .models import Form, Comment, University
from rest_framework.permissions import IsAuthenticated


class FormsListView(generics.ListAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [IsAuthenticated]


class CreateForm(generics.CreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class UniListView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class CreateUni(generics.CreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CreateComment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)

