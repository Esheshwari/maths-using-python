def my_cos(x):
    # Pre-calculate powers and factorials
    x2 = x * x
    x4 = x2 * x2
    x6 = x4 * x2
    
    fact2 = 2.0
    fact4 = 24.0  # 4 * 3 * 2 * 1
    fact6 = 720.0 # 6 * 5 * 4 * 3 * 2 * 1
    
    # Calculate the series
    return 1.0 - (x2 / fact2) + (x4 / fact4) - (x6 / fact6)

def solve_rk2_no_lib():
    # --- Define the differential equation ---
    def f(x, y):
        """dy/dx = cos(x + y)"""
        return my_cos(x + y)

    # --- Initial Conditions ---
    x = 0.0
    y = 0.0
    h = 0.1
    
    # --- Iteration ---
    print("--- Solving y' = cos(x+y) with RK2 (h=0.1) ---")
    print(f"Initial: y({x:.1f}) = {y:.6f}")
    
    # We need 3 steps to get from 0.0 to 0.3
    for i in range(3):
        
        # 1. Calculate k1
        k1 = f(x, y)
        
        # 2. Calculate k2
        k2 = f(x + h, y + h * k1)
        
        # 3. Calculate new y (y_n+1)
        y_new = y + (h / 2.0) * (k1 + k2)
        
        # 4. Update x and y
        x = x + h
        y = y_new
        
        # Print the result for this step
        print(f"Step {i+1}:   y({x:.1f}) = {y:.6f}")
        
    print("---------------------------------------------")
    print(f"Final estimate: y(0.3) ≈ {y:.4f}")

# Run the solver
if __name__ == "__main__":
    solve_rk2_no_lib()