# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
from typing import List

import numpy as np
from scipy.spatial import distance


def calculate_length(points: np.ndarray, route: List[int]) -> float:
    return sum(distance.euclidean(points[route[i]], points[route[i + 1]])
               for i in range(len(route) - 1))
