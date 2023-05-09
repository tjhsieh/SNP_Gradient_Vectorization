from svgpathtools import svg2paths, wsvg, Path
import os

def addCSS( file, pathn, itern, output_dir ) :
    '''Combine SVG paths into one compound path.'''
    #print(file)
    paths, attributes, svg_attributes = svg2paths(file, return_svg_attributes=True)
    for i in range( 0, pathn + 1 ) :
        attributes[i]['opacity'] = 1.0
        attributes[i]['stroke-width'] = 0.5

    new_file = output_dir + str(pathn+1) + "-iter" + str(itern) + ".svg"
    wsvg(paths, attributes=attributes,svg_attributes=svg_attributes, filename=new_file)
    return new_file

num_iter = 500
num_path = 100
experiment_dir = "log/test/sunflowers_rendered_single_stroke_0041"
output_dir = "output/test/sunflowers_rendered_single_stroke_0041/video-svg_with_stroke/"
pathn_record_str = "1"

if __name__ == "__main__":
    for i in range( 0, num_path ) : # num_path
        for iter in range( 0, num_iter ): # num_iter
            filename = os.path.join(experiment_dir, "video-svg", "{}-iter{}.svg".format(pathn_record_str, iter))
            addCSS( filename, i, iter, output_dir )
        pathn_record_str += "-1"      