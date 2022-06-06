
import Augmentor
#reading the images 
p = Augmentor.Pipeline(r'F:\Study_Backup\PracML\Normal')

p.set_seed(123)

p.rotate(probability=0.7, max_left_rotation=5, max_right_rotation=5)
p.flip_random(probability=0.7)
p.scale(probability=0.7,scale_factor=1.15)

##p.shear(probability=0.7, max_shear_left=0.05,max_shear_right=0.05)

p.sample(2500)

