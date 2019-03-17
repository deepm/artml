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


# Training Model

1. Place images into the **customizedImg/train** and **customizedImg/val** folders (Should have equal number of iamges in each folder)
2. Run **pix2pix-keras.ipynb**
