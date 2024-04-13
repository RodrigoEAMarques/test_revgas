from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Banco
from .serializers import BancoSeralizers
from django.shortcuts import get_object_or_404, render


def page(request):
    return render(request, 'index.html')


class BancoList(APIView):
    def get(self, request):
        bancos = Banco.objects.all()
        serializer = BancoSeralizers(bancos, many=True)
        return Response(serializer.data)


class ConsultaBanco(APIView):
    def get(self, request, codigo):
        banco = get_object_or_404(Banco, id_compensacao=codigo)
        serializer = BancoSeralizers(banco)
        return Response(serializer.data)