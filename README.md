My girlfriend needed to print images that didn´t fit into a regular A4 sheet, therefore she needed somehow, to split the image in four, to glue them together after that. The problem was that, although there are several web tools that allow you to easily split an image in four, all four pieces are equal size. She once told me that her work would be much easier if there was a way to leave an extra space (an overlap) on some of those images. That way she would be able to glue them together much faster. So I came up with this program.

Long story short, this program turns `IMG.png` into `IMG 1.png`, `IMG 2.png`, `IMG 3.png` and `IMG 4.png` (check the repo). 

She needed it as soon as possible, so I didn't develop any UI. 

You can test it the easy way, by downloading the `image-splitter.exe`:
1. Create an empty folder on your PC, let's say `C:\EmptyFolder`
2. Paste the `image-splitter.py` file in that empty folder
3. Paste any `.PNG`, `.JPGE` or `.JPG` image into that repository
4. Double click on `image-splitter.exe`
5. Now, as a result, you should find the four new images on `C:\EmptyFolder` 


Or you can also try following these steps:
1. Install Python in your PC
2. Install the PIP module
    ```
    py -m pip install --upgrade pip
    ```
3. Intall the PIL module
    ```
    py -m pip install PIL
    ```
4. Create an empty folder on your PC, let's say `C:\EmptyFolder`
5. Paste the `image-splitter.py` file in that empty folder
6. Paste any `.PNG`, `.JPGE` or `.JPG` image into that repository
7. Go to your `cmd` and position yourself in the new repository
    ```
    cd C:\EmptyFolder
    ```
8. Run the following command
    ```
    py image-splitter.py
    ```
9. Now, as a result, you should find the four new images on `C:\EmptyFolder` 


If you happen to have more than one image on the same folder, then it will pick one of them randomly.