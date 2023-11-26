import itertools
from threading import Thread, Barrier
from queue import Queue
from typing import List, Callable
import time

from mocker.drone import TelloDrone


class MockSwarm:
    def __init__(self, ips: List[str]):
        # Define different ports for command and state
        command_ports = itertools.count(8889, 10)
        state_ports = itertools.count(8890, 10)

        self.tellos = [
            TelloDrone(ip, next(command_ports), next(state_ports)) for ip in ips
        ]

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