# License Plate Recognition

Create new environment then install the proper libraries.

run `yoloscript.py`
then `mainscript.py`

`mainscript.py` grabs images from `./resultsimg` so try to detect the object first before running it to avoid errors.

If both scripts "succeeds" metadata will be collected in `results.txt`

### Limitations
If run right after another, `cv2.imwrite` overwrites the images in sequences starting from zero, however it does not update its date created property.
`os.path.getctime` gets date created time for the images therefore messing with the main script before eventually catching up.

**Solution**:
Delete or backup `./resultsimg/*` images somewhere else, then re-run `yoloscript.py` and `mainscript.py`

# Installation
This is application of ALPR uses:
1. YOLOv8 Pipeline
2. Paddlepaddle Pipeline

The main problem of using this is Paddle, for some reason wants the user to install CUDA and cuDNN on the PC.
The version I used is:

  `CUDA 11.8`

  `cuDNN 8.x`

Other requirements will be in requirements.txt

## YOLO

I recommend creating a virtual environment with Conda, then after installing YOLO, reinstall Torch with CUDA.
     
     pip install 
     pip uninstall torch torchvision torchaudio
     pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

## PADDLE
For installing Paddle refer to this PaddleOCR Quickstart Guide:

https://github.com/PaddlePaddle/PaddleOCR/blob/main/doc/doc_en/quickstart_en.md

For its CUDA (Windows):

https://www.paddlepaddle.org.cn/en/install/quick?docurl=/documentation/docs/en/install/pip/windows-pip_en.html
