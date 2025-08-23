# --------------------------------------------------------
# Copyright © 2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
from typing import List

import numpy as np
from scipy.spatial import distance


def calculate_length(dots: np.ndarray, route: List[int]) -> float:
    return sum(distance.euclidean(dots[route[i]], dots[route[i + 1]])
               for i in range(len(route) - 1))
