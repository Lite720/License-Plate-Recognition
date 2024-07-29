# License-Plate-Recognition

This is application of ALPR uses:
1. YOLOv8 Pipeline
2. Paddlepaddle Pipeline

The main problem of using this is Paddle, for some reason wants the user to install CUDA and cuDNN on the PC.
The version I used is:
  CUDA 11.8
  cuDNN 8.x

Other requirements will be in requirements.txt

I recommend creating a virtual environment with Conda, then after installing YOLO, reinstall Torch with CUDA.
# use  : pip install 
#      : pip uninstall torch torchvision torchaudio
#      : pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118


For installing Paddle refer to this PaddleOCR Quickstart Guide:
# https://github.com/PaddlePaddle/PaddleOCR/blob/main/doc/doc_en/quickstart_en.md
For its CUDA (Windows):
# https://www.paddlepaddle.org.cn/en/install/quick?docurl=/documentation/docs/en/install/pip/windows-pip_en.html
