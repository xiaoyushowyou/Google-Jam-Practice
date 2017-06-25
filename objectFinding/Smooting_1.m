pkg load image;

img=imread('Einstein.jpg');
img=im2double(img)
imshow(img);

noise=randn(size(img)) .* 1;
noisy_img = img + noise;

imshow(noisy_img);

%create Guassian Filter
filter_size=11;
filter_sigma=2;
%pkg load image;
filter=fspecial('gaussian',filter_size,filter_sigma);

smoothed=imfilter(noisy_img,filter)

imshow(smoothed)
% for sigma=1:3:10
%     h=fspecial('guassian',fsize,sigma);
%     out=imfilter(im,h);
%     imshow(out);
%     pause;
% end
