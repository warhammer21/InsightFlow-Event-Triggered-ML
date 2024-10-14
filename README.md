# InsightFlow

## Overview

**InsightFlow** is a machine learning-powered application designed to provide instant insights from user-uploaded datasets. The application leverages an event-driven architecture that enables seamless data processing and prediction functionalities, allowing users to upload data and receive predictions in a reliable, user-friendly manner.

## Architecture

### Event-Driven Architecture

InsightFlow is built upon a loosely coupled event-driven architecture, which enhances flexibility, scalability, and maintainability. In this architecture:

- **Cloud Storage**: Users upload their datasets to a Google Cloud Storage bucket.
- **Cloud Functions**: Triggers are set up to respond to changes in the storage bucket, invoking Cloud Functions that handle data processing and task management.
- **Cloud Tasks**: These functions create asynchronous tasks, sending data to the prediction API, allowing for efficient task management and processing.

### Choreography and Orchestration

The system employs a blend of choreography and orchestration:

- **Choreography**: Individual components communicate through events, where each service reacts to changes in state without central control. For instance, when a file is uploaded to Cloud Storage, the corresponding Cloud Function is triggered automatically, reacting to the event.
  
- **Orchestration**: Certain processes are orchestrated to ensure proper flow and management of tasks. For example, Cloud Functions manage the interaction between the Cloud Storage bucket and the prediction API by orchestrating how data is sent and tasks are created.

This hybrid approach allows for a robust, responsive system that can easily adapt to changes in requirements and scale as needed.

## Features

- **Seamless Data Upload**: Users can upload datasets directly to Cloud Storage.
- **Instant Predictions**: The application provides real-time predictions based on the uploaded data.
- **Event-driven Processing**: The architecture allows for reactive processing of data, ensuring efficient resource utilization.

## Getting Started

### Prerequisites

- Google Cloud Platform account
- Access to Google Cloud Storage, Cloud Functions, and Cloud Tasks

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/insightflow.git
