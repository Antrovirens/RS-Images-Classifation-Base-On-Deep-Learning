# 1

```py
plt.imshow(
    X,
    cmap=None,
    norm=None,
    aspect=None,
    interpolation=None,
    alpha=None,
    vmin=None,
    vmax=None,
    origin=None,
    extent=None,
    shape=None,
    filternorm=1,
    filterrad=4.0,
    imlim=None,
    resample=None,
    url=None,
    *,
    data=None,
    **kwargs,
)
```

## 参数：X

图像数据。支持的数组形状是：

（M，N） ：带有标量数据的图像。数据可视化使用色彩图。
（M，N，3） ：具有RGB值的图像（float或uint8）。
（M，N，4） ：具有RGBA值的图像（float或uint8），即包括透明度。前两个维度（M，N）定义了行和列图片，即图片的高和宽；RGB（A）值应该在浮点数[0, …, 1]的范围内,或者整数[0, … ,255]。超出范围的值将被剪切为这些界限。

## 参数：cmap

将标量数据映射到色彩图

颜色默认为：rc：image.cmap。

可能的取值
可能的取值：
    Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, viridis, viridis_r, winter, winter_r

常用的取值
    gray：0-255 级灰度，0：黑色，1：白色，黑底白字；
    gray_r：翻转 gray 的显示，如果 gray 将图像显示为黑底白字，gray_r 会将其显示为白底黑字；
    binary
    diverging colormaps：两端发散的色图 colormaps；
    seismic
    qualitative colormaps：量化（离散化）色图；
    miscellaneous colormaps：其他色图；
    rainbow

## 参数：norm :~matplotlib.colors.Normalize

如果使用scalar data ，则Normalize会对其进行缩放[0,1]的数据值内。

默认情况下，数据范围使用线性缩放映射到颜色条范围。 RGB（A）数据忽略该参数
