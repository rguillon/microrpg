
class Statistic:

    def __init__(self):
        self.events = {}

    def add_event(self, event):
        try:
            self.events[event] += 1
        except KeyError:
            self.events[event] = 1

    def display_events(self):
        for event in sorted(self.events):
            print("Event <%s> occurred %d times" % (event, self.events[event]))

def main():
    s = Statistic()

    s.add_event("e1")
    s.add_event("e2")
    s.add_event("e3")
    s.add_event("e3")
    s.add_event("e3")
    s.add_event("e2")

    s.display_events()


if __name__ == '__main__':
    main()