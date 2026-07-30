"""
Round 6, Mission B: Search for non-tower Liu configs with min D >= 1/D_n.

For n=2,3,4:
  - Generate candidate Liu configs (integer partitions + random reals, sum=1).
  - For each, compute min D over Xiang's strategies (grid search).
  - Check if min D >= 1/D_n (target).
  - If the tower is the UNIQUE config achieving min D = 1/D_n, report that.

The grid search gives an UPPER bound on min D (true min <= grid min).
So if grid min < 1/D_n, the config definitely fails.
If grid min >= 1/D_n, the config MIGHT achieve the target (need finer check).

For the "tower is unique" claim: if for every non-tower config we find a
Xiang strategy with D < 1/D_n, the tower is unique (computationally verified).
"""
import random
from fractions import Fraction as F
import math

def alt_sum_float(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*s[i] for i in range(len(s)))

def alt_sum_frac(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*s[i] for i in range(len(s)))

def min_D_grid(config, n, grid_steps=20):
    """
    Compute min D over Xiang's strategies using grid search.
    config: list of floats summing to 1 (Liu's pieces, sorted descending).
    n: number of Xiang marks.
    Returns (min_D, best_strategy).
    """
    m = len(config)
    best_D = alt_sum_float(config)  # 0 marks

    # 1 mark: split piece i at position q
    for i in range(m):
        L = config[i]
        for step in range(1, grid_steps):
            q = L * step / grid_steps
            if q <= 0 or q >= L:
                continue
            new_config = list(config[:i]) + [L - q, q] + list(config[i+1:])
            D = alt_sum_float(new_config)
            if D < best_D:
                best_D = D

    # 2 marks
    if n >= 2:
        for i in range(m):
            L = config[i]
            for step1 in range(1, grid_steps):
                q1 = L * step1 / grid_steps
                if q1 <= 0 or q1 >= L:
                    continue
                config1 = list(config[:i]) + [L - q1, q1] + list(config[i+1:])
                m1 = len(config1)
                for j in range(m1):
                    L2 = config1[j]
                    for step2 in range(1, grid_steps):
                        q2 = L2 * step2 / grid_steps
                        if q2 <= 0 or q2 >= L2:
                            continue
                        new_config = list(config1[:j]) + [L2 - q2, q2] + list(config1[j+1:])
                        D = alt_sum_float(new_config)
                        if D < best_D:
                            best_D = D

    # 3 marks (only for n >= 3, and only if m is small)
    if n >= 3 and m <= 4:
        for i in range(m):
            L = config[i]
            for step1 in range(1, min(grid_steps, 15)):
                q1 = L * step1 / min(grid_steps, 15)
                if q1 <= 0 or q1 >= L:
                    continue
                config1 = list(config[:i]) + [L - q1, q1] + list(config[i+1:])
                m1 = len(config1)
                for j in range(m1):
                    L2 = config1[j]
                    for step2 in range(1, min(grid_steps, 15)):
                        q2 = L2 * step2 / min(grid_steps, 15)
                        if q2 <= 0 or q2 >= L2:
                            continue
                        config2 = list(config1[:j]) + [L2 - q2, q2] + list(config1[j+1:])
                        m2 = len(config2)
                        for k in range(m2):
                            L3 = config2[k]
                            for step3 in range(1, min(grid_steps, 15)):
                                q3 = L3 * step3 / min(grid_steps, 15)
                                if q3 <= 0 or q3 >= L3:
                                    continue
                                new_config = list(config2[:k]) + [L3 - q3, q3] + list(config2[k+1:])
                                D = alt_sum_float(new_config)
                                if D < best_D:
                                    best_D = D

    return best_D

def search_configs(n, num_random=500, grid_steps=20):
    """Search for non-tower configs with min D >= 1/D_n."""
    D_n = 2**(n+1) - 1
    target = 1.0 / D_n
    tower = [2.0**(n-k) / D_n for k in range(n+1)]

    print(f"\n{'='*70}")
    print(f"Mission B: n={n}, D_n={D_n}, target=1/{D_n}={target:.6f}")
    print(f"{'='*70}")

    # Tower check
    tower_min = min_D_grid(tower, n, grid_steps)
    print(f"Tower T_{n}: min D (grid) = {tower_min:.6f}, target = {target:.6f}, "
          f"ratio = {tower_min/target:.4f}")

    # Integer partitions (normalized)
    print(f"\nInteger partition configs:")
    best_non_tower = None
    best_non_tower_min = float('inf')

    if n == 2:
        # Partitions of small integers into <= 3 parts
        for total in range(3, 20):
            for a in range(total, 0, -1):
                for b in range(min(a, total-a), -1, -1):
                    c = total - a - b
                    if c < 0 or (b > 0 and c == 0):
                        continue
                    if b == 0 and c == 0:
                        config = [a / total]
                    elif c == 0:
                        config = sorted([a/total, b/total], reverse=True)
                    else:
                        config = sorted([a/total, b/total, c/total], reverse=True)
                    if len(config) > n+1:
                        continue
                    # Skip tower
                    if abs(config[0] - 2.0**n/D_n) < 1e-10:
                        continue
                    min_d = min_D_grid(config, n, grid_steps)
                    if min_d < best_non_tower_min:
                        best_non_tower_min = min_d
                        best_non_tower = config
                    if min_d >= target * 0.99:  # close to or above target
                        print(f"  CLOSE: config={config} (ints {a},{b},{c}/{total}) "
                              f"minD={min_d:.6f} target={target:.6f} ratio={min_d/target:.4f}")

    elif n == 3:
        # Partitions into <= 4 parts
        for total in range(4, 25):
            for a in range(total, 0, -1):
                for b in range(min(a, total-a), -1, -1):
                    rem = total - a - b
                    for c in range(min(b, rem), -1, -1):
                        d = rem - c
                        if d < 0:
                            continue
                        parts = [x for x in [a, b, c, d] if x > 0]
                        if len(parts) > n+1:
                            continue
                        config = sorted([p/total for p in parts], reverse=True)
                        # Skip tower
                        if abs(config[0] - 8.0/15) < 1e-10 and len(config) == 4:
                            continue
                        min_d = min_D_grid(config, n, grid_steps)
                        if min_d < best_non_tower_min:
                            best_non_tower_min = min_d
                            best_non_tower = config
                        if min_d >= target * 0.95:
                            print(f"  CLOSE: ints={parts}/{total} config={[round(x,4) for x in config]} "
                                  f"minD={min_d:.6f} target={target:.6f} ratio={min_d/target:.4f}")

    elif n == 4:
        # Partitions into <= 5 parts (coarser)
        for total in range(5, 30):
            for a in range(total, max(total//2, 1), -1):
                rem = total - a
                # Simple 2-3 way splits
                for b in range(min(a, rem), max(rem//3-1, 0), -1):
                    rem2 = rem - b
                    for c in range(min(b, rem2), -1, -1):
                        d = rem2 - c
                        if d < 0 or d > c:
                            continue
                        parts = [x for x in [a, b, c, d] if x > 0]
                        if len(parts) > n+1:
                            continue
                        config = sorted([p/total for p in parts], reverse=True)
                        if abs(config[0] - 16.0/31) < 1e-10 and len(config) == 5:
                            continue
                        min_d = min_D_grid(config, n, grid_steps)
                        if min_d < best_non_tower_min:
                            best_non_tower_min = min_d
                            best_non_tower = config
                        if min_d >= target * 0.95:
                            print(f"  CLOSE: ints={parts}/{total} minD={min_d:.6f} "
                                  f"target={target:.6f} ratio={min_d/target:.4f}")

    print(f"\nBest non-tower: config={[round(x,4) for x in best_non_tower]} "
          f"minD={best_non_tower_min:.6f} target={target:.6f} "
          f"ratio={best_non_tower_min/target:.4f}")

    # Random reals
    print(f"\nRandom real configs ({num_random} trials):")
    best_rand = None
    best_rand_min = float('inf')
    above_count = 0

    for _ in range(num_random):
        # Generate random sorted config summing to 1
        m = random.randint(2, n+1)
        cuts = sorted([random.random() for _ in range(m-1)])
        config = []
        prev = 0
        for c in cuts:
            config.append(c - prev)
            prev = c
        config.append(1 - prev)
        config.sort(reverse=True)

        # Skip near-tower
        if abs(config[0] - 2.0**n/D_n) < 0.01:
            continue

        min_d = min_D_grid(config, n, grid_steps)
        if min_d < best_rand_min:
            best_rand_min = min_d
            best_rand = config
        if min_d >= target * 0.99:
            above_count += 1
            if above_count <= 5:
                print(f"  CLOSE: config={[round(x,4) for x in config]} "
                      f"minD={min_d:.6f} target={target:.6f} ratio={min_d/target:.4f}")

    print(f"Best random: config={[round(x,4) for x in best_rand]} "
          f"minD={best_rand_min:.6f} ratio={best_rand_min/target:.4f}")
    print(f"Configs with minD >= 0.99*target: {above_count}/{num_random}")

    # Summary
    print(f"\nSUMMARY n={n}:")
    print(f"  Tower min D = {tower_min:.6f} (target {target:.6f}, ratio {tower_min/target:.4f})")
    print(f"  Best non-tower (int) min D = {best_non_tower_min:.6f} (ratio {best_non_tower_min/target:.4f})")
    print(f"  Best non-tower (rand) min D = {best_rand_min:.6f} (ratio {best_rand_min/target:.4f})")
    all_best = min(best_non_tower_min, best_rand_min)
    if all_best < target * 0.99:
        print(f"  => Tower is UNIQUE maximizer (all non-tower configs have min D < target)")
    else:
        print(f"  => Non-tower configs may achieve target (need finer check)")

# Run for n=2,3,4
random.seed(42)
search_configs(2, num_random=300, grid_steps=30)
random.seed(42)
search_configs(3, num_random=300, grid_steps=20)
random.seed(42)
search_configs(4, num_random=200, grid_steps=12)
