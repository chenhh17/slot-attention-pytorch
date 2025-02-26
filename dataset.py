import os
from PIL import Image
from torchvision import transforms
from torch.utils.data import Dataset

your_path = os.path.dirname(os.path.abspath(__file__))


class PARTNET(Dataset):
    def __init__(self, split='train'):
        super(PARTNET, self).__init__()
        
        assert split in ['train', 'val', 'test']
        self.split = split
        self.root_dir = your_path
        self.files = os.listdir(self.root_dir)
        self.img_transform = transforms.Compose([
               transforms.ToTensor()])

    def __getitem__(self, index):
        path = self.files[index]
        image = Image.open(os.path.join(
            self.root_dir, path, "0.png")
            ).convert("RGB")
        image = image.resize((128, 128))
        image = self.img_transform(image)
        sample = {'image': image}

        return sample

    def __len__(self):
        return len(self.files)
