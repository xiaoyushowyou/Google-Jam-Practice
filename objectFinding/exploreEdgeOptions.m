img=imread('bridge.png');
%img=im2double(img);

filter_size=25;
filter_sigma=40;
filter=fspecial('gaussian',filter_size,filter_sigma);

%smoothed=imfilter(img,filter,0)
%Input array values outside the bounds of the array are computed by implicitly assuming the input array is periodic.
%smoothed=imfilter(img,filter,'circular')  
%smoothed=imfilter(img,filter,'replicate')

smoothed=imfilter(img,filter,'symmetric')
imshow(smoothed)

%add salt&pepper noise 
noisy_img=imnoise(img,'salt & pepper',0.02);

imshow(noisy_img);
newIM=medfilt2(noisy_img);
imshow(newIM)