import scipy
lena = scipy.lena()
lena = (-lena).astype(float)
y, x = np.ogrid[0:512,0:512]
medaillon_mask = (((x-308)**2 + (y-312)**2)<18**2)
lena[red_nose_mask] = -400
lena[0,0] = -430
imshow(lena, cmap=cm.RdGy)
