import Controller
from time import sleep
import sys


class PyCreatures(object):

    """docstring for PyCreatures"""

    def __init__(self):

        self.width = 79
        self.height = 29
        self.ctlr = Controller.Controller()
<<<<<<< HEAD
        self.ctlr.new_world(self.width, self.height)
        self.ctlr.print_map()

        self._should_quit = False

    def _redraw(self, string, is_last=False):
        print(string)

        if not is_last:
            sys.stdout.write('\b\r' * (string.count('\n') + 1))
=======
        self.ctlr.new_world(79, 29)
        self._print_map()

        self._should_quit = False

    def _print_map(self):

        print(self.ctlr.draw_map())
>>>>>>> cef63903c2bfb1a37f54a3775d17f0f626351558

    def _animate_cycles(self, amount, dt=0):

        if amount > 0:

            for cycle in range(amount):

                self.ctlr.next_cycle()
<<<<<<< HEAD

                self._redraw(self.ctlr.draw_map(), cycle == amount - 1)
=======
>>>>>>> cef63903c2bfb1a37f54a3775d17f0f626351558

                if dt > 0:
                    self._print_map()
                    sleep(dt)

            if not (dt > 0):
                self._print_map()

    def _perform_animate_cycles(self, args):

        if args[0].isdigit():
            self._animate_cycles(int(args[0]))

        elif len(args) == 2 and args[1].isdigit():

            cycle_amount = int(args[1])
            self._animate_cycles(cycle_amount, 0.05)

        elif len(args) == 3 and args[1].isdigit() and args[2].isdigit():

            cycle_amount = int(args[1])
            dt = int(args[2]) / 1000

            self._animate_cycles(cycle_amount, dt)

    def _perform_spawn(self, args):

        if len(args) != 3 or not args[1].isdigit():
            return

        self.ctlr.spawn_multiple_at_random_pos(args[2], int(args[1]))
        self._print_map()

    def _perform_quit(self):
        self._should_quit = True

    def _print_help(self):

        help_str = "Failed to load README.txt :("

        try:
            f = open("./README.txt")
            help_str = f.read()

        except Exception:
            pass

        print(help_str)

    def perform_command(self, command_str):

        args = command_str.split()

        if not args:
            self._animate_cycles(1)

        elif args[0] == "h":
            self._print_help()

        elif args[0] == "q":
            self._perform_quit()

        elif args[0] == "spawn":
            self._perform_spawn(args)

        elif args[0] == "anim":
            self._perform_animate_cycles(args)

        elif args[0].isdigit():
            self._perform_animate_cycles(args)

        else:
        	self._print_map()

    @property
    def should_quit(self):
        return self._should_quit
