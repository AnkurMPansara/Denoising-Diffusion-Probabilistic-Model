import os
import glob
from PIL import Image
from tqdm import tqdm

class ImagePreprocessor:
    def __init__(self, input_dir, output_dir, image_ext='jpg', target_size=(480, 704)):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.image_ext = image_ext
        self.target_size = target_size

        self.resize_images()

    def resize_images(self):
        os.makedirs(self.output_dir, exist_ok=True)

        image_paths = glob.glob(os.path.join(self.input_dir, '*', f'*.{self.image_ext}'))
        print(f"Found {len(image_paths)} images.")

        for idx, img_path in enumerate(tqdm(image_paths, desc='Resizing and Saving')):
            try:
                img = Image.open(img_path).convert('RGB')
                img_resized = img.resize((self.target_size[1], self.target_size[0]), Image.BICUBIC)
                img_resized.save(os.path.join(self.output_dir, f'{idx}.{self.image_ext}'))
            except Exception as e:
                print(f"Error processing {img_path}: {e}")

# Example usage:
# processor = ImagePreprocessor('your/input/path', 'your/output/path')
