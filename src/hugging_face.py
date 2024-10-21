# hf_dataset.py

from datasets import Dataset, DatasetDict
from datasets import load_dataset, load_metric
import pandas as pd
import os

class HFDataset:
    def __init__(self, df, dataset_name, task='text-classification'):
        self.df = df
        self.dataset_name = dataset_name
        self.task = task
    
    def create_dataset(self):
        """Convert DataFrame to Hugging Face Dataset"""
        self.dataset = Dataset.from_pandas(self.df)
        return self.dataset
    
    def save_dataset(self, path="data/"):
        """Save dataset to disk"""
        if not os.path.exists(path):
            os.makedirs(path)
        self.dataset.save_to_disk(f"{path}/{self.dataset_name}")
        print(f"Dataset saved to {path}/{self.dataset_name}")
    
    def upload_to_hf(self, token):
        """Upload dataset to Hugging Face Hub"""
        from huggingface_hub import HfApi, HfFolder
        HfFolder.save_token(token)
        api = HfApi()
        api.upload_folder(repo_id=f"{self.dataset_name}", 
                          folder_path=f"data/{self.dataset_name}", 
                          repo_type="dataset", 
                          path_in_repo=".")
        print(f"Dataset {self.dataset_name} uploaded to Hugging Face Hub.")

# Usage example:
if __name__ == "__main__":
    # Example DataFrame
    data = {'text': ['Hello world!', 'Hugging Face rocks!'], 'label': [0, 1]}
    df = pd.DataFrame(data)
    
    # Instantiate HFDataset class
    hf_dataset = HFDataset(df, 'my_dataset')
    
    # Create dataset
    dataset = hf_dataset.create_dataset()
    print(dataset)
    
    # Save dataset
    hf_dataset.save_dataset()
    
    # Upload to Hugging Face (replace 'YOUR_HF_TOKEN' with your actual token)
    # hf_dataset.upload_to_hf('YOUR_HF_TOKEN')
