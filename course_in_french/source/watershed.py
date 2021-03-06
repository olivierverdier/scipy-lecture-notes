a = np.zeros((512, 512)).astype(uint8) #type needed by watershed
y, x = np.ogrid[0:512, 0:512]
m1 = ((y-200)**2 + (x-100)**2 < 30**2)
m2 = ((y-350)**2 + (x-400)**2 < 20**2)
m3 = ((y-260)**2 + (x-200)**2 < 20**2)
a[m1+m2+m3]=1
xm, ym = np.ogrid[0:512:10, 0:512:10]
# If you know where to put the seeds
b = np.zeros_like(a).astype(int16)
b[0, 0] = 1
b[200, 100] = 2
b[350, 400] = 3
b[260, 200] = 4
res1 = ndimage.watershed_ift(a.astype(uint8), b)
c = np.zeros_like(a).astype(int16)
c[xm, ym]= np.arange(52**2).reshape((52,52))
res2 = ndimage.watershed_ift(a.astype(uint8), c)
res2[xm, ym] = res[xm-1, ym-1] # remove the isolate seeds
figure()

figure()
subplot(131)
imshow(a, cmap=cm.gray)
axis('off')
title('a')
subplot(132)
imshow(res1, cmap=cm.jet)
axis('off')
title('res1')
subplot(133)
imshow(res2, cmap=cm.jet)
axis('off')
title('res2')
