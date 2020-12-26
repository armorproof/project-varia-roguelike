from typing import Iterable, List, Reversible, Tuple
import textwrap

import tcod

import color


class Message:
    def __init__( self, text: str, fg: Tuple[ int, int, int ] ):
        # I'm guessing fg has to do with colour but, why fg?
        self.plain_text = text
        self.fg = fg
        self.count = 1

    @property
    def full_text( self ) -> str:
        """The full text of this message, including the count if necessary."""
        if self.count > 1:
            return f"{self.plain_text} (x{self.count})"
        return self.plain_text


class MessageLog:
    def __init__( self ) -> None: # This seems like a pretty standard line for a constructor, worth memorizing?
        self.messages: List[ Message ] = []

    def add_message(
        self,
        text: str,
        fg: Tuple[ int, int, int ] = color.white,
        *, # What does this mean?
        stack: bool = True,
    ) -> None:
        """
        Add a message to this log.
        'Text' is the message text, 'fg' is the text colour.
        If 'stack' is True then this message can stack with a previous message
        of the same text.
        """
        if stack and self.messages and text == self.messages[ -1 ].plain_text:
            # Reminder, -1 means the last entry
            self.messages[ -1 ].count += 1
        else:
            self.messages.append( Message( text, fg ) )
    
    def render(
        self,
        console: tcod.Console,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        """
        Render this log over the given area.
        'x', 'y', 'width', 'height' is the rectangular region to render onto the 'console'.
        """
        self.render_messages( console, x, y, width, height, self.messages )

    @staticmethod
    def wrap( string: str, width: int ) -> Iterable[ str ]:
        """Return a wrapped text message."""
        for line in string.splitlines(): # Handle newlines in messages.
            yield from textwrap.wrap( # See PEP 380 for information on yield from.
                line, width, expand_tabs = True,
            )

    @classmethod
    def render_messages(
        cls,
        console: tcod.Console,
        x: int,
        y: int,
        width: int,
        height: int,
        messages: Reversible[ Message ],
    ) -> None:
        """
        Render the messages provided.
        The 'messages' are rendered starting at the last message and working backwards.
        """
        y_offset = height - 1

        for message in reversed( messages ):
            for line in reversed( list( cls.wrap( message.full_text, width ) ) ):
                console.print( x = x, y = y + y_offset, string = line, fg = message.fg )
                y_offset -= 1
                if y_offset < 0:
                    return # No more space to print messages.