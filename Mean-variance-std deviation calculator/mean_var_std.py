import numpy as np

def calculate(nlist):
    try:
        matr = np.array(nlist).reshape(3,3)
    except:
        raise ValueError('List must contain nine numbers.')

    mean_x = matr.mean(axis = 0)
    mean_x_list = mean_x.tolist()
    mean_y = matr.mean(axis = 1)
    mean_y_list = mean_y.tolist()
    mean_all = matr.mean()
    
    var_x = matr.var(axis = 0)
    var_x_list = var_x.tolist()
    var_y = matr.var(axis = 1)
    var_y_list = var_y.tolist()
    var_all = matr.var()
    
    std_x = matr.std(axis = 0)
    std_x_list = std_x.tolist()
    std_y = matr.std(axis = 1)
    std_y_list = std_y.tolist()
    std_all = matr.std()
    
    max_x = matr.max(axis = 0)
    max_x_list = max_x.tolist()
    max_y = matr.max(axis = 1)
    max_y_list = max_y.tolist()
    max_all = matr.max()
    
    sum_x = matr.sum(axis = 0)
    sum_x_list = sum_x.tolist()
    sum_y = matr.sum(axis = 1)
    sum_y_list = sum_y.tolist()
    sum_all = matr.sum()
    
    min_x = matr.min(axis = 0)
    min_x_list = min_x.tolist()
    min_y = matr.min(axis = 1)
    min_y_list = min_y.tolist()
    min_all = matr.min()
    
    calculations = {
        'mean': [mean_x_list, mean_y_list, mean_all],
        'variance': [var_x_list, var_y_list, var_all],
        'standard deviation': [std_x_list, std_y_list, std_all],
        'max': [max_x_list, max_y_list, max_all],
        'min': [min_x_list, min_y_list, min_all],
        'sum': [sum_x_list, sum_y_list, sum_all]
    }
    
    return calculations