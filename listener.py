from distutils.log import error
import socket, json, datetime

incomingMsgLog = "logs/incMsg.log"
outgoingMsgLog = "logs/outMsg.log"
incomingPort = 921
outgoingPort = 9090

# Map GC3 message to ProTee message
def translateMessage(inputMessage: json) -> json:
    outputMessage = {
    "protocol":"PROTEE",
    "info":{
        "device":"EXT",
        "units":inputMessage['Units']},
    "data":{
        "counter": inputMessage['ShotNumber'],
        "shotnumber":inputMessage['ShotNumber'],
        "clubspeed":inputMessage['ClubData']['Speed'],
        "clubface":inputMessage['ClubData']['FaceToTarget'],
        "clubpath":inputMessage['ClubData']['AngleOfAttack'],
        "sweetspot":"0",
        "ballspeed":inputMessage['BallData']['Speed'],
        "ballpath":inputMessage['BallData']['HLA'],
        "launchangle":inputMessage['BallData']['VLA'],
        "backspin":inputMessage['BallData']['BackSpin'],
        "sidespin":inputMessage['BallData']['SideSpin'],
        "drag":"1.0"}
}
    return outputMessage

rec_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

rec_socket.bind(('localhost', incomingPort))

rec_socket.listen(1)

while True:
    connection, client_address = rec_socket.accept()
    inputLog = open(incomingMsgLog, "a")
    outputLog = open(outgoingMsgLog,"a")
    try:
        data = connection.recv(1000)
        inputMessage = json.loads(data.decode())
        timestamp = "Message received at " + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + ":\n"
        
        # log message
        inputLog.write(timestamp)
        json.dump(inputMessage, inputLog, indent=4)
        inputLog.write("\n")
        
        outputMessage = translateMessage(inputMessage)
        
        # log output
        outputLog.write(timestamp)
        json.dump(outputMessage, outputLog, indent=4)
        outputLog.write("\n")

        send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            send_socket.connect(('localhost', outgoingPort))
            send_socket.sendall(json.dumps(outputMessage).encode())
        except OSError as e:
            outputLog.write("\n")
            outputLog.write(str(e))
            outputLog.write("\n")
        except:
            outputLog.write("\n")
            outputLog.write("An error occurred.")
            outputLog.write("\n")
        finally:
            send_socket.close()
    except OSError as e:
        inputLog.write("\n")
        inputLog.write(str(e))
        inputLog.write("\n")
    finally:
        connection.close()
        inputLog.close()
        outputLog.close()
