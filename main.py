import cv2
import os
import pickle
import matplotlib.pyplot as plt


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

    cur_dir = os.getcwd()
    image_dir = os.path.join(cur_dir, "images")
    contour_dir = os.path.join(cur_dir, "contours")
    res_path = os.path.join(cur_dir, "result.txt")
    if os.path.exists(res_path):
        with open(res_path, "r") as f:
            for s_line in f:
                last_str = s_line
        last_str_list = last_str.rstrip("\n").split(",")
        assert len(last_str_list) == 3, "'result.txt' is not created correctly. Please remove 'result.txt' in this directory"
        start_num = int(last_str_list[0])
        resume = True
    else:
        start_num = 0
        resume = False
    image_num = 60
    val_list = [str(n) for n in range(1, 5)]

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 4))
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
        
        ax1.imshow(img[:,:,::-1])
        ax2.imshow(img_conts[:,:,::-1])
        plt.tight_layout()
        
        print("This is the picture No.%03d / %03d with all masks."%(image_id, image_num))

        fig.savefig("now_image_1.jpg")

        plt.pause(0.01)
        input("Please push the enter button.")

        tmp_vals = []
        for ci, contour in enumerate(contours_list):                
            img_cont = cv2.drawContours(img.copy(), contour, -1, color_palette[ci], 3)      

            ax2.imshow(img_cont[:,:,::-1])
            fig.savefig("now_image_2.jpg")
            plt.pause(0.01)

            while True:
                print("------------------------------------------")
                print("image %3d / %3d,     mask %3d / %3d"\
                % (image_id, image_num, ci + 1, len(contours_list)))
                print("------------------------------------------")
                print("1: The %10s mask is very   important"%(colors[ci]))
                print("2: The %10s mask is rather important"%(colors[ci]))
                print("3: The %10s mask is not so important"%(colors[ci]))
                print("4: The %10s mask is not    important"%(colors[ci]))
                print("------------------------------------------")
                val = input("Your answer >> ")
                if val in val_list:
                    tmp_vals.append(val)
                    
                    break
                elif val == "exit":
                    print("Interrupt the questionnaire.") 
                    print("If you resume this, please run 'main.py' again.")
                    exit()
                else:
                    print("Please input 1 - 4.")
        
        for vi, val in enumerate(tmp_vals):
            with open(res_path, "a") as f:
                f.write("%d,%d,%s\n"%(image_id, vi, val))

    print("You answered all images.")
    print("Thank you very much for your cooperation!")



