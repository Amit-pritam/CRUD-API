from django.shortcuts import render
from rest_framework import viewsets
from api.models import CompanyModel,EmployeeModel
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response





class ComapnyViewSet(viewsets.ModelViewSet):
	queryset = CompanyModel.objects.all()
	serializer_class = CompanySerializer

	@action(detail=True,methods=['get'])
	def employees(self,request,pk=None):
		try:
			company = CompanyModel.objects.get(pk=pk)
			emps = EmployeeModel.objects.filter(company=company)
			emps_serializers = EmployeeSerializer(emps,many = True,context={'request':request})
			return Response(emps_serializers.data)
		except Exception as  e:
			print(e)
			return Response({'message':'Company might not exist!! Error.'})

class EmployeeViewSet(viewsets.ModelViewSet):
	queryset = EmployeeModel.objects.all()
	serializer_class = EmployeeSerializer	


