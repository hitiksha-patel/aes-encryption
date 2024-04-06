from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AgentSerializer
from .models import Agent
from .renderers import CustomRenderer

import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from .renderers import AES_SECRET_KEY, AES_IV
import json

class AgentListView(APIView):
    def get(self, request):
        agents = Agent.objects.all()
        if agents:
            try:
                serializers = AgentSerializer(agents, many=True)
                data = serializers.data
            except Exception as ex:
                print(ex,"error")
                data = None
        data = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'data': data
        }
        return Response(data, status = status.HTTP_200_OK)

class AgentListEncrypted(APIView):
    renderer_classes = [CustomRenderer]

    def get(self, request):
        agents = Agent.objects.all()

        if agents:
            serializer = AgentSerializer(agents, many=True)
            data = serializer.data

        data = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'data': data
        }
        return Response(data, status = status.HTTP_200_OK)

class DecryptAgentList(APIView):
    def post(self, request, *args, **kwargs):
        # Decode the request data from base64
        encrypted_data = request.data['ciphertext']
        enc = base64.b64decode(encrypted_data)
        cipher = AES.new(AES_SECRET_KEY, AES.MODE_CBC, AES_IV)
        try:
            decrypted_data = unpad(cipher.decrypt(enc),16)
            decrypted_data = json.loads(decrypted_data)
            data = {
                "data" : decrypted_data
            }
            return Response(data)
        except Exception as e:
            return Response({"data": f"An error- {e}"})