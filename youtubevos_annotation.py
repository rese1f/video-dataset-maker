import argparse
import json
import os

def parse_args():
    parser = argparse.ArgumentParser(description='YouTubeVOS dataset annotation maker')
    parser.add_argument('--mask', default='', type=str,
                        help='mask folder path')
    parser.add_argument('--catagory-list', nargs='+', default=[], type=str,
                        help='catagory list of objects')
    parser.add_argument('--id', default='', type=str,
                        help='video id')
    
    parser.add_argument('--resume', default='', type=str,
                        help='existing json file path')
    parser.add_argument('--save', default='meta.json', type=str,
                        help='json file saving path')
    
    args = parser.parse_args()
    
    return args

if __name__ == '__main__':
    args = parse_args()
    print(args)

    # initial dictionary
    annotation = {}
    if args.resume != '':
        annotation = json.load(args.resume)["videos"]
    elif args.save == '':
        args.save = args.resume
    
    # create dictionary
    annotation[args.id] = {}
    annotation[args.id]["objects"] = {}
    for i, object in enumerate(args.catagory_list):
        obj = {}
        obj["category"] = object
        obj["frames"] = [name.split('.')[0] for name in os.listdir(args.mask)]
        annotation[args.id]["objects"][str(i+1)] = obj
    
    # save to json file
    saved_annotation = {"videos": annotation}
    with open(args.save, 'w') as f:
        json.dump(saved_annotation, f, indent=4)