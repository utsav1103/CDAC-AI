import numpy as np 

arr = np.array([50,20,80,10,40])

#normal sorting
print(np.sort(arr))

# sorting in descending order
print(np.sort(arr)[::-1])

# reshaping array
a = np.array([1,2,3,4,5,6])

new_a = a.reshape(2,3)

print(new_a)

#NumPy can automatically calculate one dimension.
print(a.reshape(2, -1))


#Flattening converts a multidimensional array into a 1D array
b = np.array([[1, 2, 3],
                [4, 5, 6]])

print(b.flatten())


#4. Joining arrays
#Joining means combining two or more arrays 
#concatenate = combines arrays along a specified axis.

a1 = np.array([1, 2, 3])
b1 = np.array([4, 5, 6])

print(np.concatenate((a1, b1)))

#B. np.vstack() — Vertical joining
print(np.vstack((a1, b1)))


#np.hstack() — Horizontal joining
print(np.hstack((a1, b1)))


#5. Splitting arrays
#Splitting divides one array into multiple smaller arrays

ar = np.array([10, 20, 30, 40, 50, 60])

result = np.split(ar, 3)

print(result)

#You can also split at specific indices:
print(np.split(ar, [2, 4]))


val = np.array([10,20,np.nan,40,np.nan,60])
print(np.isnan(val))
print(np.isnan(val).sum())
print(np.nanmean(val))