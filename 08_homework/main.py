import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_classification

# 1
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=6,
    n_classes=2,
    random_state=42
)
# df = pd.read_csv("heart.csv")

df = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(10)])
df["target"] = y

X = df.drop("target", axis=1)
y = df["target"]
print(y.value_counts(normalize=True))

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train = torch.FloatTensor(X_train)
X_test = torch.FloatTensor(X_test)

y_train = torch.FloatTensor(y_train.values).view(-1, 1)
y_test = torch.FloatTensor(y_test.values).view(-1, 1)

# 2
input_size = X_train.shape[1]

model = nn.Sequential(
    nn.Linear(input_size, 16),
    nn.ReLU(),

    nn.Linear(16, 8),
    nn.ReLU(),

    nn.Linear(8, 1),
    nn.Sigmoid()
)

# 3
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

epochs = 30

loss_history = []
accuracy_history = []
for epoch in range(epochs):
    model.train()

    outputs = model(X_train)
    loss = criterion(outputs, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    preds = (outputs.detach().numpy() > 0.5).astype(int)
    acc = accuracy_score(y_train.numpy(), preds)

    loss_history.append(loss.item())
    accuracy_history.append(acc)

    print(f"Epoch {epoch+1}/{epochs} | Loss: {loss.item():.4f} | Accuracy: {acc:.4f}")
    
model.eval()

with torch.no_grad():
    test_outputs = model(X_test)
    test_loss = criterion(test_outputs, y_test).item()

    test_preds = (test_outputs.numpy() > 0.5).astype(int)
    test_acc = accuracy_score(y_test.numpy(), test_preds)

print("\n📌 Final Metrics:")
print(f"Loss: {test_loss:.4f}")
print(f"Accuracy: {test_acc:.4f}")
          
# 4
import matplotlib.pyplot as plt
plt.figure()
plt.plot(loss_history, label="Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Loss over epochs")
plt.legend()
plt.savefig("loss_healthrisk_mlp.png")
plt.show()

plt.figure()
plt.plot(accuracy_history, label="Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("Accuracy over epochs")
plt.legend()
plt.savefig("accuracy_healthrisk_mlp.png")
plt.show()