from datasets import load_dataset
from PIL import Image
import random

# Stream the dataset
dataset = load_dataset("szili2011/captcha-ocr-dataset", streaming=True, split="train")

# Take a random subset (e.g., 250k samples)
subset_size = 250_000
sampled_data = []

for i, sample in enumerate(dataset.shuffle(seed=42)):
    if i >= subset_size:
        break
    img = sample["image"]  # PIL Image
    label = sample["text"] # Ground truth text
    sampled_data.append((img, label))

# Now 'sampled_data' can be wrapped into a PyTorch Dataset for training
print(f"Collected {len(sampled_data)} samples")
