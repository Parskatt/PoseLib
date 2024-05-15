from enum import Enum
from pyposelib.poselib import *



class LossType(Enum):
    TRIVIAL = 0
    TRUNCATED = 1
    HUBER = 2
    CAUCHY = 3
    # This is the TR-IRLS scheme from Le and Zach, 3DV 2021
    TRUNCATED_LE_ZACH = 4