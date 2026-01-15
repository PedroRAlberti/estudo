from the_well.data import WellDataset
from torch.utils.data import DataLoader

# The following line may take a couple of minutes to instantiate the datamodule
trainset = WellDataset(
    well_base_path="hf://datasets/polymathic-ai/",  # access from HF hub
    well_dataset_name="active_matter",
    well_split_name="train",
)
train_loader = DataLoader(trainset)