import time

class TrafficLight:
    def __init__(self, red_time=5, yellow_time=2, green_time=5):
        self.states = {
            "red":     ("Красный🔴", red_time),
            "yellow1": ("Жёлтый🟡",  yellow_time),
            "green":   ("Зелёный🟢", green_time),
            "yellow2": ("Жёлтый🟡",  yellow_time),
        }
        
        self.transitions = {
            "red":     "yellow1",
            "yellow1": "green",
            "green":   "yellow2",
            "yellow2": "red",
        }
        
        self.current_state = "red"
    def next(self):
        
        name, duration = self.states[self.current_state]
        
        print(name)
        for sec in range(duration, 0, -1):
            print(f"  {sec}с")
            time.sleep(1)
        
        self.current_state = self.transitions[self.current_state]
    
    def run(self):
        
        while True:
            self.next()


light = TrafficLight(red_time=10, yellow_time=2, green_time=10)
light.run()