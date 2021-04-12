from rest_framework import serializers
from blog.models import post

class PostFormSeralisers(serializers.ModelSerializer):
	class Meta:
		model=post
		fields="id","user","title","content"

class PostCreateSeralisers(serializers.ModelSerializer):
	class Meta:
		model=post
		fields="title","content"



class PostUpdateSeralisers(serializers.ModelSerializer):
	class Meta:
		model=post
		fields="title","content"




class PostDetailSeralisers(serializers.ModelSerializer):
	class Meta:
		model=post
		fields="id","user", "image","title","content","update"