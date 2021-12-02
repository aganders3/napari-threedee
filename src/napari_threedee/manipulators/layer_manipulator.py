from typing import Optional

import numpy as np
from napari_threedee.manipulators.base_manipulator import BaseManipulator


class LayerManipulator(BaseManipulator):

    def __init__(self, viewer, layer, line_length=50, order=0):
        self._line_length = line_length
        self._initial_translate = None

        self._centroid = np.array([0, 0, 0])

        self._initial_translator_normals = np.asarray(
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]
            ]
        )
        self._initial_rotator_normals = np.empty((0, 3))

        super().__init__(viewer, layer, order)

    def _pre_drag(
            self,
            click_point: np.ndarray,
            selected_translator: Optional[int],
            selected_rotator: Optional[int]
    ):
        self._initial_translate = self._layer.translate

    def _while_translator_drag(self, selected_translator: int, translation_vector: np.ndarray):
        new_translation = self._initial_translate + translation_vector
        self._layer.translate = np.squeeze(new_translation)

    def _on_click_cleanup(self):
        self._initial_translate = None
