#https://postd.cc/image-processing-101/

#ref ipython notebook how to : https://qiita.com/payashim/items/d4fe5227b21a5215e78b
'''
r 3
ipython notebook



'''


# coding: utf-8

# In[1]:


import cv2, matplotlib


# In[9]:


import numpy as np


# In[10]:


abc.name


# In[11]:


import matplotlib.pyplot as plt


# In[15]:


img = cv2.imread('images/IMG_3171.JPG')


# In[16]:


print(img)


# In[17]:


plt.imshow(img)


# In[18]:


img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[19]:


plt.imshow(img2)


# In[20]:


plt.imshow(img2)


# In[21]:


img3 = cv2.imread('images/IMG_3171.JPG')


# In[23]:


plt.imshow(img3)


# In[24]:


img4 = cv2.imread('images/IMG_3166.PNG')


# In[25]:


plt.imshow(img4)


# In[26]:


gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


# In[27]:


print(gray_img)


# In[28]:


_, threshold_img = cv2.threshold(gray_img, 60, 255, cv2.THRESH_BINARY)


# In[29]:


plt.imshow(threshold_img)


# In[30]:


_, threshold_img = cv2.threshold(gray_img, 100, 255, cv2.THRESH_BINARY)
plt.imshow(threshold_img)

#閾値より低い値を探さなくても、 =========================================
piet = cv2.imread('images/IMG_3171.JPG')
# piet = cv2.imread('images/piet.png')
piet_hsv = cv2.cvtColor(piet, cv2.COLOR_BGR2HSV)
 
# threshold for hue channel in blue range
blue_min = np.array([100, 100, 20], np.uint8)
# blue_min = np.array([100, 100, 100], np.uint8)
blue_max = np.array([140, 255, 255], np.uint8)
threshold_blue_img = cv2.inRange(piet_hsv, blue_min, blue_max)
 
threshold_blue_img = cv2.cvtColor(threshold_blue_img, cv2.COLOR_GRAY2RGB)
 
plt.imshow(threshold_blue_img)

#------------------------------------------
piet = cv2.imread('images/IMG_3171.JPG')
piet_RGB = cv2.cvtColor(piet, cv2.COLOR_BGR2RGB)
plt.imshow(piet_RGB)

piet_hsv = cv2.cvtColor(piet_RGB, cv2.COLOR_BGR2HSV)
plt.imshow(piet_hsv)

blue_min = np.array([100, 100, 20], np.uint8)
blue_max = np.array([140, 255, 255], np.uint8)
threshold_blue_img = cv2.inRange(piet_hsv, blue_min, blue_max)
plt.imshow(threshold_blue_img)

mask_RGB = cv2.inRange(piet_RGB, blue_min, blue_max)
plt.imshow(mask_RGB)

plt.imshow(piet_RGB)
blue_min = np.array([0, 10, 10], np.uint8)
blue_max = np.array([20, 100, 100], np.uint8)
mask_RGB = cv2.inRange(piet_RGB, blue_min, blue_max)
plt.imshow(mask_RGB)

#ref https://stackoverflow.com/questions/2462725/cv-saveimage-in-opencv
cv2.imwrite('01.png',mask_RGB)

# -----------------------------------------
mask_RGB_cvted = cv2.cvtColor(mask_RGB, cv2.COLOR_GRAY2RGB)
plt.imshow(mask_RGB)
plt.imshow(mask_RGB_cvted)



# -----------------------------------------
# clipping
#ref https://qiita.com/satoshicano/items/bba9594a1203e24e2a31
height, width, channels = mask_RGB_cvted.shape

off_set = 280

clp = mask_RGB_cvted[(height - off_set) : height, (width - off_set) : width]
plt.imshow(clp)  
# cv2.imshow(clp)  
# clp = img[0:height/2, 0:width/2]

# -----------------------------------------
cv2.imwrite('images/clp.png',clp)

clp_LeftBottom = mask_RGB_cvted[(height - off_set) : height, 0 : off_set]
plt.imshow(clp_LeftBottom)  