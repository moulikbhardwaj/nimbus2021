from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import uuid
import datetime
from .models import VCQueue, VCLog, Report
from users.models import User
from .serializers import ReportSerializer
from .RtcTokenBuilder import RtcTokenBuilder, Role_Publisher


# Create your views here.

# https://numbus2021-omegle-token-gen.herokuapp.com/access_token?channel=test&uid=222

@api_view()
def joinVCView(request, uid):
    """
    Join Video call
    """
    # Uncomment the following code to check if the user exists
    # if User.objects.filter(firebase=uid).exists() == False:
    #     return Response({"Message": "Invalid User ID"}, status.HTTP_400_BAD_REQUEST)
    users = User.objects.filter(firebase=uid)
    if len(users) > 0 and users[0].omegleAllowed == False:
        return Response({"Message": "Not allowed"}, status.HTTP_403_FORBIDDEN)
    entry = VCQueue.objects.filter(uid=uid)
    if len(entry) == 0:
        # If the user doesn't exist'
        VCQueue.objects.create(uid=uid)
    elif entry[0].channel != '':
        # If the user has already been assigned a room
        response = serialize(entry[0])
        entry[0].delete()
        return Response(response)
    else:
        # If the user is already in the queue
        queue = VCQueue.objects.exclude(uid=uid)
        # Removing old entries from the queue
        i = 0
        while i < len(queue):
            if isExpired(queue[i]):
                queue[i].delete()
            else:
                break
            i += 1
        if i == len(queue):
            # If the queue is empty
            entry[0].save()
        else:
            # Assigning channel and tokens to current user and earliest user in the queue
            user1 = entry[0]
            user2 = queue[i]
            channel = getChannel()
            token1, token2 = getTokens(user1.uid, user2.uid, channel)
            user1.channel = channel
            user2.channel = channel
            user1.token = token1
            user2.token = token2
            user1.uid2 = user2.uid
            user2.uid2 = user1.uid
            VCLog.objects.create(
                channel=channel,
                uid1 = user1.uid,
                uid2 = user2.uid
            )
            user2.save()
            response = serialize(user1)
            user1.delete()
            return Response(response)
    return Response({"Message": "Waiting for someone else to join"})

@api_view()
def logView(request, channel):
    queryset = VCLog.objects.filter(channel=channel)
    if len(queryset) > 0:
        queryset[0].save()
        return Response({})
    return Response({"Message:" "Invalid channel"}, status.HTTP_400_BAD_REQUEST)

@api_view()
def reportView(request, uid):
    queryset = User.objects.filter(firebase=uid)
    if len(queryset) > 0:
        queryset[0].omegleReports += 1
        queryset[0].save()
        return Response({"Message": "Reported"})
    return Response({"Message:" "Invalid uid"}, status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def reportNewView(request):
    data = request.data
    serializer = ReportSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.filter(firebase=data['reported'])
        if len(user) > 0:
            user[0].omegleReports += 1
            user[0].save()
        return Response({"Message": "Reported"})
    return Response({"Message:" "Invalid data"}, status.HTTP_400_BAD_REQUEST)

def getChannel():
    return uuid.uuid4().hex


def getTokens(uid1, uid2, channel):
    APP_ID = "abe9aa77ff8946f8b653b7e7ad96348c"
    APP_CERTIFICATE = "d1d939a63bb744ac888ef0bdd278fcba"

    token1 = RtcTokenBuilder.buildTokenWithAccount(
        APP_ID,
        APP_CERTIFICATE,
        channel,
        uid1,
        Role_Publisher,
        0
    )
    token2 = RtcTokenBuilder.buildTokenWithAccount(
        APP_ID,
        APP_CERTIFICATE,
        channel,
        uid2,
        Role_Publisher,
        0
    )
    return token1, token2


def isExpired(entry: VCQueue):
    EXPIRE_TIME = 3
    return (datetime.datetime.now().timestamp() - entry.lastPingTime.timestamp() > EXPIRE_TIME)


def serialize(queueObj: VCQueue):
    return {
        'uid': queueObj.uid,
        'uid2': queueObj.uid2,
        'channel': queueObj.channel,
        'token': queueObj.token
    }
