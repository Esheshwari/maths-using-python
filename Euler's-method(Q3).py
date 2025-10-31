def my_exp(x):
    # Factorials
    fact2 = 2 * 1
    fact3 = 3 * 2 * 1
    fact4 = 4 * 3 * 2 * 1
    
    # Powers
    x2 = x * x
    x3 = x2 * x
    x4 = x3 * x
    
    return 1 + x + (x2 / fact2) + (x3 / fact3) + (x4 / fact4)

def my_log1p(y):

    # Powers
    y2 = y * y
    y3 = y2 * y
    y4 = y3 * y
    
    return y - (y2 / 2) + (y3 / 3) - (y4 / 4)

def solve_euler_no_lib():
    
    # Define the derivative function dy/dx = f(x, y)
    def f(x, y):
        """The differential equation: e^x - ln(1+y)"""
        # Use our custom-built functions
        return my_exp(x) - my_log1p(y)

    # --- Initial Conditions ---
    x = 0.0
    y = 0.0
    h = 0.1  # Step size
    
    # --- Iteration ---
    print("--- Euler's Method Calculation (No Libraries) ---")
    print(f"h = {h}, y(0) = {y}")
    print("-----------------------------------------------------------------")
    print("  x_n  |    y_n     |  Slope f(x_n, y_n) | h*f(x,y) |   y_{n+1}")
    print("-----------------------------------------------------------------")
    
    results = {} # To store intermediate results

    for i in range(3):
        
        # Calculate the slope at the current point
        slope = f(x, y)
        
        # Calculate the change in y (delta_y)
        delta_y = h * slope
        
        # Calculate the new y
        y_new = y + delta_y
        
        # Print the details for this step
        print(f" {x:5.1f} | {y:10.6f} | {slope:18.6f} | {delta_y:8.6f} | {y_new:10.6f}")
        
        # Update x and y for the next iteration
        y = y_new
        x = x + h
        
        # Store the result
        results[round(x, 1)] = y
        
    print("-----------------------------------------------------------------")
    print(f"\nFinal estimate: y({x:.1f}) ≈ {y:.6f}")
    
    print("\n--- Summary of Results (rounded to 4 decimal places) ---")
    print(f"y(0.1) ≈ {results[0.1]:.4f}")
    print(f"y(0.2) ≈ {results[0.2]:.4f}")
    print(f"y(0.3) ≈ {results[0.3]:.4f}")

# Run the solver
if __name__ == "__main__":
    solve_euler_no_lib()