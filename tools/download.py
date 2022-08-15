import argparse
import os

from pytube import YouTube
from tqdm import tqdm


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Download YouTube videos')
  parser.add_argument('--videolist', default='./configs/videolist.txt')
  parser.add_argument('--videopath', default='videos')
  
  args = parser.parse_args()

  if not os.path.exists(args.videopath):
    os.mkdir(args.videopath)

  count = 0

  with open(args.videolist, "r") as f:
    urls = [url.replace('\n','') for url in f.readlines()]

  for url in tqdm(urls):
    try:
      video = YouTube(r"https://www.youtube.com/watch?v=" + url)
      video.streams \
        .filter(progressive=True, file_extension='mp4') \
        .order_by('resolution')[-1] \
        .download(args.videopath, filename=url)
      count += 1
      print(f"Processed {url}")
    except:
      print(f"Cannot process {url}")
      continue

  print(f"Downloaded {count}/{len(urls)} videos")
