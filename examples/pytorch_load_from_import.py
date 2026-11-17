from torch import load
from torch.serialization import load as serialization_load

# from-import form without weights_only (should trigger B614)
model = load('model_weights.pth')

# aliased torch.serialization.load from-import (should trigger B614)
model2 = serialization_load('model_weights.pth')

# safe: weights_only=True (should NOT trigger B614)
model3 = load('model_weights.pth', weights_only=True)
