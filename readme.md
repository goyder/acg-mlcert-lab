# ACG Modelling Lab

The purpose of this project is to capture the ACloud Guru modelling lab.

## Process

Within this lab, we wish to:

* Explore and examine the dataset in order to create a dataset ready for analysis
* Applying transformations and uploading the data to S3, where it is available for modelling
* Apply a suitable algorithm via SageMaker
* Interpret the results.

## In more detail

### Exploration

Initial exploration of the dataset is to take place in a Jupyter Lab environment.

We are interested in determining:

* What columns are relevant to our analysis?
* What filtering and cleaning will need to take place?
* What is the distribution of the key variables?
* What does the distribution of points around the globe look like?

The end point of this process is to define a "spec" for a data cleaning tool.

### Data transformation and upload

In this section, we will develop a pipeline to:

* Apply transformations (as determined in the previous step)
* Create an output dataset that can be uploaded to S3
    * Including a unique name for traceability
* Upload it to S3

This could be executed either in a Notebook or as independent command-line scripts. I tend towards the latter.

### Apply a suitable algorithm via SageMaker

Here, we will:

* Take the input dataset we have generated in the previous step
* Apply a k-means algorithm to it
* Retrieve the results

### Interpret the results

We will take the results back and plot them. 

This can take place in the Jupyter environment.

## K-means in SageMaker

Documentation for the K-means algo includes:
* [Algorithm homepage](https://docs.aws.amazon.com/sagemaker/latest/dg/k-means.html)
* [Hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/k-means-api-config.html)
* [How does K-means work?](https://docs.aws.amazon.com/sagemaker/latest/dg/algo-kmeans-tech-notes.html)

Some basic requirements for the model are:

* Tabular data 
* Of continuous variables 
* Where the `n` features correspond to `n` dimensional space to group the points in.