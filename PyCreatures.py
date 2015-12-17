"""

PyCreatures module

Provides user access to high-level methods of Controller

"""

import Controller

from time import sleep


class PyCreatures(object):

    def __init__(self):
        """

        Initialisation of the PyCreatures object.

        """

        self.ctlr = Controller.Controller()
        self.ctlr.new_world(79, 29)
        self.ctlr.print_map()

        self._should_quit = False

    def _animate_cycles(self, amount, dt=0):
        """

        Advances the world by n cycles and draws each iteration with
        a time offset of dt

        """

        if amount > 0:

            for cycle in range(amount):

                self.ctlr.next_cycle()
                self.ctlr.print_map()

                if dt > 0:
                    sleep(dt)

    def _perform_animate_cycles(self, args):
        """

        Wraps _animate_cycles to validate user input.

        """

        if args[0].isdigit():
            self._animate_cycles(int(args[0]))

        elif len(args) == 1:
            self._animate_cycles(1)

        elif len(args) == 2 and args[1].isdigit():

            cycle_amount = int(args[1])
            self._animate_cycles(cycle_amount, 0.05)

        elif len(args) == 3 and args[1].isdigit() and args[2].isdigit():

            cycle_amount = int(args[1])
            dt = int(args[2]) / 1000

            self._animate_cycles(cycle_amount, dt)

    def _perform_spawn(self, args):
        """

        Wraps spawn_multiple_at_random_pos to validate user input.

        """

        if len(args) != 3 or not args[1].isdigit():
            return

        self.ctlr.spawn_multiple_at_random_pos(args[2], int(args[1]))

    def _perform_quit(self):
        """

        Sets _should_quit to True.

        """

        self._should_quit = True

    def _print_help(self):
        """

        Gets the contents of README.txt and prints them out.
        Prints error message if read fails.

        """

        help_str = "Failed to load README.txt :("

        try:
            f = open("./README.txt")
            help_str = f.read()

        except Exception:
            pass

        print(help_str)

    def perform_command(self, command_str):
        """

        Performs a command by the user.
        Performs only one command, the input string should only contain
        a single command.
        Malformed command strings are ignored.

        """

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

    @property
    def should_quit(self):
        """

        A getter for _should_quit.

        """

        return self._should_quit
