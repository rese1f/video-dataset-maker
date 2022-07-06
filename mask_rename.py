import argparse
import os
from tokenize import Intnumber

def parse_args():
    parser = argparse.ArgumentParser(description='mask rename')
    parser.add_argument('--mask', default='', type=str,
                        help='mask folder path')

    parser.add_argument('--shift', default=1, type=int,
                        help='id shift adjust')
    parser.add_argument('--frequency', default=4, type=int,
                        help='mask frequency')

    
    args = parser.parse_args()
    
    return args

if __name__ == '__main__':
    args = parse_args()
    print(args)
    
    img_list = os.listdir(args.mask)
    
    for img_name in img_list:
        src = os.path.join(args.mask, img_name)
        id, suffix = img_name.split('.')
        
        new_id = int(id) * args.frequency + args.shift
        new_img_name = '%06d'%new_id + '.' + suffix
        tar = os.path.join(args.mask, new_img_name)
        os.rename(src, tar)
