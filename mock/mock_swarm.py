from threading import Thread, Barrier
from queue import Queue
from typing import List, Callable
import time

from mock.drone import TelloDrone


class MockSwarm:
    def __init__(self, ips: List[str]):
        self.tellos = [TelloDrone(ip) for ip in ips]

    def sequential(self, func: Callable[[int, TelloDrone], None]):
        for i, tello in enumerate(self.tellos):
            func(i, tello)

    def parallel(self, func: Callable[[int, TelloDrone], None]):
        for tello in self.tellos:
            func(0, tello)  # Simulate parallel behavior for each Tello

    def takeoff(self):
        print("Mock: All drones taking off")

    def land(self):
        print("Mock: All drones landing")