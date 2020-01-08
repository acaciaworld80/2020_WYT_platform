from rest_framework import serializers
from api_wyt.models import thoughts

class thoughts_serializer(serializers.ModelSerializer):
	class Meta:
		model = thoughts
		fields = ('id','created','title','author','description')
		
