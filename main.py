import tcod

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler

def main() -> None:

    #print( "Hello World!" )

    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity( int( screen_width / 2 ), int( screen_height / 2 ), "@", ( 255, 255, 255 ) )
    npc = Entity( int( screen_width / 2 - 5 ), int( screen_height / 2 ), "@", ( 255, 255, 0 ) )
    
    # Collection of all the entities in the game?
    entities = { npc, player }

    # With is basically C#'s using statement
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset = tileset,
        title = "Yet Another Roguelike Tutorial",
        vsync = True,
    ) as context:
        root_console = tcod.Console( screen_width, screen_height, order = "F" )
        while True: # Main game loop?
            root_console.print( x = player.x, y = player.y, string=player.char, fg = player.color )

            # Reminder, context is the above tcod terminal
            context.present( root_console ) # Updates the screen

            root_console.clear()

            for event in tcod.event.wait(): # This listens for user input
                
                action = event_handler.dispatch( event )

                # So we pass the keypress to the event handler that returns to us the resulting action
                if action is None:
                    continue

                if isinstance( action, MovementAction ):
                    player.move( dx = action.dx, dy = action.dy )

                elif isinstance( action, EscapeAction ):
                    raise SystemExit()

if __name__ == "__main__":
    main()