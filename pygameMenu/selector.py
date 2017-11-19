# coding=utf-8
"""
SELECTOR
Selector class, manage elements and adds entries to menu.

"""


class Selector(object):
    """
    Selector object
    """

    def __init__(self, title, elements, onchange=None, onreturn=None, **kwargs):
        """
        Constructor.
        
        :param title: Title of the selector
        :param elements: Elements of the selector
        :param onchange: Event when changing the selector
        :param onreturn: Event when pressing return button
        :param kwargs: Optional arguments
        """
        self._kwargs = kwargs
        self._elements = elements
        self._index = 0
        self._on_change = onchange
        self._on_return = onreturn
        self._title = title
        self._total_elements = len(elements)

    def apply(self):
        """
        Apply the selected item when return event.
        
        :return: None
        """
        if self._on_return is not None:
            paramlist = self._elements[self._index]
            paraml = []
            for i in range(1, len(paramlist)):
                paraml.append(paramlist[i])

            if len(self._kwargs) > 0:
                self._on_return(*paraml, **self._kwargs)
            else:
                self._on_return(*paraml)

    def change(self):
        """
        Apply the selected item when changing.
        
        :return: None
        """
        if self._on_change is not None:
            paramlist = self._elements[self._index]
            paraml = []
            for i in range(1, len(paramlist)):
                paraml.append(paramlist[i])

            if len(self._kwargs) > 0:
                self._on_change(*paraml, **self._kwargs)
            else:
                self._on_change(*paraml)

    def get(self):
        """
        Return element text.
        
        :return: String
        """
        return '{0} < {1} >'.format(self._title, self._elements[self._index][0])

    def left(self):
        """
        Move selector to left.
        
        :return: 
        """
        self._index = (self._index - 1) % self._total_elements
        self.change()

    def right(self):
        """
        Move selector to right.
        
        :return: 
        """
        self._index = (self._index + 1) % self._total_elements
        self.change()
