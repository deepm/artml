# Instructions
1. Download **Multistyle_transfer** project from GitHub

2. Go to local **Multistyle_transfer** project

3. Place your source images into the **SourceImg** folder

4. Go to **StyleImg** folder to select and organize desire styles

   * All files will be processed by alphabetical order
   * Organize and rename the style images according to the order you want them to be processed
  
   **Order 1**
   ![alt text](https://github.com/frank113/art-ml-project1/blob/master/Multistyle_transfer/Reference/Order1.JPG)
   
   
   **Order 2**
   ![alt text](https://github.com/frank113/art-ml-project1/blob/master/Multistyle_transfer/Reference/Order2.JPG)
   
   
 5. Open a new terminal to transer the project to AWS EC2
 
    **`scp -i [key.pem] -r ~/path/Multistyle_transfer ubuntu@public_DNS:~/ArtML`**
 
 6. Go to Jupyter notebook and run the code
    
    * Make sure the environment is in **conda_tensorflow_p27**
    ![alt text](https://github.com/frank113/art-ml-project1/blob/master/Multistyle_transfer/Reference/Env.JPG)
    
    * If the environment is off, go to **`Kernel > Change Kernel > Environment(conda_tensorflow_p27)`**
 
    
    
    * You can change the number of iterations in **block 4** (the lower the iteration is the faster it runs)
    ![alt text](https://github.com/frank113/art-ml-project1/blob/master/Multistyle_transfer/Reference/Block4.JPG)
    
    
    * Default iteration (20) takes 15 mins to run per image
    
    * You can use the **Style_transfer_keras** project to test how many iteration you need to produce the result you like 
    
    * To assign different iterations for different styles:
      
      Go to **block 4** and **13** and do the fllowing edit (`style_iterations = [style1_iteration,style2_iteration,style3_iteration]`)
      ![alt text](https://github.com/frank113/art-ml-project1/blob/master/Multistyle_transfer/Reference/StyleIter1.JPG)
      
      
      ![alt text](https://github.com/frank113/art-ml-project1/blob/master/Multistyle_transfer/Reference/StyleIter2.JPG)
      
      
    
    * The **Intermediate** folder contains all the images produced for each iteration
    
    * The intermediate files will be named in this format: [style1_style2_style3_sourceImgName]
    
    * **The final result will be the images in the SouceImg folder** (it overwrites)
    
 7. Download the final images
 
    **`scp -i [key.pem] -r ubuntu@public_DNS:~/ArtML/Multistyle_transfer localpath`**
 
