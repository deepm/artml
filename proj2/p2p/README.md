# Instructions
1. Download **p2p** project from GitHub

2. Go to local **p2p** project

3. Place your source images into the **customizedImg/sourceImg** folder 

**if your files are in png format, place them under customizedImg/sourceImg/png**
   
4. Open a new terminal to transer the project to AWS EC2
 
    **`scp -i [key.pem] -r ~/path/p2p ubuntu@public_DNS:~/ArtML`**
 
5. Go to Jupyter notebook and run the code

# Convert PNG to JPG

1. Run **convert_png_to_jpg.ipynb**
2. Result files will be in **customizedImg/sourceImg** in jpg format

# Get Edge Image
**make sure files are in jpg format**

1. Place all images in **customizedImg/sourceImg**
2. Run **canny_edge_detection.ipynb**
3. Result files will be in **customizedImg/combinedImg**
4. Run **move_from_combinedImg_to_train_val.ipynb** to place combined images to train and val folders
      Mode:firstX will move the first X [mvFileNum] files (in alphabetical order) to train folder
      Mode:unordered will move [mvFileNum] files (not in order) to train folder
      mvFileNum is default to 400. Make sure this is half of your data size


# Training Model

1. Place images into the **customizedImg/train** and **customizedImg/val** folders (Should have equal number of iamges in each folder)
2. Run **pix2pix-keras.ipynb**

# Get Output
**Make sure you have trained your model. If the session dies, you may need to retrain your model**
1. Place outline images into **datasets/customizedImg/test/outlines**
2. Run **duplicate_input_img.ipynb**
3. Run block **25 - 28** to get your output
**Change the batch input according to the number of outline images you have**
![alt text](https://github.com/deepm/artml/blob/master/proj2/p2p/documentImg/Capture.PNG)
