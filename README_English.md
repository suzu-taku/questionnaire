# Questionnaire on important regions in images

## Purpose

Movies and images are widely used as a means of information communication, but these opress capacity for channels.

Uniform compression is current popular method but may cause loss of important regions when high compressed.

So image compression without loss of important regions is needed.

That's why we need to know where are important regions in images.

## Installation

Python 3.0+ is required.

Download this repository like this:

```
$ git clone https://github.com/suzu-taku/questionnaire.git
```

Install all the python dependencies (OpenCV, matplotlib>=3.0.0, numpy) using pip.

```
$ cd questionnaire
$ pip install -r requirements.txt
```

## Execution

Run "main.py" with your questionnaire ID.

```
$ python main.py questionnaire_ID
```

Following image and words are output after running.

![](demo/demo_image_1.jpg)

```
This is the picture No.001 / 060 with all masks.
Please push the enter button.
```

Left: original image, Right: target image with all candidate regions

This image is stored as "now_image_1.jpg". If the image is not displayed, refer to that.

After confirming the image, press the enter key.

Following image and words are output next.

![](demo/demo_image_2.jpg)

```
------------------------------------------
image   1 /  60,     mask   1 /   3
------------------------------------------
1: The        red mask is very   important
2: The        red mask is rather important
3: The        red mask is not so important
4: The        red mask is not    important
------------------------------------------
Your answer >>
```

Left: original image, Right: target image with a candidate region

This image is stored as "now_image_1.jpg". If the image is not displayed, refer to that.

If the masked region is very   important -> input 1

If the masked region is        important -> input 2
                 
If the masked region is not so important -> input 3
                 
If the masked region is not    important -> input 4                 

## Interruption

When you want to interrupt the questionnaire, input "exit" as "Your answer".

```
Your answer >> exit
```

When you resume the questionnaire, run "main.py" with your questionnaire ID again.

## Submission

When the questionnaire is executed to the end, the following words are output and the program ends.

```
You checked all images.
Thank you very much for your cooperation!
```

Please submit the "result_ID.txt" [***HERE***](https://www.dropbox.com/request/dqUKYzZdGBerNj2a7zgu).

