from load_image import ft_load
import pimp_image

array = ft_load("../landscape.jpg")
pimp_image.ft_invert(array)
pimp_image.ft_red(array)
pimp_image.ft_green(array)
pimp_image.ft_blue(array)
pimp_image.ft_grey(array)
print(pimp_image.ft_invert.__doc__)
