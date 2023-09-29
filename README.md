# Oral Cancer

## Installation and Setup

<details><summary> <b>Expand for installation steps</b> </summary>

### Creating a Virtual Environment

To avoid version conflicts with existing Python packages, it is recommended to create a separate virtual environment using `virtualenv` and `virtualenvwrapper`:

```shell
mkvirtualenv oral_cancer_env  # This will create and activate the virtual environment
workon oral_cancer_env
```

This assumes that the user has `virtualenv` and `virtualenvwrapper` installed.

```shell
#Clone this repository to your local machine:
git clone https://github.com/ASADEL-TECHNOLOGIES/oralcancer.git
cd oralcancer
```

### Install the dependencies
```shell
#Install the required Python packages:
pip install -r requirements.txt

#Install PyTorch, torchvision, and torchaudio:
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

#Install Weights & Biases:
pip install wandb
```
Note: Please check for the latest stable version of PyTorch [here](https://pytorch.org/get-started/locally/).

</details>

### Download the dataset:

The dataset is stored in an AWS S3 bucket. Use the following AWS CLI command to sync the dataset to your local machine:
``` shell
aws s3 sync s3://oralcancer/5k_dataset/ ./dataset/
```
Note: Downloading the dataset might require admin privileges. If you do not have the required access, you can use a custom dataset. Ensure the directory structure is as follows:

```shell
-dataset/
   |
   ├── train/
   |    ├── images/
   |    └── labels/
   |
   ├── val/
   |    ├── images/
   |    └── labels/
   |
   └── test/
        ├── images/
        └── labels/

```

### Downloading Pre-trained Weights
For our use case, we use the standard model weights from [YOLOv7](https://github.com/WongKinYiu/yolov7/releases). You can also experiment with other weights available.
```shell
wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt
```

## Training
```shell
#To train the model with custom weights on your dataset, run the following command:
python train.py --weights yolov7.pt --data data/data.yaml --batch-size 32 --cfg yolov7.yaml --workers 4 --device 1 --linear-lr --noautoanchor --project 'give your project name' --name 'give a name for the run' --epoch 40
```
you can download the custom weight: [`oralcancer.pt`]()
```shell 
#You can also train the model using our custom weights:
python train.py --weights oralcancer.pt --data data/data.yaml --batch-size 32 --cfg yolov7.yaml --workers 4 --device 1 --linear-lr --noautoanchor --project 'give your project name' --name 'give a name for the run' --epoch 40
```

## Inference

```shell
#To perform inference on a new image, use the detect.py script:
python detect.py --weights 'choose which weights to use' --conf 0.25 --img-size 640 --source <source-of-your-image>

