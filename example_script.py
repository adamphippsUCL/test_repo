import matplotlib.pyplot as plt
import scipy
import numpy as np
import pickle

# print(np.pi)

# x = np.array([i for i in range(1,10)])

# fig = plt.figure()
# plt.plot(x,x*x)
# plt.show()
# fig.savefig('lol.png')


# test_array = np.array([1,2,3,4,5])



# with open('test_array.pickle', 'wb') as handle:
#     pickle.dump( test_array, handle, protocol=pickle.HIGHEST_PROTOCOL)

# with open('test_array.pickle', 'rb') as handle:
#     test_array = pickle.load(handle)


# truth_array = np.array([ [x == test_array[i] for x in test_array] for i,y in enumerate(test_array)])

# print(truth_array)

# image = plt.figure()
# plt.imshow(truth_array)
# image.savefig('savefig.png')  


my_img = plt.imread('oxford logo.jpg')

print(my_img.shape)

img_red = my_img[:,:,0]

fig = plt.figure()
plt.imshow(img_red, cmap = 'jet')
fig.savefig('just da red.png')




