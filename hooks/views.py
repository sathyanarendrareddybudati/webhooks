from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework.permissions import IsAuthenticated
from .helper import send_admin_notification


class Webhook(APIView):

    # permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):

        data = json.loads(request.body)
        
        if data.get('event') == 'signup':
            user_data = data.get('user')

            send_admin_notification(user_data)
            
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'message': 'Invalid event'}, status=status.HTTP_400_BAD_REQUEST)
        

