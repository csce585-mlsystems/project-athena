# Structure of Athena Project
**Open issues on [GitHub](https://github.com/csce585-mlsystems/project-athena/issues) if there are any questions.**

1. ``data``, where the baseline adversarial examples locate. Check the readme.md in the ``data`` folder for detailed descriptions.
2. ``documnets``, where all the project documents (e.g., requirements) locate.
3. ``models``, where the weak defenses in the vanilla version of Athena locate. Check the readme.md in the ``models`` foler for detailed descriptions.
4. ``notebooks``, where the jupyture notebooks or markdown notes locate.
5. ``src``, where the source codes locate.
    1. ``attacks`` --- scripts implemented adversarial attacks.
    2. ``configs`` --- configuration files.
    3. ``models`` --- scripts related to models. Currently, we have model wrappers and definition of the ensemble model here.
    4. ``scripts`` --- scripts for experiments.
    5. ``tutorials`` --- Athena tutorials.
    5. ``utils`` --- utility functions.