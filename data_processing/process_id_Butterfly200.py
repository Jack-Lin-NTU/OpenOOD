from pathlib import Path
from shutil import copyfile

from fire import Fire
from rich.progress import track


def get_files(txt_file):
    with open(txt_file, 'r') as f:
        lines = f.readlines()
    return [x.split(' ')[0] for x in lines]


def main(
    data_folder='data/fine-grained/butterfly/ID/Butterfly200',
    output_folder='data/fine-grained/processed/benchmark_imglist',
    output_image_folder='data/fine-grained/processed/images_finegrained',
):
    data_folder = Path(data_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(exist_ok=True, parents=True)
    output_image_folder = Path(output_image_folder)
    output_image_folder.mkdir(exist_ok=True, parents=True)

    files = get_files(data_folder / 'Butterfly200_train_release.txt')
    outs = []
    for file in track(files, description='Processing train files'):
        relative_path = Path(data_folder.name, 'images', file)
        output_img_path = output_image_folder / relative_path
        output_img_path.parent.mkdir(exist_ok=True, parents=True)
        copyfile(Path(data_folder, 'images', file), output_img_path)
        outs.append([str(relative_path), str(int(file.split('.')[0]) - 1)])

    with open(output_folder / 'train_Butterfly200.txt', 'w') as f:
        for line in outs:
            f.write(' '.join(line) + '\n')

    files = get_files(data_folder / 'Butterfly200_val_release.txt')
    outs = []
    for file in track(files, description='Processing val files'):
        relative_path = Path(data_folder.name, 'images', file)
        output_img_path = output_image_folder / relative_path
        output_img_path.parent.mkdir(exist_ok=True, parents=True)
        copyfile(Path(data_folder, 'images', file), output_img_path)
        outs.append([str(relative_path), str(int(file.split('.')[0]) - 1)])

    with open(output_folder / 'val_Butterfly200.txt', 'w') as f:
        for line in outs:
            f.write(' '.join(line) + '\n')

    files = get_files(data_folder / 'Butterfly200_test_release.txt')
    outs = []
    for file in track(files, description='Processing test files'):
        relative_path = Path(data_folder.name, 'images', file)
        output_img_path = output_image_folder / relative_path
        output_img_path.parent.mkdir(exist_ok=True, parents=True)
        copyfile(Path(data_folder, 'images', file), output_img_path)
        outs.append([str(relative_path), str(int(file.split('.')[0]) - 1)])

    with open(output_folder / 'test_Butterfly200.txt', 'w') as f:
        for line in outs:
            f.write(' '.join(line) + '\n')


Fire(main)
