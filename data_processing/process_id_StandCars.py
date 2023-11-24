from pathlib import Path
from shutil import copyfile

from fire import Fire
from rich.progress import track


def get_file_and_labels(txt_file):
    with open(txt_file, 'r') as f:
        lines = f.readlines()
    files = ['images' + '/' + Path(x.split(' ')[0]).name for x in lines]
    labels = [str(int(x.split(' ')[1]) - 1) for x in lines]
    return files, labels


def main(
    data_folder='data/fine-grained/car/ID/StandCars',
    output_folder='data/fine-grained/processed/benchmark_imglist',
    output_image_folder='data/fine-grained/processed/images_finegrained',
):
    data_folder = Path(data_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(exist_ok=True, parents=True)
    output_image_folder = Path(output_image_folder)
    output_image_folder.mkdir(exist_ok=True, parents=True)

    files, labels = get_file_and_labels(data_folder / 'car_train.txt')
    outs = []
    for file, label in track(list(zip(files, labels)), description='Processing train files'):
        src_file = data_folder / file
        relative_path = Path(data_folder.name, file)
        output_img_path = output_image_folder / relative_path
        output_img_path.parent.mkdir(exist_ok=True, parents=True)
        copyfile(src_file, output_img_path)
        outs.append([str(relative_path), label])

    with open(output_folder / 'train_StandCars.txt', 'w') as f:
        for line in outs:
            f.write(' '.join(line) + '\n')

    files, labels = get_file_and_labels(data_folder / 'car_test.txt')
    outs = []
    for file, label in track(list(zip(files, labels)), description='Processing test files'):
        src_file = data_folder / file
        relative_path = Path(data_folder.name, file)
        output_img_path = output_image_folder / relative_path
        output_img_path.parent.mkdir(exist_ok=True, parents=True)
        copyfile(src_file, output_img_path)
        outs.append([str(relative_path), label])

    with open(output_folder / 'test_StandCars.txt', 'w') as f:
        for line in outs:
            f.write(' '.join(line) + '\n')


Fire(main)
