from mock_swarm import MockSwarm

if __name__ == "__main__":
    # Example usage of the MockSwarm class
    ips = [
        "10.1.1.202",  # Replace with actual IP addresses
    ]

    swarm = MockSwarm(ips)
    swarm.takeoff()

    swarm.parallel(lambda i, tello: tello.move_up(100))
    swarm.sequential(lambda i, tello: tello.move_up((i + 1) * 50))
    swarm.parallel(lambda i, tello: tello.land())
