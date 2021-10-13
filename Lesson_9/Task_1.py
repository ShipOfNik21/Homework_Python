from time import sleep


class TrafficLight:
    __color__ = "Черный"

    def running(self):
        while True:
            print("TrafficLight is red now")
            sleep(7)
            print("TrafficLight is yellow now")
            sleep(2)
            print("TrafficLight is green now")
            sleep(7)
            print("TrafficLight is yellow now")
            sleep(2)


trafficLight = TrafficLight()
trafficLight.running()