from __future__ import annotations

from typing import List, Tuple

import numpy as np  # type: ignore
import tcod

from actions import Action
from components.base_component import BaseComponent


class BaseAI( Action, BaseComponent ): # Multiple inheritance!

    def perform( self ) -> None:
        raise NotImplementedError()

    def get_path_to( self, dest_x: int, dest_y: int ) -> List[ Tuple[ int, int ] ]:
        """Compute and return a path to the target position.

        If there is no valid path, return an empty list.
        """
        raise NotImplementedError()