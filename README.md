# Student Performance Prediction (SPP)

 This project aims to predict the final grade`G3` student can get by taking his/her studytime, previous markings, class attendance and related informations.

 ## Dataset
 This dataset came from the Machine Learning Repository hosted by UCI(University of California,Irvine).
 I didn't used Gits or Respo of fellow developers as the official dataset is untouched, citable source.

 files:
 - student-mat.csv
 - student-por.csv
 - student.txt
 - student-merge.R
 This project currently uses student-mat.csv only.

 ## Status
Created a separate virtual environment .venv with `py -m venv .venv`. It is done so that each project gets its own private set of packages, so one project's need can't break another's and also to avoid version conflicts as different projects can use different versions of the same packages.

 ## Packages installed:
  1. Pandas(3.1.1): Loads and handles tabular data as Dataframes.
     Used for exploring and cleaning the student dataset.
  2. Scikit-learn(1.9.1): The machine learning library.
     Used later for models train/test splits and metrics.