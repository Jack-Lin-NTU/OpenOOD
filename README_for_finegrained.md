# Fine-grained customization

## 1. Prepare the dataset

### 1.1 Download the dataset and put them to the right place

Download the datasets from [google drive](https://drive.google.com/drive/u/0/folders/180JZOQyz1SZ4uOIvD8TmeODZpi-VIiyX)

Put the downloaded datasets to the right place:

```text
data/bird
data/butterfly
data/car
```

### 1.2 Preprocess the dataset

```bash
pip install ipython
bash data_processing/process_bird.sh
bash data_processing/process_butterfly.sh
bash data_processing/process_car.sh
```

## 2. Evalation

Please refer to the [script](./scripts/eval_ood_bird-finegrained.py)

Noted: I use docker to run the script for the convenience of the environment.

### 2.1 build docker

```bash
bash docker/build.sh
bash docker/run.sh bash scripts/demo_bird-finegrained.sh
bash docker/run.sh bash scripts/demo_butterfly-finegrained.sh
bash docker/run.sh bash scripts/demo_car-finegrained.sh
```

## 3. Train

Please refer to the [script](./scripts/train_bird-finegrained.sh)

```bash
bash scripts/train_bird-finegrained.sh
```
