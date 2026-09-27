# Data

This folder is a placeholder for the plant disease image dataset.
The raw data is not committed to the repository (see `.gitignore`).

## Suggested dataset

The [PlantVillage dataset](https://www.kaggle.com/datasets/emmarex/plantdisease)
is a commonly used dataset for this task, containing labeled images of
healthy and diseased plant leaves across multiple species.

## Expected structure

After downloading, organize the data as follows:

```
data/
├── train/
│   ├── class_1/
│   ├── class_2/
│   └── ...
├── val/
│   ├── class_1/
│   ├── class_2/
│   └── ...
└── test/
    ├── class_1/
    ├── class_2/
    └── ...
```

## Download steps

1. Download the dataset from Kaggle (or your source of choice).
2. Extract it into `data/`.
3. Split into `train/`, `val/`, and `test/` subfolders (an 80/10/10 split
   is a reasonable default), or update the notebook's data-loading cell
   to point at your own split.
