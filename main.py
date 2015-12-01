import World
import Mouse
import Corn


w = World.World()
w.add_thing(Mouse.Mouse(), 0, 0)
w.add_thing(Corn.Corn(), 10, 0)

print(w.print_map())
