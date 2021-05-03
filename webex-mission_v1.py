import json
import sys
import requests

#MISSION: FILL IN THE REQUESTED DETAILS
ACCESS_TOKEN = "" #Replace None with your access token between quotes.
BOT_ID = "Y2lzY29zcGFyazovL3VzL1BFT1BMRS81MDI5Mjg4YS00OWEzLTQ3MTctYjUyMy0yYWUzYzQyNjg1M2I"


#sets the header to be used for authentication and data format to be sent.
def getWebexTeamsHeader():
    accessToken_hdr = 'Bearer ' + ACCESS_TOKEN
    webex_teams_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
    return (webex_teams_header)


#check if the room already exists. If so return the space id
def findRoom(headers, room_name):
    roomId=None
    uri = 'https://api.ciscospark.com/v1/rooms'
    resp = requests.get(uri, headers=headers)
    resp = resp.json()
    print('resp', resp)
    for room in resp["items"]:
        if room["title"] == room_name:
            print()
            print("findRoom JSON: ", room)
            print("MISSION: findRoom: REPLACE None WITH CODE THAT PARSES JSON TO ASSIGN ROOM ID VALUE TO VARIABLE roomId")
            roomId=room['id']
            break
    return(roomId)

# checks if the room already exists and if true returns that room ID. If not creates a new room and returns the space id.
def createRoom(headers, room_name):
    roomId=findRoom(headers, room_name)
    if roomId==None:
        roomInfo = {"title":room_name}
        uri = 'https://api.ciscospark.com/v1/rooms'
        resp = requests.post(uri, json=roomInfo, headers=headers)
        var = resp.json()
        print()
        print("createRoom JSON: ", var)
        print("createRoom JSON: ", var['id'])
        print("MISSION: createRoom: REPLACE None WITH CODE THAT PARSES JSON TO ASSIGN ROOM ID VALUE TO VARIABLE roomId.")
        roomId=var['id']
    return(roomId)

# adds a new member to the space. Member e-mail is test@test.com
def addDxnetBot(headers, roomId):
    member = {"roomId":roomId,"personEmail": "dxnet-labs@webex.bot", "isModerator": False}
    uri = 'https://api.ciscospark.com/v1/memberships'
    resp = requests.post(uri, json=member, headers=headers)
    resp_json = resp.json()
    print("addMembers JSON: ", resp_json)
    return resp_json

# posts a message to the space
def sendMsgToPerson(headers, personId, message):
    message = {"toPersonId":personId,"text":message}
    uri = 'https://api.ciscospark.com/v1/messages'
    resp = requests.post(uri, json=message, headers=headers)
    print()
    print("postMsg JSON: ", resp.json())

# posts a message to the space
def sendMsgToRoom(headers, roomId, message):
        message = {"roomId": roomId, "text": message}
        uri = 'https://api.ciscospark.com/v1/messages'
        resp = requests.post(uri, json=message, headers=headers)
        resp_json = resp.json()
        print()
        print("sendMsgToRoom JSON: ", resp_json)
        return resp_json

def getMyOwnDetails(headers):
    uri = 'https://api.ciscospark.com/v1/people/me'
    resp = requests.get(uri, headers=headers)
    resp_json =  resp.json()
    print("getMyOwnDetails JSON: ", resp_json)
    return resp_json

def getPersonDetails(headers, personId):
    uri = 'https://api.ciscospark.com/v1/people/' + personId
    resp = requests.get(uri, headers=headers)
    resp_json =  resp.json()
    print("getMyOwnDetails JSON: ", resp_json)
    return resp_json

def getDirectMessages(headers, personId):
    uri = 'https://api.ciscospark.com/v1/messages/direct'
    queryParams = {'personId': personId}

    resp = requests.get(uri, headers=headers, params=queryParams)
    resp_json = resp.json()
    print("getMyOwnDetails JSON: ", resp_json)
    return resp_json

# MISSION: WRITE CODE TO RETRIEVE AND DISPLAY DETAILS ABOUT THE ROOM.
def getRoomInfo(headers, roomId):
    print("In function getRoomInfo")
    #MISSION: Replace None in the URI variable with the Webex Teams REST API call
    uri = None
    if uri == None:
        sys.exit("Please add the URI call to get room details. See the Webex Teams API Ref Guide")
    resp = requests.get(uri, headers=headers)
    print("Room Info: ",resp.text)
    resp = resp.json()
    print("MISSION: Add code to parse and display details about the space.")
    print(resp)

    # MISSION: WRITE CODE TO RETRIEVE AND DISPLAY DETAILS ABOUT THE ROOM.

def postUserInRoom(email):
    message = {"email": email}
    uri = 'https://dxnet-webex-api.herokuapp.com/postUserInRoom'
    resp = requests.post(uri, json=message)
    resp_json = resp.json()
    print()
    print("sendMsgToRoom JSON: ", resp_json)
    return resp_json


if __name__ == '__main__':
    # TODO: Pre requirements and set the ACCESS_TOKEN
    if ACCESS_TOKEN==None:
        sys.exit("Please check that variables ACCESS_TOKEN, have values assigned.")

    #TODO: Add user in room with your email - save   ROOM_ID

    #TODO: ASK USER OW TO WIN

    #TODO: GO TO YOUR WEBEX APP. IN A CONVERSATION WITH THE DXNET-LABS 'BOT' COPY THE WINNER CODE

    #TODO: GO TO DXNET Jornadas Informática and paste the winner code.

