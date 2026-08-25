from pathlib import Path
import shutil
folder = Path("myfiles") # to check path for myfies
print(folder.exists()) 
for item in folder.iterdir(): # to iterate in directory
    print(item.name,item.suffix)

for item in folder.iterdir():
    if item.suffix == ".png":
        print(item.name,"-> images")
    elif item.suffix == ".pdf":
            print(item.name,"-> pdf")
    elif item.suffix == "..mp4":
                print(item.name,"-> videos")
    elif item.suffix == ".txt":
                print(item.name,"-> text files")
images = folder / "images"  #creating images file to store images 
text_files = folder / "text files"
videos = folder / "videos"
pdf = folder /"pdf"
images.mkdir(exist_ok=True) #exist_ok true means if folder exist dont give error
text_files.mkdir(exist_ok=True)
videos.mkdir(exist_ok=True)
pdf.mkdir(exist_ok=True)

for item in folder.iterdir():
    if item.is_file():
            if item.suffix == ".png":
                  shutil.move(item , images / item.name)
            elif item.suffix == ".pdf":
                  shutil.move(item , pdf / item.name)
            elif item.suffix == ".mp4":
                              shutil.move(item , videos / item.name)
            elif item.suffix == ".txt":
                              shutil.move(item , text_files / item.name)