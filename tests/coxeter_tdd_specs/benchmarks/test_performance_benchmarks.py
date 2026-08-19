"""
Performance benchmarks for Coxeter implementations.

Measures execution time and complexity characteristics.
"""

import pytest


@pytest.mark.benchmark
@pytest.mark.very_slow
@pytest.mark.performance
@pytest.mark.not_implemented
class TestGramMatrixPerformance:
    """Benchmark GramMatrix construction and operations."""
    
    def test_gram_matrix_construction_scaling(self, performance_timer, complexity_analyzer, benchmark_data_generator):
        """Benchmark GramMatrix construction scaling."""
        try:
            from coxeter_matrices import GramMatrix
            
            timer = performance_timer()
            analyzer = complexity_analyzer()
            generator = benchmark_data_generator()
            
            # Generate test cases of increasing rank
            input_sizes = [2, 3, 4, 5, 6, 7, 8]
            
            def input_generator(rank):
                return ['A', rank]
            
            def construction_func(coxeter_type):
                return GramMatrix.from_coxeter_type(coxeter_type)
            
            # Measure scaling
            measurements = analyzer.measure_scaling(
                construction_func, 
                input_sizes, 
                input_generator
            )
            
            # Analyze complexity
            complexity_analysis = analyzer.analyze_complexity(measurements)
            
            # Construction should be at most O(n²) for rank n
            estimated_complexity = complexity_analysis['estimated_complexity']
            assert estimated_complexity in ['O(n)', 'O(n²)'], \
                f"GramMatrix construction too slow: {estimated_complexity}"
            
            # Check absolute performance
            for size, timing in measurements.items():
                if size <= 5:  # Small cases should be very fast
                    assert timing['avg_time'] < 0.01, \
                        f"A{size} construction too slow: {timing['avg_time']:.4f}s"
                
        except ImportError:
            pytest.skip("Implementation not yet available")
    
    def test_gram_matrix_determinant_performance(self, performance_timer, performance_baselines):
        """Benchmark determinant calculation performance."""
        try:
            from coxeter_matrices import GramMatrix
            
            timer = performance_timer()
            baselines = performance_baselines['gram_matrix_construction']
            
            for coxeter_type_key, baseline in baselines.items():
                # Parse type from key (e.g., 'A_2' -> ['A', 2])
                parts = coxeter_type_key.split('_')
                coxeter_type = [parts[0], int(parts[1])]
                
                # Create Gram matrix
                gram = GramMatrix.from_coxeter_type(coxeter_type)
                
                # Time determinant calculation
                timer.start()
                det = gram.determinant()
                duration = timer.stop()
                
                # Check against baseline
                max_time = baseline['max_time']
                assert duration < max_time, \
                    f"{coxeter_type} determinant too slow: {duration:.4f}s > {max_time}s"
                
        except ImportError:
            pytest.skip("Implementation not yet available")


@pytest.mark.benchmark
@pytest.mark.very_slow
@pytest.mark.performance
@pytest.mark.not_implemented
class TestWeylGroupPerformance:
    """Benchmark Weyl group operations."""
    
    def test_weyl_group_order_computation_scaling(self, complexity_analyzer):
        """Benchmark Weyl group order computation scaling."""
        try:
            from weyl_groups import WeylGroup
            
            analyzer = complexity_analyzer()
            
            # Test A_n series scaling
            input_sizes = [2, 3, 4, 5, 6]
            
            def input_generator(rank):
                return ['A', rank]
            
            def order_computation(coxeter_type):
                wg = WeylGroup.from_coxeter_type(coxeter_type)
                return wg.order
            
            measurements = analyzer.measure_scaling(
                order_computation,
                input_sizes,
                input_generator
            )
            
            # Order computation should be reasonable
            complexity_analysis = analyzer.analyze_complexity(measurements)
            
            # Should not be exponential for reasonable sizes
            estimated_complexity = complexity_analysis['estimated_complexity']
            assert estimated_complexity != 'O(2^n)', \
                f"Weyl group order computation too slow: {estimated_complexity}"
            
        except ImportError:
            pytest.skip("Implementation not yet available")
    
    def test_weyl_group_element_enumeration_performance(self, performance_timer):
        """Benchmark Weyl group element enumeration."""
        try:
            from weyl_groups import WeylGroup
            
            timer = performance_timer()
            
            # Test enumeration for various types
            test_cases = [
                (['A', 3], 24),   # S₄
                (['B', 3], 48),   # Hyperoctahedral 
                (['G', 2], 12)    # Dihedral D₆
            ]
            
            for coxeter_type, expected_order in test_cases:
                wg = WeylGroup.from_coxeter_type(coxeter_type)
                
                # Time element enumeration
                timer.start()
                elements = list(wg.elements)
                duration = timer.stop()
                
                # Verify correctness
                assert len(elements) == expected_order
                
                # Check performance (should be reasonable for small groups)
                if expected_order <= 100:
                    assert duration < 1.0, \
                        f"{coxeter_type} enumeration too slow: {duration:.4f}s"
                
        except ImportError:
            pytest.skip("Implementation not yet available")


@pytest.mark.benchmark
@pytest.mark.very_slow
@pytest.mark.performance
@pytest.mark.stress_test
@pytest.mark.not_implemented
class TestStressTests:
    """Stress tests for robustness and performance limits."""
    
    def test_large_rank_stress_test(self, stress_test_runner, benchmark_data_generator):
        """Stress test with large rank Coxeter groups."""
        try:
            from coxeter_matrices import GramMatrix
            
            runner = stress_test_runner()
            generator = benchmark_data_generator()
            
            # Generate large rank test cases
            large_ranks = list(range(10, 21))  # Ranks 10-20
            test_inputs = []
            
            for rank in large_ranks:
                # Only test A_n series for large ranks (others get very large)
                test_inputs.append(['A', rank])
                
                # Maybe a few B_n for comparison
                if rank <= 15:  # B_n grows faster
                    test_inputs.append(['B', rank])
            
            def construction_test(coxeter_type):
                """Test construction doesn't crash or take too long."""
                gram = GramMatrix.from_coxeter_type(coxeter_type)
                det = gram.determinant()  # Also test determinant
                return {'rank': gram.rank, 'determinant': det}
            
            # Run stress test
            results = runner.run_stress_test(
                construction_test, 
                test_inputs, 
                max_failures=5
            )
            
            # Should have reasonable success rate
            assert results['failure_rate'] < 0.1, \
                f"Too many failures in stress test: {results['failure_rate']:.2%}"
            
            print(f"Stress test results: {results['successes']}/{results['total_tests']} passed")
            
        except ImportError:
            pytest.skip("Implementation not yet available")
    
    def test_random_matrix_robustness(self, stress_test_runner, benchmark_data_generator):
        """Test robustness with random (potentially invalid) matrices."""
        try:
            from coxeter_matrices import GramMatrix
            
            runner = stress_test_runner()
            generator = benchmark_data_generator()
            
            # Generate random matrices
            random_matrices = generator.generate_random_matrices(100)
            
            def validation_test(matrix_data):
                """Test that validation properly rejects invalid matrices."""
                try:
                    gram = GramMatrix(matrix_data)
                    return {'valid': True, 'determinant': gram.determinant()}
                except ValueError as e:
                    return {'valid': False, 'error': str(e)}
            
            # Run robustness test
            results = runner.run_stress_test(validation_test, random_matrices)
            
            # Most random matrices should be rejected (invalid)
            # The few that pass should be handled correctly
            print(f"Robustness test: {results['successes']} valid, {results['failures']} invalid")
            
            # Should not crash on any input
            assert results['total_tests'] == 100, "Some tests didn't complete"
            
        except ImportError:
            pytest.skip("Implementation not yet available")


@pytest.mark.benchmark
@pytest.mark.slow
@pytest.mark.performance
@pytest.mark.memory
@pytest.mark.not_implemented
class TestMemoryBenchmarks:
    """Memory usage benchmarks."""
    
    def test_gram_matrix_memory_usage(self, memory_profiler):
        """Benchmark GramMatrix memory usage."""
        try:
            from coxeter_matrices import GramMatrix
            
            profiler = memory_profiler()
            profiler.start_profiling()
            
            # Create many Gram matrices
            matrices = []
            for rank in range(1, 11):  # A₁ through A₁₀
                gram = GramMatrix.from_coxeter_type(['A', rank])
                matrices.append(gram)
                profiler.record_peak()
            
            # Memory usage should scale reasonably
            memory_stats = profiler.get_memory_usage()
            
            # Should not use excessive memory for small matrices
            assert memory_stats['delta_mb'] < 100, \
                f"Excessive memory usage: {memory_stats['delta_mb']:.2f} MB"
            
            print(f"Memory usage for A₁-A₁₀: {memory_stats['delta_mb']:.2f} MB")
            
        except ImportError:
            pytest.skip("Implementation not yet available")
    
    def test_weyl_group_memory_scaling(self, memory_profiler):
        """Benchmark Weyl group memory scaling."""
        try:
            from weyl_groups import WeylGroup
            
            profiler = memory_profiler()
            profiler.start_profiling()
            
            # Create Weyl groups of increasing size
            groups = []
            for rank in [2, 3, 4, 5]:  # Don't go too high
                wg = WeylGroup.from_coxeter_type(['A', rank])
                groups.append(wg)
                profiler.record_peak()
            
            memory_stats = profiler.get_memory_usage()
            
            # Memory should scale reasonably with group order
            print(f"Memory usage for A₂-A₅ Weyl groups: {memory_stats['delta_mb']:.2f} MB")
            
            # For A₅ (120 elements), should not use excessive memory
            assert memory_stats['delta_mb'] < 50, \
                f"Excessive memory for Weyl groups: {memory_stats['delta_mb']:.2f} MB"
            
        except ImportError:
            pytest.skip("Implementation not yet available")


@pytest.mark.benchmark
@pytest.mark.slow
@pytest.mark.performance
@pytest.mark.regression
@pytest.mark.not_implemented
class TestPerformanceRegression:
    """Performance regression tests."""
    
    def test_performance_regression_baseline(self, performance_timer, benchmark_reporter):
        """Test performance doesn't regress from baseline."""
        try:
            from coxeter_matrices import GramMatrix
            from weyl_groups import WeylGroup
            
            timer = performance_timer()
            reporter = benchmark_reporter()
            
            # Baseline test cases
            baseline_tests = [
                ('gram_A5', lambda: GramMatrix.from_coxeter_type(['A', 5])),
                ('gram_E8', lambda: GramMatrix.from_coxeter_type(['E', 8])), 
                ('weyl_A4', lambda: WeylGroup.from_coxeter_type(['A', 4])),
                ('weyl_B3', lambda: WeylGroup.from_coxeter_type(['B', 3]))
            ]
            
            for test_name, test_func in baseline_tests:
                # Run multiple times for accuracy
                times = []
                for _ in range(5):
                    timer.start()
                    result = test_func()
                    duration = timer.stop()
                    times.append(duration)
                
                # Record results
                measurements = {
                    'min_time': min(times),
                    'avg_time': sum(times) / len(times),
                    'max_time': max(times)
                }
                reporter.add_result(test_name, measurements)
            
            # Generate performance report
            report = reporter.generate_report()
            print(report)
            
            # Could save to file for CI comparison
            # reporter.save_report('benchmark_results.txt')
            
        except ImportError:
            pytest.skip("Implementation not yet available")