# Oral Cancer

Download the dataset:

``` shell
aws s3 sync s3://oralcancer/5k_dataset/ ./dataset/
```
Download the weight: More can be found [here](https://github.com/WongKinYiu/yolov7/releases):

```shell
cd yolov7
wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt
```
Run the model to train on custom data:

```shell
python train.py --weights yolov7.pt --data data/data.yaml --batch-siz 32 --project 'give any name' --name 'give name'
```