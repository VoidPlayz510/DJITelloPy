from mock.drone import TelloDrone

drone = TelloDrone(host='10.1.1.202')
drone2 = TelloDrone(host='10.1.1.202', port=9000, state_udp_port=9001)
drone.takeoff()
drone2.takeoff()