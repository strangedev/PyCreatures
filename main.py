import World
import Thing
import Controller
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

    ctlr = Controller.Controller()

    ctlr.new_world(79, 29)
    ctlr.spawn_multiple_at_random_pos("Corn", 20)

    for i in range(120):

        ctlr.next_cycle()
        ctlr.print_map()

        time.sleep(0.01)


if __name__ == "__main__":
    #  milestone_1()
    milestone_2()
