
# Automatic Radiographic hand bone segment using Yolo

Build environment:
Windows 10 WSL2 Ubuntu 18.04
CUDA 11.0.228

Read following for setting up environment:
- [EN] https://towardsdatascience.com/custom-object-detection-using-darknet-9779170faca2
- [CN] https://blog.csdn.net/weixin_42769131/article/details/86472775

Need to install following before running make:
```bash
sudo apt install make gcc g++ python2
```

Run dos2unix to baa-obj.data and train.txt and val.txt, otherwise it willl complain about file not found error.

Run following command to start training:
```bash
./darknet detector train data/baa/baa-obj.data data/baa/yolov3-tiny.cfg darknet53.conv.74
```

# Build Darknet with CUDA 11 on Ubuntu 18.04 WSL2

Read following for setting up environment:
- https://docs.nvidia.com/cuda/wsl-user-guide/index.html
- https://blog.csdn.net/gzroy/article/details/111190131?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-0&spm=1001.2101.3001.4242 
- https://stackoverflow.com/questions/63497928/ubuntu-wsl-with-docker-could-not-be-found 
- https://blog.csdn.net/qq_40423339/article/details/87885086 

Run following command to verify installation success:
```
docker run --gpus all --env NVIDIA_DISABLE_REQUIRE=1 nvcr.io/nvidia/k8s/cuda-sample:nbody nbody -gpu -benchmark
```
