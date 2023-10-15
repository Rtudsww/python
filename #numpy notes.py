# dot product

'''def crop_yield(region,weights):
    crop_yield=0
    for i,j in zip(region,weights):
        crop_yield=crop_yield + i*j
    print(crop_yield)

khan=[12,2,3]
wd=[22,2,2]
dds=[23,4,2]

w1=[0.2,0.1,0.1]

crop_yield(khan,w1)

'''
import numpy as np

###help(np.dot)


khan=np.array([12,2,3])
wd=np.array([22,2,2])

w1=np.array([0.2,0.1,0.1])

print(np.dot(khan,w1))

##element wise multiplication --
print(w1*khan)

##dot product 
print((w1*khan).sum())


# MULTI DIMENSIONAL NUMPY ARRAY--
##2d array
### column1-temp, c2-humidity, c3-rain
climate_data=np.array([[1,2,3],
                      [12,3,4],
                      [4,3,2],
                      [2,3,4]])#data for different regions

print('the shape of climate_data is::',climate_data.shape)#give the dimensions of the array
print('the shape of the w1 is::',w1.shape)

##3d array
arr3=np.array([[[1,2,3],
                [1,2,3]],
               
               [[2,3,4],
                [3,4,5.5]]])

print(arr3)
print(arr3.shape)
print(arr3.dtype)# to check the data type of the elements.


## matrix multiplication ( cross product)
print("climate_data @ w1",np.matmul(climate_data,w1))
print("climate_data @ w1",climate_data  @ w1)
print("climate_data @ w1 shape",(climate_data @ w1 ).shape)
print("order=4,1",(climate_data@w1).reshape(4,1))
print("order=1,4",(climate_data@w1).reshape(1,4))#the shape of climate_data is (4,1) but after matmul it gives it shape as (4,) i.e. not acceptable for further  calculations 
# so we need to reshape it for futher use

#WORKING WITH THE CSV DATA FILES---

### to import the webpage or download a file we use urllib.request
import urllib.request as ub

'''ub.urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/08/climate.csv','climate.txt')'''
#in the argument we give the url or the path of the file ton be downloaded and 
# the second is the name of the file or the path of the file where we want to download it.
#file is not found so it throws an error.
'''

climate_data_downloaded=np.genfromtxt('climate.txt',delimiter=',',skip_header=1)#to convert array from text
#delimiter is the character by which we want to separate or data.
# skip_header -- skips the line 1
print(climate_data_downloaded)
 '''


# concatenate and split
arr4=np.array([[[1,2,3],
              [1,2,3]],
              
              [[1,3,4],
               [2,3,4]]])
concat=np.concatenate([arr3,arr4],axis=2)#we need to provide the lists or arrays that  we need to concatenate as list in the argument 
#and also provide the direction or the dimension in which we want to concatenate it.
concat1=np.concatenate([arr3,arr4],axis=1)
print("the concatenated matrix is ::")
print(concat)
print(concat1)


# arithematic operations--

# if the shape of the arrays in the operations does not match then numpy makes 
# replicas or projection of the smaller array such that shapes of the operating arrays are same as 
# all the operations of the matrix are defined for same dimensional matrices.--this is called broadcasting.
print(arr3+arr4,"--the sum of arr3+arr4")

print(arr3-arr4,"the arr3-arr4")

print(arr3*arr4,"multiplies the elements of one matrix with the corresponnding element of the other matrix.")

print(arr3*2,"multiplies all elements of thew arr3 with 2")

print(arr3%3,"divides all the elements with 3 and gives the remainder.")


array1=np.array([12,3,3])
array2=np.array([[2,3,4],
                [2,44,4]])
sum=array1+ array2,"array1 + array2"
print(sum)
array1_replicated=np.array([[12,3,3],
                           [12,3,3]])
sum1=array1_replicated+array2
print(sum1,"array1_replicated +array2")

#if the smaller array could not be broadcasted into theshape of the larger array then it throws an error.


#comparing of the arrays-- the comparisions occur for the arrays of same shape and
# if shape dont match then it is broadcasted , if broadcasting is not possible then it throws an error
# it compares each element with the corresponding element.

print(array1==array2)
print(array1!=array2)
print(array1>array2)
print((array1!=array2).sum())# here true represents 1 in bool and false is 0 in bool 
# this gives the sum of the trues.



# indexing and slicing
print(arr3)
print(arr3.shape)
print(arr3[1,1,1])


#special arrays first argument is shape and second argument is data type. 
# the shape is given in () paranthesis.
print(np.zeros((3,2)))
print(np.ones((2,3,4,3,6)))
print(np.eye((7)))
print(np.eye((7),2))
print(np.eye((7),2,5))#? 


#random
#rand --# picks a value unniformly between 0 and 1.

print(np.random.rand(5,3,4))#shape as arguments

#randn- 
# return the values from a gaussian distribution such that the mean will be zero and standard deviation of 1.

print(np.random.randn(2,3))#shape as arguments

#fixed value matrix--
print(np.full((2,3),42))#arguments - ((shape),value)

#arange
print(np.arange(10,90,3))#arguments--(startvalue,endvalue,steps)
print((np.arange(10,90,3)).reshape(3,3,-1))


#linespace
print(np.linspace(3,4,100))#arguments-- (start,end,number of numbers btw start and end value both terminal values are included.)




