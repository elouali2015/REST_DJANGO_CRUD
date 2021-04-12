from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,RetrieveUpdateAPIView
from blog.models import post
from .seralizers import PostFormSeralisers,PostCreateSeralisers,PostUpdateSeralisers,PostDetailSeralisers
from django.shortcuts import get_object_or_404
#from rest_framework.permissons import AllowAny, IsAuthenticated,IsAdminuser;IsAuthenticatedOrReadOnly

class PostListAPIView(ListAPIView):
	queryset=post.objects.all()
	serializer_class=PostFormSeralisers

class PostCreateAPIView(CreateAPIView):
	queryset=post.objects.all()
	serializer_class=PostCreateSeralisers
	def perform_create(self,seralizer):
		seralizer.save(user=self.request.user)


class DetailAPIView(RetrieveAPIView):
	queryset=post.objects.all()
	serializer_class=PostDetailSeralisers
	def delete(self,request,pk):
		queryset=get_object_or_404(post,pk=pk)
		queryset.delete()

class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset=post.objects.all()
	serializer_class=PostDetailSeralisers

class PostDeleteAPIView(DestroyAPIView):
	queryset=post.objects.all()
	serializer_class=PostFormSeralisers