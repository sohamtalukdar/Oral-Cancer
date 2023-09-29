# Oral Cancer

## Using Docker (Recommended)

<details><summary> <b>Expand for Docker steps</b> </summary>

```shell
# Pull the Docker image
docker pull ghcr.io/asadel-technologies/yolov7-image:v0.2

# Run the Docker container (Adapt the command to your needs, such as mounting volumes, exposing ports, etc.)
docker run -it --rm ghcr.io/asadel-technologies/yolov7-image:v0.2
```

</details>

## Installation and Setup (Alternative Method)
 
<details><summary> <b>Expand for installation steps</b> </summary>

```shell
# Clone the Repository
git clone https://github.com/ASADEL-TECHNOLOGIES/oralcancer.git
cd oralcancer
# Create and Activate a Virtual Environment
mkvirtualenv yolov7
workon yolov7
# Install Dependencies
pip install -r requirements.txt
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
</details>

### Download the dataset:

Use the AWS CLI command below to sync the dataset from the AWS S3 bucket to your local machine:

``` shell
aws s3 sync s3://oralcancer/5k-dataset/ ./dataset/
```
Note: This may require admin privileges. If access is restricted, utilize a custom dataset and maintain the following directory structure:      

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
python train.py --weights yolov7.pt --data data/data.yaml --batch-size 32 --cfg yolov7.yaml --workers 4 --device 1 --linear-lr --noautoanchor --project <project-name> --name <run-name> --epoch 40
```
you can download the custom weight: [`oralcancer.pt`](https://github.com/ASADEL-TECHNOLOGIES/oralcancer/releases/download/v0.1/oralcancer.pt)
```shell 
#You can also train the model using our custom weights:
python train.py --weights oralcancer.pt --data data/data.yaml --batch-size 32 --cfg yolov7.yaml --workers 4 --device 1 --linear-lr --noautoanchor --project <project-name> --name <run-name> --epoch 40
```

## Inference

```shell
#To perform inference on a new image, use the detect.py script:
python detect.py --weights oralcancer.pt --conf 0.25 --img-size 640 --source <source-of-your-image>
```

**Note: Replace < project-name >, < run-name >, and < source-of-your-image > with your project name, run name, and the source of your image respectively.**