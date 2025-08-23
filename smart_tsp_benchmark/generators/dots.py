# --------------------------------------------------------
# Copyright © 2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
import numpy as np


class RandomDotGenerator:
    @classmethod
    def generate(cls, n, scale):
        return np.random.rand(n, 2) * scale


class ClusterDotGenerator:
    @classmethod
    def generate(cls, n, scale):
        clusters = np.random.randint(3, 7)
        sizes = np.random.multinomial(n, np.ones(clusters) / clusters)
        return np.concatenate([
            np.random.randn(size, 2) * (scale / 10) + np.random.rand(2) * scale * 0.8
            for size in sizes
        ])


class CircleDotGenerator:
    @classmethod
    def generate(cls, n, scale, noise):
        angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
        base = scale / 2 + (scale / 3) * np.column_stack([np.cos(angles), np.sin(angles)])
        return base + np.random.randn(n, 2) * noise


class GridDotGenerator:
    @classmethod
    def generate(cls, n, scale, noise):
        grid_size = int(np.sqrt(n)) + 1
        x = np.linspace(0, scale, grid_size)
        y = np.linspace(0, scale, grid_size)
        xx, yy = np.meshgrid(x, y)
        points = np.column_stack([xx.ravel(), yy.ravel()])
        return points[:n] + np.random.randn(n, 2) * noise


class SpiralDotGenerator:
    @classmethod
    def generate(cls, n, scale, noise):
        t = np.linspace(0, 10 * np.pi, n)
        r = t / t.max() * scale / 2
        x = scale / 2 + r * np.cos(t)
        y = scale / 2 + r * np.sin(t)
        return np.column_stack([x, y]) + np.random.randn(n, 2) * noise




def generate_dots(
        n: int,
        seed: int = 42,
        method = 'random',
        scale: float = 100.0,
        noise: float = 5.0
) -> np.ndarray:
    np.random.seed(seed)

    if method == 'random':
        return RandomDotGenerator.generate(n, scale)

    elif method == 'cluster':
        return ClusterDotGenerator.generate(n, scale)

    elif method == 'circle':
        return CircleDotGenerator.generate(n, scale, noise)

    elif method == 'grid':
        return GridDotGenerator.generate(n, scale, noise)

    elif method == 'spiral':
        return SpiralDotGenerator.generate(n, scale, noise)

    else:
        raise ValueError(f"Unknown method: {method}")


if __name__ == "__main__":
    berlin_like = generate_dots(52, method='circle', noise=2.0)
    pr439_like = generate_dots(439, method='cluster')
    att532_like = generate_dots(532, method='grid', noise=1.5)
    rd400_like = generate_dots(400, method='random')
