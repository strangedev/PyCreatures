import World
import Thing
from Entities.Creatures import Mouse
from Entities.Creatures import Cat
from Entities.Creatures import JohnCena
from Entities.Plants import Corn
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

    print(w.draw_map())


def milestone_2():

    w = World.World(140, 40)

    for i in range(20):
        w.add_thing(Corn.Corn(), i, 0)

    for i in range(20):
        w.add_thing(Corn.Corn(), 0, i)

    for i in range(5):
        w.add_thing(Mouse.Mouse(), i, 3)

    while True:
        time.sleep(0.0000001)

        w.compute_life_cycle()
        print(w.draw_map())
        print()

if __name__ == "__main__":
    #  milestone_1()
    milestone_2()
