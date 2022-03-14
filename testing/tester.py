import socket, json
from typing import final
send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

testData = """{
    "DeviceID": "GSPro LM 1.1",
    "Units": "Yards",
    "ShotNumber": 13,
    "APIversion": "1",
    "BallData": {		
        "Speed": 147.5,
        "SpinAxis": -13.2,
        "TotalSpin": 3250.0,
        "BackSpin": 2500.0,
        "SideSpin": -800.0,
        "HLA": 2.3,
        "VLA": 14.3,
        "CarryDistance": 256.5
    },
    "ClubData": {							
        "Speed": 0.0,
        "AngleOfAttack": 0.0,
        "FaceToTarget": 0.0,
        "Lie": 0.0,
        "Loft": 0.0,
        "Path": 0.0,
        "SpeedAtImpact": 0.0,
        "VerticalFaceImpact": 0.0,
        "HorizontalFaceImpact": 0.0,
        "ClosureRate": 0.0
    },
    "ShotDataOptions": {
        "ContainsBallData": true,
        "ContainsClubData": false,
        "LaunchMonitorIsReady": true,
        "LaunchMonitorBallDetected": true,
        "IsHeartBeat": false
    }
}"""

send_socket.connect(('localhost', 921))
try:
    send_socket.sendall(testData.encode())
finally:
    send_socket.close()