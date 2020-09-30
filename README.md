# RobertaGithubIssuesClassification
 Repo for ML model to classify Github Issues using Roberta from Huggingface library.

## Overview

 The dataset is taken from https://github.com/dotnet/machinelearning-samples/tree/master/samples/CLI/MulticlassClassification_CLI.
 I wanted to try and compare how a Deep Learning approach would do.
 At the moment, the result is basically the same (around 80% accuracy), but with a much bigger model for the DL.
 Next steps is to try and change hyperparams to improve.

 I preprocess the dataset and train with TF2 using a Roberta base model.
 I also generate an ONNX model from the resulting model to use in a C# app (check my other repo).
 Generating the ONNX model required to transform the TF2 model to Pytorch first (easy using HuggingFace library) and creating the ONNX model from it, because creating from TF2 resulted in a botched ONNX model (not sure what the issue is ...).

 I also used the occasion to try out using Pytorch Lightning (PL). The model trains but this is still a work in progress at the moment.


