## Sorting Hat: Epub to Folder Sorter

### THE WHY ~~~
I have been a big fan and customer of [HumbleBundle](#) for a long time. I've used their service for killer game deals, software and books, for a great price along with helping charity at the same time.

One of the issues I was having was when I would buy a book pack, I would throw it on my NAS, and not have any real way to read the ebooks on a laptop or tablet, in a meaningful way. 

Then about a year ago, I found [Kavita](#). Kavita is basically, Plex for your ebooks. It runs in a Docker container, so I run it off my Synology (since it's lightweight), and I can serve these ebooks I've purchased (including cooking book bundles in the past for my wife). 

Using Kavita, it's often easier to organize series of books and singular epub files in folders. Kavita can most likely deal without the folders, but for us humans, it really helps when you start to amasse a lot of books, like I do.

**Example of how it looks when you download a bundle of epubs from Humble Bundle**

![](/solutions/sorting-hat/assets/eww.png)

In the past, I would create a new folder, by hand for every epub, and then move the .epub file(s) into the respective folders. This is a pain in the ass. So, I decided to make it automated. 

This Python script, is extremely simple. It looks for every .epub in the folder, extracts the official title, clenses the title of any characters the OS would have an issue with being in a folder name, creates a folder and then moves the file into the new folder. It then continues with however many .epub it finds. Simple and easy. 

**In my example, you end up with this:**

![.](/solutions/sorting-hat/assets/yummy.png)

 **Much. Nicer.**

### INSTRUCTIONS ~~~

```
pip install ebooklib
```

Download (or copy) the script into a new file, (ex. sorting-hat.py) in the same directory as all of your epubs (it does not work recursively). 

Run it:


```
python sorting-hat.py
```

You should see output that is simliar to this. 

![.](/solutions/sorting-hat/assets/term-success.png)

Any errors should be listed, and you'll have to find/fix any issues it lists.

### Success.

***

**Looking for a disclaimer?** <br>
All disclaimers and legalese can be found in the root [README.md](../../) file. 
