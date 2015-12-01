import World
import Thing
import Mouse
import Corn


if __name__ == "__main__":

    w = World.World()
    w.add_thing(Thing.Thing(), 15, 0)
    w.add_thing(Thing.Thing(), 15, 9)

    thing1 = w.get_thing(15, 0)

    print(thing1.symbol)
