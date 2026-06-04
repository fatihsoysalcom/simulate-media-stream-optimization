import time
import random

def generate_high_res_data(length=1000, max_value=255):
    """Simulates a high-resolution data stream (e.g., pixel values or audio samples)."""
    print(f"Generating high-resolution data stream of {length} samples...")
    data = [random.randint(0, max_value) for _ in range(length)]
    print(f"Original data size: {len(data)} units.")
    return data

def optimize_data_stream(high_res_data, optimization_factor=4):
    """
    Simulates an optimization algorithm by downsampling the data.
    This reduces data size (bandwidth) but also detail (quality trade-off).
    This represents Opticast's 'benzersiz optimizasyon algoritmaları' (unique optimization algorithms)
    aiming to 'bant genişliği kullanımını minimize ederken kaliteyi maksimize etmeyi' (minimize bandwidth while maximizing quality).
    """
    print(f"\nApplying optimization (downsampling by factor {optimization_factor})...")
    optimized_data = []
    for i in range(0, len(high_res_data), optimization_factor):
        chunk = high_res_data[i:i + optimization_factor]
        if chunk:
            # Simple average as a form of downsampling/compression
            optimized_data.append(sum(chunk) // len(chunk))
    print(f"Optimized data size: {len(optimized_data)} units.")
    return optimized_data

def simulate_streaming(data, stream_name="Data", delay_per_unit=0.0001):
    """Simulates sending data chunks over a network, illustrating latency."""
    print(f"Simulating streaming of '{stream_name}' data...")
    start_time = time.time()
    for i, unit in enumerate(data):
        # In a real streaming platform like Opticast, this would involve network packet transmission.
        # Here, we simulate the time taken to process/send each unit.
        time.sleep(delay_per_unit)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Finished streaming '{stream_name}' data in {duration:.4f} seconds.")
    return duration

if __name__ == "__main__":
    # Define stream parameters for the simulation
    STREAM_LENGTH = 5000 # Number of data points in the stream (e.g., frames, samples)
    MAX_VALUE = 255      # Max value for a data point (e.g., 8-bit pixel intensity)
    OPTIMIZATION_FACTOR = 5 # How much to downsample (e.g., 5 original units become 1 optimized unit)
    DELAY_PER_UNIT = 0.00005 # Simulate network latency per data unit (lower for faster demo)

    print("--- Opticast Stream Optimization Simulation ---")

    # 1. Generate high-resolution data, representing raw media content.
    high_res_stream = generate_high_res_data(STREAM_LENGTH, MAX_VALUE)

    # 2. Optimize the data stream using a simulated algorithm.
    optimized_stream = optimize_data_stream(high_res_stream, OPTIMIZATION_FACTOR)

    # 3. Simulate streaming both versions to compare performance.
    print("\n--- Streaming High-Resolution Data ---")
    high_res_duration = simulate_streaming(high_res_stream, "High-Res", DELAY_PER_UNIT)

    print("\n--- Streaming Optimized Data ---")
    optimized_duration = simulate_streaming(optimized_stream, "Optimized", DELAY_PER_UNIT)

    # 4. Compare results to demonstrate the benefits of optimization.
    print("\n--- Comparison ---")
    original_size = len(high_res_stream)
    optimized_size = len(optimized_stream)
    bandwidth_saving_percent = ((original_size - optimized_size) / original_size) * 100

    print(f"Original stream size: {original_size} units")
    print(f"Optimized stream size: {optimized_size} units")
    print(f"Simulated bandwidth saving: {bandwidth_saving_percent:.2f}%")
    print(f"Time to stream original: {high_res_duration:.4f} seconds")
    print(f"Time to stream optimized: {optimized_duration:.4f} seconds")

    # Emphasize the core concept from the article.
    print("\nThis simulation demonstrates how Opticast's technical approach aims to")
    print("reduce data size and streaming time, crucial for 'düşük gecikmeyle' (low latency)")
    print("and 'bant genişliği kullanımını minimize' (minimize bandwidth usage) streaming.")
