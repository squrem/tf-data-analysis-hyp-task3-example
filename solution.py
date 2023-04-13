import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 434559054 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
  if ttest_ind(x, y, equal_var=False, alternative="less").pvalue < 0.03:
    return True
  else:
    return False  
