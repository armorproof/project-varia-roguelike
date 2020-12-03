import tcod

def main() -> None:

    #print( "Hello World!" )

    screen_width = 80
    screen_height = 50

    player_x = int( screen_width / 2 )
    player_y = int( screen_height / 2 )

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

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
            root_console.print( x = player_x, y = player_y, string="@" )

            # Reminder, context is the above tcod terminal
            context.present( root_console ) # Updates the screen

            for event in tcod.event.wait(): # Is this like an event listener?
                if event.type == "QUIT":
                    raise SystemExit()

if __name__ == "__main__":
    main()