import pyposelib
import numpy as np

a = pyposelib.Camera()
b = pyposelib.CameraPose(np.random.rand(4,1), np.random.rand(3,1))

hej = pyposelib.Image((b,a))

print(hej)