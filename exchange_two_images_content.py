from PIL import Image 

box1 = 285,433, 902, 478 # (x,y) (x+w,y+h)
x1, y1 , *_ = box1 

box2 = 85, 729, 483, 856
x2, y2, *_ = box2

im1 = Image.open(r"C:\Users\xcy\Desktop\微信图片_20201230193708.jpg")
im2 = Image.open(r"C:\Users\xcy\Desktop\微信图片_20201230193738.jpg")

tmp1 = im1.crop(box1)
tmp2 = im1.crop(box2)
im2.paste(tmp1, (x1, y1))
im2.paste(tmp2, (x2, y2))
im2.save("result.jpg")
