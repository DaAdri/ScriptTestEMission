import json


class Trip:
    liste = []
    startlat = -33.89024429693447
    currlat = startlat
    startlong = 151.19991587790943
    currlong = startlong
    startts = 1692085445.01
    currts = startts
    plateform = "ios"

    def dt(self):
        self.currts += 0.01

    def AddTransition(self, state, transition):
        self.liste.append(
            {
                "data": {
                    "currState": state,
                    "transition": transition,
                    "ts": self.currts,
                },
                "metadata": {
                    "platform": self.plateform,
                    "write_ts": self.currts,
                    "time_zone": "UTC",
                    "key": "statemachine/transition",
                    "read_ts": 0,
                    "type": "message",
                },
            }
        )

    def SoftStart(self):
        self.AddTransition("STATE_WAITING_FOR_TRIP_START", "T_EXITED_GEOFENCE")
        self.dt()

        self.AddTransition("STATE_WAITING_FOR_TRIP_START", "T_TRIP_STARTED")
        self.dt()

        self.AddTransition("STATE_ONGOING_TRIP", "T_TRIP_STARTED")
        self.dt()

        self.AddTransition("STATE_ONGOING_TRIP", "T_TRIP_RESTARTED")
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
                    "platform": self.plateform,
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
                    "platform": self.plateform,
                    "write_ts": self.currts,
                    "time_zone": "UTC",
                    "key": "background/filtered_location",
                    "read_ts": 0,
                    "type": "sensor-data",
                },
            },
        )

    def SoftEnd(self):
        self.AddTransition("STATE_ONGOING_TRIP", "T_VISIT_STARTED")
        self.dt()

        self.AddTransition("STATE_ONGOING_TRIP", "T_TRIP_END_DETECTED")
        self.dt()

        self.AddTransition("STATE_ONGOING_TRIP", "T_END_TRIP_TRACKING")
        self.dt()

        self.AddTransition("STATE_ONGOING_TRIP", "T_TRIP_ENDED")
        self.dt()

        self.AddTransition("STATE_WAITING_FOR_TRIP_START", "T_NOP")
        self.dt()

        self.AddTransition("STATE_WAITING_FOR_TRIP_START", "T_DATA_PUSHED")
        self.dt()

    def MotionPoint(
        self, bike
    ):  # Note : the server can override this (cf test ID NewVerifPythonGenerated25)
        self.liste.append(
            {
                "data": {
                    "cycling": bike,
                    "walking": False,
                    "running": not bike,
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
                    "platform": self.plateform,
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

for i in range(500):
    trip.NewPoint()
    trip.dt()
    trip.MotionPoint(i > 50)
    trip.currlat += 0.001
    trip.currlong -= 0.001
    trip.currts += 25

trip.SoftEnd()


body = {"user": "605jpqg0zj7", "phone_to_server": trip.liste}

print(json.dumps(body))
