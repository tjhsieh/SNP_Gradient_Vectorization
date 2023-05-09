'''
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import os


num_iter = 500
num_path = 100
experiment_dir = "output/test/sunflowers_rendered_single_stroke_0041/video-svg_with_stroke/"
output_dir = "output/test/sunflowers_rendered_single_stroke_0041/video-png/"

if __name__ == "__main__":
    for i in range( 0, num_path ) : # num_path
        for iter in range( 499, num_iter ): # num_iter
            input_filename = os.path.join(experiment_dir, "{}-iter{}.svg".format(i+1, iter))
            output_filename = os.path.join(output_dir, "{}-iter{}.png".format(i+1, iter))
            drawing = svg2rlg(input_filename)
            renderPM.drawToFile(drawing, output_filename, fmt='PNG')
'''

import pydiffvg
import torch
import os
from utils import check_and_create_dir

num_iter = 500
num_path = 100
if __name__ == "__main__":

    device = pydiffvg.get_device()
    render = pydiffvg.RenderFunction.apply
    para_bg = torch.tensor([0., 0., 0.], requires_grad=False, device=device)

    experiment_dir = "data"
    input_filename = os.path.join(experiment_dir, "gradient.svg")
    output_filename = os.path.join(experiment_dir, "gradient.png")

    h, w, shapes, shape_groups = pydiffvg.svg_to_scene(input_filename)

    scene_args = pydiffvg.RenderFunction.serialize_scene(w, h, shapes, shape_groups)
    
    img = render(w, h, 2, 2, 0, None, *scene_args)
    img = img[:, :, 3:4] * img[:, :, :3] + para_bg * (1 - img[:, :, 3:4])

    check_and_create_dir(output_filename)
    imshow = img.detach().cpu()
    pydiffvg.imwrite(imshow, output_filename, gamma=1.0)