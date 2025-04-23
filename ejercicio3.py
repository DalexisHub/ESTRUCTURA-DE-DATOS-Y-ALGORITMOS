import random
from collections import deque

class Vehicle:
    def __init__(self, arrival_time, direction):
        self.arrival_time = arrival_time
        self.direction = direction

class TrafficLightSimulation:
    def __init__(self, green_duration=3, total_time=20):
        self.green_duration = green_duration
        self.total_time = total_time
        self.queues = {"NS": deque(), "EW": deque()}
        self.current_light = "NS"
        self.stats = {"total_wait": 0, "vehicles_passed": 0, "max_queue": {"NS": 0, "EW": 0}}

    def simulate(self):
        time = 0
        light_timer = 0

        while time < self.total_time:
            # Random arrival: 50% chance a car arrives in each direction
            for direction in ["NS", "EW"]:
                if random.random() < 0.5:
                    self.queues[direction].append(Vehicle(time, direction))
                    self.stats["max_queue"][direction] = max(self.stats["max_queue"][direction], len(self.queues[direction]))

            # Pass cars if green light
            if self.queues[self.current_light]:
                car = self.queues[self.current_light].popleft()
                wait_time = time - car.arrival_time
                self.stats["total_wait"] += wait_time
                self.stats["vehicles_passed"] += 1

            # Update traffic light
            light_timer += 1
            if light_timer >= self.green_duration:
                light_timer = 0
                self.current_light = "EW" if self.current_light == "NS" else "NS"

            time += 1

        # Final statistics
        avg_wait = self.stats["total_wait"] / self.stats["vehicles_passed"] if self.stats["vehicles_passed"] else 0
        return {
            "average_wait_time": avg_wait,
            "max_queue_NS": self.stats["max_queue"]["NS"],
            "max_queue_EW": self.stats["max_queue"]["EW"],
            "vehicles_passed": self.stats["vehicles_passed"]
        }

sim = TrafficLightSimulation(green_duration=3, total_time=30)
result = sim.simulate()
print(result)

sim = TrafficLightSimulation(green_duration=1, total_time=20)
print(sim.simulate())

sim = TrafficLightSimulation(green_duration=5, total_time=20)
print(sim.simulate())

# Modificar el random.random() para simular sin tráfico (si < 0.0)
