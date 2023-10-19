"""
Flight: BCN->AMS->JFK has two segments (BCN->AMS, AMS->JFK)

"""
from typing import List


class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination


class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    def __repr__(self) -> str:
        """
        :return: string in the format GLA -> LHR -> CAN
        """
        # option 1:
        # seg = ""
        # for index, segment in enumerate(self.segments):
        #     if index == 0:
        #         seg = f"{segment.departure} -> {segment.destination}"
        #     else:
        #         seg += f" -> {segment.destination}"

        # return seg
    
        # option 2
        stops = [self.segments[0].departure, self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)
        return ' -> '.join(stops)

    @property
    def departure_point(self) -> str:
        return self.segments[0].departure

    # define setter from a property function
    @departure_point.setter
    def departure_point(self, val):
        # self.segments[0].departure = val
        dest = self.segments[0].destination
        self.segments[0] = Segment(departure=val, destination=dest)


flight = Flight([Segment("GLA", "LHR"), Segment("LHR", "JFK")])
print(flight.departure_point)  # Output: GLA
flight.segments[0].departure = "EDI"
print(flight.departure_point)  # Output: EDI
flight.departure_point = "BCN"
print(flight.departure_point)  # Output: BCN
print(flight)
