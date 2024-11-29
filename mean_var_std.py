import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    np_list = np.array(list).reshape(3,3)

    calculations = {
        'mean' : [
            np_list.mean(axis=0).tolist(),   
            np_list.mean(axis=1).tolist(),  
            np_list.mean()
        ],
        'variance' : [
            np_list.var(axis=0).tolist(),    
            np_list.var(axis=1).tolist(),   
            np_list.var()
        ],
        'standard deviation' : [
            np_list.std(axis=0).tolist(),    
            np_list.std(axis=1).tolist(),   
            np_list.std()
        ],
        'max' : [
            np_list.max(axis=0).tolist(),    
            np_list.max(axis=1).tolist(),   
            np_list.max()
        ],
        'min' : [
            np_list.min(axis=0).tolist(),    
            np_list.min(axis=1).tolist(),   
            np_list.min()
        ],
        'sum' : [
            np_list.sum(axis=0).tolist(),    
            np_list.sum(axis=1).tolist(),   
            np_list.sum()
        ]
    }


    return calculations