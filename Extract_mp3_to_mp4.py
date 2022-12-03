import moviepy as mp
import moviepy.editor as moe

video=moe.VideoFileClip("Shape_of_You _Ed_Sheeran_Lyrics_720p.mp4")
audio = video.audio
audio.write_audiofile('Shape_of_You_Ed_Sheeran_Lyrics_720p.mp3')
print('Finish....................')

