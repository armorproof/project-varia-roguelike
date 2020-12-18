from __future__ import annotations

from typing import TYPE_CHECKING

import color

if TYPE_CHECKING:
    from tcod import Console


# This feels really hard coded.
# Maybe have this be an object with a draw function that you pass values into?
def render_bar(
    console: Console,
    current_value: int,
    maximum_value: int,
    total_width: int,
) -> None:
    """Utilizes the tcod draw_rect functions to draw two rectangular bars and overlays it with text."""
    bar_width = int( float( current_value ) / maximum_value * total_width )

    # I wonder if there's anything I could create and throw in here instead of so many arguments?
    console.draw_rect( x = 0, y = 45, width = 20, height = 1, ch = 1, bg = color.bar_empty )

    if bar_width > 0:
        console.draw_rect( x = 0, y = 45, width = bar_width, height = 1, ch = 1, bg = color.bar_filled )

    console.print( x = 1, y = 45, string = f"HP: {current_value}/{maximum_value}", fg = color.bar_text )