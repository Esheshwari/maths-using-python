def solve_rk2_mixing_problem():
    
    # --- Define the differential equation ---
    def f(t, y):
        """dy/dt = 10 - y/20"""
        # The 't' parameter is not used, but we include it
        # for a standard function definition.
        return 10.0 - (y / 20.0)

    # --- Initial Conditions ---
    t = 0.0
    y = 0.0  # y(0) = 0 (pure water)
    h = 5.0  # Step size (minutes)
    
    # We need 3 steps to get from 0.0 to 15.0
    num_steps = 3
    
    # --- Iteration ---
    print("--- Solving Mixing Problem with RK2 (h=5) ---")
    print(f"Initial: y({t:.1f}) = {y:.6f} g")

    for i in range(num_steps):
        
        # 1. Calculate k1 (slope at the beginning)
        k1 = f(t, y)
        
        # 2. Calculate k2 (slope at the end)
        # We need the y-value at the end of the interval,
        # as predicted by a simple Euler step.
        y_temp_end = y + h * k1
        k2 = f(t + h, y_temp_end)
        
        # 3. Calculate new y (average the slopes)
        y_new = y + (h / 2.0) * (k1 + k2)
        
        # 4. Update t and y for the next loop
        t = t + h
        y = y_new
        
        # Print the result for this step
        print(f"Step {i+1}:   y({t:.1f}) = {y:.6f} g")
        
    print("---------------------------------------------")
    print(f"Final estimate: y(15.0) ≈ {y:.4f} g")

# Run the solver
if __name__ == "__main__":
    solve_rk2_mixing_problem()