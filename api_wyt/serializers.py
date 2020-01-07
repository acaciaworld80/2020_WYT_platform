from rest_framework import serializers
from api_wyt.models import thoughts

class thoughts_serializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	title = serializers.CharField(max_length=200)
	created = serializers.DateTimeField()
	author = serializers.CharField(max_length=200)
	description = serializers.CharField(max_length=500,required=False)

	def create(self,validated_data):
		return thoughts.objects.create(**validated_data)

	def update(self,instance,validated_data):
		instance.title = validated_data.get('title',instance.title)
		instance.created = validated_data.get('created',instance.created)
		instance.author = validated_data.get('author',instance.author)
		instance.description = validated_dat.get('description',instance.description)
		instance.save()
		return instance
