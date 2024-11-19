# cintel-05-cintel

## Project Overview

"In this module, we'll look at integrating live data streams and how "data in motion" is different from "data at rest". You'll see a lot of water analogies when working with modern analytics and data flows. Industry uses data lakes, data pipelines, data warehouses, and data lake houses. In this module, we'll introduce some of those terms, primarily so you can converse in the language of live data and look up information as needed.

Our focus in this course will stay with designing and implementing the user interaction associated with live data streams. To that end, we will introduce a new data structure (called a deque) and approaches for applying machine learning to data in motion so we can enable live, continuous intelligence."

## Important Definitons

### Key Terms

- **Data at Rest vs. Data in Motion** Data at rest is stationary, stored data, unchanged until it is accessed or modified. In contrast, data in motion is actively transferring, such as streaming data from IoT devices. Data in motion requires different management, processing, and insight derivation approaches.

- **Traditional Methods vs. Live Data:** Traditional data analysis often relies on batch processing, suited for data at rest. However, live data's continuous and rapid nature requires real-time processing methods, making traditional batch processing ineffective for timely insights and actions.
Data Streams: These are sequences of data generated continuously by different data sources. Understanding data streams is crucial for real-time analytics and decision-making.

- **Continuous Intelligence (CI):** This is the practice of using real-time analytics to process data in motion. CI enables immediate insights and actions based on live data, contrasting with batch processing used for data at rest.

- **Deque (Double-Ended Queue):** A deque (pronounced "deck") is a data structure that allows insertion and removal of elements from both ends efficiently. In the context of live data, deques are useful for holding recent data points for quick analysis without the overhead of processing the entire stream. For example, a deque makes it easy to do analytics on the last, most recent 20 points. It enables continuously updated machine learning models reflecting the current trend. 

- **Data Lake:** A storage repository that holds a vast amount of raw data in its native format. Data lakes are flexible and can store both structured and unstructured data.

- **Data Warehouse:** A system used for reporting and data analysis, storing structured, filtered data that has already been processed for a specific purpose.

- **Data Pipeline:** A set of data processing elements connected in series, where the output of one element is the input of the next. Data pipelines are essential for moving and transforming data in motion.

- **Data Lakehouse:** A newer concept that combines elements of data lakes and data warehouses, offering the scalability and flexibility of lakes with the governance and performance of warehouses.

## Key Tools

- **Apache Kafka:** An open-source stream-processing software platform designed for handling real-time data feeds. Kafka is widely used for building real-time streaming data pipelines and applications. Example users include LinkedIn and Netflix. 

- **Apache Flink:** An open-source framework and distributed processing engine for stateful computations over data streams. Flink is designed for high throughput and low latency. Example users include Uber,  energy companies, and Alibaba (particularly during their annual Singles' Day (11/11) global shopping festival, processing billions of events in real-time).

- **Spark Streaming:** Part of Apache Spark, this tool enables scalable, high-throughput, fault-tolerant stream processing of live data streams. Example users include Netflix recommendations, Pinterest, eBay, and Amazon analytics. 

- **RabbitMQ:** An open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). RabbitMQ facilitates the efficient handling of messages in a distributed system, making it ideal for scenarios where high-throughput and reliable message delivery are required for data streams. Example users include Instagram and Reddit. 

- **Python Libraries for Streaming:** Libraries like Streamz, Faust, and Pulsar help work with streaming data in Python environments, integrating with common tools.

- **Streamz** is a simple option that works with Pandas

- **Faust**, built on Kafka, is scaleable and enables complex analysis

- **Pulsar** is a distributed system for high-throughput publish/subscribe systems that includes distributed storage and is used by Splunk, Yahoo, and Overstock. 

- **Python Data Structure for Streaming:**  We will use Python's collections.deque class to understand how you can manage recent data efficiently. We'll use the deque class in our project. 

## Create a GitHub Project Repo

Login to GitHub. Click Repositories. Create a new project repo named cintel-05-cintel with a default README.md and a default .gitignore for Python. 

Use the GitHub web interface to add a file named requirements.txt (exactly!) and click commit to save the file. In the most basic version of the Module 5 project, we may only need packages from the Python Standard Library - and those already included in the PyShiny Playground environment. If working in the browser, you likely won't need requirements.txt at all for this project. However, very few real applications do NOT need a requirements.txt file, so I'd say keep it around and use it as needed. If you work on the project locally (on your machine), you will need to requirements.txt and install various packages into your local project virtual environment. This is very common in real-world Python and great practice. 

Use the GitHub web interface to add a new empty file named app.py (exactly!)  and click commit to save the file. 

Verify your project repo has all 4 files:

- README.md
- .gitignore
- requirements.txt
- app.py (OR dashboard/app.py if working locally and deploying to GitHub pages - see more below).

If you decide to try the local development, you'll be able to deploy your live date site using GitHub Pages. To make it easy to build our app from a folder and export the app into the docs folder (for Pages), please move your app.py file into a folder. I named my folder "dashboard", so I have a dashboard/app.py file and no app.py in the root folder. This is a more common organization for Python projects.

Your code is safely stored in the cloud - you can copy from it (and improve it) as you work through this module and complete Project 5.  