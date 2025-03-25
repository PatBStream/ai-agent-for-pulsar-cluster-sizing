# AI Agent for Apache Pulsar Sizing and Configuration
## Overview
This AI Agent assists in determining the optimal size and configuration of an Apache Pulsar deployment. It provides recommendations on the number of Brokers and Bookies, along with best practices and configuration options tailored to your system's requirements.​

### Features
> **Broker and Bookie Sizing:** Calculates the recommended number of Brokers and Bookies based on your messaging throughput and storage needs.​

> **Configuration Recommendations:** Suggests optimal configurations for hardware resources, including CPU, memory, and storage, to ensure efficient operation.​

> **Best Practices Guidance:** Offers insights into best practices for deploying and managing Apache Pulsar clusters, including replication strategies and hardware considerations.​

## How to use
To generate accurate recommendations, the agent works best when the following inputs are provided:

> - **Desired Messaging Throughput:** Specify the target number of messages per second your system needs to handle.​
> - **Message Size:** Provide the average size of the messages (in KB or MB).​

> - **Data Retention Period:** Indicate how long messages should be retained within the system.​

> - **# of Consumers:** Provide an estimate of the total number of Consumers for these messages.  For example, 10 unique Consumers for each message produced, so a total of 10 Consumers.

> - **Hardware Specifications (optional):** Detail the available CPU, memory, and storage resources to tailor recommendations accordingly.​

## Run the Agent
**Update the main.py** file are stated in the comments with your specific Pulsar requirements.  

Then run the agent:
```
$ python3 -m venv mypulsaragent
(mypulsaragent)$ pip install -r requirements.txt
(mypulsaragent)$ export OPENAI_API_KEY='cat my_openai_key.txt`
(mypulsaragent)$ python3 main.py
```

## Recommended Sizing Output
The agent will create a "recommendations.md" file based on the inputs:

Number of Brokers: Recommended count to achieve desired throughput and redundancy.​
Number of Bookies: Suggested number to handle storage requirements and ensure data durability.​

**Hardware Recommendations:**
Brokers: Suggested CPU, memory, and storage configurations.​
Bookies: Recommended hardware specifications for optimal performance.​
Configuration Settings: Proposed settings for Apache Pulsar configurations, including replication settings, data retention policies, and storage configurations.​
Best Practices: Guidelines on deployment strategies, hardware selection, and performance tuning.​

## Assumptions
This AI Agent assumes you have access and setup OpenAI API "key" to interact with OpenAI models.