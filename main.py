import os
import sys
import pickle
import matplotlib.pyplot as plt
import numpy as np
import cv2


if __name__ == "__main__":
    color_palette = [
        (0, 0, 255),
        (0, 255, 0),
        (255, 0, 0),
        (0, 255, 255),
        (255, 255, 0),
        (255, 0, 255),
        (0, 0, 127),
        (0, 127, 0),
        (127, 0, 0),
        (0, 127, 127),
        (127, 127, 0),
        (127, 0, 127),
        (191, 191, 191),
        (127, 127, 127),
        (0, 165, 225),
        (212, 255, 127),
        (235, 206, 135),
        (0, 0, 0)
    ]

    colors = [
        "red",
        "lime",
        "brue",
        "yellow",
        "cyan",
        "magenta",
        "maroon",
        "green",
        "navy",
        "olive",
        "teal",
        "purple",
        "silver",
        "gray",
        "orange",
        "aquamarine",
        "skyblue",
        "black"
    ]

    args = sys.argv
    try:
        id = int(args[1])
    except:
        print("Please input questionnaire ID.")
        exit()

    max_id = 16
    if not (id in range(0, max_id + 1)):
        print("ID must be 1 - %d"%(max_id))

    cur_dir = "."
    image_dir = os.path.join(cur_dir, "images")
    contour_dir = os.path.join(cur_dir, "contours")
    res_path = os.path.join(cur_dir, "result_%02d.txt"%(id))

    H, W = 640, 1046

    if os.path.exists(res_path):
        with open(res_path, "r") as f:
            for s_line in f:
                last_str = s_line
        last_str_list = last_str.rstrip("\n").split(",")
        assert len(last_str_list) == 3, "'result_%02d.txt' is not created correctly. Please remove 'result_%02d.txt' in this directory"%(id, id)
        start_num = int(last_str_list[0])
        resume = True
    else:
        start_num = 0
        resume = False
    image_num = 60
    val_list = [str(n) for n in range(1, 5)]

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(W/100, H/200))
    ax1.tick_params(
        labelbottom=False, labelleft=False, labelright=False, labeltop=False,
        bottom=False, left=False, right=False, top=False
        )
    ax2.tick_params(
        labelbottom=False, labelleft=False, labelright=False, labeltop=False,
        bottom=False, left=False, right=False, top=False
        )

    for i in range(start_num, image_num):
        image_id = i + 1
        img = cv2.imread(os.path.join(image_dir, "%03d.jpg"%(image_id)))
        with open(os.path.join(contour_dir, "%03d.pickle"%(image_id)), "rb") as f:
            contours_list = pickle.load(f)
        
        img_conts = img.copy()
        for ci in range(len(contours_list)):
            img_conts = cv2.drawContours(img_conts, contours_list[ci], -1, color_palette[ci], 3)

        h, w = img.shape[:2]

        mag = min(H / h, W / w)
        resize_img = cv2.resize(img, (int(w*mag), int(h*mag)))
        resize_img_conts = cv2.resize(img_conts, (int(w*mag), int(h*mag)))

        nh, nw = resize_img.shape[:2]

        norm_img = np.full((H, W, 3), 255, dtype=np.uint8)
        norm_img_conts = norm_img.copy()
        norm_img_cont = norm_img.copy()

        start_h, start_w = (H - nh) // 2, (W - nw) // 2
        norm_img[start_h : start_h + nh, start_w : start_w + nw, :] = resize_img
        norm_img_conts[start_h : start_h + nh, start_w : start_w + nw, :] = resize_img_conts
        
        if i == start_num:
            window1 = ax1.imshow(norm_img[:,:,::-1])
            window2 = ax2.imshow(norm_img_conts[:,:,::-1])
        else:
            window1.set_data(norm_img[:,:,::-1])
            window2.set_data(norm_img_conts[:,:,::-1])
        plt.tight_layout()
        
        print("This is the picture No.%03d / %03d with all masks."%(image_id, image_num))

        fig.savefig("now_image_1.jpg")

        plt.pause(0.01)
        input("Please push the enter button.")

        tmp_vals = []
        for ci, contour in enumerate(contours_list):                
            img_cont = cv2.drawContours(img.copy(), contour, -1, color_palette[ci], 3)
            resize_img_cont = cv2.resize(img_cont, (int(w*mag), int(h*mag)))

            norm_img_cont[start_h : start_h + nh, start_w : start_w + nw, :] = resize_img_cont

            window2.set_data(norm_img_cont[:,:,::-1])
            fig.savefig("now_image_2.jpg")
            plt.pause(0.01)

            while True:
                print("------------------------------------------")
                print("image %3d / %3d,     mask %3d / %3d"\
                % (image_id, image_num, ci + 1, len(contours_list)))
                print("------------------------------------------")
                print("1: The %10s mask is very   important"%(colors[ci]))
                print("2: The %10s mask is        important"%(colors[ci]))
                print("3: The %10s mask is not so important"%(colors[ci]))
                print("4: The %10s mask is not    important"%(colors[ci]))
                print("------------------------------------------")
                val = input("Your answer >> ")
                if val in val_list:
                    tmp_vals.append(val)
                    
                    break
                elif val == "exit":
                    print("Test is interrupted.") 
                    print("When you resume this, please run 'main.py' again.")
                    exit()
                else:
                    print("Please input 1 - 4.")
        
        for vi, val in enumerate(tmp_vals):
            with open(res_path, "a") as f:
                f.write("%d,%d,%s\n"%(image_id, vi, val))

    print("You checked all images.")
    print("Thank you very much for your cooperation!")
