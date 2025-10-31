def solve_gauss_jacobi():
    
    # Initial guess (k=0)
    x0 = 0.0
    y0 = 0.0
    z0 = 0.0
    
    # Tolerance for 4 decimal places. 
    # We use 1e-5 (0.00001) to ensure the 4th place is stable.
    tolerance = 0.00001 #tolerance is the stopping condition for the iterative method.
    
    # Max iterations to prevent an infinite loop
    max_iterations = 100
    
    # --- Iteration ---
    
    print("Solving with Gauss-Jacobi Method:")
    print("Iteration |     x     |     y     |     z")
    print("-------------------------------------------------")
    # Print initial guess
    print(f"{0:9} | {x0:9.6f} | {y0:9.6f} | {z0:9.6f}")

    for i in range(1, max_iterations + 1):
        
        # Calculate new values (k+1) using old values (k)
        x1 = (20 + 2*y0 - z0) / 8
        y1 = (-10 - x0 + 3*z0) / 7
        z1 = (30 - 2*x0 - y0) / 9
        
        # Print the results for this iteration
        print(f"{i:9} | {x1:9.6f} | {y1:9.6f} | {z1:9.6f}")
        
        # --- Check for Convergence ---
        # Calculate the absolute difference (error)
        err_x = abs(x1 - x0)
        err_y = abs(y1 - y0)
        err_z = abs(z1 - z0)
        
        # Find the maximum error
        max_err = max(err_x, err_y, err_z)
        
        if max_err < tolerance:
            print("\nConvergence reached.")
            break
            
        # --- Update for Next Iteration ---
        # The new values become the "old" values for the next loop
        x0 = x1
        y0 = y1
        z0 = z1
        
    else: 
        # This 'else' block runs if the 'for' loop completes without 'break'
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
    solve_gauss_jacobi()