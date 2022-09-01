# from .models import *
import os
from PIL import Image
from colorthief import ColorThief
from moviepy.editor import VideoFileClip


def time_movies(path):
    clip = VideoFileClip(path)
    sec = int(round(clip.duration))
    min = sec // 60
    h = sec // 3600
    sec = sec - (h*3600 + min*60)
    return f"{h}:{min}:{sec}"


def dominant_color(path1, path2):
    img = Image.open(path1)
    img = img.crop((img.width-1400, 400, img.width, img.height-400))
    img = img.resize((50, 50), Image.Resampling.LANCZOS)
    img.save(path2)
    color_thief = ColorThief(path2)
    return '#%02x%02x%02x' % color_thief.get_color(quality=1)

# class DataMixin:
#
#     def get_movie_context(self, **kwargs):
#
#         context = kwargs
#
#         context['top'] = top
#
#         return  context