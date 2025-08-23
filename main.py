# --------------------------------------------------------
# Copyright © 2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
from smart_tsp_benchmark.tsp_benchmark import TSPBenchmark


def main():
    benchmark = TSPBenchmark(config_path='tsp_config.json')
    benchmark.run_benchmark()


if __name__ == '__main__':
    main()
