from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_wyt.models import thoughts
from api_wyt.serializers import thoughts_serializer

# Create your views here.

@api_view(['GET','POST'])
def thought_list(request):
	if request.method == "GET":
		thoughts_content = thoughts.objects.values('created','title','author')
		thoughts_serializer_data = thoughts_serializer(thoughts_content,many=True)
		return JSONResponse(thoughts_serializer_data.data)

	elif request.method == "POST":
		thoughts_serializer_data = thoughts_serializer(data = request.data)
		if thoughts_serializer_data.is_valid():
			thoughts_serializer_data.save()
			return Response(thoughts_serializer_data.data,status = status.HTTP_201_CREATED)
		return Response(thoughts_serializer_data.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def thought_details(request,pk)	:
	try:
		thoughts_data = thoughts.objects.get(pk=pk)
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		thoughts_serializer_data = thoughts_serializer(thoughts_data)
		return Response(thoughts_serializer_data.data)
						
	
