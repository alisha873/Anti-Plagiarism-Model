from transformers import RobertaTokenizer, RobertaModel  #used to load codebert
import torch #handle tensors
import numpy as np  #to convert final embeddings to useful array

tokenizer=RobertaTokenizer.from_pretrained("microsoft/graphcodebert-base")
model=RobertaModel.from_pretrained("microsoft/graphcodebert-base")

def embed_code(code):
    inputs= tokenizer(code,return_tensors="pt",truncation=True,max_length=512) #converts code to tokenid and code is truncated to 512 if too long and the output is in the form of PyTorch tensors
    with torch.no_grad():
        outputs=model(**inputs) #runs tokenized input through codebert, **inputs basically unpacks the dictionary we get from inputs
        embeddings=outputs.last_hidden_state #list of embeddings one for each token in the list
        avg_embedding=torch.mean(embeddings,dim=1).squeeze().numpy()
        return avg_embedding
    
