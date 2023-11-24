from pathlib import Path
from shutil import copyfile

from fire import Fire
from rich.progress import track


def main(
    data_folder='data/fine-grained/car/OOD/compcar',
    output_folder='data/fine-grained/processed/benchmark_imglist',
    output_image_folder='data/fine-grained/processed/images_finegrained',
):
    data_folder = Path(data_folder)
    files = list(data_folder.rglob('data/image/**/*.jpg'))
    output_folder = Path(output_folder)
    output_folder.mkdir(exist_ok=True, parents=True)
    output_image_folder = Path(output_image_folder)
    output_image_folder.mkdir(exist_ok=True, parents=True)
    # get train txt
    outs = []
    for file in track(files, description='Processing files'):
        relative_path = file.relative_to(data_folder.parent)
        output_img_path = output_image_folder / relative_path
        output_img_path.parent.mkdir(exist_ok=True, parents=True)
        copyfile(file, output_img_path)
        outs.append([str(relative_path), str(-1)])
    outs = sorted(outs, key=lambda x: x[1])
    with open(output_folder / 'test_compcar.txt', 'w') as f:
        for line in outs:
            f.write(' '.join(line) + '\n')


Fire(main)
