from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from api_wyt.models import thoughts
from api_wyt.serializers import thoughts_serializer

# Create your views here.

class JSONResponse(HttpResponse):
	def __init__(self,data,**kwargs):
		content=JSONRenderer().render(data)
		kwargs["content_type"] = "application/json"
		super(JSONResponse,self).__init__(content,**kwargs)


@csrf_exempt
def thought_list(request):
	if request.method == "GET":
		thoughts_content = thoughts.objects.values('created','title','author')
		thoughts_serializer_data = thoughts_serializer(thoughts_content,many=True)
		return JSONResponse(thoughts_serializer_data.data)

	elif request.method == "POST":
		thoughts_content = JSONParser().parse(request)
		thoughts_serializer_data = thoughts_serializer(data = thoughts_content)
		if thoughts_serializer_data.is_valid():
			thoughts_serializer_data.save()
			return JSONResponse(thoughts_serializer_data.data,status = status.HTTP_201_CREATED)
		return JSONResponse(thoughts_serializer_data.errors,status = status.HTTP_400_BAD_REQUEST)

def thought_details(request,pk)	:
	try:
		thoughts_data = thoughts.objects.get(pk=pk)
	except:
		return HTTPResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		thoughts_serializer_data = thoughts_serializer(thoughts_data)
		return JSONResponse(thoughts_serializer_data.data)
						
	
