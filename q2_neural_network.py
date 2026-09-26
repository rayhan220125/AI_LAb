x = 2
w = 1
b = 0
lr = 0.1

# Actual value
y_true = x**2 + 1

# Forward pass
z = w*x + b
y_pred = max(0, z)

# Error and loss
error = y_pred - y_true
loss = 0.5 * error**2

# Backward pass
relu_grad = 1 if z > 0 else 0
dw = error * relu_grad * x
db = error * relu_grad

# Update
w = w - lr * dw
b = b - lr * db

# New prediction
y_pred_new = max(0, w*x + b)

print("Actual y =", y_true)
print("Old prediction =", y_pred)
print("Error =", error)
print("Loss =", loss)
print("Updated weight =", w)
print("Updated bias =", b)
print("New prediction =", y_pred_new)
