import json


class Trip:
    liste = []
    startlat = -33.89024429693447
    currlat = startlat
    startlong = 151.19991587790943
    currlong = startlong
    startts = 1692085445.01
    currts = startts

    def dt(self):
        self.currts += 0.01

    def SoftStart(self):
        self.liste.append(
            {
                "data": {
                    "currState": "STATE_WAITING_FOR_TRIP_START",
                    "transition": "T_EXITED_GEOFENCE",
                    "ts": self.currts,
                },
                "metadata": {
                    "platform": "ios",
                    "write_ts": self.currts,
                    "time_zone": "UTC",
                    "key": "statemachine/transition",
                    "read_ts": 0,
                    "type": "message",
                },
            }
        )
        self.dt()
        self.liste.append(
            {
                "data": {
                    "currState": "STATE_WAITING_FOR_TRIP_START",
                    "transition": "T_TRIP_STARTED",
                    "ts": self.currts,
                },
                "metadata": {
                    "platform": "ios",
                    "write_ts": self.currts,
                    "time_zone": "UTC",
                    "key": "statemachine/transition",
                    "read_ts": 0,
                    "type": "message",
                },
            }
        )
        self.dt()
        self.liste.append(
            {
                "data": {
                    "currState": "STATE_ONGOING_TRIP",
                    "transition": "T_TRIP_STARTED",
                    "ts": self.currts,
                },
                "metadata": {
                    "platform": "ios",
                    "write_ts": self.currts,
                    "time_zone": "UTC",
                    "key": "statemachine/transition",
                    "read_ts": 0,
                    "type": "message",
                },
            }
        )
        self.dt()
        self.liste.append(
            {
                "data": {
                    "currState": "STATE_ONGOING_TRIP",
                    "transition": "T_TRIP_RESTARTED",
                    "ts": self.currts,
                },
                "metadata": {
                    "platform": "ios",
                    "write_ts": self.currts,
                    "time_zone": "UTC",
                    "key": "statemachine/transition",
                    "read_ts": 0,
                    "type": "message",
                },
            }
        )
        self.dt()

    def NewPoint(self):
        self.liste.append(
            {
                "data": {
                    "accuracy": 23.6,
                    "altitude": 22.3,
                    "bearing": 167.98,
                    "filter": "distance",
                    "floor": 0,
                    "latitude": self.currlat,
                    "longitude": self.currlong,
                    "sensed_speed": 0.44,
                    "ts": self.currts,
                    "vaccuracy": 1.3,
                },
                "metadata": {
                    "platform": "ios",
                    "write_ts": self.currts,
                    "time_zone": "UTC",
                    "key": "background/location",
                    "read_ts": 0,
                    "type": "sensor-data",
                },
            }
        )
        self.liste.append(
            {
                "data": {
                    "accuracy": 23.6,
                    "altitude": 22.3,
                    "bearing": 167.98,
                    "filter": "distance",
                    "floor": 0,
                    "latitude": self.currlat,
                    "longitude": self.currlong,
                    "sensed_speed": 0.44,
                    "ts": self.currts,
                    "vaccuracy": 1.3,
                },
                "metadata": {
                    "platform": "ios",
                    "write_ts": self.currts,
                    "time_zone": "UTC",
                    "key": "background/filtered_location",
                    "read_ts": 0,
                    "type": "sensor-data",
                },
            },
        )

    def SoftEnd(self):
        self.liste.append(
            {
                "data": {
                    "currState": "STATE_ONGOING_TRIP",
                    "transition": "T_VISIT_STARTED",
                    "ts": self.currts,
                },
                "metadata": {
                    "platform": "ios",
                    "write_ts": self.currts,
                    "time_zone": "UTC",
                    "key": "statemachine/transition",
                    "read_ts": 0,
                    "type": "message",
                },
            }
        )
        self.dt()
        self.liste.append(
            {
                "data": {
                    "currState": "STATE_ONGOING_TRIP",
                    "transition": "T_TRIP_END_DETECTED",
                    "ts": self.currts,
                },
                "metadata": {
                    "platform": "ios",
                    "write_ts": self.currts,
                    "time_zone": "UTC",
                    "key": "statemachine/transition",
                    "read_ts": 0,
                    "type": "message",
                },
            }
        )
        self.dt()

        self.NewPoint()
        self.dt()

        self.liste.append(
            {
                "data": {
                    "currState": "STATE_ONGOING_TRIP",
                    "transition": "T_END_TRIP_TRACKING",
                    "ts": self.currts,
                },
                "metadata": {
                    "platform": "ios",
                    "write_ts": self.currts,
                    "time_zone": "UTC",
                    "key": "statemachine/transition",
                    "read_ts": 0,
                    "type": "message",
                },
            }
        )
        self.dt()
        self.liste.append(
            {
                "data": {
                    "currState": "STATE_ONGOING_TRIP",
                    "transition": "T_TRIP_ENDED",
                    "ts": self.currts,
                },
                "metadata": {
                    "platform": "ios",
                    "write_ts": self.currts,
                    "time_zone": "UTC",
                    "key": "statemachine/transition",
                    "read_ts": 0,
                    "type": "message",
                },
            }
        )
        self.dt()
        self.liste.append(
            {
                "data": {
                    "currState": "STATE_WAITING_FOR_TRIP_START",
                    "transition": "T_NOP",
                    "ts": self.currts,
                },
                "metadata": {
                    "platform": "ios",
                    "write_ts": self.currts,
                    "time_zone": "UTC",
                    "key": "statemachine/transition",
                    "read_ts": 0,
                    "type": "message",
                },
            }
        )
        self.dt()
        self.liste.append(
            {
                "data": {
                    "currState": "STATE_WAITING_FOR_TRIP_START",
                    "transition": "T_DATA_PUSHED",
                    "ts": self.currts,
                },
                "metadata": {
                    "platform": "ios",
                    "write_ts": self.currts,
                    "time_zone": "UTC",
                    "key": "statemachine/transition",
                    "read_ts": 0,
                    "type": "message",
                },
            }
        )
        self.dt()

    def MotionPoint(
        self, bike
    ):  # Note : the server can override this (cf test ID NewVerifPythonGenerated25)
        self.liste.append(
            {
                "data": {
                    "cycling": True,
                    "walking": False,
                    "running": False,
                    "automotive": False,
                    "stationary": False,
                    "confidence": 100,
                    "unknown": False,
                    "ts": self.currts,
                    "confidence_level": "high",  # Necessary, is "confidence" also necessary?
                },
                "metadata": {
                    "write_ts": self.currts,
                    "time_zone": "UTC",
                    "platform": "ios",
                    "key": "background/motion_activity",
                    "read_ts": 0,
                    "type": "sensor-data",
                },
            }
        )


trip = Trip()

trip.SoftStart()

for i in range(100):
    trip.NewPoint()
    trip.dt()
    trip.MotionPoint(True)
    trip.dt()

    trip.currlat += 0.001
    trip.currlong += 0.001
    trip.currts += 25


trip.currts += 305  # 630 ne donne pas de trajet, pause trop longue. 60 marche. Interprétation du code du serveur : 5 min si on est en "time", 10 en "distance". Cependant les deux donnent un trajet avec un "trou" entre le point de départ du premier segment et le trajet du deuxième. 5 min n'est pas la limite exacte non plus (305s de pause marche).
trip.SoftEnd()
trip.currts += 7000

trip.currlat += 0.003

trip.SoftStart()

for i in range(50):
    trip.NewPoint()
    trip.dt()
    trip.MotionPoint(False)
    trip.currlat += 0.001
    trip.currlong -= 0.001
    trip.currts += 25

trip.currts += 1000
trip.currlat += 0.1

for i in range(50):
    trip.NewPoint()
    trip.dt()
    trip.MotionPoint(False)
    trip.currlat += 0.001
    trip.currlong -= 0.001
    trip.currts += 25

trip.SoftEnd()


body = {"user": "NewVerifPythonGenerated6", "phone_to_server": trip.liste}

print(json.dumps(body))
