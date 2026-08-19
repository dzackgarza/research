"""
Benchmark test specific fixtures.

Performance and complexity benchmarks for our implementations.
"""

import pytest
import time
import gc
from pathlib import Path


@pytest.fixture
def performance_timer():
    """High-precision timer for performance measurements."""
    class PerformanceTimer:
        def __init__(self):
            self.start_time = None
            self.end_time = None
            self.measurements = []
        
        def start(self):
            """Start timing."""
            gc.collect()  # Clean garbage before timing
            self.start_time = time.perf_counter()
        
        def stop(self):
            """Stop timing and record measurement."""
            self.end_time = time.perf_counter()
            duration = self.end_time - self.start_time
            self.measurements.append(duration)
            return duration
        
        def average_time(self):
            """Get average time from multiple measurements."""
            return sum(self.measurements) / len(self.measurements) if self.measurements else 0
        
        def min_time(self):
            """Get minimum time from measurements."""
            return min(self.measurements) if self.measurements else 0
        
        def reset(self):
            """Reset all measurements."""
            self.measurements = []
    
    return PerformanceTimer


@pytest.fixture
def memory_profiler():
    """Memory usage profiler."""
    try:
        import psutil
        import os
        
        class MemoryProfiler:
            def __init__(self):
                self.process = psutil.Process(os.getpid())
                self.initial_memory = None
                self.peak_memory = None
            
            def start_profiling(self):
                """Start memory profiling."""
                gc.collect()
                self.initial_memory = self.process.memory_info().rss
                self.peak_memory = self.initial_memory
            
            def record_peak(self):
                """Record current memory as peak if higher."""
                current = self.process.memory_info().rss
                if current > self.peak_memory:
                    self.peak_memory = current
            
            def get_memory_usage(self):
                """Get memory usage statistics."""
                current = self.process.memory_info().rss
                return {
                    'initial_mb': self.initial_memory / 1024 / 1024,
                    'current_mb': current / 1024 / 1024,
                    'peak_mb': self.peak_memory / 1024 / 1024,
                    'delta_mb': (current - self.initial_memory) / 1024 / 1024
                }
        
        return MemoryProfiler
        
    except ImportError:
        # Fallback if psutil not available
        class DummyMemoryProfiler:
            def start_profiling(self):
                pass
            def record_peak(self):
                pass  
            def get_memory_usage(self):
                return {'note': 'psutil not available for memory profiling'}
        
        return DummyMemoryProfiler


@pytest.fixture
def complexity_analyzer():
    """Analyzer for algorithmic complexity."""
    class ComplexityAnalyzer:
        def __init__(self):
            self.measurements = {}
        
        def measure_scaling(self, func, input_sizes, input_generator):
            """Measure how function scales with input size."""
            results = {}
            
            for size in input_sizes:
                test_input = input_generator(size)
                
                # Time multiple runs for accuracy
                times = []
                for _ in range(3):  # 3 runs minimum
                    gc.collect()
                    start = time.perf_counter()
                    func(test_input)
                    end = time.perf_counter()
                    times.append(end - start)
                
                results[size] = {
                    'min_time': min(times),
                    'avg_time': sum(times) / len(times),
                    'max_time': max(times)
                }
            
            return results
        
        def analyze_complexity(self, measurements):
            """Analyze complexity from measurements."""
            sizes = sorted(measurements.keys())
            times = [measurements[size]['avg_time'] for size in sizes]
            
            # Simple complexity estimation
            if len(sizes) < 3:
                return {'note': 'Need at least 3 data points for analysis'}
            
            # Check if quadratic O(n²)
            quadratic_fit = self._check_quadratic(sizes, times)
            # Check if linear O(n)
            linear_fit = self._check_linear(sizes, times)
            # Check if exponential O(2^n)
            exponential_fit = self._check_exponential(sizes, times)
            
            return {
                'linear_fit': linear_fit,
                'quadratic_fit': quadratic_fit,
                'exponential_fit': exponential_fit,
                'estimated_complexity': self._best_fit(linear_fit, quadratic_fit, exponential_fit)
            }
        
        def _check_linear(self, sizes, times):
            """Check linear fit quality."""
            # Simple correlation check
            if len(sizes) != len(times):
                return 0.0
                
            # Normalize and check proportionality
            normalized_sizes = [s / max(sizes) for s in sizes]
            normalized_times = [t / max(times) for t in times]
            
            correlation = sum(s * t for s, t in zip(normalized_sizes, normalized_times))
            return correlation / len(sizes)
        
        def _check_quadratic(self, sizes, times):
            """Check quadratic fit quality."""
            # Check if times grow roughly as squares of sizes
            squared_sizes = [s * s for s in sizes]
            return self._check_linear(squared_sizes, times)
        
        def _check_exponential(self, sizes, times):
            """Check exponential fit quality."""
            # This is a simplified check
            if len(sizes) < 2:
                return 0.0
            
            ratios = []
            for i in range(1, len(times)):
                if times[i-1] > 0:
                    ratios.append(times[i] / times[i-1])
            
            # If ratios are roughly constant, it's exponential
            if not ratios:
                return 0.0
            
            avg_ratio = sum(ratios) / len(ratios)
            variance = sum((r - avg_ratio) ** 2 for r in ratios) / len(ratios)
            
            # Lower variance means better exponential fit
            return 1.0 / (1.0 + variance)
        
        def _best_fit(self, linear, quadratic, exponential):
            """Determine best complexity fit."""
            fits = {
                'O(n)': linear,
                'O(n²)': quadratic, 
                'O(2^n)': exponential
            }
            return max(fits.items(), key=lambda x: x[1])[0]
    
    return ComplexityAnalyzer


@pytest.fixture
def benchmark_data_generator():
    """Generate test data of various sizes for benchmarks."""
    class BenchmarkDataGenerator:
        def __init__(self):
            self.generators = {}
        
        def register_generator(self, name, func):
            """Register a data generator."""
            self.generators[name] = func
        
        def generate_coxeter_types(self, max_rank):
            """Generate Coxeter types up to given rank."""
            types = []
            for rank in range(1, max_rank + 1):
                types.extend([
                    ['A', rank],
                    ['B', rank] if rank >= 2 else None,
                    ['C', rank] if rank >= 2 else None,
                    ['D', rank] if rank >= 4 else None
                ])
            return [t for t in types if t is not None]
        
        def generate_random_matrices(self, size):
            """Generate random matrices for stress testing."""
            import random
            matrices = []
            for _ in range(size):
                n = random.randint(2, 10)
                matrix = [[random.randint(-5, 5) for _ in range(n)] for _ in range(n)]
                # Make symmetric
                for i in range(n):
                    for j in range(i):
                        matrix[j][i] = matrix[i][j]
                matrices.append(matrix)
            return matrices
        
        def generate_scaling_inputs(self, base_generator, sizes):
            """Generate inputs of increasing size."""
            return {size: base_generator(size) for size in sizes}
    
    return BenchmarkDataGenerator


@pytest.fixture
def benchmark_reporter():
    """Generate benchmark reports."""
    class BenchmarkReporter:
        def __init__(self):
            self.results = {}
        
        def add_result(self, test_name, measurements):
            """Add benchmark result."""
            self.results[test_name] = measurements
        
        def generate_report(self):
            """Generate complete benchmark report."""
            report = []
            report.append("=" * 80)
            report.append("COXETER GROUP PERFORMANCE BENCHMARK REPORT")
            report.append("=" * 80)
            report.append("")
            
            for test_name, measurements in self.results.items():
                report.append(f"Test: {test_name}")
                report.append("-" * (6 + len(test_name)))
                
                if isinstance(measurements, dict):
                    for key, value in measurements.items():
                        if isinstance(value, float):
                            report.append(f"  {key}: {value:.6f}s")
                        else:
                            report.append(f"  {key}: {value}")
                else:
                    report.append(f"  Result: {measurements}")
                
                report.append("")
            
            return "\n".join(report)
        
        def save_report(self, filepath):
            """Save report to file."""
            with open(filepath, 'w') as f:
                f.write(self.generate_report())
    
    return BenchmarkReporter


@pytest.fixture
def performance_baselines():
    """Performance baselines for regression testing."""
    return {
        'gram_matrix_construction': {
            'A_2': {'max_time': 0.001},  # 1ms
            'B_5': {'max_time': 0.01},   # 10ms
            'E_8': {'max_time': 0.1}     # 100ms
        },
        'root_system_creation': {
            'A_10': {'max_time': 0.1},
            'D_20': {'max_time': 1.0}
        },
        'weyl_group_order_computation': {
            'A_5': {'max_time': 0.01},
            'B_6': {'max_time': 0.1},
            'E_8': {'max_time': 10.0}  # Can be slow for E₈
        }
    }


@pytest.fixture(autouse=True)
def benchmark_markers(request):
    """Automatically apply benchmark marker.""" 
    if not any(mark.name == 'benchmark' for mark in request.node.iter_markers()):
        pytest.fail("Benchmark tests must be marked with @pytest.mark.benchmark")
    yield


@pytest.fixture
def stress_test_runner():
    """Runner for stress tests."""
    class StressTestRunner:
        def __init__(self):
            self.failures = []
            self.successes = []
        
        def run_stress_test(self, func, inputs, max_failures=10):
            """Run function on many inputs, track failures."""
            failure_count = 0
            
            for i, inp in enumerate(inputs):
                try:
                    result = func(inp)
                    self.successes.append((i, inp, result))
                except Exception as e:
                    self.failures.append((i, inp, str(e)))
                    failure_count += 1
                    
                    if failure_count >= max_failures:
                        break
            
            return {
                'total_tests': len(self.successes) + len(self.failures),
                'successes': len(self.successes),
                'failures': len(self.failures),
                'failure_rate': len(self.failures) / (len(self.successes) + len(self.failures))
            }
    
    return StressTestRunner