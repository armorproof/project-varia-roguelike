from typing import Optional

import tcod.event # The tcod event system

from actions import Action, BumpAction, MovementAction

# Ooh, a custom event handler class!
class EventHandler( tcod.event.EventDispatch[ Action ] ): # Subclass of EventDispatch
    def ev_quit( self, event: tcod.event.Quit ) -> Optional[ Action ]: # This is foreign
        raise SystemExit()

    def ev_keydown( self, event: tcod.event.KeyDown ) -> Optional[ Action ]:
        action: Optional[ Action ] = None # Strange?

        key = event.sym

        # Classic key switch statement
        if key == tcod.event.K_UP: # Guessing these are fixed variables representing each key
            action = BumpAction( dx = 0, dy =- 1 )
        elif key == tcod.event.K_DOWN:
            action = BumpAction( dx = 0, dy = 1 )
        elif key == tcod.event.K_LEFT:
            action = BumpAction( dx =- 1, dy = 0 )
        elif key == tcod.event.K_RIGHT:
            action = BumpAction( dx = 1, dy = 0 )

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action