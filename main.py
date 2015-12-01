import World
import Thing
import Mouse
import Corn
import time


def milestone_1():
    w = World.World(20, 10)
    w.add_thing(Thing.Thing(), 15, 0)
    w.add_thing(Thing.Thing(), 15, 9)

    thing1 = w.get_thing(15, 0)
    print(thing1.symbol)

    things_neighbor = w.get_neighbor_from_coords(15, 0, World.NORTH)
    print(things_neighbor)

    w.remove_thing_at_coords(15, 9)

    things_neighbor = w.get_neighbor_from_coords(15, 0, World.NORTH)
    print(things_neighbor)

    print(w.print_map())


def milestone_2():

    w = World.World(79, 29)

    for i in range(20):
        w.add_thing(Corn.Corn(), i, 0)

    for i in range(20):
        w.add_thing(Corn.Corn(), 0, i)

    for i in range(5):
        w.add_thing(Mouse.Mouse(), i, 3)

    for k in range(1000):
        time.sleep(0.01)

        w.compute_life_cycle()
        print(w.print_map())

if __name__ == "__main__":
    #  milestone_1()
    milestone_2()
