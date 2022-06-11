import os
import shutil
import argparse
from util import *


def parse_args():
    parser = argparse.ArgumentParser(description='video dataset maker script')
    parser.add_argument('--url', default='./example.txt', type=str,
                        help='url list .txt file path')
    parser.add_argument('--output', default='./output', type=str,
                        help='output path')
    parser.add_argument('--suffix', default='.png', type=str,
                        help='suffix of extracted images')
    parser.add_argument('--h', default=360, type=int,
                        help='height of extracted images')
    parser.add_argument('--w', default=640, type=int,
                        help='width of extracted images')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    
    if os.path.exists(args.output):
        shutil.rmtree(args.output)
    os.mkdir(args.output)
    
    with open(args.url) as f:
        url_list = f.readlines()
    f.close()
    
    for id, url in enumerate(url_list):
        path = os.path.join(args.output, str(id))
        os.mkdir(path)
        
        dl_cmd = 'yt-dlp -f bestvideo[height={}][ext=mp4]/best[ext=mp4]/best\
                  {}\
                  -o {}.mp4'.format(download_resolution(args.h),
                                    url.strip('\n'),
                                    path,
                                    )
        os.system(dl_cmd)

        ex_cmd = 'ffmpeg -i {}.mp4\
                 -vf scale={}:{}\
                 {}/%04d{}'.format(path,
                                  args.w,
                                  args.h,
                                  path,
                                  args.suffix,
                                  )
        os.system(ex_cmd)
        
        continue