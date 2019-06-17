#https://postd.cc/image-processing-101/

#ref ipython notebook how to : https://qiita.com/payashim/items/d4fe5227b21a5215e78b
'''
    file : 2-1.for-memo.py
    date : 2018/05/13 11:42:34
r 3

pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\2_image-prog\2_projects\1_sort-out\2_\
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


img = cv2.imread('../images/IMG_3171.JPG')


# In[16]:


print(img)


# In[17]:


plt.imshow(img)


# In[18]:


img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img2)
#aa

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
plt.imshow(gray_img)

gray_img[0]


# In[28]:


_, threshold_img = cv2.threshold(gray_img, 60, 255, cv2.THRESH_BINARY)
plt.imshow(threshold_img)

_, threshold_img = cv2.threshold(gray_img, 60, 100, cv2.THRESH_BINARY)
plt.imshow(threshold_img)

_, threshold_img = cv2.threshold(gray_img, 20, 255, cv2.THRESH_BINARY)
plt.imshow(threshold_img)


# In[30]:


_, threshold_img = cv2.threshold(gray_img, 100, 255, cv2.THRESH_BINARY)
plt.imshow(threshold_img)

#閾値より低い値を探さなくても、 =========================================
piet = cv2.imread('../images/IMG_3171.JPG')
# piet = cv2.imread('images/piet.png')
piet_hsv = cv2.cvtColor(piet, cv2.COLOR_BGR2HSV)

len(piet_hsv)

# threshold for hue channel in blue range
blue_min = np.array([100, 100, 20], np.uint8)
blue_min[0]
len(blue_min)

# blue_min = np.array([100, 100, 100], np.uint8)
blue_max = np.array([140, 255, 255], np.uint8)
threshold_blue_img = cv2.inRange(piet_hsv, blue_min, blue_max)
 
plt.imshow(threshold_blue_img)
 
val_max = 80
blue_min = np.array([20, 20, 20], np.uint8)
blue_max = np.array([val_max, val_max, val_max], np.uint8)
threshold_blue_img = cv2.inRange(piet_hsv, blue_min, blue_max)
plt.imshow(threshold_blue_img)
 
threshold_blue_img_Cnvtd = cv2.cvtColor(threshold_blue_img, cv2.COLOR_GRAY2RGB)
plt.imshow(threshold_blue_img_Cnvtd)
 

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

# ----------------------------------------- 20180513_120247
plt.imshow(img2)

height, width, channels = img2.shape
off_set = 280
clp = img2[(height - off_set) : height, 0 : off_set]
plt.imshow(clp)

# ----------------------------------------- 20180513_130130
img = cv2.imread('C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/images/IMG_3171.JPG')
#     img = cv2.imread('../images/IMG_3171.JPG')

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#     plt.imshow(img2)
#     
dpath = "C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/2_/images"
#     
#     fname = "image.%s.png" % (libs.get_TimeLabel_Now())
#     
#     fpath = "%s/%s" % (dpath, fname)
#     
#     plt.savefig(fpath)

#ref display image https://github.com/PrinzEugen7/ImageProcessing/blob/master/Image/Python/Matplotlib/draw_opencv_img.py
#     plt.show()

'''###################
    get : data
###################'''
# data
height, width, channels = img2.shape
off_set = 280

tlabel = "20180513_130233"
# tlabel = libs.get_TimeLabel_Now()

plt_ = plt


# save image
'''###################
    corner : LB        
###################'''
titles = ["clp_LB", "clp_RB", "clp_LU", "clp_RU"]

clips = [
    
        img2[(height - off_set) : height, 0 : off_set], # clp_LB
        img2[(height - off_set) : height, width - off_set : width], # clp_RB
        img2[0 : off_set, 0 : off_set], # clp_LU
        img2[0 : off_set, width - off_set : width], # clp_RU
    ]

clips[0]

clip_0 = clips[0]
len(clip_0)
len(clip_0[0])
clip_0[0][0]


# ----------------------------------------- 20180513_130451
max_R = -1

for item in clip_0[0]:

    R = item[0]
    
    if R > max_R : #if R > max_R
    
        max_R = R
        
    #/if R > max_R
    
#/for item in clip_0[0]:

print("max_R => %d" % max_R)

# ----------------------------------------- 20180513_130745
max_R = -1; max_G = -1; max_B = -1

for item in clip_0[0]:

    R = item[0]; G = item[1]; B = item[2]
    
    if R > max_R : max_R = R
    if G > max_G : max_G = G
    if B > max_B : max_B = B
        
    #/if G > max_G
    
#/for item in clip_0[0]:

print("max_R = %d, max_G = %d, max_B = %d" % (max_R, max_G, max_B))

