import streamlit as st
questions = [ 
 {
        'question': 'What are the main features of HBase?',
        'options': ['High reliability', 'column oriented', 'high performance','adjustable'],
        'correct_answers': ['High reliability', 'column oriented', 'high performance','adjustable']
    },
    {
        'question': 'Which of the following descriptions about the functions of HRegionServe in HBase are incorrect?',
        'options': ['The RegionServer is generally deployed with the NameNode of the HDFS cluster to realize the data storage function.', 'Manage all Regions, Regions can be migrated between RegionServers', 'Data processing and computing unit of HBase','Regionserver is the data service process of HBase, responsible for processing user data read and write requests'],
        'correct_answers': ['The RegionServer is generally deployed with the NameNode of the HDFS cluster to realize the data storage function.', 'Manage all Regions, Regions can be migrated between RegionServers']
    },
    {
        'question': 'What is Spark in the context of Big Data?',
        'options': ['A popular programming language for Big Data', 'A distributed computing cluster for massive data processing', 'A relational database management system'],
        'correct_answers': ['A distributed computing cluster for massive data processing']
    },
     {
        'question': 'Which programming language is primarily used to develop Spark applications?',
        'options': ["Java","Python","Ruby","All programming languages can be used"],
        'correct_answers': ['All programming languages can be used']
    },
    {
        'question': 'two Transformations. What types of data flow can be divided into?',
        'options': ['one-to-many stream', 'redistributing stream', 'distributingi flow','one-to-one'],
        'correct_answers': ['one-to-many stream', 'one-to-one']
    },
    {
        'question': 'Which Spark API is often used for real-time data stream processing?',
        'options': ["Spark SQL","Spark MLlib","Spark Streaming","Spark GraphX"],
        'correct_answers': ['Spark Streaming']
    },
    {
        'question': 'What Spark data structure is used to store tabular data with named columns?',
        'options': ["DataFrame","RDD","Dataset","DataStream"],
        'correct_answers': ['DataFrame']
    },
    {
        'question': 'What is the distributed storage component used by Spark to store data in a resilient and fault-tolerant manner?',
        'options': ["HDFS","Amazon S3","Google Cloud Storage","Spark File System (SFS)"],
        'correct_answers': ['HDFS']
    },
    {
        'question': '"What is the primary function of Spark MLlib?"',
        'options': ["Real-time data processing","Data exploration and statistical analysis","Machine learning and machine learning algorithms","Managing computing clusters"],
        'correct_answers': ['Machine learning and machine learning algorithms']
    },
    {
        'question': 'What does RDD stand for in the context of Spark?',
        'options': ["Resilient Data Distribution","Reliable Data Discovery","Resilient Distributed Dataset","Robust Data Decomposition"],
        'correct_answers': ['Resilient Distributed Dataset']
    },
    {
        'question': "What does Spark's 'Lazy Evaluation' mean?",
        'options': ["Spark takes frequent breaks during processing","Spark postpones the execution of transformations until an action is called","Spark evaluates data lazily and doesn't execute any operations","Spark only works during off-peak hours"],
        'correct_answers': ['Spark postpones the execution of transformations until an action is called']
    },
    {
        'question': "Under the HDFS federation mechanism, metadata between NameNodes is not shared",
        'options': ["False","True"],
        'correct_answers': ['True']
    },
    {
        'question': 'What languages are supported by the Flink streaming data processing interface Datastream API?',
        'options': ['Java', 'Scala', 'Python','C'],
        'correct_answers': ['Java', 'Scala']
    },
    {
        'question': "ElasticSearch is strongly dependent on Zookeeper.",
        'options': ["False","True"],
        'correct_answers': ['True'] 
    },
    {
        'question': "Which of the following descriptions about Zookeeper features is wrong?",
        'options': ["A message needs to be received by more than half of the servers.it will be able to successfully write to disk","Message updates can only succeed or fail, with no intermediate states.","Updates sent by the client are applied in the order in which they were sent.","The number of Zookeeper nodes must be odd."],
        'correct_answers': ['The number of Zookeeper nodes must be odd.'] 
    },
    {
        'question': "Which module in Hadoop is responsible for data storage in HDFS?",
        'options': ["Zookeeper","JobTaoker","NameNode","Data Node"],
        'correct_answers': ['Data Node'] 
    },
    {
        'question': "If HDFS is deployed with a single name node, what limitations may exist? (multiple choice)",
        'options': ["The amount of leaf swallowing of the entire distributed file system is limited by the throughput of a single name node","Failure of this unique name node will render the entire cluster unavailable","It will affect the functional implementation of the upper-level components based on HDFS","The number of objects (files, blocks) that a name node can hold is limited by the size of the memory space"],
        'correct_answers': ["The amount of leaf swallowing of the entire distributed file system is limited by the throughput of a single name node","Failure of this unique name node will render the entire cluster unavailable","The number of objects (files, blocks) that a name node can hold is limited by the size of the memory space"]
    },
    {
        'question': "Redis adopts a non-central self-organizing structure. Nodes use the Gossip protocol to exchange node status information.",
        'options': ["False","True"],
        'correct_answers': ['True'] 
    },
    {
        'question': "Similar to Spark Streaming, Flink is an event-driven real-time streaming system",
        'options': ["False","True"],
        'correct_answers': ['False'] 
    },
    {
        'question': "Under the HDFS federation mechanism, metadata between NameNodes is not shared.",
        'options': ["False","True"],
        'correct_answers': ['True'] 
    }



]

score = 0

feedback = []

st.title("Quiz Simple")

for i, q in enumerate(questions, 1):
    st.markdown(f"<span style='font-weight:bold'> Question {i}:  {q['question']}</span>", unsafe_allow_html=True)

if len(q['correct_answers']) > 1:
        user_answers = []
        for option in q['options']:
            if st.checkbox(option, key=f'question_{i}_{option}'):
                user_answers.append(option)
    else:
        user_answer = st.radio("",q['options'], key=f'question_{i}_radio')

    if len(q['correct_answers']) > 1:
        if set(user_answers) == set(q['correct_answers']):
            score += 1
            feedback.append("✅ Bonne réponse")
        else:
            feedback.append("❌ Mauvaise réponse")
    else:
        if user_answer == q['correct_answers'][0]:
            score += 1
            feedback.append("✅ Bonne réponse")
        else:
            feedback.append("❌ Mauvaise réponse")


if st.button("Terminer le quiz"):
    st.write("Résultats du quiz :")
    for i, fb in enumerate(feedback, 1):
        st.write(f"Question {i}: {fb}")
    st.write(f"Score final : {score}/{len(questions)}")