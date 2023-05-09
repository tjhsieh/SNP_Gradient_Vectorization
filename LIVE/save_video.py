import os
import cv2
from utils import check_and_create_dir
num_iter = 1000
num_path = 1
experiment_dir = "log/sparse_100_iter1000/sunflowers_rendered_single_stroke_0001/"
output_dir = "log/sparse_100_iter1000/sunflowers_rendered_single_stroke_0001/"
w = 512
h = 512

if __name__ == "__main__":

    for i in range(0, num_path):
        img_array = []
        for iter in range( 0, num_iter ): # num_iter
            filename = os.path.join( experiment_dir, "video-png", 
            "{}-iter{}.png".format(i+1, iter))
            img = cv2.imread(filename)
            #print(filename)
            img_array.append(img)

        videoname = os.path.join(output_dir, "video-avi", "{}.mp4".format(i+1))
        check_and_create_dir(videoname)
        out = cv2.VideoWriter(
            videoname, 
            cv2.VideoWriter_fourcc(*'mp4v'),
             #cv2.VideoWriter_fourcc(*'FFV1'), 
            20.0, (w, h))
        print(len(img_array))
        for iii in range(len(img_array)):
            out.write(img_array[iii])
        out.release()