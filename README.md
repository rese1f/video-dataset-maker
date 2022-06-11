# Video Dataset Maker
A pipeline covers downloading videos from YouTube and extracting frames using ffmpeg.

Our goal is to build a fast pipeline to produce new datasets for deep learning practitioners in the field of video understanding. We have already done some action recognition and video target segmentation datasets with this tool.

- [Video Dataset Maker](#video-dataset-maker)
  - [DENPENDENCY](#denpendency)
    - [Python Environment](#python-environment)
    - [yt-dlp](#yt-dlp)
    - [FFmpeg](#ffmpeg)
  - [INSTALLATION](#installation)
  - [GET STARTED](#get-started)
  - [TODO](#todo)

The project is organized as:
```
.
├── LICENSE
├── README.md
├── example.txt
├── main.py
├── requirements.txt
└── util.py
```

## DENPENDENCY

### Python Environment
Personally suggest [Conda](https://www.anaconda.com/). Please follow its guidance.

### yt-dlp
[yt-dlp](https://github.com/yt-dlp/yt-dlp#installation) is a [youtube-dl](https://github.com/ytdl-org/youtube-dl) fork based on the now inactive youtube-dlc. The main focus of this project is adding new features and patches while also keeping up to date with the original project.

### FFmpeg
[FFmpeg](https://www.ffmpeg.org/) is a complete, cross-platform solution to record, convert and stream audio and video.

## INSTALLATION

We suggest creating a virtual environment. The python version doesn't matter.
```
conda create -n name python=3.x
```

Activate the virtual environment you created before installing the following things and using the script.

Install yt-dlp with pip. Follow the [guidance](https://github.com/yt-dlp/yt-dlp#installation) if there is any problem with that.
```
python3 -m pip install -U yt-dlp
```

Install other packages with pip by using the command:
```
pip install -r requirements.txt
```

Download [FFmpeg]((https://www.ffmpeg.org/)) with your version. You can also retrieve the source code through Git by using the command:
```
git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
```

## GET STARTED

- Store the target url list in a .txt file as [example](example.txt).
- Run the script `main.py` with arguments input.
  ```
  python main.py --url ${URL FILE}\
                --output ${OUTPUT PATH}\
                --suffix ${SUFFIX}\
                --h ${H}\
                --w ${W}
  ```
  ```
  python main.py --url ./example.txt --output ./output --suffix .png --h 360 --w 640
  ```
- The dataset will be organized as:
  ```
  ├── output
     ├── 0
     │   ├── 0001.png
     │   ├── 0002.png
     │   ├── 0003.png
     │   ├── 0004.png
     │   ├── ...
     │   └── 0116.png
     ├── 1
     │   ├── 0001.png
     │   ├── 0002.png
     │   ├── 0003.png
     │   ├── 0004.png
     │   ├── ...
     │   └── 0116.png
     ├── 0.mp4
     └── 1.mp4
  ```

## TODO

Parallel command