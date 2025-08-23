# Smart TSP Benchmark

---

⚡ Smart TSP Benchmark is a professional algorithm testing infrastructure with customizable scenarios and detailed metrics.

---

---

![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smart-tsp-benchmark)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smart-tsp-benchmark)](https://github.com/smartlegionlab/smart-tsp-benchmark/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smart-tsp-benchmark)](https://github.com/smartlegionlab/smart-tsp-benchmark/blob/master/LICENSE)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/smart-tsp-benchmark?style=social)](https://github.com/smartlegionlab/smart-tsp-benchmark/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/smart-tsp-benchmark?style=social)](https://github.com/smartlegionlab/smart-tsp-benchmark/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smart-tsp-benchmark?style=social)](https://github.com/smartlegionlab/smart-tsp-benchmark/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smart-tsp-benchmark?label=pypi%20downloads)](https://pypi.org/project/smart-tsp-benchmark/)
[![PyPI](https://img.shields.io/pypi/v/smart-tsp-benchmark)](https://pypi.org/project/smart-tsp-benchmark)
[![PyPI - Format](https://img.shields.io/pypi/format/smart-tsp-benchmark)](https://pypi.org/project/smart-tsp-benchmark)

---

### Install

```bash
pip install smart-tsp-solver
```

---

Example of creating a configuration file `tsp_config.json`:

```json
{
  "algorithms": {
    "Angular-radial v1": {
      "enabled": true,
      "params": {
        "sort_by": "angle_distance",
        "look_ahead": 100,
        "max_2opt_iter": 100
      }
    },
    "Angular-radial v2": {
      "enabled": true,
      "params": {
        "sort_by": "angle_distance",
        "look_ahead": 100,
        "max_2opt_iter": 100
      }
    },
    "Dynamic-gravity v1": {
      "enabled": true,
      "params": {
        "delta": 0.5,
        "fast_2opt_iter": 100
      }
    },"Dynamic-gravity v2": {
      "enabled": true,
      "params": {
        "delta": 0.5,
        "fast_2opt_iter": 100
      }
    },
    "Greedy v2": {
      "enabled": true,
      "params": {
        "start_point": 0
      }
    }
  },
  "benchmark": {
    "n_cities": 100,
    "seed": 777,
    "city_generation": "cluster",
    "use_post_optimization": false,
    "plot_results": false,
    "verbose": true
  }
}
```

## Example of use

```python
from smart_tsp_benchmark.tsp_benchmark import TSPBenchmark


def main():
    benchmark = TSPBenchmark(config_path='tsp_config.json')
    benchmark.run_benchmark()


if __name__ == '__main__':
    main()

```

## 👨‍💻 Author

**A.A. Suvorov**

- Researcher specializing in computational optimization and high-performance algorithms
- Focused on bridging theoretical computer science with practical engineering applications
- This project represents extensive research into spatial optimization techniques

*Explore other projects on [GitHub](https://github.com/smartlegionlab).*

## 📄 License

This project is licensed under the **BSD 3-Clause License** - see the [LICENSE](LICENSE) file for details. 
This permits academic and commercial use while protecting author rights.

## 🔗 Related Research

For those interested in the theoretical foundations:

- **[smart-tsp-solver](https://github.com/smartlegionlab/smart-tsp-solver)** - My Python library featuring advanced heuristics (`Dynamic Gravity`, `Angular Radial`) for solving *large* TSP instances where finding the exact optimum is impractical.
- **Exact TSP Solutions (TSP ORACLE):** [exact-tsp-solver](https://github.com/smartlegionlab/exact-tsp-solver) - Optimal solutions for small instances
- **Spatial Optimization:** Computational geometry approaches for large-scale problems
- **Heuristic Analysis:** Comparative study of modern TSP approaches

## 📚 Citation

If this work contributes to your research, please cite:

```bibtex
@software{suvorov2025tspsolver,
  title = {Smart TSP Solver Suite: Advanced Heuristic Algorithms},
  author = {Suvorov, A.A.},
  year = {2025},
  url = {https://github.com/smartlegionlab/smart-tsp-benchmark}
}
```

## 🎨 Advanced Visualization

![LOGO](https://github.com/smartlegionlab/smart-tsp-benchmark/raw/master/data/images/tsp100.png)
![LOGO](https://github.com/smartlegionlab/smart-tsp-benchmark/raw/master/data/images/tsp1001.png)
*Visual analysis showing Angular-radial's optimal sector-based routing, Dynamic-gravity's smooth trajectories, Greedy's suboptimal clustering*

---

## 📊 Sample Output

```
==================================================
          SMART TSP ALGORITHMS BENCHMARK          
==================================================
Cities:         100
Seed:           123
Generation:     cluster
Post-opt:       OFF
Algorithms:    
  - Angular-radial v1: sort_by=angle_distance, look_ahead=1001, max_2opt_iter=1001
  - Angular-radial v2: sort_by=angle_distance, look_ahead=1000, max_2opt_iter=1001
  - Dynamic-gravity v1: delta=0.5, fast_2opt_iter=1001
  - Dynamic-gravity v2: delta=0.5, fast_2opt_iter=1001
  - Greedy v2: start_point=0
==================================================


==================================================
Running Angular-radial v1 algorithm...
Description: Angular-radial v1
Parameters: sort_by=angle_distance, look_ahead=1001, max_2opt_iter=1001
Completed in 0.0842 seconds
Route length: 553.66
==================================================

==================================================
Running Angular-radial v2 algorithm...
Description: Angular-radial v2
Parameters: sort_by=angle_distance, look_ahead=1000, max_2opt_iter=1001
Completed in 0.0088 seconds
Route length: 553.66
==================================================

==================================================
Running Dynamic-gravity v1 algorithm...
Description: Dynamic gravity v1
Parameters: delta=0.5, fast_2opt_iter=1001
Completed in 0.0075 seconds
Route length: 567.00
==================================================

==================================================
Running Dynamic-gravity v2 algorithm...
Description: Dynamic gravity v2
Parameters: delta=0.5, fast_2opt_iter=1001
Completed in 0.0073 seconds
Route length: 534.90
==================================================

==================================================
Running Greedy v2 algorithm...
Description: Classic greedy TSP algorithm
Parameters: start_point=0
Completed in 0.0016 seconds
Route length: 609.21
==================================================

==============================================================================================================================
                                                DETAILED ALGORITHM COMPARISON                                                 
==============================================================================================================================
Algorithm            | Time (s) |  vs Best  | Length | vs Best | Params                                                       
------------------------------------------------------------------------------------------------------------------------------
Greedy v2            | 0.0016 | BEST | 609.21 | +13.89% | start_point=0                                                
Dynamic-gravity v2   | 0.0073 | +348.65%  | 534.90 | BEST | delta=0.5, fast_2opt_iter=1001                               
Dynamic-gravity v1   | 0.0075 | +361.28%  | 567.00 | +6.00%  | delta=0.5, fast_2opt_iter=1001                               
Angular-radial v2    | 0.0088 | +441.26%  | 553.66 | +3.51%  | sort_by=angle_distance, look_ahead=1000, max_2opt_iter=1001  
Angular-radial v1    | 0.0842 | +5064.72% | 553.66 | +3.51%  | sort_by=angle_distance, look_ahead=1001, max_2opt_iter=1001  
==============================================================================================================================

PERFORMANCE ANALYSIS:
- Fastest algorithm(s): Greedy v2 (0.0016 sec)
- Shortest route(s): Dynamic-gravity v2 (534.90 units)
```

```
==================================================
          SMART TSP ALGORITHMS BENCHMARK          
==================================================
Cities:         1001
Seed:           0
Generation:     cluster
Post-opt:       OFF
Algorithms:    
  - Angular-radial v1: sort_by=angle_distance, look_ahead=1001, max_2opt_iter=1001
  - Angular-radial v2: sort_by=angle_distance, look_ahead=1000, max_2opt_iter=1001
  - Dynamic-gravity v1: delta=0.5, fast_2opt_iter=1001
  - Dynamic-gravity v2: delta=0.5, fast_2opt_iter=1001
  - Greedy v2: start_point=0
==================================================


==================================================
Running Angular-radial v1 algorithm...
Description: Angular-radial v1
Parameters: sort_by=angle_distance, look_ahead=1001, max_2opt_iter=1001
Completed in 0.2531 seconds
Route length: 1388.82
==================================================

==================================================
Running Angular-radial v2 algorithm...
Description: Angular-radial v2
Parameters: sort_by=angle_distance, look_ahead=1000, max_2opt_iter=1001
Completed in 0.1263 seconds
Route length: 1388.82
==================================================

==================================================
Running Dynamic-gravity v1 algorithm...
Description: Dynamic gravity v1
Parameters: delta=0.5, fast_2opt_iter=1001
Completed in 0.0279 seconds
Route length: 1486.12
==================================================

==================================================
Running Dynamic-gravity v2 algorithm...
Description: Dynamic gravity v2
Parameters: delta=0.5, fast_2opt_iter=1001
Completed in 0.0248 seconds
Route length: 1485.03
==================================================

==================================================
Running Greedy v2 algorithm...
Description: Classic greedy TSP algorithm
Parameters: start_point=0
Completed in 0.0022 seconds
Route length: 1612.74
==================================================

================================================================================================================================
                                                 DETAILED ALGORITHM COMPARISON                                                  
================================================================================================================================
Algorithm            | Time (s) |  vs Best   |  Length | vs Best | Params                                                       
--------------------------------------------------------------------------------------------------------------------------------
Greedy v2            | 0.0022 | BEST | 1612.74 | +16.12% | start_point=0                                                
Dynamic-gravity v2   | 0.0248 | +1016.15%  | 1485.03 | +6.93%  | delta=0.5, fast_2opt_iter=1001                               
Dynamic-gravity v1   | 0.0279 | +1156.99%  | 1486.12 | +7.01%  | delta=0.5, fast_2opt_iter=1001                               
Angular-radial v2    | 0.1263 | +5590.97%  | 1388.82 | BEST | sort_by=angle_distance, look_ahead=1000, max_2opt_iter=1001  
Angular-radial v1    | 0.2531 | +11304.79% | 1388.82 | BEST | sort_by=angle_distance, look_ahead=1001, max_2opt_iter=1001  
================================================================================================================================

PERFORMANCE ANALYSIS:
- Fastest algorithm(s): Greedy v2 (0.0022 sec)
- Shortest route(s): Angular-radial v1, Angular-radial v2 (1388.82 units)
```

---

**Disclaimer:** Performance results shown are for clustered distributions. 
Results may vary based on spatial characteristics. 
Always evaluate algorithms on your specific problem domains.

---

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.