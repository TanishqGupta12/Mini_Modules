import os

def createnoexist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move (foldername , files):
    for file in files:
        os.replace(file,f"{foldername}/{file}")
    
# files = os.remove("clear.py")
#files = os.listdir () --> mean  how many files are there in folder 

files = os.listdir()
print(files)
# os.makedirs() mean make a dir in which item folder 


createnoexist('Images')
imgExts = [".png",".jpg","jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts] 
move("Images",images)
    
# createnoexist(' video')
# VideoExts = [".mkv",".mp4",".wmv",".webm"]
# Video = [file for file in files if os.path.splitext(file)[1].lower() in VideoExts] 
# move("Video",Video)

# createnoexist(' Music')
# MusExts = [".mp3",".msv",]
# Music = [file for file in files if os.path.splitext(file)[1].lower() in MusExts] 
# move("Music",Music)

# createnoexist(' Pdf ')
# pdfExts = [".pdf"]
# pdf = [file for file in files if os.path.splitext(file)[1].lower()in pdfExts] 
# move("Pdf",pdf)

# createnoexist('Zip')
# zipExts = [".zip",".zipx"]
# zip = [file for file in files if os.path.splitext(file)[1].lower()in zipExts] 
# move("zip",zip)

# createnoexist('Prograamming lanugae')
# ProlanExts = [".cpp",".java",".py"]
# prolang= [file for file in files if os.path.splitext(file)[1].lower()in ProlanExts]
# move("Prograamming lanugae",prolang)

# other = []
# for file in files:
#     if (os.path.splitext(file)[1].lower() not in imgExts, VideoExts,MusExts,pdfExts,zipExts,ProlanExts):
#         other.append(file) 
#         move("Other",other)
