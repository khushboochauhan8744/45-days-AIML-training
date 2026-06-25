import matplotlib.pyplot as plt

# Loss function and its gradient
def get_loss(theta):
    return (theta - 3.5)**2 + 1

def get_gradient(theta):
    return 2 * (theta - 3.5)

# Simplified simulator function
def run_gradient_descent(learning_rate):
    theta = 0.0 # Start at random value 0
    loss_history = []
    
    # Run for 12 steps
    for step in range(13):
        loss = get_loss(theta)
        grad = get_gradient(theta)
        
        # Only print the step values for the optimal learning rate (0.4)
        if learning_rate == 0.4:
            print(f"Step {step}: Theta = {theta:.3f}, Loss = {loss:.3f}, Gradient = {grad:.3f}")
            
        loss_history.append(loss)
        
        # Update equation
        theta = theta - (learning_rate * grad)
        
    return loss_history

print("--- Step-by-Step Table for Learning Rate 0.4 ---")
history_low = run_gradient_descent(0.1)
history_good = run_gradient_descent(0.4)
history_high = run_gradient_descent(1.1)

# Plotting the loss results
plt.figure()
plt.plot(history_low, label="Low LR (0.1)", marker="o")
plt.plot(history_good, label="Good LR (0.4)", marker="s")
plt.plot(history_high, label="Too High LR (1.1)", marker="x")

plt.title("Task 2: Learning Rate Comparison")
plt.xlabel("Iteration Step")
plt.ylabel("Loss Value")
plt.grid(True)
plt.legend()
plt.show()