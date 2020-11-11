* Here are the 67 SVM weak defenses and 1 SVM undefended model (model-mnist-svm-clean.pkl) in the SVM Athena.

* We will not use the undefended svm model in this project.

* Each weak defense is a supervised image classifier that is associated with one transformation. A weak defense is named in the pattern of "model-<dataset>-<model_type>-<transformation>.pkl", where dataset is "mnist" and model_type is "svm".

* **Some models are compressed (``.zip`` packages) because their size exceed the limit of GitHub.** You need to unzip the packages to get the model.

* The list of transformations is the same as that for the ``cnn`` models (but **1** items shorter: ``model-mnist-svm-cartoon_gaussian_type3.pkl``).
