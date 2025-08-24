# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
from smart_tsp_benchmark.tsp_benchmark import TSPBenchmark


def main():
    config = {
        'n_dots': 1000,
        'seed': 777,
        'dot_generation': 'random',
        'use_post_optimization': False,
        'plot_results': False,
        'verbose': True
    }
    benchmark = TSPBenchmark(config=config)
    benchmark.run_benchmark()


if __name__ == '__main__':
    main()
