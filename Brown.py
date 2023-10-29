import numpy as np
test_dict = {"height": 5}
if "Weight" not in test_dict:
    test_dict["Weight"] = np.NaN
print(test_dict)