import pandas as pd
import numpy as np


chat_id = 235789175 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    e = -17 + np.exp(1) 
    m1 = np.mean(x)  
    a = (m1 - e) / 10  
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return a
