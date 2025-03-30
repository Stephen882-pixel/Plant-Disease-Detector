import torch
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
from torchvision import models
import io

# List of plant diseases your model can detect
DISEASE_CLASSES = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    # Add more disease classes as per your model
]

def get_model():
    # Load a pre-trained ResNet model
    model = models.resnet50(pretrained=True)
    
    # Modify the final layer to match our number of classes
    num_ftrs = model.fc.in_features
    model.fc = torch.nn.Linear(num_ftrs, len(DISEASE_CLASSES))
    
    # Load your fine-tuned weights
    # model.load_state_dict(torch.load('path_to_your_model_weights.pth'))
    
    # For this example, we'll use a pre-trained model without fine-tuning
    # In a real application, you would load your fine-tuned weights
    
    model.eval()  # Set to evaluation mode
    return model

def predict_disease(image_bytes):
    """
    Take an image and return the predicted disease
    """
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    image_tensor = transform(image).unsqueeze(0)
    
    # Load model (in production, you'd cache this)
    model = get_model()
    
    # Make prediction
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted = torch.max(outputs, 1)
    
    return DISEASE_CLASSES[predicted.item()]