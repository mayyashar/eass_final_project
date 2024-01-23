from typing import List
import numpy as np


def compute_dot_product(vec_a: list, vec_b: List) -> float:
    vec_a = np.array(vec_a)
    vec_b = np.array(vec_b)

    try:
        dot = np.dot(vec_a, vec_b)
        return dot

    except ValueError:
        return np.nan