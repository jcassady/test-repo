# hf_dataset.py
from datasets import Dataset
import pandas as pd
import os
from huggingface_hub import HfApi, HfFolder

class HFDataset:
    def __init__(self, df, dataset_name):
        self.df = df
        self.dataset_name = dataset_name

    def create_dataset(self):
        self.dataset = Dataset.from_pandas(self.df)
        return self.dataset

    def save_dataset(self, path="data/"):
        os.makedirs(path, exist_ok=True)
        self.dataset.save_to_disk(f"{path}/{self.dataset_name}")
        print(f"Dataset saved to {path}/{self.dataset_name}")

    def upload_to_hf(self, token):
        HfFolder.save_token(token)
        api = HfApi()
        api.upload_folder(repo_id=f"{self.dataset_name}",
                          folder_path=f"data/{self.dataset_name}",
                          repo_type="dataset", path_in_repo=".")
        print(f"Dataset {self.dataset_name} uploaded to Hugging Face Hub.")

# Usage example:
if __name__ == "__main__":
    data = {'text': ['Hello world!', 'Hugging Face rocks!'], 'label': [0, 1]}
    df = pd.DataFrame(data)
    hf_dataset = HFDataset(df, 'my_dataset')
    print(hf_dataset.create_dataset())
    hf_dataset.save_dataset()
    # hf_dataset.upload_to_hf('YOUR_HF_TOKEN')
