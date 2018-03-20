#MyImageLib
为了统一坐标方向，基于OpenCV、PIL和numpy，封装了常用的图形处理函数

- 规定MyImageLib中的坐标系：  
 所有形如(x, y)的参数，横向为x，纵向为y，图像左上角为(0, 0)

----
> ##basic(基本操作)
### Rotate(src, angle, center=(x, y))
旋转
>src:        图片源文件  
>angle:      旋转角度(角度制)，逆时针为正方向  
>center:     旋转中心，缺省为图片中心
### Translation(src, direction=(dx, dy))
平移
>src:        图片源文件  
>direction:  平移方向

### Resize(src, size=(w, h))
缩放
>src:        图片源文件  
>size:       缩放后的尺寸

### EnlargeCanvas(src, size, fit)
扩大画布尺寸
>src:        图片源文件  
>size:       扩大后的画布尺寸  
>fit:        是否将图片移动到化部中央(True/False),缺省为False  

### CropRect(src, xmin, xmax, ymin, ymax)
裁剪矩形区域
>src:        图片源文件   
>xmin等:     字面意思

----
> ##advanced(高级操作)
###removeBorder(src, background=(minCol, maxCol))
将周围一圈背景去掉
>src:        图片源文件   
>background: 背景的颜色范围，缺省为(0, 0)  

### addBorder(src, width, color=0)
给图加边框
>src:        图片源文件  
>width:      边框宽度  
>color:      边框颜色

----
> #noise(加噪声)
### SaltAndPepper(src, percetage)
椒盐噪声
>src:        图片源文件   
>percetage:  噪声比例  

### GaussianNoise()
还没写