# --------------------------------------------------------
# Copyright © 2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
from typing import List


def two_opt_swap(route: List[int], i: int, k: int) -> List[int]:
    return route[:i] + route[i:k + 1][::-1] + route[k + 1:]
