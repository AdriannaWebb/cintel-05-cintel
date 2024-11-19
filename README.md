# cintel-05-cintel

## Part 1

### Project Overview
___

"In this module, we'll look at integrating live data streams and how "data in motion" is different from "data at rest". You'll see a lot of water analogies when working with modern analytics and data flows. Industry uses data lakes, data pipelines, data warehouses, and data lake houses. In this module, we'll introduce some of those terms, primarily so you can converse in the language of live data and look up information as needed.

Our focus in this course will stay with designing and implementing the user interaction associated with live data streams. To that end, we will introduce a new data structure (called a deque) and approaches for applying machine learning to data in motion so we can enable live, continuous intelligence."

### Important Definitons
---
#### Key Terms

- **Data at Rest vs. Data in Motion** Data at rest is stationary, stored data, unchanged until it is accessed or modified. In contrast, data in motion is actively transferring, such as streaming data from IoT devices. Data in motion requires different management, processing, and insight derivation approaches.

- **Traditional Methods vs. Live Data:** Traditional data analysis often relies on batch processing, suited for data at rest. However, live data's continuous and rapid nature requires real-time processing methods, making traditional batch processing ineffective for timely insights and actions.
Data Streams: These are sequences of data generated continuously by different data sources. Understanding data streams is crucial for real-time analytics and decision-making.

- **Continuous Intelligence (CI):** This is the practice of using real-time analytics to process data in motion. CI enables immediate insights and actions based on live data, contrasting with batch processing used for data at rest.

- **Deque (Double-Ended Queue):** A deque (pronounced "deck") is a data structure that allows insertion and removal of elements from both ends efficiently. In the context of live data, deques are useful for holding recent data points for quick analysis without the overhead of processing the entire stream. For example, a deque makes it easy to do analytics on the last, most recent 20 points. It enables continuously updated machine learning models reflecting the current trend. 

- **Data Lake:** A storage repository that holds a vast amount of raw data in its native format. Data lakes are flexible and can store both structured and unstructured data.

- **Data Warehouse:** A system used for reporting and data analysis, storing structured, filtered data that has already been processed for a specific purpose.

- **Data Pipeline:** A set of data processing elements connected in series, where the output of one element is the input of the next. Data pipelines are essential for moving and transforming data in motion.

- **Data Lakehouse:** A newer concept that combines elements of data lakes and data warehouses, offering the scalability and flexibility of lakes with the governance and performance of warehouses.

#### Key Tools

- **Apache Kafka:** An open-source stream-processing software platform designed for handling real-time data feeds. Kafka is widely used for building real-time streaming data pipelines and applications. Example users include LinkedIn and Netflix. 

- **Apache Flink:** An open-source framework and distributed processing engine for stateful computations over data streams. Flink is designed for high throughput and low latency. Example users include Uber,  energy companies, and Alibaba (particularly during their annual Singles' Day (11/11) global shopping festival, processing billions of events in real-time).

- **Spark Streaming:** Part of Apache Spark, this tool enables scalable, high-throughput, fault-tolerant stream processing of live data streams. Example users include Netflix recommendations, Pinterest, eBay, and Amazon analytics. 

- **RabbitMQ:** An open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). RabbitMQ facilitates the efficient handling of messages in a distributed system, making it ideal for scenarios where high-throughput and reliable message delivery are required for data streams. Example users include Instagram and Reddit. 

- **Python Libraries for Streaming:** Libraries like Streamz, Faust, and Pulsar help work with streaming data in Python environments, integrating with common tools.

- **Streamz** is a simple option that works with Pandas

- **Faust**, built on Kafka, is scaleable and enables complex analysis

- **Pulsar** is a distributed system for high-throughput publish/subscribe systems that includes distributed storage and is used by Splunk, Yahoo, and Overstock. 

- **Python Data Structure for Streaming:**  We will use Python's collections.deque class to understand how you can manage recent data efficiently. We'll use the deque class in our project. 

### Create a GitHub Project Repo
---
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

## Part 2
### Overview
---
Learn about the Python collections.deque data structure and how and why it's useful for managing the most recent data in a stream.  The deque data structure class comes from the collections package.  (Along with many other helpful collections - it's worth looking atLinks to an external site..) 

It typically takes only a couple weeks or months to learn syntax, but it can take years to learn the vast array of free code that can make us more efficient in our work. 

### New Package: Collections
---
When adding a new Python package:

- Is it part of the [**Python Standard Library**](https://docs.python.org/3/library/index.html) or do we need to **install** it?

To check, consult an AI or the official Python documentation. Frequently used packages become familiar over time.

- Standard Library packages can be imported without installation into the project's virtual environment.

For example, the collections package is part of the Standard Library, so it doesn't need to be added to requirements.txt in PyShiny.

### PyShiny Express Issues
---
PyShiny Express is very picky about white space and comments in the wrong place. Read the error messages and delete any extra white space after a statement, etc. to get the code to run.

### Action 1: Import From Collections
---
Open the PyShiny playground to any example.

[https://shinylive.io/py/examples/Links to an external site.](https://shinylive.io/py/examples/#plotly)

Delete the existing content. Add a new import statement to the top of the file.

```
from collections import deque
```

### Action 2: Create a deque
---
After the import statement, create a deque by calling the the **deque()** constructor and **passing in a list** of values.

Lists in Python use **square brackets**, and each element is separated by a **comma**. If you like, you can create a list and assign it to a named variable, then pass in the name of your list variable and use that.

For example, you might do something like this - change the values as you like:

```
# Create an empty deque
empty_deque =deque()
print(empty_deque)

# Create a deque by passing in a list with values
temp_deque_F =deque([56, 58, 47, 54, 55])
print(temp_deque_F)

# Create a deque by passing in a list variable
temp_list_C = [5, 6, 8, 4, 3, 2]
temp_deque_C =deque( temp_list_C)
print(temp_deque_C )
```

### Action 3: Append elements
---
In a deque:

- The front of a deque (the oldest item) is to the left. <----
- The end of a deque (the newest item added) is to the right --->

We can append to the **end** of the deque by calling the **append() method** of our deque. This is the method we use to add each new point as it becomes available.

We can append to the front of a deque by calling the **appendleft() method** on our deque. We don't typically use this method when working with live data.

We use the general deque class to create the real world objects we need. In typical Object-Oriented manner, we start with the name of our deque object and use the dot operator ( . ) to access the deque's method. We **pass in** the most recent value to be added to the end of our deque.

**Important:**

- Use the variable name you gave your deque. I named mine **temp_deque_F**. Yours might be different.
- **Always include units** with any variable name that holds numeric values - conversion errors from thinking it is C when actually F can be very expensive.
- Review the updated deque after making changes - verify it does what you expect.

```
temp_deque_F.append(60)
temp_deque_F.append(62)
temp_deque_F.append(64)
temp_deque_F.append(61)
```

### Action 4: Remove Elements
---
We can remove from the end of the deque at the right (the default) by calling the **pop() method** of our deque. We can remove from the front or left of our deque by calling the **popleft() method** on our deque.

We don't need to pass in anything. We don't usually need to pop() values when working with live data, but it's nice to know we can.

**Important:**

- Use the variable name you gave your deque. I named mine temp_deque_F.
- **Always include units** with any variable name that holds numeric values - conversion errors from thinking it is C when actually F can be very expensive.
- Review the updated deque after making changes - verify it does what you expect.

```
temp_deque_F.pop()
temp_deque_F.popleft()
```
### Action 5: Get the Length (Count)
---
Call the built-in Python function len() to get the length of the deque - the count of items in the deque. Call len() and pass in the deque using the variable name you assigned.

```
len(temp_deque_F)
```

### Action 6: Clear the Deque
---
To empty a deque, for example to begin new readings for a new day, call the **clear() method** on the deque. No need to pass in anything else.

```
temp_deque_F.clear()
```

### Action 7: Limit the Size of the Deque
---
We use a deque to perform analytics on the N most recent number of readings where N is an integer. For example, the last N temperature readings. I'll use N=3 for a max just to illustrate, but this is the real power of a deque for streaming data - it starts empty, we add values, it builds up to the max length, and we keep adding and it will automatically knock off the older data so we can continously analyze just the last N values.

```
from collections import deque

# Initialize deque with a max length of 3 to store last 3 stock prices
msft_prices = deque(maxlen=3)

# Clear the deque (we might call this at the start of a new day)
msft_prices.clear()

# Simulate updating the stock price with new values
msft_prices.append(310.35)
print("MSFT stock prices:", list(msft_prices))

msft_prices.append(312.31)
print("MSFT stock prices:", list(msft_prices))

msft_prices.append(315.25)
print("MSFT stock prices:", list(msft_prices))

msft_prices.append(317.41)
print("MSFT stock prices:", list(msft_prices))

```

### Choosing Appropriate Data Structures
---
Try enough values to get an understanding of how a deque can be used to keep the last N values. By choosing a great data structure for this application, we can avoid writing lots of logic. Instead, we create a deque, fill it up, and now we can run all our machine learning calculations on whatever amount of "most recent data" we like. We can do the last 5 points, or the last 20, or the last 50 - or all three of these, depending on our application.

