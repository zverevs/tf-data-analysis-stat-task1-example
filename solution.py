import pandas as pd
import numpy as np


chat_id = 235789175 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = len(x)
    
    sample_mean = np.mean(x)

    lambda_ = 1 / (sample_mean - 17)
    
    a = lambda_ * (1 - np.exp(-10*lambda_)) 
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return a
