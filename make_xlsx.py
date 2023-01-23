#!/usr/bin/env python
# coding: utf-8
#2020.1.14西野君ソースコードQlearn_and_run.pyを参考

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main(): 
    data = [[0.0, 0.0]]
    x = y = 0.0
    while True:
        x += 0.01
        y = np.sin(x) 
        data.append([x, y]) 
        if x >= 100:
            break

    df = pd.DataFrame(
        data, 
        columns=pd.Index(["x[m]", "y[m]"])
    )
    df.to_excel("test.xlsx")

main()
