def solve_newtons_cooling():

    # --- Parameters ---
    k = 0.07         # Cooling constant (per minute)
    T_ambient = 25.0 # Ambient temperature (C)
    h = 5.0          # Step size (minutes)
    
    # --- Initial Conditions ---
    t = 0.0
    T = 85.0        # Initial temperature (C)
    
    # --- Iteration ---
    print("--- Euler's Method for Newton's Cooling ---")
    print(f"Initial: T({t}) = {T}°C")
    print(f"Step size h = {h} minutes")
    print("---------------------------------------------")

    # Set how many steps you want to calculate
    num_steps = 3 

    for i in range(1, num_steps + 1):
        
        # 1. Calculate slope (derivative) at the current T
        # f(t, T) = -k * (T - T_ambient)
        slope = -k * (T - T_ambient)
        
        # 2. Calculate the change in T
        delta_T = h * slope
        
        # 3. Calculate the new T
        T_new = T + delta_T
        
        # 4. Update t
        t = t + h
        
        # Print the details for this step
        print(f"\nStep {i} (t = {t} min):")
        print(f"  Slope f(t, T) = -{k} * ({T:.4f} - {T_ambient}) = {slope:.4f}")
        print(f"  T_new = T + h * slope")
        print(f"  T_new = {T:.4f} + {h} * ({slope:.4f})")
        print(f"  T({t}) = {T_new:.4f}°C")
        
        # Update T for the next loop
        T = T_new
        
    print("---------------------------------------------")
    print("\nFinal estimations complete.")

# Run the solver
if __name__ == "__main__":
    solve_newtons_cooling()