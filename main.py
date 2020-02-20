import imageio
import os

video = os.path.abspath('video.mp4')


def gif_converter(inputPath, targetFormat):
    output_path = os.path.splitext(inputPath)[0] + targetFormat

    print(f'converting {inputPath} \n to {output_path}')

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(output_path, fps=fps)

    for image in reader:
        writer.append_data(image)
        print(f'Image {image}')

    print('Finished')
    writer.close()


gif_converter(video, '.gif')
