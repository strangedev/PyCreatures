import copy

__author__ = "5966916: Noah Hummel, 5987733: Kyle Rinfreschi"


class ImageHistory(object):
    """
    Keeps a history of data with appropriate labeling.
    Supports reverting the current state of data to a previous state.
    Also supports reverting to a more recent state, when a previous
    undo had been performed.
    Overwrites more recent states, if data is changed after reverting to
    a previous state, keeps only one timeline.
    """

    def __init__(self):
        """
        Intialises labels and data.
        """

        self._content_current = None
        self._content_history = []
        self._content_future = []

        self._label_current = None
        self._label_history = []
        self._label_future = []

    def advance_state(self, content, label):
        """
        Sets current data state to state passed in
        content and label.
        Archives previous state to history.
        """

        if self._content_current is not None:

            self._archive_current_to_past()

        self._update_current(content, label)

        if len(self._content_future) > 0:
            self._label_future = []  # advancing the state rewrites future
            self._content_future = []  # advancing the state rewrites future

    def _update_current(self, content, label):
        """
        Setter for current state, handles deepcopying of data
        to avoid referencing issues with mutable datatypes.
        """

        self._content_current = copy.deepcopy(content)
        self._label_current = copy.deepcopy(label)

    def _archive_current_to_past(self):
        """
        Abstraction method to implement dry principle.
        """

        self._content_history.append(self._content_current)
        self._label_history.append(self._label_current)

    def _archive_current_to_future(self):
        """
        Abstraction method to implement dry principle.
        """

        self._content_future.append(self._content_current)
        self._label_future.append(self._label_current)

    def restore_past_state(self):
        """
        Abstraction method to implement dry principle.
        Also checks if history is available and stores current
        state in future.
        """

        if len(self._content_history) > 0:

            self._archive_current_to_future()

            self._content_current = self._content_history.pop()
            self._label_current = self._label_history.pop()

    def restore_future_state(self):
        """
        Abstraction method to implement dry principle.
        Also checks if future is available and stores current
        state in history.
        """

        if len(self._content_future) > 0:

            self._archive_current_to_past()

            self._content_current = self._content_future.pop()
            self._label_current = self._label_future.pop()

    @property
    def undo_available(self):
        """
        Getter for dynamic flag.
        """
        return len(self._content_history) > 0

    @property
    def redo_available(self):
        """
        Getter for dynamic flag.
        """
        return len(self._content_future) > 0

    @property
    def current(self):
        """
        Getter for data encapsulation purposes.
        """
        return self._content_current

    @property
    def undo_label(self):
        """
        Getter for data encapsulation purposes.
        Also handles error cases.
        """
        return self._label_current if self._label_history else None

    @property
    def redo_label(self):
        """
        Getter for data encapsulation purposes.
        Also handles error cases.
        """
        return self._label_future[-1] if self._label_future else None

    @property
    def history(self):
        """
        Getter for data encapsulation purposes.
        """
        return self._label_history

    @property
    def future(self):
        """
        Getter for data encapsulation purposes.
        """
        return self._label_future

"""
Test code. Left in for easier validation without GUI.

hist = ImageHistory(1, "Loaded 1")
print("Undo:", hist.undo_label)

print("future:", hist.future)
print("current:", hist.current)
print("history:", hist.history)

hist.advance_state(2, "1 -> 2")

print("future:", hist.future)
print("current:", hist.current)
print("history:", hist.history)

hist.restore_past_state()

print("future:", hist.future)
print("current:", hist.current)
print("history:", hist.history)

hist.restore_future_state()

print("future:", hist.future)
print("current:", hist.current)
print("history:", hist.history)

# hist.restore_past_state()
print("Undo:", hist.undo_label)

print("Redo:", hist.redo_label)
"""
