
# Automatic Radiographic hand bone segment using Yolo

Build environment:
Windows 10 WSL2 Ubuntu 18.04
CUDA 11.0.228

Read following for setting up environment:
[EN] https://towardsdatascience.com/custom-object-detection-using-darknet-9779170faca2
[CN] https://blog.csdn.net/weixin_42769131/article/details/86472775

Need to install following before running make:
```bash
sudo apt install make gcc g++ python2
```

Run dos2unix to baa-obj.data and train.txt and val.txt, otherwise it willl complain about file not found error.

Run following command to start training:
```bash
./darknet detector train data/baa/baa-obj.data data/baa/yolov3-tiny.cfg darknet53.conv.74
```
