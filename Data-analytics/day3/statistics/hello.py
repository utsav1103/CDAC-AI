import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


print("hello")
ages = np.random.randint(18, 81, size=500)
print("ages : " ,ages,sep="\t:\t")
print("mode of ages :",stats.mode(ages), sep="\t:\t")