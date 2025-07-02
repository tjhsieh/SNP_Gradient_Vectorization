import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import cv2
import numpy as np
import PIL
import PIL.Image
import json
import argparse

def find_color_locaiton(image,color_mask) : 
    _, component, cstats, ccenter = cv2.connectedComponentsWithStats(
    (color_mask==1).astype(np.uint8), connectivity=4)
    # connected_component_plot(_, cstats)
    csize = [ci[-1] for ci in cstats[1:]]
    # print("max size: " ,max(csize))
    if max(csize) < 4 :
        return 0,0,0
    target_cid = csize.index(max(csize))+1
    center = ccenter[target_cid][::-1]
    coord = np.stack(np.where(component == target_cid)).T
    dist = np.linalg.norm(coord-center, axis=1)
    target_coord_id = np.argmin(dist)
    coord_h, coord_w = coord[target_coord_id]
    color=image[coord_h][coord_w]
    # print(coord_w, coord_h,color)
    return coord_w, coord_h, color

def connected_component_plot(_, cstats):
    ax = plt.subplots()
    for i in range(1, _):
        # 获取当前连通组件的外接矩形框信息
        x, y, w, h, area = cstats[i]
        print(area)
        rect = plt.Rectangle((x, y), w, h, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
    plt.show()


def cluster_scatter( clt, map, figure_tile, figure_name ) :
    labels = clt.labels_
    centers = clt.cluster_centers_
    plt.scatter(map, np.zeros_like(map), cmap='viridis', c=labels)
    plt.scatter(centers, [0,0], marker='x', s=200, c='r')
    plt.title(figure_tile, fontfamily='serif')
    plt.xticks(fontfamily='serif')
    plt.yticks(fontfamily='serif')
    plt.savefig(figure_name, format='pdf')
    plt.show()
    
def channel_distribution( channel, figure_tile, figure_name) :
    plt.hist(channel, bins=25) 
    plt.xlabel('Value', fontfamily='serif') 
    plt.ylabel('Frequency', fontfamily='serif')  
    plt.yticks(fontfamily='serif')
    plt.title(figure_tile,fontfamily='serif')  
    plt.savefig(figure_name, format='pdf')
    plt.show()
    
def load_single_stroke_file(file_direct, stroke_num ) :
    stroke_name = ""
    num = str(stroke_num)
    num_of_zeros = 4 - len(num)
    for i in range(num_of_zeros) :
        stroke_name += '0'
    stroke_name += num
    filname = file_direct +  stroke_name + ".png"
    image = np.array(PIL.Image.open(filname))
    if image.shape[2] == 4:
        print("Input image includes alpha channel, simply dropout alpha channel.")
        image = image[:, :, :3]
    return image

def color_cluster( nums, direc ) :
    file_direct = direc
    stroke_cluster = []
    for stroke_num in range(1, int(nums)+1 ) :
        need_H_cluster = True
        H_distribution_even = False
        print(stroke_num)
        data = []
        image = load_single_stroke_file( file_direct, stroke_num )

        HSV_image = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
        resize_image = cv2.resize(HSV_image, ( int(image.shape[0]/2), int(image.shape[1]/2) ))

        # Remove White Points
        S_range = np.logical_and(resize_image[:,:,1] >= 0, resize_image[:,:,1] <= 5)
        V_range = np.logical_and(resize_image[:,:,2] >= 250, resize_image[:,:,2] <= 255)
        white_point_mask = np.logical_and(S_range, V_range)
        stroke_image = resize_image[white_point_mask==0]

        # Remove Outliers in H channel
        HS_image = stroke_image[:,0:2]
        H_channel = HS_image[:,0]
        S_channel = HS_image[:,1]
        h_average = int(np.average(H_channel))
        h_std = int(np.std(H_channel))
        s_average = int(np.average(S_channel))
        s_std = int(np.std(S_channel))
        # channel_distribution( H_channel, 'Distribution of H channel Data', 'H_distribution.pdf' )
        if ( h_std == 0 ) : # pixels are the same Hue value, don't need to do H channel cluster
            need_H_cluster = False
        else:
            if h_std > h_average * 0.8 :
                 x = 2
            else : 
                 x = 1
            h_thre_image = np.logical_and( stroke_image[:, 0] >= h_average - x * h_std, stroke_image[:, 0] <= h_average + x * h_std)



        # first stage ( H channel clustering )
        if (need_H_cluster) :
            f = stroke_image[h_thre_image]
            H_map = f[:,0].reshape(-1, 1)
            H_clt = KMeans(n_clusters = 2)
            H_clt.fit(H_map)
            labels = H_clt.labels_
            cluster_counts = np.bincount(H_clt.labels_)
            max_index = np.argmax(cluster_counts)
            if ( cluster_counts[max_index] / len(H_clt.labels_) > 0.9 ) :
                centers = H_clt.cluster_centers_[max_index]
                H_centers = np.array([centers,centers])
                S_map = f[:,1]
                S_map = S_map[labels==max_index].reshape(-1,1)
            else :
                H_distribution_even = True 
                H_centers = H_clt.cluster_centers_
                S_map = f[:,1]
        else :
            print("not need_H_cluster")
            H_centers = np.array([[h_average],[h_average]])
            S_map = stroke_image[:,1].reshape(-1,1)

        # cluster_scatter( H_clt, H_map, 'Cluster of H channel', 'H_cluster.pdf' )

        # second stage ( S channel clustering )
        S_centers = np.empty((2, 1))
        if( H_distribution_even ) :
            print("H_distribution_even")
            for i in range(0,2):
                s_map = S_map[H_clt.labels_==i].reshape(-1,1)
                if( s_map.shape[0] > 1) :
                    S_clt = KMeans(n_clusters = 2)
                    S_clt.fit(s_map)
                    S_labels = S_clt.labels_
                    cluster_counts = np.bincount(S_labels)
                    S_centers[i] = S_clt.cluster_centers_[np.argmax(cluster_counts)]
                    # cluster_scatter( S_clt, s_map, 'Cluster of S channel', 'S_cluster' + str(i) + '.pdf' )
        else :
            print("H_distribution_not_even")
            S_clt = KMeans(n_clusters = 2)
            S_clt.fit(S_map)
            S_labels = S_clt.labels_
            S_centers = S_clt.cluster_centers_
            cluster_counts = np.bincount(S_labels)
            s_max_index = np.argmax(cluster_counts)

            if ( cluster_counts[s_max_index] / len(S_labels) > 0.80 ) :
                centers = S_clt.cluster_centers_[s_max_index]
                S_centers = np.array([centers,centers])
            else:
                S_centers = S_clt.cluster_centers_[:,0].reshape(-1,1)
            # cluster_scatter( S_clt, S_map, 'Cluster of S channel', 'S_cluster.pdf' )    

        # find color position
        color_list = np.concatenate((H_centers, S_centers), axis=1)
        color_list = np.round(color_list)
        print(color_list)
        for color in color_list :
            h_color = color[0]
            s_color = color[1]
            color_mask =  np.zeros((image.shape[0], image.shape[1]))
            for w in range(image.shape[0]):
                for h in range(image.shape[1]):
                    if h_color-6 <= HSV_image[w][h][0]  <= h_color+6 :

                        if s_color-5 <= HSV_image[w][h][1]  <= s_color+5 :
                                    color_mask[w][h] = 1
            # print(len(color_mask[color_mask==1]))
            if len(color_mask[color_mask==1]) > 0 :
                coord_w, coord_h, c = find_color_locaiton(HSV_image,color_mask)
                if coord_w != 0 and  coord_h != 0 :
                    coord_color = cv2.cvtColor(np.uint8([[c]]),cv2.COLOR_HSV2RGB)
                    data.append({'coord': [coord_w.tolist(), coord_h.tolist()] ,'color_rgb': coord_color[-1,-1,:].tolist()})    
        stroke_cluster.append(data)
        # print(data)
    with open( './hsv_pixels.json', 'w') as file:
        json.dump(stroke_cluster, file,indent=4)    


if __name__ == "__main__":
    # python HSV_color_cluster.py  -d ./resource/flower/single_strokes/sunflowers_rendered_single_stroke_ -n 495
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="stroke png directory")
    parser.add_argument("-n", "--nums", help="stroke png numbers")
    args = parser.parse_args()
    direc = args.directory
    nums = args.nums
    color_cluster( nums, direc )
    