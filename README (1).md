# Plant Disease Classification

A deep learning project for classifying plant leaf images as healthy or
diseased using convolutional neural networks (a custom CNN and an
EfficientNetB0 transfer-learning model).

## Project Structure

```
plant-disease-classification/
│
├── app.py                     # Inference app (Streamlit/CLI)
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── .gitignore
│
├── notebooks/
│   └── plant_disease_classification.ipynb   # Training & EDA notebook
│
├── models/
│   ├── plant_disease_cnn.keras              # Custom CNN model
│   └── plant_disease_efficientnetb0.keras   # EfficientNetB0 model
│
├── assets/
│   ├── demo.png                # App/demo screenshot
│   └── confusion_matrix.png    # Model evaluation plot
│
└── data/
    └── README.md               # Dataset instructions
```

## Setup

```bash
git clone <your-repo-url>
cd plant-disease-classification
pip install -r requirements.txt
```

## Usage

### Train / explore
Open `notebooks/plant_disease_classification.ipynb` to see data
preparation, model training, and evaluation.

### Run inference
```bash
python app.py path/to/leaf_image.jpg
```

or, if using Streamlit:
```bash
streamlit run app.py
```

## Models

| Model | Description |
|---|---|
| `plant_disease_cnn.keras` | Custom CNN trained from scratch |
| `plant_disease_efficientnetb0.keras` | EfficientNetB0 fine-tuned via transfer learning |

## Data

See [`data/README.md`](data/README.md) for dataset download and setup
instructions.

## Results

Evaluation plots (e.g. confusion matrix) are available in `assets/`.

## License

Add your license here.
