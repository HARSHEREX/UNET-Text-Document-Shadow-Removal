import os
import shutil
import cv2
import numpy as np
# aspect ratio = 1:2 | h:w

def gen_shadow(data_dir,save_dir):
  try:
    os.mkdir(save_dir)
  except:
    shutil.rmtree(save_dir)
    os.mkdir(save_dir)

  shadow_dir = os.path.join(save_dir,'shadow/')
  shaded_img_dir = os.path.join(save_dir,'/shaded/')
  os.mkdir(shadow_dir)
  os.mkdir(shaded_img_dir)
  for i in tqdm(os.listdir(data_dir)[:]):
      for k in range(2,5):
          kc = k
          kk=0
          # if k>4:
          k=np.random.choice([4,5,6])
          rh,rw = np.random.randint(k-kk,int(k*1.5)+1-kk),np.random.randint(k-kk,(k*2)-kk)
          x = np.random.rand(rh,rw)
          m =np.random.randint(110,120)/100
          x = x/(x.max()*m)
          # x = x+(1-x.max())
          img = cv2.imread(data_dir+i,0)
          if img.shape[0]>img.shape[1]:
              img  = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
          img = cv2.resize(img,(256,128),interpolation=cv2.INTER_AREA)
          h,w = img.shape[:2]
          j = cv2.resize(x,(5,7),interpolation=cv2.INTER_AREA)
          j = cv2.resize(j,(w,h),interpolation=cv2.INTER_CUBIC)        
          n = np.random.randint(30,50)/100
          j[j>n]=1.0
          j[j<=n]=n

          ks = np.random.choice([5,7,11])
          j = cv2.GaussianBlur(j,(ks,ks),0)
          img = img*j
          cv2.imwrite(shaded_img_dir+str(kc)+i,img)
          cv2.imwrite(shadow_dir+str(kc)+i,(j*255))

