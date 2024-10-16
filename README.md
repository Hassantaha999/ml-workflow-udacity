# ML Workflow fo Scones Unlimited on Amazon Sagemker - Vehicle Image Classification Project

## Project Introduction

Welcome to the **Scones Unlimited** vehicle image classification project! This project aims to develop an image classification model that identifies the type of delivery vehicle (bicycle or motorcycle) used by delivery drivers. By classifying vehicles correctly, the logistics team can optimize the delivery process by routing different vehicle types to the most efficient loading bays and order assignments.

This image classifier will serve as a key component in **Scones Unlimited**'s operations, helping to:

- Detect delivery vehicles in real-time video feeds.
- Optimize order routing based on delivery vehicle type (bicycle for nearby orders, motorcycle for farther destinations).
- Enhance social media engagement through automated tagging of vehicle types in images.
- Detect defects in scones using similar image classification techniques.

## Background

Image classification is a powerful tool used across industries like autonomous vehicles, augmented reality, and medical diagnostics. In logistics, image classification can help automate processes, improve efficiency, and enhance decision-making.

At **Scones Unlimited**, we are leveraging machine learning to optimize delivery routes and make smarter logistics decisions. This project will build and deploy a vehicle classification model that helps route delivery vehicles based on their type, allowing us to assign delivery professionals with bicycles to nearby orders and motorcyclists to farther orders, streamlining our delivery operations.

This project is built using **AWS Sagemaker**, **AWS Lambda**, and **AWS Step Functions** to ensure a scalable, robust, and production-ready solution.

## Project Overview

The project is divided into the following steps:

### Step 1: Data Staging

- **Objective**: Collect and preprocess a dataset of images containing bicycles and motorcycles.
- **Tasks**: Organize images, split them into training and test sets, and ensure the dataset is ready for model training.

### Step 2: Model Training and Deployment

- **Objective**: Train an image classification model to differentiate between bicycles and motorcycles.
- **Tasks**: 
  - Use **AWS Sagemaker** to build and train the model.
  - Evaluate model performance using accuracy metrics.
  - Deploy the trained model on **AWS Sagemaker Endpoint** for real-time inference.

### Step 3: Lambda Functions and Step Function Workflow

- **Objective**: Build serverless services that interact with the image classifier.
- **Tasks**:
  - Develop **AWS Lambda** functions to interact with the Sagemaker model.
  - Design a workflow using **AWS Step Functions** to manage the lifecycle of the image classification requests and responses.

### Step 4: Testing and Evaluation

- **Objective**: Ensure the model and workflow are functioning correctly in a production environment.
- **Tasks**:
  - Test the deployment using a set of new images.
  - Monitor model performance and scalability.
  - Implement safeguards to detect performance degradation or model drift.

### Step 5: Optional Challenge

- **Objective**: Extend the solution.
- **Tasks**: Add extra features such as real-time video feed integration or defect detection for scones.

### Step 6: Cleanup Cloud Resources

- **Objective**: Deallocate and clean up cloud resources after the project is complete.
- **Tasks**:
  - Delete unused **AWS Sagemaker** endpoints, **Lambda** functions, **Step Functions**, and any other associated cloud resources.

## Tech Stack

- **AWS Sagemaker**: Used for model training and deployment.
- **AWS Lambda**: Serverless functions to handle requests and interact with the Sagemaker endpoint.
- **AWS Step Functions**: Orchestrates the workflow and integrates the various services.
- **Python**: Core programming language used for data preprocessing, model building, and scripting.

## Future Enhancements

- **Add more vehicle classes**: Expand the model to classify additional types of delivery vehicles (e.g., cars, trucks).
- **Real-time video classification**: Extend the model to work on live video feeds for real-time vehicle detection.
- **Scone defect detection**: Use similar image classification techniques to automatically detect defects in scones.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Scones Unlimited** © 2024. All rights reserved.
