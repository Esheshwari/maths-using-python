# Solve the following system using the Gauss–Seidel method up to Four decimal
# places:

# 4x − y + z = 7,
# −x + 5y + 2z = −8,
# 2x + y + 6z = 6.

# Take initial guesses x

# (0) = 0, y(0) = 0, z(0) = 0.

def solve_gauss_seidel():

    # Initial guess (k=0)
    x0 = 0.0
    y0 = 0.0
    z0 = 0.0
    
    # To store new values (k+1)
    x1, y1, z1 = 0.0, 0.0, 0.0
    
    # Tolerance for 4 decimal places
    tolerance = 0.00001
    max_iterations = 100 # Max iterations to prevent infinite loop
    
    
    print("Solving with Gauss-Seidel Method:")
    print("Iter. |     x     |     y     |     z")
    print("---------------------------------------------")
    # Print initial guess
    print(f"{0:5} | {x0:9.6f} | {y0:9.6f} | {z0:9.6f}")

    for i in range(1, max_iterations + 1):
        
        # 1. Calculate new x (x1) using old y (y0) and old z (z0)
        x1 = (7 + y0 - z0) / 4
        
        # 2. Calculate new y (y1) using NEW x (x1) and OLD z (z0)
        y1 = (-8 + x1 - 2*z0) / 5
        
        # 3. Calculate new z (z1) using NEW x (x1) and NEW y (y1)
        z1 = (6 - 2*x1 - y1) / 6
        
        # Print the results for this iteration
        print(f"{i:5} | {x1:9.6f} | {y1:9.6f} | {z1:9.6f}")
        
        # --- Check for Convergence ---
        # Find the maximum change between new and old values
        err_x = abs(x1 - x0)
        err_y = abs(y1 - y0)
        err_z = abs(z1 - z0)
        
        if max(err_x, err_y, err_z) < tolerance:
            print("\nConvergence reached.")
            break
            
        # --- Update "old" values for the next iteration ---
        x0 = x1
        y0 = y1
        z0 = z1
        
    else: 
        print(f"\nMax iterations ({max_iterations}) reached without convergence.")

    # --- Final Result ---
    print("\n--- Final Solution ---")
    print(f"x (raw) = {x1}")
    print(f"y (raw) = {y1}")
    print(f"z (raw) = {z1}")
    
    print("\nSolution rounded to 4 decimal places:")
    print(f"x = {x1:.4f}")
    print(f"y = {y1:.4f}")
    print(f"z = {z1:.4f}")

# Run the solver
if __name__ == "__main__":

    solve_gauss_seidel()
