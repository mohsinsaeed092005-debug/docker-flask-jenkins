import json
import random


def load_data(n=100, seed=42):
    """Step 1 - Data: synthetic data banao (y = 2x + 1 + noise)."""
    random.seed(seed)  # seed fixed = result reproducible
    data = []
    for _ in range(n):
        x = random.uniform(0, 10)
        y = 2 * x + 1 + random.uniform(-0.5, 0.5)
        data.append((x, y))
    return data


def train(data):
    """Step 2 - Training: simple linear regression (least squares)."""
    n = len(data)
    mean_x = sum(x for x, _ in data) / n
    mean_y = sum(y for _, y in data) / n
    w = sum((x - mean_x) * (y - mean_y) for x, y in data) / sum(
        (x - mean_x) ** 2 for x, _ in data
    )
    b = mean_y - w * mean_x
    return {"w": w, "b": b}  # Step 3 - Model


def predict(model, x):
    return model["w"] * x + model["b"]


def evaluate(model, data):
    """Step 4 - Testing: Mean Squared Error."""
    return sum((predict(model, x) - y) ** 2 for x, y in data) / len(data)


def save_model(model, path="model.json"):
    """Model ko file mein save karo (versioning ke liye)."""
    with open(path, "w") as f:
        json.dump(model, f)


if __name__ == "__main__":
    data = load_data()
    split = int(0.8 * len(data))
    train_data, test_data = data[:split], data[split:]

    model = train(train_data)
    mse = evaluate(model, test_data)

    print(f"Model: w={model['w']:.3f}, b={model['b']:.3f}")
    print(f"Test MSE: {mse:.4f}")

    assert mse < 1.0, "Model quality kharab hai, deploy nahi hoga"
    save_model(model)
    print("Model saved to model.json")