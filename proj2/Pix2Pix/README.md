# Instructions

## Generate Edge images

1. Download **Pix2Pix** project from GitHub

2. Go to local **Pix2Pix** project

3. Place your source images into the **customizedImg/sourceImg** folder

4. Open a new terminal to transer the project to AWS EC2 or just upload the **canny_edge_detection.ipynb** file and **customizedImg** folder
**Make sure customizedImg is under datasets folder**
 
    **`scp -i [key.pem] [-r] ~/path/[project or file name] ubuntu@public_DNS:~/ArtML/`**
 
5. Go to Jupyter notebook and run the code

6. Result files will be in **customizedImg/combinedImg**


# Training Model

1. Place images into the **customizedImg/train** and **customizedImg/val** folders (Should have equal number of iamges in each folder)
2. Run **pix2pix-keras.ipynb**
