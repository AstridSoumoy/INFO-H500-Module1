from skimage.io import imread,imsave,imshow
%matplotlib inline

watermarkImg = imread('watermark.png')
photography = imread('road.jpg')
print('test')
imshow(photography)
imsave('result.jpg', photography)
