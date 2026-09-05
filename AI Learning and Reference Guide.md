# **📘 Foundations of Artificial Intelligence: Architecture, Applications & Governance**

> **Source Material:** User Handwritten Notes & Reference Guides

> **Target Audience:** College Freshers / Tech Beginners, Senior Managers / Tech Leaders, and Software Developers

> **Format:** Multi-tier Reference Guide & Practical Handbook

## **📑 Table of Contents**

1. [Executive Introduction](#bookmark=id.pj2i0dg29063)  
2. [Big Picture & Visual AI Landscape](#bookmark=id.44lhvnzctjmw)  
3. [Core Concept: What is Artificial Intelligence (AI)?](#bookmark=id.bbb8ocqdpz7z)  
4. [The Paradigm Shift: Traditional Programming vs. Machine Learning](#bookmark=id.1527bn4gkhl5)  
5. [The Triad of Machine Learning Paradigms](#bookmark=id.h5ddihngtewd)  
   * 5.1 [Supervised Learning (House Price Prediction)](#bookmark=id.40ibkfdm1jbq)  
   * 5.2 [Unsupervised Learning (Customer Segmentation)](#bookmark=id.ic8x60k0z3zl)  
   * 5.3 [Reinforcement Learning (Autonomous Chess Mastery)](#bookmark=id.o8wwl2y4v6c2)  
6. [Deep Learning & Neural Networks](#bookmark=id.sxu7vkakb3g9)  
7. [The Frontier: Large Language Models (LLMs) & Generative AI](#bookmark=id.kd7ffw7oqthc)  
8. [Classification of AI: Capabilities vs. Functionality](#bookmark=id.umnjg8osr25f)  
   * 8.1 [By Capability: ANI vs. AGI vs. ASI](#bookmark=id.j8evlj3go4uk)  
   * 8.2 [By Functionality: Reactive vs. Limited Memory vs. Theory of Mind](#bookmark=id.exx246rf4nta)  
9. [Enterprise Perspectives: Architecture, ROI & Governance](#bookmark=id.sitxf2dkkar0)  
10. [Developer Integration: Patterns, APIs & Pipelines](#bookmark=id.s380pkttldq8)  
11. [Comprehensive Comparison Matrices](#bookmark=id.oyf19lb1eogc)  
12. [Frequently Asked Questions (FAQ)](#bookmark=id.rccfyw4tq7jl)  
13. [Interview & Discussion Questions](#bookmark=id.u0xj4u5ys8my)  
14. [Quick Reference Cheat Sheet](#bookmark=id.2dynf89d62cq)

## **1\. Executive Introduction**

### **What You Will Learn**

This guide deconstructs Artificial Intelligence (AI) from first principles to enterprise deployment. Starting from fundamental definitions, we explore how machine learning shifts the computational paradigm from manual rule-authoring to automated pattern discovery, the mathematical mechanisms behind learning types, and how modern Large Language Models (LLMs) operate.

### **How to Read This Guide**

* 🟢 **Freshers / Beginners:** Start with the *In Simple Terms* explanations, real-world analogies, and core conceptual breakdowns. Avoid getting bogged down in implementation specifics on your first pass.  
* 👔 **Managers & Business Leaders:** Focus on the *Enterprise & Management Perspective* sections, business value analyses, risk matrices, and cost considerations.  
* 💻 **Developers & Engineers:** Dive into *Under the Hood*, *Developer Integration Patterns*, system flowcharts, and technical architecture schemas.

## **2\. Big Picture & Visual AI Landscape**

The handwritten notes establish a critical hierarchy: **"AI is not a single technology."** Instead, it is an umbrella domain encompassing several nested disciplines.

mindmap  
  root((Artificial Intelligence))  
    Machine Learning ML  
      Supervised Learning  
        Classification  
        Regression House Prices  
      Unsupervised Learning  
        Clustering Customer Segmentation  
        Dimensionality Reduction  
      Reinforcement Learning  
        Trial and Error  
        Rewards and Penalties Chess  
    Deep Learning DL  
      Artificial Neural Networks ANN  
      Convolutional Neural Networks CNN  
      Recurrent Neural Networks RNN  
      Transformers  
    Specialized Domains  
      Natural Language Processing NLP  
        Large Language Models LLMs  
        Next-Token Prediction  
        Sentiment Analysis  
      Computer Vision CV  
        Image Classification  
        Object Detection  
        Optical Character Recognition OCR  
    Evolutionary Capabilities  
      ANI Artificial Narrow Intelligence  
      AGI Artificial General Intelligence  
      ASI Artificial Super Intelligence

### **Hierarchy Breakdown (Concentric Model)**

flowchart TD  
    subgraph AI\["Artificial Intelligence (Broadest Field)"\]  
        direction TB  
        subgraph ML\["Machine Learning (Data-Driven Learning)"\]  
            direction TB  
            subgraph DL\["Deep Learning (Multi-Layer Neural Nets)"\]  
                direction TB  
                subgraph LLM\["Large Language Models & GenAI"\]  
                    direction TB  
                    LLMNode\["Transformer Architectures\<br/\>Next-Word Prediction Engines"\]  
                end  
            end  
        end  
    end

## **3\. Core Concept: What is Artificial Intelligence (AI)?**

### **Concept Definition**

**Artificial Intelligence (AI)** is a discipline of computer science dedicated to designing software and hardware systems capable of carrying out tasks that traditionally mandate human intelligence—including reasoning, pattern recognition, semantic comprehension, problem-solving, and continuous learning.

### **Level 1 — In Simple Terms**

Imagine you are teaching a child to recognize a mango. You don't hand the child a 400-page manual specifying color hex codes, surface curvature formulas, and stem angles. Instead, you show them ten different mangoes, point at them, and say "mango." Within minutes, the child identifies a mango they have never seen before. AI brings this same observational learning capability to software.

### **Level 2 — Under the Hood**

AI is an umbrella term spanning symbolic systems, heuristic search algorithms, statistical models, and neural computations:

* **Symbolic AI (Classical/Good Old-Fashioned AI):** Built on explicit propositional logic, ontologies, and deterministic knowledge bases (if-then inference engines).  
* **Statistical AI (Modern AI):** Built on stochastic processes, optimization algorithms (e.g., Stochastic Gradient Descent), linear algebra, and probability distributions to minimize an empirical loss function ![][image1] over high-dimensional parameter spaces.

### **Level 3 — Enterprise Perspective**

For leadership, AI represents the transition from **deterministic software** (which executes fixed business workflows) to **probabilistic systems** (which optimize ambiguous, high-variety business decisions). AI should be deployed where deterministic rules become too complex or brittle to maintain—such as dynamic credit risk pricing, real-time logistics rerouting, and personalized consumer engagement.

## **4\. The Paradigm Shift: Traditional Programming vs. Machine Learning**

A central insight from the source notes illustrates how the software development paradigm is inverted by Machine Learning.

flowchart LR  
    subgraph Traditional\["Traditional Programming (Rule-Based)"\]  
        direction LR  
        D1\[Data\] \--\> P1\[Logic / Rules Written by Human\]  
        P1 \--\> O1\[Answers / Output\]  
    end

    subgraph ModernML\["Machine Learning (Inductive Learning)"\]  
        direction LR  
        D2\[Data\] \--\> P2\[Machine Learning Algorithm\]  
        O2\[Answers / Historical Outcomes\] \--\> P2  
        P2 \--\> M2\[Rules / Trained Model\]  
    end

### **Detailed Walkthrough: The Spam Filter Problem**

The notes use the email spam filter as the canonical example:

sequenceDiagram  
    autonumber  
    actor Spammer  
    participant Filter as Rule Engine / ML Model  
    actor Engineer as Software Engineer

    Note over Filter: Traditional Approach (Rule-Based)  
    Engineer-\>\>Filter: Add Rule: If body contains "WIN FREE MONEY" \-\> Mark Spam  
    Spammer-\>\>Filter: Sends: "WIN FREE MONEY"  
    Filter--\>\>Filter: Evaluated as Spam (Rule match)  
    Spammer-\>\>Filter: Modifies payload to: "WIN FR33 MON3Y"  
    Filter--\>\>Filter: Rule failed (Exact string missing) \-\> Delivers to Inbox\!  
    Engineer-\>\>Filter: Manually patch rule: Add regex for variations

    Note over Filter: Machine Learning Approach  
    Engineer-\>\>Filter: Feed 50,000 Valid Emails \+ 50,000 Spam Emails  
    Filter-\>\>Filter: Extracts features (odd sending hours, letter substitutions, grammar quirks)  
    Spammer-\>\>Filter: Sends: "WIN FR33 MON3Y"  
    Filter--\>\>Filter: Calculates spam probability \= 99.4% \-\> Blocks Automatically\!

### **Breakdown of the Paradigm**

| Attribute | Traditional Programming | Machine Learning |
| :---- | :---- | :---- |
| **Input** | Rules (Code) \+ Input Data | Input Data \+ Known Output (Labels) |
| **Output** | Answers / Decisions | Generalized Predictive Logic (Trained Model) |
| **Handling Edge Cases** | Requires manual software code changes | Requires additional representative training data |
| **Brittleness** | Extremely brittle when environments shift | Highly adaptable via continuous training pipelines |
| **Maintainability** | Complex nested if-else trees collapse at scale | Maintained via data curation, validation, and retraining |

## **5\. The Triad of Machine Learning Paradigms**

flowchart TD  
    ML\[Machine Learning\]  
    ML \--\> SL\[1. Supervised Learning\]  
    ML \--\> UL\[2. Unsupervised Learning\]  
    ML \--\> RL\[3. Reinforcement Learning\]

    SL \--\> SL\_D\["Data: Labeled Features \+ Targets"\]  
    SL \--\> SL\_G\["Goal: Predict target for unseen inputs"\]  
      
    UL \--\> UL\_D\["Data: Unlabeled Raw Features"\]  
    UL \--\> UL\_G\["Goal: Discover hidden structures/clusters"\]  
      
    RL \--\> RL\_D\["Data: Interactive Environment State"\]  
    RL \--\> RL\_G\["Goal: Maximize cumulative reward signal"\]

### **5.1 Supervised Learning**

#### **Definition**

Supervised learning trains a model using **labeled data**, meaning every training sample includes both the input attributes (features, ![][image2]) and the verified correct answer (label or target, ![][image3]). The model learns a mathematical mapping function:

#### **![][image4]Real-World Case: House Price Prediction (Regression)**

flowchart LR  
    subgraph Training Phase  
        H\_Data\["Historical Housing Data\<br/\>(Size, Bedrooms, Location)"\] \--\> Trainer\["Supervised Model Training"\]  
        H\_Prices\["Actual Sale Prices ($)"\] \--\> Trainer  
        Trainer \--\> Model\["Trained Valuation Model f(x)"\]  
    end

    subgraph Inference Phase  
        New\_House\["New Listing:\<br/\>1,500 sq ft, 3 Beds"\] \--\> Model  
        Model \--\> Prediction\["Predicted Value: $385,000"\]  
    end

* **The Data:** A spreadsheet of 10,000 historical real estate transactions. Features include surface area, bedroom count, zip code, and age. The label is the final transacted price ($).  
* **The Process:** The algorithm minimizes the difference between its guesses and actual selling prices using an optimization algorithm (e.g., Mean Squared Error loss minimization).  
* **The Outcome:** When a new property (e.g., 1,500 sq ft, 3 bedrooms) enters the system, the model outputs an accurate price estimate.

#### **Perspectives**

##### **👔 Senior Management Perspective**

* **Use Cases:** Credit scoring, insurance claim payout estimation, algorithmic churn prediction, demand forecasting.  
* **Cost Driver:** High initial cost. High-quality labeled data requires human annotators or reliable transaction histories.  
* **Operational Risk:** Concept drift—if market dynamics change (e.g., interest rate fluctuations), the historical relationship breaks down, requiring model retraining.

##### **💻 Developer & Architecture Perspective**

* **Typical Tech Stack:** Python, scikit-learn, XGBoost, LightGBM, Pandas, MLflow.  
* **Serving Pattern:** REST or gRPC microservice exposing a /predict endpoint, accepting JSON payloads and returning numerical vectors or probability scores.

### **5.2 Unsupervised Learning**

#### **Definition**

Unsupervised learning models process **unlabeled data**. The algorithm receives no predefined answers or category labels. Instead, it mathematically evaluates distributions, distances, and densities to uncover hidden clusters, associations, and anomalous patterns.

#### **Real-World Case: Customer Segmentation (Clustering)**

flowchart TD  
    Raw\["50,000 Unlabeled Customer Records\<br/\>(Visit Frequency, Total Spend, Cart Sizes)"\]  
    Raw \--\> Cluster\["Clustering Algorithm (e.g., k-Means / DBSCAN)"\]  
      
    Cluster \--\> G1\["Cohort 1: Deal Seekers\<br/\>(High spend, strictly during sales)"\]  
    Cluster \--\> G2\["Cohort 2: Habitual Commuters\<br/\>(Low basket size, weekly frequency)"\]  
    Cluster \--\> G3\["Cohort 3: Impulse Buyers\<br/\>(Irregular cadence, high margin)"\]

* **The Data:** Transaction logs from 50,000 retail accounts containing timestamped purchase amounts, visit intervals, and categories, with no prior classification.  
* **The Process:** The algorithm measures multidimensional geometric distances (e.g., Euclidean or Cosine distance) between customer records, grouping proximate points into mathematical clusters.  
* **The Outcome:** Marketing teams discover organic archetypes without human bias and can tailor automated campaigns for each specific segment.

#### **Perspectives**

##### **👔 Senior Management Perspective**

* **Use Cases:** Market basket analysis, fraud/anomaly detection in wire networks, data organization, genomic grouping.  
* **Value Proposition:** Uncovers opportunities and risks without requiring upfront labeling investments.  
* **Limitation:** Subjectivity in evaluation. Interpreting what a cluster represents requires cross-functional business domain expertise.

##### **💻 Developer & Architecture Perspective**

* **Typical Tech Stack:** scikit-learn (KMeans, DBSCAN, PCA), Apache Spark MLlib (for big data processing), UMAP.  
* **Data Flow:** Batch processing pipelines (e.g., Airflow/Prefect) running nightly or weekly over data warehouse tables (Snowflake, BigQuery).

### **5.3 Reinforcement Learning (RL)**

#### **Definition**

Reinforcement Learning involves an autonomous **Agent** operating in an **Environment**. The agent observes the current state, executes an action, receives a feedback signal (reward or penalty), and transitions into a new state. It learns optimal decision sequences through trial and error to maximize cumulative rewards over time.

flowchart LR  
    Agent\["AI Agent\<br/\>(Policy Network)"\]  
    Env\["Environment\<br/\>(e.g., Chess Board)"\]

    Agent \-- "Action (e.g., Move Pawn to E4)" \--\> Env  
    Env \-- "State (New Board Configuration)" \--\> Agent  
    Env \-- "Reward (+1 Win / \-1 Loss / \+0.1 Capture)" \--\> Agent

#### **Real-World Case: Teaching AI to Play Chess**

* **The Data:** **Zero initial training dataset.** The AI starts with only the permissible rule boundaries of the game.  
* **The Process:** The system plays millions of self-play games.  
  * Moving into checkmate: ![][image5] (Reward)  
  * Losing a Queen recklessly: ![][image6] (Penalty)  
  * Capturing high-value pieces: ![][image7] (Reward)  
* **The Outcome:** Over millions of iterations, the agent's policy network converges on optimal strategic gameplay, developing grandmaster-tier strategies without human guidance.

#### **Perspectives**

##### **👔 Senior Management Perspective**

* **Use Cases:** Warehouse robotics, heating/cooling energy grid optimization, algorithmic portfolio execution, semiconductor layout routing.  
* **Strategic Risk:** Extremely high compute consumption. Training requires massive simulation infrastructure before models can be deployed safely to production environments.

##### **💻 Developer & Architecture Perspective**

* **Typical Tech Stack:** PyTorch, Ray RLlib, OpenAI Gym/Farama Gymnasium, Stable-Baselines3.  
* **Integration Complexity:** Requires building a deterministic, high-throughput digital simulation environment before real-world execution.

## **6\. Deep Learning & Neural Networks**

### **Level 1 — In Simple Terms**

Deep Learning is a specialized sub-discipline of Machine Learning. It uses **Artificial Neural Networks** inspired by the biological connections in the human brain. While standard machine learning requires engineers to manually select and calculate mathematical features (like edge detection or color histograms), deep learning models discover these features on their own across multiple computational layers.

flowchart LR  
    subgraph Biological\["Biological Neuron"\]  
        Dendrite\["Dendrites (Inputs)"\] \--\> CellBody\["Cell Body (Summation)"\]  
        CellBody \--\> Axon\["Axon (Threshold Fire)"\]  
    end

    subgraph Artificial\["Artificial Perceptron"\]  
        X\["Inputs (x1, x2) \* Weights (w1, w2)"\] \--\> Sum\["Summation (Σ w·x \+ b)"\]  
        Sum \--\> Act\["Activation Function (ReLU / Sigmoid)"\]  
        Act \--\> Y\["Output Activation"\]  
    end

### **Level 2 — Under the Hood**

A deep neural network consists of an input layer, multiple hidden layers, and an output layer.

flowchart LR  
    subgraph Inputs  
        I1\["x₁ (Pixel 1)"\]  
        I2\["x₂ (Pixel 2)"\]  
        I3\["x₃ (Pixel 3)"\]  
    end

    subgraph Hidden1\["Hidden Layer 1 (Edges)"\]  
        H11(( ))  
        H12(( ))  
        H13(( ))  
    end

    subgraph Hidden2\["Hidden Layer 2 (Textures/Shapes)"\]  
        H21(( ))  
        H22(( ))  
    end

    subgraph Outputs\["Output Layer"\]  
        O1\["P(Cat)"\]  
        O2\["P(Dog)"\]  
    end

    I1 \--\> H11 & H12 & H13  
    I2 \--\> H11 & H12 & H13  
    I3 \--\> H11 & H12 & H13

    H11 & H12 & H13 \--\> H21 & H22  
    H21 & H22 \--\> O1 & O2

1. **Forward Pass:** Information flows from left to right. Inputs are multiplied by parameter matrices (weights ![][image8]), combined with biases ![][image9], and passed through non-linear activation functions ![][image10] (such as ReLU):![][image11]  
2. **Loss Evaluation:** The final output is compared against ground truth using a loss function (e.g., Cross-Entropy).  
3. **Backpropagation:** The error gradient is propagated backward through the network using the calculus chain rule, calculating partial derivatives ![][image12].  
4. **Optimization:** An optimizer (e.g., Adam, SGD) updates weights to reduce overall error:![][image13]

## **7\. The Frontier: Large Language Models (LLMs) & Generative AI**

The source notes highlight that an **LLM (Large Language Model)** is:

1. A machine learning model inspired by the human brain.  
2. A deep neural network trained to **predict the next word in a sequence**.

flowchart TD  
    subgraph Pretraining\["1. Massive Pre-training (Next-Token Prediction)"\]  
        Corpus\["Terabytes of Raw Internet Text, Code, & Books"\] \--\> Transformer\["Transformer Architecture\<br/\>(Self-Attention Mechanism)"\]  
        Transformer \--\> BaseLLM\["Base Foundation Model\<br/\>(Predicts Next Most Probable Token)"\]  
    end

    subgraph Alignment\["2. Post-Training & Alignment"\]  
        BaseLLM \--\> SFT\["Supervised Fine-Tuning (Instruction Dataset)"\]  
        SFT \--\> RLHF\["RLHF (Reinforcement Learning from Human Feedback)"\]  
        RLHF \--\> ProductionModel\["Production AI Assistant (e.g., Gemini)"\]  
    end

### **Next-Token Prediction Engine**

At its core, an LLM calculates the conditional probability distribution over a vocabulary ![][image14]:

![][image15]flowchart LR  
    Input\["Context: 'The patient was admitted to the...'"\] \--\> LLM\["LLM Inference Engine"\]  
    LLM \--\> Dist\["Probability Distribution:  
    \- 'hospital' (78%)  
    \- 'clinic' (14%)  
    \- 'emergency' (5%)  
    \- 'moon' (0.00001%)"\]  
    Dist \--\> Output\["Selected Token: 'hospital'"\]

### **From Completion Engine to AI Agents**

* **Foundational LLMs:** Trained to complete strings.  
* **Instruction-Tuned LLMs:** Calibrated to answer questions, follow constraints, and converse safely.  
* **AI Agents / Agentic Workflows:** LLMs equipped with external tools (calculators, web scrapers, database drivers, APIs) that plan multi-step workflows, execute code, verify output, and self-correct.

## **8\. Classification of AI: Capabilities vs. Functionality**

The source notes separate AI classifications into capability-based stages and functional operation models.

### **8.1 By Capability**

timeline  
    title The Spectrum of AI Evolution  
    Current Reality : ANI (Artificial Narrow Intelligence) : Specialized for single domains (Siri, Gemini, Chess Engines, Image Generators). Lacks generalized reasoning.  
    Theoretical Future : AGI (Artificial General Intelligence) : Matches human adaptability across any intellectual discipline. Can transfer skills autonomously.  
    Hypothetical Horizon : ASI (Artificial Superintelligence) : Vastly eclipses all collective human intellect across science, strategy, and emotional creativity.

* **Artificial Narrow Intelligence (ANI):** The **only form of AI that exists today**. Models operate strictly within predefined statistical bounds. They cannot autonomously transfer skills from one discipline to another without retraining.  
* **Artificial General Intelligence (AGI):** A theoretical system possessing cognitive breadth equivalent to a human, capable of autonomous reasoning, cross-domain skill transfer, and creative generalization.  
* **Artificial Superintelligence (ASI):** A hypothetical future tier where machine intelligence surpasses the collective intellectual capacity of all human minds.

### **8.2 By Functionality**

flowchart TD  
    subgraph Classification\["Functional Taxonomy"\]  
        F1\["1. Reactive Machines"\]  
        F2\["2. Limited Memory"\]  
        F3\["3. Theory of Mind"\]  
    end

    F1 \--\> D1\["No memory of past states.\<br/\>Pure stimulus-response mappings.\<br/\>\<b\>Example:\</b\> IBM Deep Blue."\]  
    F2 \--\> D2\["Stores short-term observations.\<br/\>Underpins almost all modern AI.\<br/\>\<b\>Example:\</b\> Self-driving car trajectory prediction, LLM chats."\]  
    F3 \--\> D3\["Hypothetical systems capable of understanding\<br/\>human emotional states, beliefs, and social nuances."\]

## **9\. Enterprise Perspectives: Architecture, ROI & Governance**

### **Enterprise Value Realization Matrix**

quadrantChart  
    title Enterprise AI Opportunity Matrix  
    x-axis Low Technical Risk \--\> High Technical Risk  
    y-axis Low Business Value \--\> High Business Value  
    quadrant-1 Strategic Bets (High Compute/R\&D)  
    quadrant-2 Core Automation Wins (Immediate ROI)  
    quadrant-3 Low-Priority Pilots  
    quadrant-4 Science Experiments (Avoid)  
    "Customer Support Chatbots": \[0.25, 0.75\]  
    "Document Parsing / OCR": \[0.2, 0.85\]  
    "Real-time Fraud Detection": \[0.4, 0.9\]  
    "Predictive Maintenance": \[0.35, 0.65\]  
    "Fully Autonomous Supply Chain": \[0.85, 0.8\]  
    "Fine-tuning In-House Foundation Model": \[0.9, 0.4\]

### **Risk & Governance Framework (Senior Leadership)**

flowchart TD  
    Gov\["Enterprise AI Governance"\]  
    Gov \--\> R1\["1. Data Privacy & Leakage"\]  
    Gov \--\> R2\["2. Hallucinations & Reliability"\]  
    Gov \--\> R3\["3. Algorithmic Bias"\]  
    Gov \--\> R4\["4. Financial & Inference Costs"\]

    R1 \--\> P1\["Prevent training on proprietary source code and customer PII."\]  
    R2 \--\> P2\["Use deterministic validation layers and human-in-the-loop review."\]  
    R3 \--\> P3\["Audit training data distributions for systematic sampling bias."\]  
    R4 \--\> P4\["Monitor token usage, manage GPU costs, and enforce API rate limits."\]

## **10\. Developer Integration: Patterns, APIs & Pipelines**

Software engineers rarely train foundation models from scratch. Instead, they integrate pre-trained models into existing software architectures using two primary patterns: **Direct API Integration** and **Retrieval-Augmented Generation (RAG)**.

### **Enterprise Integration Pattern: Retrieval-Augmented Generation (RAG)**

sequenceDiagram  
    autonumber  
    actor User  
    participant App as Web / Mobile Application  
    participant Embed as Embedding API  
    participant VectorDB as Vector Database (e.g., pgvector / Pinecone)  
    participant LLM as Foundation Model API (e.g., Gemini)

    User-\>\>App: Submits query: "What is our company's refund policy?"  
    App-\>\>Embed: Convert query into dense numerical vector  
    Embed--\>\>App: Returns query vector \[0.12, \-0.98, 0.45, ...\]  
    App-\>\>VectorDB: Query top-k nearest neighbors via cosine similarity  
    VectorDB--\>\>App: Returns relevant policy snippets from internal docs  
    App-\>\>LLM: Injects context: "Answer using only this text: \[Policy Snippets\]. Question: \[Query\]"  
    LLM--\>\>App: Returns grounded, hallucination-free response  
    App--\>\>User: Displays validated policy answer

### **Production Checklist for Developers**

* **Model Selection:** Use lightweight, task-specific models where possible (e.g., small classifiers) and reserve expensive LLMs for complex, generative tasks.  
* **Fallbacks & Timeouts:** AI APIs introduce variable latency. Implement timeouts, retries with exponential backoff, and graceful UI fallbacks.  
* **Guardrails:** Add input sanitation to prevent prompt injections, and validate model outputs using schema validators (like Pydantic) before passing data to downstream databases.  
* **Telemetry:** Log token consumption, inference latency, prompt versions, and user feedback metrics (thumbs up/down) to central observability tools.

## **11\. Comprehensive Comparison Matrices**

### **Matrix 1: The Core Machine Learning Types**

| Dimension | Supervised Learning | Unsupervised Learning | Reinforcement Learning |
| :---- | :---- | :---- | :---- |
| **Training Data** | Labeled (![][image2] paired with ![][image3]) | Unlabeled (Only ![][image2]) | No initial dataset (Dynamic environment) |
| **Feedback Mechanism** | Explicit loss compared against ground truth | Implicit distance or density metrics | Reward and penalty signals (![][image16]) |
| **Core Objective** | Predict labels for new inputs | Discover underlying structure/groupings | Find the optimal decision policy |
| **Representative Example** | House price prediction, Spam detection | Customer segmentation, Fraud detection | Autonomous chess, Robotics locomotion |
| **Common Algorithms** | Linear Regression, Random Forest, XGBoost | k-Means, Hierarchical Clustering, PCA | PPO, DQN, Q-Learning |

### **Matrix 2: Classical Programming vs. Traditional ML vs. Generative AI**

| Dimension | Classical Programming | Traditional Machine Learning | Generative AI / Foundation LLMs |
| :---- | :---- | :---- | :---- |
| **Core Mechanism** | Explicit rules authored by software engineers | Statistical feature learning on tabular/structured data | Multi-billion parameter Transformer networks |
| **Output Type** | Deterministic values / Direct control flow | Scalar predictions, class labels, probabilities | Novel synthetic artifacts (Text, Code, Images) |
| **Primary Failure Mode** | Unhandled edge cases throw runtime exceptions | Degraded accuracy due to distributional shift | Hallucinations, subtle factual inaccuracies |
| **Modification Method** | Refactoring source code | Collecting new labeled data & retraining | Prompt engineering, RAG, Fine-tuning |

## **12\. Frequently Asked Questions (FAQ)**

### **Q1: Is Machine Learning fundamentally different from Artificial Intelligence?**

**Yes.** AI is the overarching scientific discipline focused on building systems that simulate human intelligence. Machine Learning is a specific subfield of AI focused on systems that learn patterns from data rather than following hardcoded logic.

### **Q2: Why does an email filter use Machine Learning instead of hardcoded rules?**

Spammers constantly adapt their messaging (e.g., changing "FREE MONEY" to "FR33 M0N3Y"). Hardcoded rules require developers to write and deploy new filters for every variation. An ML model automatically identifies the underlying patterns across thousands of signals (sending times, character structures, domain reputations), catching new variants without manual code changes.

### **Q3: What is the difference between an AI Model and an AI Application?**

An **AI model** is a mathematical file containing learned weights (e.g., an XGBoost regression model or an LLM artifact). An **AI application** is the production software system that surrounds it—including web frontends, authentication layers, vector databases, security guardrails, monitoring, and integration APIs.

### **Q4: Can an AI model achieve 100% accuracy?**

In practical applications, **no**. Machine Learning models are probabilistic systems that generalize across noise and variance. Aiming for 100% training accuracy usually results in **overfitting**—where the model memorizes the training data and fails to generalize to new, real-world inputs.

## **13\. Interview & Discussion Questions**

### **🟢 Level 1: Beginner / College Fresher**

1. **Question:** Explain the fundamental difference between Supervised and Unsupervised Learning using a real-world scenario.  
   *Discussion Point:* Supervised learning uses labeled inputs and outputs (e.g., historical house features with known prices). Unsupervised learning works with unlabeled data to find organic groupings (e.g., clustering retail customers by spending patterns without prior tags).  
2. **Question:** Why can't we classify current LLMs like Gemini as Artificial General Intelligence (AGI)?  
   *Discussion Point:* Current LLMs are Artificial Narrow Intelligence (ANI). While they handle broad language tasks, they operate through statistical token prediction within bounded training patterns. They lack autonomous agency, cross-domain common sense, genuine self-awareness, and real-time world comprehension.

### **💻 Level 2: Software Developer**

1. **Question:** What is the technical difference between training an LLM and running inference on an LLM?  
   *Discussion Point:* Training involves backward propagation, calculating gradients, and updating billions of parameters across massive compute clusters (thousands of GPUs over weeks). Inference is a forward pass that processes a prompt and generates tokens without modifying model weights, requiring far less compute per request.  
2. **Question:** When should an engineering team choose Retrieval-Augmented Generation (RAG) over Fine-Tuning?  
   *Discussion Point:* RAG is ideal for dynamic knowledge bases, private company documentation, and preventing hallucinations by citing specific source documents. Fine-tuning is better for teaching models a specialized tone, domain-specific vocabulary, or strict output formats (such as custom code generation).

### **👔 Level 3: Senior Manager / Solutions Architect**

1. **Question:** How do you evaluate whether a business workflow is suitable for an AI deployment?  
   *Discussion Point:* High suitability: Repetitive tasks with large amounts of historical data, high-volume classification, and tolerant of minor probabilistic errors (e.g., support ticket routing). Low suitability: Low-tolerance workflows with zero margin for error, regulated environments requiring complete deterministic auditing, or problems easily solved with standard business logic.  
2. **Question:** What is "Data Drift," and how should an enterprise manage it?  
   *Discussion Point:* Data drift occurs when production data diverges from the model's original training data (e.g., changes in consumer behavior during an economic shift). Enterprises manage this with automated monitoring pipelines that track performance metrics, flag anomalies, and trigger retraining workflows.

## **14\. Quick Reference Cheat Sheet**

\========================================================================================  
                          ARTIFICIAL INTELLIGENCE CHEAT SHEET  
\========================================================================================  
\[1\] THE DISCIPLINE HIERARCHY  
    Artificial Intelligence (AI) ──► Machine Learning (ML) ──► Deep Learning (DL) ──► LLMs

\[2\] THE THREE CORE ML PARADIGMS  
    ┌─────────────────────────┬─────────────────────────┬──────────────────────────────┐  
    │ Supervised Learning     │ Unsupervised Learning   │ Reinforcement Learning       │  
    ├─────────────────────────┼─────────────────────────┼──────────────────────────────┤  
    │ • Labeled data (X \-\> Y) │ • Unlabeled data (X)    │ • Agent in dynamic env       │  
    │ • Predicts outcomes     │ • Finds hidden patterns │ • Learns via reward/penalty  │  
    │ • Ex: House prices      │ • Ex: Customer clusters │ • Ex: Chess self-play        │  
    └─────────────────────────┴─────────────────────────┴──────────────────────────────┘

\[3\] EVOLUTIONARY TIERS  
    • ANI (Narrow): Performs single tasks well (Chatbots, Vision). ONLY TYPE IN EXISTENCE.  
    • AGI (General): Theoretical human-equivalent adaptability across diverse domains.  
    • ASI (Super): Hypothetical machine intelligence vastly surpassing all human intellect.

\[4\] FUNCTIONAL STYLES  
    • Reactive Machines: Pure state-action lookups with no memory (IBM Deep Blue).  
    • Limited Memory: Uses historical data windows for real-time decisions (Modern AI).  
    • Theory of Mind: Hypothetical comprehension of emotions, beliefs, and intentions.

\[5\] LARGE LANGUAGE MODELS (LLMs)  
    • Architecture: Deep neural networks using Transformer self-attention.  
    • Core Task: Autoregressively predicts the most probable next token in a sequence.  
    • Production Deployment: Typically paired with RAG systems to access private enterprise data.  
\========================================================================================  


[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAaCAYAAADFTB7LAAACqElEQVR4Xu2WzWtTURDFExJU/EYJkXy9JFZSg2ArKAoqKIi4FLoRVFwUFBREdyIi6MaFIgQt7sQuFTcWrCIFISCI6NJNN933j6i/I2/kZXg3SW3RTQ4cXnLm486dO/clmcwIIwzG2NjY9iiKHler1RPe1ge5Wq02xTPrDUHU6/WdjUbjJIudSpKF93pfQ6FQ2IrPcxa7mElZrFgsbsF+HS7AyaStX1wqKHCCoDm4DFfgNxJ84HnO+xqIuYX9CV3c6G0C9nfkuCk7fp9gw2z6rPyr7PzvQBU322q1tnmbQx6/TqC4PMXdgeMm4DsPZ9A2mUaBTbQuPG/aIOTiAm97g4cWh2e9LjAqR8ixyMecaRTz0W+83W5vQH8KX5rWF5VKZZcKDC2cBEkv4Vf3enycHbic1Pn+Hb7RrCd15ZEtqQVB8AW/yzTEG5nLJDpkQJ+ON/nI6TqZBxl3KbRJ9G5SCyGnpNEQx0uB+9j5V69rvoifiYtZ1CWIL9pnaeqWjymXy7uxzeu4va0H1pVhjhef8SjlWDjeQjxrS/C0Fo8LOAR/MpsHfYxOC9tsqVTa7G09ULCSpM2VgG0SHtPnUIFo++EPFaliTef7GRWRNjoqDPuLQQXa8a54gxC/Djq2QKhA/I4rB8/7pvGeK6lgPZO+hqE6qN3i9D5QoN539+C0CaEZpIjD+C2xgSum4TcVuRudxFAzaInTFkW7rGPD54BpoVusLqEvUOA1fY83/hY+S/oloZGK+tzibLPZ3IHDDXUPvrbBFok9Gus9vxj2gk2ZKb3oH5o/z7vKSZ49zu8PrDleXzPU0Xr4xufVZS962Ea1IW9bM+wXI/BbPBTiy9fVLfe2dQHJv9DFCa8PiSyxV+ErjZk3rgsG/R/sh7+NWzX+2T/qEUb4D/gFmGe2Sii8qTcAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAYCAYAAADzoH0MAAABHElEQVR4XmNgGF5ARkaGU05OzlpeXt4RGQPFtEHysrKyyuhyKAYoKSnJAQWXAvEeIP4PxUeBBsSC5BUUFDKA/NtQ8dNAvBnFACTACFIE1LgTaKsUmng2UHwHiI0kjgmAtl0CGQKkA2BiICcDNa8Aikkgq8UKgApDoAZcArpCB8jfAMRa6OpwApDTQV6AGjIRZDu6GkIA5N8SaIA9QJckCgBdYQrSDMSv0eUIAmiaqAdqfgxyhYqKCju6GnyACai5TVRUlAcWFqA0gK4IF2AEaogBaYbxoWGxFugqIRSV2AAsrpHFQNEICgeguCuyOAaAaUZPKCDXQGNjErawYATmAX6gZBUQPwfiZhAfWR5oqCDIAGjqtCLKK6NgKAEAzaZJ+7frAE4AAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAWCAYAAAAfD8YZAAABBUlEQVR4XmNgGJpARkaGU05OzlpeXt4RGSOrUVFR4VNUVLRDlgeKiTIAGYoKCgoLgfRzIP4PxLeBhu1E1gyUNwCK74fKg/BcoKXSyArcoRIPgGwLJL0gOQmggStANiKLw4GsrKwUyEaoASXIckD+VKBcDJDJiCyODJiBipqhmtciibMA+SkgGkkMEwD9IQTSCDIAyGUB2QayFV0dLsAIcjJIM1BjLMifIP+iK8IJQIEFCjQgPgbUrIUujxcA41MfqPEa0BAFdDmCAKgnAORsKSkpLnQ5QoAZqLkDGmDEA2lpaWGgJi+of88B/SsIFGZCV4cBREVFeUC2oeHXQGyJrnYUDBQAAAzZQTBt0F/ZAAAAAElFTkSuQmCC>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAA/CAYAAABdEJRVAAAEV0lEQVR4Xu3dy2skVRQH4ASCLxRFCUjS3dXdRONERUUFRREjqAOCC3GjMLhRnK3iRhRmISjoQhkYmZ0woAtfCMqMItkoDLjQxSCu3bnwj4jnmO5QXKof6dCdiN8Hl666596uqt2Pul3VS0sAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwHHQ6XTOt1qt28r+g2i328+urq5eX/YDABy5CDrXRuB5pKqq7Vp7uD5mXG0RNjY2ro7j7kS7GLvL9Vq/3789zv/Oel8qznl7OKYb6v1x/XcPpixH6SOhDQA4tiK8vBFtt91u39VQez/ahbJ/EfJ8IkhdicD1Sp5fbN80rMX2q9H3eX18XYavnBPtq3p/7D8Tc0/W+1L03Ru1y2U/AMCx0Ov17omw8ke0l4vScvSdO6o7TxGiTmfoarVa67H9UlH7KYLc8/W+Usz9O9twP++oxZxv6mOGBnfyzq6trV1X1kbZ2tq6Kua8XfYDAMxFBJlTET7+jCD0UO7H5+Ox/105bpHi+Jei7ZT9GSDzt2uTwlUG0Ax8eacul0/zmsoxdVHPJdPXy/5R8vgx/oOyHwBgLgZ3i3ajXYzccmt8bpdjFiXvdEUg+35wPr/ndt5tG9YzeEV7uj6nSV5TzP0wg2iv13uqrDfIO4o7EfDWykKTWQNbnNO7Me+vwTV+XdYBAEYaBKRcRvxyqfiB/zgx/sUMH9O0fr9/Yzl/lDyfCGYvlP3xPaeiPVr2N8lgl9cU458sa01i7K8x546yv8ksga2z95DHZ9F6ZQ0AYKJq7wGD3dhcKWuL1mq1bo5z+TmXKctahJ4z04SqmH+uGiyLxvgrZb1Jjh0VBqvi6dP4zpPx+WnZ3263Hyjnpqi9k98f7Ykc1+v1HuvWHqQAAJgoQsS3GSjK/qOQgSzO5cLm5uYNZW2awJavLIkxb8bmSoz/YXBdE+8a5rjDBrZqxOtPhucxvNsY218c9h1yAMD/TIaJaoZXeFRzWBKNMHS627AcmjoTlkQzqEX9veF+7fUgY58qTdUcl0Tj+L/E+EtlPwDAVGoPHbxV1hZt+LBABK0Hy1rqjn/oYKUqXkUyfGVHfOcnE15RMteHDvL4GQjLfgCAsSL4XDMIavV2pKEtjn8i2m+jXtuRy6Sd4rUeMf7j4hr23ylX7T1IsV/LMDis1XX37D+NOslBA1tYjmPfH3N+jM8z1d4S9JE9jQsAMLO8e5bBquyvq0Y8kHAYedymf3sYZYbA9q9cFl5fX79laYrf1AEAHCsRfi4P7oCdj8+zZb0uwtVr1Zi/pjqorr+mAgCYLJcjBz/Mv6+sNYlxJzoNf/4+g+WuP38HAJiPvBt32FdjRPB7Ll8DUvYDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPDf9A9DYf8QP/YMegAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAZCAYAAABHLbxYAAABU0lEQVR4Xu2VvUoDQRSFIwQVm9gJy/67iGxjLYhgp4VgYakQsNNUtkFs7CxsrYX4ANpY2wbB9/Ah9LuQhcuYnZ1IsljMgcPunDl37pnZTbbT8fDw+B+I43gvSZIBfIbfMjY9NVjCe0bNWO6Loljhfpim6btptCIMw4LCOwpXzTkNPJcSNMuy/VmCsu42/g94VWl5nvcYj4IgWNNeKyYL3bsWiW+WoHiv4Rfc1Tr1t2x6R2tWtBD0SU5U+midcV+oNStaCCqP/VdQ6s/ho2tfH7TCn4JGUbRJ0YGmFHAdsdCh1uXXjbZurtFK0Glo4URf64KiD7VmxaKD4ntIav6e6H2iNSvmHLSL/qZDMT4Vvw5VluWybIDXK6m0RrgGlfdJGk5j5Zls4hMe6Vq+RFv0eWGNY+Yu4BjeaE8jXIPOAV36DORkOckNc7IRrt96Dw8Pj8XgB3XVgC7LNt3RAAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAZCAYAAABHLbxYAAABvUlEQVR4Xu1UsUoDQRS8xEPURkEUueTu4t0hIX8gWGglFoKFBISoCIKNldiI+AM2dulshDQGC21iY29zkN4mnZ+hM7DC4xFOdK9IsQOP3Z2dtzu3e289z8HBYTIQx/EWIo+iqI1hFe0RxsNGo7GptQoVaDvQ9tiv1+uzJjfXwlIAQ89Y/BZd31A+x+SlTgOmEuge0zQNBV1B3lmSJPOCKwfY7AuLH0gOJg7JS04DOXvQ9NEuSB65G+CakisDUzTExSXJazdGK5KXMB8zQrsreeRuh2EYSM4atVptcZxRjslzXvIKPkxdUYd4R/8YbQ9xo4XWsDTqsYBozJhlPMDwitZZw9YoCmkZui5iIMwWVj0rlc/Mr4H/J/1JsjHKk4PmCXFqTvYC8ck8VP2a1lsBm80UGeW85CUw/8aCGsOvIrpFuf+CMfTn5wnzOStc80EQzCH/rtVqTes5K2DDEa9NcbzGD0H52PwV3LrQ9BGXnnrC+NhDuy+5UpBl2RI2vEcMsEGbV8qrk/8nTwncELEjUvk8nfBDzTN1jfaFawlN6ahikyaMdnAikVfw0GvwBGHunLlcA1RVaxwcHBwmGN9ZUnu7/iWb/wAAAABJRU5ErkJggg==>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAZCAYAAABHLbxYAAAByElEQVR4Xu2VO0sDQRSF8yqCWAgSCHnsJjGFnZ0oiMROrawCgtoKNmKEWASsrLQURAQbwcpGq9hYWQspxCaNnT9Dv4uz4TLGyQbio9gDh8mce+7syc7ubCwWIUKE/wHf95fgk+d5daYJxi3mnVKpVLO9GplMZhzfKdzHm2XcgW/w2fY6USgUqjQdsUjarmlQv8N3zM+UkVIyF137bFDf408d8jNppDjaNr3vxWIxp6xu0DRN00kulxuzaxqyMN51rRFgU3St2aB+JR68zUBjnRLaI8Oa9joRMmjSXGxBi/TWTNC41jWo35je80DL5/OTaG3Y0l4nwgQ1C38JKnPRpa71QSiXyzP0vXDtObv2Lf4gqOxOy+xE8LwPxm8H5W7O0tOFF3atB96yKf/zmOnRvBDXBF7WOgsuok1I36iCsl6WnlsJGbanhzB3FE/aFVTqWu8HOU/Nm9/bbnpXlcWNMEEFJtDQx5NBCu+BjFq013NiiKCvsGFpDdhVkgS6R5u3tCbcle0OyIcmb++QE2GDVqvVDL5L2OYCdcYHeKafNVkDrQNXAk38ctf7cajnNGxQg4T4CbpRqVS8mOOgHznCfusjRIgQ4WfwAQDfibHqUAKEAAAAAElFTkSuQmCC>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAaCAYAAACzdqxAAAABk0lEQVR4Xu1TPS8FQRSdl5eQCEFkm137aWNlG6IlQqJQKIhaqZYoNAoJCZqnI2qVUCo2IlqNvERENH6A4v0Izl13uGbXe69SyJ7kZGfumXtm5t5ZpSr8CVzXHfN9f0ES4ToR4+kSLUcQBENhGM7puOd5M9+uSEZgG8Ib+A6+Yn6TpmmPZVn9mB+DLdaewWthPIX5LWsP4Kk01ouOaAFMd00N8Yw0rJk3NcdxRpEzbMa/QIZtjPMTQ1s3pBpim0bsJ5C4xclntm336TidBvHHMmPcYAKxQxkrgJK4VlfUFIphHIIn4J55GyoL9UZ9Nvl3YNEsG2eo24jipoKLukzUB4pHUTSIeYM2Nn0KEMZ3eH42d3w/juNefHf4xHmZMF7FeANpNdOnALzHSSS8gE2qHZmSOWm6TMK4gQ0t06MUbNZkg2V5Taon3yajm8nmdgTVlRLZ+EKJa+oyYYMnX/wgXUEag5dSE2WiTQ+k1hFJkgwg8Rxs4WRLUhNluseLGJdaN6jDYAWJnilww9a8dr9uhQr/EB8O9noHX4ujFgAAAABJRU5ErkJggg==>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAbCAYAAACuj6WAAAAA/0lEQVR4XmNgGKRARUWFT05OLlVBQaESSPuiy4MBUEJbXl7+ChD/ByqMRJeHA6CCJiC+pqioqI8uBwdABWeBpnQAmczocnAAsgpobSy6OAoAKnoAVGQNNM0d5AEQjaJAXV2dF+QeIN4M8iXIXUD2XFFRUR64IqAuByDOQNIH8rENUGE1XADIKZKVlbVFUgPS6A5UWA/jcAAVTQPSCsiKQBpBGMyRlpYWBnK2S0lJccEUQN24CGiSK4oimAIQABqqAQo3GRkZIZgYM1CgWUlJiR/EAQUDkH8BSMcgtDGAI1gUKLEKKDEDSB8GBoEbUJgJRREIABUIQo1nQZcbBcQBAPx1MEFqK53uAAAAAElFTkSuQmCC>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAAaCAYAAAA0R0VGAAACZElEQVR4Xu2WPWsUURSGJ674DSKybNiPmdllI7ogVlqprYIIESSVdoq92ohFwMpGLCQiWIggFtqkU4uAKAZEYiGSJk06C3+Eed7dezd3j7Mfs9kixT5wmJn3nHvm3HvPnd0omjLlf+I4vpEkyT1uC9bXj2azWWw0GiesPmlmKGypWCwesY5hMKllrGX1iVGv189RXN3qo8C4a9h7raL17Zg0TS+T/KvV88DKXSfPl3EnmEm5XD5E4hckfmx9eWB8qglit6xvbMh5koRrXOetLw9+kjLr66FUKh3WqcP+YP+skWDRx/L8EFup1WrlMIeHomfV8G7cR66nKpVKVZYRO4//r9V7cMl+E/yA613dYz/RF2j8iyQ+rjj8B9CfYx+8ZtAJvs+4p9hVbT3P37ANGyiIOa9JWL2LPgUErIZHW82qQSS/FMaGW6H70Oco6BvGKdyvh2q1ejDprPQVGyiY+Bl861bvwotuqhijtWckX6iPUFwXN+lHrrAZ6xe+f63exjtbrda+QC647dikr84G+sjF6ftlx2YxcOVY9tMU8ivU1Oi8/BP2yn79R+g5xczifxZqbPVRHbpQEwN7juLmCPgeaiS/w4ANirwQ6h7XQ5mn1RX2Jhyr/uMdt6OM39+0c1o3rd5GA3E+0cycpNO25nqwX58o4bq2xPrQl7C32Evsc9z5lPzgumxjRdL5MqxYvQcVp20a1EcebbW2XH1pXJrMXv/g4o5xu2c7ZBvGt38h3EJMDiUk8arV86Ac6u2s9tgRWhGKexf12fphaKdYuNfq72jMHMPYvf/nRLyL/wlPmZKXLSXDll/bxqz5AAAAAElFTkSuQmCC>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAABMCAYAAADQpus6AAAJQ0lEQVR4Xu3d74tcVwHG8dnNouIPbNWYmp3MvbO7mnYV1BfVFhRaqOgboeqrBgt9UWktoiIlWmoNBNGIaCTQUqxW6QtRayA10FQaQSgp+CLFFyVv+mbBl/kj9HnmnjN75vTO7N7ZaXJn5vuBw8ycc+bunTuB8+Tce+50OgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYDn0er1Thw8ffn9ej/YoiuKEHlbzegAAsAQU1rZd8nq0iwLb0yoP5/UAAGDBbWxsfEJh7UJej/Ypy/I2BbbzerqStwEAgMV1yAFga2vrcN6A1lpxwHZ4yxsAAEBncErqaxosX9Fg+Z60Xq//4pLWzYN+v/857fdX8vpZ8bFS+V5ad+zYsTt1HJ9T/a1p/V7c39vz+/O2aXg7Yf8a7cesaT82/W/Hj2m9j1t+7CL1f0ltJ/N6AADQqQKbBsvbw8tVvX5e5QexLenaehrwv6R9vp7Xz9L6+vqH/bi9vf0uHbfPx7Cl54/Etv3K+nuW6ecqZ5O6idR3299V8v0NNN2PWUv3Z2Nj44P+XD5eoe2R3Z67dByPqt8/9HQtbwMAYOllgc2vL2vw/GJs2+3Zftrfc2HQf8ekYUjH7cvx1OsMApv3/wXt/4Np3STq/w2VE20ObMePH/+AP1fSVhvYZEX9ntK/vU/lDQAALL2awPbc0aNH3xvbdnu2n/b3fw5Ref0sxTBUF0SaBqW8v8Nm02vv9J4vtDmw+ftIQ/SEwNbxZ9cxfbnpMQAAYOGlgc1BrQinQ2Pbbs9202e4Rfv7mh7LvG2WYhjyMdPfuxLrZxDYfEr0bDx1uF83MbCt9qpr8DbKbLFAuj+eNUtP804KbJ1qwcj1OMMLAACCNLB5oEwDz5wFtge0v0/m9cGK2u/yDJzK19MGvf6sylW1fz+9ya6DU1GdcnxMQfYjsT6Gobog0jQoZadXb08XH2j7d6vuibqi5kOx300MbJ1ut7teF5LT/XGoTT+Xj1N8Xkf9rxXJLC8AAOiMBjY9PpoOlHMU2Hz902nt//15Q+TP6MDmgJPWO9yo/lLdtWPh8w/DkSWBbeR6MweRpkEpC2zD6+GamGFgW2sakvr9/qd9HHx6OK3PAtvIKc59BLZ/1oVAAACWWgxsSXC5T6/vim15/zbyCkMP9HlwSYXP58A2EsxU96Tr/ZjWq9+3iupnk0bEMOTrstT+sW63+yG/Pkhgc1DS9p51ANLjV/N+k8wqsPk9Dd93SH/3jINm3hD3x59Lzx/y50raJgY2z1r6+1C/B/I2AACWVgxsW1tb79bjL1R+NG+LDrz/2terk2aoyuoaNweBh9J61f1O5a8KCqfSevX7jW9JkdZZMsP2N5XHY72DSMPAkwYrX7/2XW3vx5M+Q07veUXveVPlip/H+qb7YU0DWzieL+qxrGmLAdIzn7/250ra9gpsp/w9Fcm1lAAALDwPqBr8fru5uflRvw4D/PBeZUW2SjTltrwuFwf6vUoIP3v9/NCKr6MLA/bbyrgw41kmt086pRcWVHiGbRjMyuoGu4dc5xmu+H7ffNcBdvjmxLhQMyawrelvvulZM18fp+dP6/m/u93ux91Y038mptnuFIHt/nA8Tx45cuR9ev1tvX49tNX+e7J9BLYHw3afzdsAAFhIGhxv08B3QQNxN9ZpMDznATF5faDA5pmd/RSHlboZq5T63Kvyln8LtFPdxPd0uq/jxEF+UmAz91F5xs/1nlu9T+H5MLCF05Njb147LtTUBDbPmn0zBJRBUC2rhQ+elbrFr8dt66Cm2W7TwJZ8N4Mb3fZCaO5UCzxq/z0ZgQ0AgIwGvtdVrmV1rzk0xNcOKGGgHpn98rVZ8fqsG8S3dNhxqIkVHvhVd3WvINYwsL2o0i+q2a7BTziF91/ycdDjM2nAzblPuprUvKI0bGs11mk7j/vvdZJFC0X1qwTpwohVb6/prTzG8XbCdzncjzraj++kYdpFdZdd8nqVn9Ttn/q+UYzeh86rdON3sBb+7Yz8aoGPW37scjH4EdgAAEvDA1+RhLNQd13ldFrXBhrwS+9rnH0KdfeE0DPxVGrDwHaprG6P4dOhAw5RRRVk+95W+p5p+bOEfR+ICwtUd0fa72ZwaIozarH4NK1LXj8uYIVjObzOTMfwTPi8I6tqm4rfOYENALA0wsA3DCDhOi7PjNxRVKsj+2n/aYTws2fR33ps3OBvnlnJw5Lec17lclpXpwzXU+0zsO2o/2fS+jCrc80zSmn9QWh7V1Uuxdfh2jxfO+hThsNZxLaY4pTo4N9R8trH9aW0zzRi+CawAQCWRhj4hiFIzz+puos+XaXHc5MC1I3mWz+Uoys4vcLwv8X+rqMbnEYrk9m5Ou7j0slmgcpwjzaVX6X1B6FtvVwkgU3Pnwp/259ruGqyLaYIbL7ZcLxWzYsr3lK5d6TTFGJg07bP5G0AACwkDXx3F9V1bC+oPK9QpIdiR+VPbQprkfbr9yr/UnlV5Xxnj1OhkU/l9ZLVl+OEkPG2i969+lTvP9k54Om8VFgV+lOVX3rmbnNz85geL+j1xWIGwWbWpghs/hWIN3Q8/15UwXRf39VeirCYIZ9tBQBg0a2lt9RwkLjBiwmaWPG+Ng2TYcbwomfp8raU+pyo23ay8GLmvN3kov21ur/fBk0Dm9Uttjgonwp1YFMQvCdvAwAAc66oVmA+mtdjvngW1OG7xf+pAAAA0/JF/b1e72zdLSgwP8Lsmq9fm9npaQAA0BIOahrsdxTc7szbMB/CKuZ0MQMAAFg0YXaG06JzKqzWPTfuZ8EAAMAC0GD/sGfZ8nq0nxdj9Hq9P3DtGgAAC259fb1bVDfa5fqnOVNWv7O6k9cDAIAF5NuC9Hq9n3Wy37FEuyms/ado4f3pAADAO0QD/xWFtvvyerST7+VWluUTHUI2AABLZc2/XNDWm9Ril2fV9F39Oa8HAADLwaHth37MG9Ae+o7+6GsP83oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIB59n86nxwDCpAnjgAAAABJRU5ErkJggg==>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB0AAAAaCAYAAABLlle3AAAChElEQVR4Xu2WzUuUURTG7zQSGYVJDMV8vfNVk2PQqkC0KIiEoJVhVEZELsTcCO1EBINoIy20FAwyVwkuIiFb5M4WEfYv2e+pe5vDS8TrmNTCBx7uPeeej3vPvXPece7PaIuiaKxUKp0sFos34XPYGRbL5fI11tc8l+G0dW4JhULhPIFWvZhi/ogNjFsbdBvoRqxu18jn8+2crq9SqXQQvJ8k63ZdSdlc1up2BQL2wFcqL+OwymeTNhqNgyq5RuvXMtj9RQJ+JElZMmMX/AZfBptarZb5a6XNZDJHSPiaBJOIKekIfgZ5SycOdrpz8Zej+/G4Ioa01SWC7tCfqsur0syfwAnNpQilZTOHmp4uFd9EYhCsQoI1nc7L3XBJdxts9Hiw2Wh6uQPY3FCVjG5HSBFgiKAzjFcZ53i9xbCI/AJ+htu6d3/3XyXbIPv4t+A+NveK8Vz/D9Rv+ZFfgJfgifj6noCSTJL4lMh8Vjo1AX4aU/AdulV4B90x+J75B8YVtU7GW9h8kY5xPh77t1CnweFhkKvVaiHy/Vcg0D37VdFGWF/MZrOHgw55AF4JciKoEchJHUmfNCUKa+guh04lsPYW2/VcLnfcy4N2k4mgNkbQEbU8AvQSYNQmZd4n+nkndg9UTl2F1w06/5FIBJWIJHOu6aR/C/qG9gQbHtY5n1RrAyS9zbjlT5/e6cNL4/iMAMtBoU2QYMGZnetEOh28rwTaAD7byP2qULBLhJBAJws6HsxZ5E/WTncX/Wz41yVHzY/7bCufNZXrsV6jl9uQJ5CHrJGScqI3emCSVVaVF7un8rG2ieAfz5JKRaAZeNfFAtXr9aNqHEHWzwf7FTZx2trtQ/gON4GnDAO1Jw0AAAAASUVORK5CYII=>

[image13]: <data:image/png;base64,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>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAZCAYAAADXPsWXAAABAElEQVR4Xu2SLwvCUBTFJwpaFFSE4f6KgwkWg0Ww2IxmQbCZzQZBsPkBzGKwG0wm8z6TnosPeTuOObDuB5e33XPfufdtzzByEnEcp+t53kSLURAEZa2khJqhXuP7vqnpbyBsEE/XdY+sKQrQdzCvsfABmxdigrixJqBzD9qZ8zFgMlYmD9bkaMgfYDRlLYbqFIkRazIBmvQ5/4VlWU05SoJJEQ1WWAuU/yYMwyoMTmwCgwGmqOu5VFC8FRNsrMg7nueIDdelgs1LMVFTdWB6kZXrUoHJTE1iYt3LJFzzE+0PRfItWM8ErnYbBncYrI0sfyMJ27YbMLnicrVYy8n5lxfdtzU1+kRDVAAAAABJRU5ErkJggg==>

[image15]: <data:image/png;base64,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>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAAAVCAYAAAD2KuiaAAABYklEQVR4Xu2Xv0vDQBzFGyoKUlCUgOTXhZhBgmMHCy510T+gazddHB0cRHFwUzoqIq7+nfq+ECE8jnAZTr9t84EvKS+v17uX3JfrYNDT0/OPBMaYMxbXhiRJ9tI0jVhfGsqy3MITnGRZdoXrG+obn+fss1FV1Sb8z6yroZ7gPetNwjAcwXONusHCT7sEAF8B/wfraoiiaBsTfGG9jS4BwHspxboafAaQ5/kJvAvZQnxPDT4DgO8BvhnrqvAcwKeq7o/JHGJS02bhNb3A9Yt1KfjH+NoGj+MSgLz2sgVYtwFfzr/dVrIOHsOJrgGgJrb9axwCwLhHqF3WbfxZADZ8bQGjufM38RHAb/dnXSWOAQRFUezEcbyPxR3UAdxie4RySCLvEPef4DsnXScuAYgHC36XhXNBf2x6pesbbd2/DZejsCv1f4aFa/dfOfDUjxHAq2VbrAdG+7nfN1j8HS5D1jXwA1lDbOIqKO/rAAAAAElFTkSuQmCC>