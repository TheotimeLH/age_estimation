# IMPORT
import torch
import torch.nn as nn

# DATA LOADER
# -> 2 versions : 
# 1) full img
# 2) croped img
def loader(opt="croped"):
    pass

# CROPER MODEL


# TRAIN CROPER


# AGE ESTIM MODEL BASED ON CROPED

# -> regression
class our_regression(nn.Model):
    def __init__(self):
        super().__init__()

# -> classification
class our_classification(nn.Model):
    def __init__(self):
        super().__init__()

def get_model(name="our_classification"):
    match name:
        case "our_classification":
            return our_classification()
        case "our_regression":
            return our_regression()
        case default:
            pass # PRETRAINED

# TRAIN AGE ESTIM


# TEST 


# MAIN FUNCTION
# -> arg parse
