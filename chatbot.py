from flask import Flask, render_template_string, request

app = Flask(__name__)

# ---------------------------
# Store chat history
# ---------------------------
chat_history = []

# ---------------------------
# HTML Template with better CSS & Watermark
# ---------------------------
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Rule-Based Chatbot</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #333;
        }
        .chat-container {
            width: 60%;
            background: #ffffffee;
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.2);
            position: relative;
        }
        h2 {
            text-align: center;
            margin-bottom: 15px;
            color: #444;
            font-size: 26px;
            font-weight: bold;
        }
        .chat-box {
            height: 420px;
            overflow-y: auto;
            border: 2px solid #e0e0e0;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 12px;
            background: #f9f9f9;
            font-size: 15px;
            line-height: 1.6;
        }
        .user {
            color: #1a73e8;
            margin: 8px 0;
            font-weight: 500;
        }
        .bot {
            color: #188038;
            margin: 8px 0;
            font-weight: 500;
        }
        form {
            display: flex;
        }
        input[type=text] {
            flex: 1;
            padding: 12px;
            border-radius: 12px;
            border: 2px solid #ddd;
            margin-right: 12px;
            outline: none;
            font-size: 15px;
            transition: all 0.3s ease;
        }
        input[type=text]:focus {
            border-color: #667eea;
            box-shadow: 0 0 8px rgba(102,126,234,0.5);
        }
        input[type=submit] {
            padding: 12px 24px;
            border: none;
            border-radius: 12px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: #fff;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        input[type=submit]:hover {
            transform: scale(1.05);
            background: linear-gradient(135deg, #5a67d8, #6b46c1);
        }
        /* Watermark */
        .watermark {
            text-align: center;
            font-size: 13px;
            color: #666;
            margin-top: 10px;
            font-style: italic;
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <h2>Engineering & IT Chatbot 🤖</h2>
        <div class="chat-box" id="chatBox">
            {% for entry in history %}
                <div class="user"><b>User:</b> {{ entry['user'] }}</div>
                <div class="bot"><b>Bot:</b> {{ entry['bot'] }}</div>
            {% endfor %}
        </div>
        <form method="POST">
            <input type="text" name="message" placeholder="Type your question..." required />
            <input type="submit" value="Send" />
        </form>
        <div class="watermark">✨ Made by Patel Studio ✨</div>
    </div>
</body>
</html>
"""

# ---------------------------
# Chatbot Logic
# ---------------------------
def chatbot_response(user_input):
    text = user_input.lower()

    
    # General greetings
    if "hello" in text or "hi" in text:
        return "Hello! 👋 I'm your study assistant. Ask me about engineering or IT subjects."

    if "how are you" in text:
        return "I'm just a bot, but I'm doing great! 😃 How can I help you?"

    if "bye" in text or "exit" in text:
        return "Goodbye! 👋 Have a great day!"

    # ---------------------------
    # Computer Science / IT
    # ---------------------------
    if "computer science" in text:
        return "💻 Computer Science is the study of algorithms, programming, data structures, operating systems, databases, AI, and more."

    if "data structures" in text:
        return ("📘 Data Structures organize data for efficiency.\n"
                "- Basic: Arrays, Linked Lists, Stacks, Queues\n"
                "- Advanced: Trees, Graphs, Hash Tables, Heaps")

    if "os" in text or "operating system" in text:
        return ("🖥️ Operating System manages hardware & software.\n"
                "- Functions: Process management, Memory management, File system, Security\n"
                "- Examples: Windows, Linux, MacOS, Android")

    if "ai" in text or "artificial intelligence" in text:
        return ("🤖 Artificial Intelligence is making machines think like humans.\n"
                "- Areas: Machine Learning, NLP, Computer Vision, Robotics, Expert Systems")

    if "ml" in text or "machine learning" in text:
        return ("📊 Machine Learning is teaching computers to learn from data.\n"
                "- Supervised Learning, Unsupervised Learning, Reinforcement Learning")

    # ---------------------------
    # Mechanical Engineering
    # ---------------------------
    if "mechanical engineering" in text:
        return "⚙️ Mechanical Engineering deals with machines, thermodynamics, robotics, CAD/CAM, manufacturing, and energy systems."

    if "thermodynamics" in text:
        return ("🔥 Thermodynamics studies heat & energy.\n"
                "- Laws of Thermodynamics, Heat Engines, Refrigeration, Entropy")

    if "fluid mechanics" in text:
        return ("💧 Fluid Mechanics studies liquids & gases.\n"
                "- Flow types: Laminar & Turbulent, Bernoulli’s theorem, CFD applications")

    # ---------------------------
    # Civil Engineering
    # ---------------------------
    if "civil engineering" in text:
        return "🏗️ Civil Engineering focuses on infrastructure: buildings, bridges, roads, dams, and environmental systems."

    if "surveying" in text:
        return ("📐 Surveying measures land & distances.\n"
                "- Methods: GPS, Theodolite, Total Station, Drone Surveying")

    if "geotechnical" in text:
        return ("🌍 Geotechnical Engineering studies soil & foundations.\n"
                "- Soil mechanics, Retaining walls, Tunnels, Foundation safety")

    # ---------------------------
    # Electrical Engineering
    # ---------------------------
    if "electrical engineering" in text:
        return "⚡ Electrical Engineering is about electricity, circuits, power systems, control systems, and renewable energy."

    if "power system" in text:
        return ("🔋 Power Systems deal with generation, transmission, and distribution of electricity.\n"
                "- Topics: Smart Grids, Renewable Integration, HVDC")

    if "control system" in text:
        return ("🎛️ Control Systems regulate processes.\n"
                "- Open Loop, Closed Loop, PID controllers, Automation, Robotics")

    # ---------------------------
    # Electronics Engineering
    # ---------------------------
    if "electronics" in text:
        return "📡 Electronics Engineering covers semiconductors, ICs, communication, signal processing, and embedded systems."

    if "signal processing" in text:
        return ("🎶 Signal Processing manipulates signals (audio, video, data).\n"
                "- Fourier Transform, Filters, Image Processing, Speech Recognition")


    # Greetings
    if "hello" in text or "hi" in text:
        return "🤖 Hello! I am InfoBot. You can ask me about Python, IT, Education, Health, Sports, Travel, History, or Geography."
    elif "how are you" in text:
        return "🤖 I'm doing great! I’m here to help you learn new things."

    # Python / IT field
    elif "python" in text:
        return ("🐍 Python is a popular programming language known for simplicity and readability. "
                "It is widely used in web development (Django, Flask), data science (NumPy, Pandas), "
                "machine learning (TensorFlow, PyTorch), and automation. Python’s syntax is close to English, "
                "which makes it beginner-friendly.")
    elif "programming" in text or "coding" in text:
        return ("💻 Programming is the process of giving instructions to a computer to perform tasks. "
                "Languages like Python, Java, C++, and JavaScript are used for app development, games, AI, and more.")
    elif "computer" in text:
        return ("🖥️ A computer is an electronic machine that processes data. It has hardware (CPU, RAM, storage, input/output devices) "
                "and software (programs, operating system) that work together to perform tasks.")
    elif "internet" in text:
        return ("🌐 The Internet is a global network that connects millions of computers. "
                "It allows communication (emails, chat), information sharing (websites, videos), and online services (banking, shopping).")
    elif "ai" in text or "artificial intelligence" in text:
        return ("🤖 Artificial Intelligence (AI) is the simulation of human intelligence in machines. "
                "AI is used in self-driving cars, voice assistants (Siri, Alexa), chatbots, recommendation systems, and healthcare.")
    elif "cybersecurity" in text:
        return ("🔒 Cybersecurity protects systems from hacking, viruses, and cyberattacks. "
                "It includes firewalls, encryption, ethical hacking, and awareness about phishing emails.")

    # Education
    elif "study" in text:
        return "📘 Best way to study is by using active recall, short sessions, and regular revisions."
    elif "exam" in text:
        return "📝 For exams, create a study plan, solve past papers, revise key concepts, and get proper rest."
    elif "math" in text:
        return "➗ Mathematics is about problem-solving. Practice algebra, geometry, and arithmetic daily for mastery."
    elif "science" in text:
        return "🔬 Science explains natural phenomena. It has three main branches: Physics, Chemistry, and Biology."

    # Health
    elif "diet" in text:
        return "🥗 A healthy diet should include fruits, vegetables, proteins, whole grains, and plenty of water."
    elif "exercise" in text:
        return "🏋️ Regular exercise improves strength, immunity, and mental health. Aim for 30 minutes daily."
    elif "sleep" in text:
        return "💤 Sleep is essential for recovery and brain function. Adults need 7–8 hours daily."
    elif "stress" in text:
        return "😌 Stress can be reduced through meditation, yoga, and hobbies like reading or music."

    # Travel
    elif "travel" in text:
        return "🌍 Travel helps you explore new cultures and places. Always pack light, carry IDs, and keep backup money."
    elif "beach" in text:
        return "🏖️ Goa, Maldives, and Bali are famous for beautiful beaches and water sports."
    elif "mountain" in text:
        return "🏔️ Shimla, Manali, and Switzerland are peaceful mountain destinations."

    # Sports
    elif "cricket" in text:
        return "🏏 Cricket is popular in India, Australia, and England. Sachin Tendulkar and Virat Kohli are cricket legends."
    elif "football" in text:
        return "⚽ Football is the most popular sport worldwide. Messi and Ronaldo are two of the greatest players."
    elif "olympics" in text:
        return "🏅 The Olympics are held every 4 years, where athletes from all over the world compete."

    # History
    elif "india independence" in text:
        return "🇮🇳 India gained independence on 15th August 1947 after a long struggle led by Mahatma Gandhi and other leaders."
    elif "world war" in text:
        return "⚔️ World War I (1914–1918) and World War II (1939–1945) were global wars that changed history."

    # Geography
    elif "continent" in text:
        return "🌍 There are 7 continents: Asia, Africa, North America, South America, Europe, Australia, and Antarctica."
    elif "ocean" in text:
        return "🌊 The 5 oceans are Pacific, Atlantic, Indian, Arctic, and Southern."
    elif "river" in text:
        return "🏞️ The Nile (Africa) is the world’s longest river, and the Ganga (India) is sacred in Hinduism."
    elif "earth" in text:
        return "🌎 Earth is the third planet from the Sun, home to land, water, air, and all living beings."
    
    # ---------------- Greetings ---------------- #
    if "hello" in text or "hi" in text:
        return (
            "🤖 Hello! I am EduBot, your learning assistant.\n"
            "I can explain Diploma & Degree subjects across Engineering, Medical, Science, Arts, Commerce, Law, and IT.\n"
            "Ask me anything!"
        )
    elif "how are you" in text:
        return "🤖 I'm always learning! Ready to help you with education-related questions."

    # ---------------- General Knowledge ---------------- #
    elif "internet" in text:
        return (
            "🌐 BASIC: The Internet connects computers globally to share information.\n"
            "📘 ADVANCED: It works via TCP/IP protocol, DNS, data packets, client-server architecture, "
            "and includes technologies like HTTP, HTTPS, VPN, and cloud computing."
        )
    elif "ai" in text or "artificial intelligence" in text:
        return (
            "🤖 BASIC: AI means making machines smart so they can think like humans.\n"
            "📘 ADVANCED: AI involves machine learning, neural networks, natural language processing, "
            "computer vision, robotics, reinforcement learning, and deep learning frameworks."
        )
    elif "cloud computing" in text:
        return (
            "☁️ BASIC: Cloud computing means using the internet to store and access data instead of your computer.\n"
            "📘 ADVANCED: It has 3 main types—SaaS, PaaS, IaaS. Uses virtualization, distributed servers, "
            "load balancing, data centers, and services like AWS, Azure, GCP."
        )

    # ---------------- IT & Computer Science ---------------- #
    elif "python" in text:
        return (
            "🐍 BASIC: Python is an easy-to-learn programming language.\n"
            "📘 ADVANCED: Supports multiple paradigms (OOP, functional, procedural). Popular frameworks: Django (web), "
            "Flask (API), Pandas/Numpy (data), TensorFlow/PyTorch (AI). It is interpreted, dynamically typed."
        )
    elif "java" in text:
        return (
            "☕ BASIC: Java is used for apps, games, and web applications.\n"
            "📘 ADVANCED: It’s an object-oriented, platform-independent language (JVM). "
            "Covers concepts like multithreading, garbage collection, JDBC, Spring Boot."
        )
    elif "database" in text:
        return (
            "🗄️ BASIC: A database stores information in tables.\n"
            "📘 ADVANCED: Types include SQL (MySQL, PostgreSQL) and NoSQL (MongoDB, Cassandra). "
            "Covers normalization, indexing, transactions (ACID), distributed databases, sharding, and data security."
        )
    elif "network" in text:
        return (
            "🌐 BASIC: A network connects devices for communication.\n"
            "📘 ADVANCED: Includes OSI model, TCP/IP stack, routing, DNS, DHCP, firewalls, "
            "cybersecurity, VPNs, IPv4/IPv6 addressing, and SDN (Software Defined Networking)."
        )

    # ---------------- Engineering Subjects ---------------- #
    elif "mechanical engineering" in text:
        return (
            "⚙️ BASIC: Mechanical Engineering studies machines and engines.\n"
            "📘 ADVANCED: It covers thermodynamics, heat transfer, fluid mechanics, design of machines, "
            "robotics, CAD/CAM, IC engines, HVAC systems, and manufacturing processes."
        )
    elif "civil engineering" in text:
        return (
            "🏗️ BASIC: Civil Engineering is about building construction.\n"
            "📘 ADVANCED: Includes structural analysis, geotechnical engineering, hydraulics, "
            "transportation engineering, surveying, concrete technology, environmental engineering."
        )
    elif "electrical engineering" in text:
        return (
            "🔌 BASIC: Electrical Engineering studies electricity and circuits.\n"
            "📘 ADVANCED: Covers power systems, machines, circuit theory, control systems, "
            "signal processing, renewable energy, and smart grids."
        )
    elif "electronics engineering" in text:
        return (
            "📡 BASIC: Electronics deals with circuits and devices.\n"
            "📘 ADVANCED: Includes microprocessors, embedded systems, VLSI, digital communication, IoT, "
            "semiconductors, and signal processing."
        )
    elif "it engineering" in text:
        return (
            "💻 BASIC: IT Engineering studies computers and software.\n"
            "📘 ADVANCED: Includes networking, programming, cybersecurity, AI, cloud computing, databases, "
            "software engineering, web development."
        )

    # ---------------- Medical ---------------- #
    elif "medicine" in text or "medical" in text:
        return (
            "🩺 BASIC: Medicine is about treating patients and diseases.\n"
            "📘 ADVANCED: Includes anatomy, physiology, pathology, surgery, pharmacology, "
            "biochemistry, radiology, diagnostics, and preventive healthcare."
        )
    elif "pharmacy" in text:
        return (
            "💊 BASIC: Pharmacy is about drugs and their use.\n"
            "📘 ADVANCED: Includes pharmaceutics, pharmacology, pharmaceutical chemistry, "
            "drug design, clinical trials, biopharmaceutics, pharmacovigilance."
        )
    elif "nursing" in text:
        return (
            "👩‍⚕️ BASIC: Nursing is about patient care.\n"
            "📘 ADVANCED: Covers pediatric nursing, psychiatric nursing, critical care, "
            "community health, midwifery, emergency nursing."
        )

    # ---------------- Commerce ---------------- #
    elif "accounting" in text:
        return (
            "📒 BASIC: Accounting means recording financial transactions.\n"
            "📘 ADVANCED: Includes double-entry bookkeeping, balance sheets, auditing, "
            "IFRS/GAAP standards, taxation, and cost accounting."
        )
    elif "economics" in text:
        return (
            "📊 BASIC: Economics is the study of money and trade.\n"
            "📘 ADVANCED: Includes microeconomics (demand, supply, pricing) and macroeconomics (GDP, inflation, monetary policy, trade)."
        )
    elif "business management" in text:
        return (
            "📈 BASIC: Business management means running companies.\n"
            "📘 ADVANCED: Includes HR management, financial management, marketing, operations, "
            "organizational behavior, entrepreneurship, and leadership strategies."
        )

    # ---------------- Arts & Humanities ---------------- #
    elif "history" in text:
        return (
            "📜 BASIC: History studies past events.\n"
            "📘 ADVANCED: Covers world history, Indian independence, revolutions, ancient civilizations, "
            "modern wars, historical analysis methods."
        )
    elif "geography" in text:
        return (
            "🌍 BASIC: Geography studies the Earth.\n"
            "📘 ADVANCED: Includes physical geography (climate, landforms), human geography (population, urbanization), "
            "GIS mapping, environment, and geopolitics."
        )
    elif "literature" in text:
        return (
            "📖 BASIC: Literature is about stories and poems.\n"
            "📘 ADVANCED: Includes classical literature, modernism, postcolonialism, literary criticism, "
            "comparative literature, and cultural studies."
        )

    # ---------------- Law ---------------- #
    elif "law" in text:
        return (
            "⚖️ BASIC: Law is about rules and justice.\n"
            "📘 ADVANCED: Covers Indian Constitution, criminal law, civil law, corporate law, "
            "cyber law, intellectual property law, and international law."
        )

    # ---------------- Science ---------------- #
    elif "physics" in text:
        return (
            "🔬 BASIC: Physics studies matter and energy.\n"
            "📘 ADVANCED: Includes mechanics, thermodynamics, electromagnetism, optics, "
            "quantum physics, nuclear physics, relativity, astrophysics."
        )
    elif "chemistry" in text:
        return (
            "⚗️ BASIC: Chemistry is about elements and reactions.\n"
            "📘 ADVANCED: Includes organic, inorganic, physical, analytical, "
            "biochemistry, polymer chemistry, spectroscopy."
        )
    elif "biology" in text:
        return (
            "🧬 BASIC: Biology studies life.\n"
            "📘 ADVANCED: Covers cell biology, genetics, molecular biology, evolution, "
            "ecology, physiology, microbiology, biotechnology."
        )
    elif "mathematics" in text or "math" in text:
        return (
            "➗ BASIC: Math is about numbers and formulas.\n"
            "📘 ADVANCED: Includes algebra, geometry, trigonometry, calculus, probability, "
            "statistics, linear algebra, differential equations, numerical methods."
        )

    # ---------------- Other Subjects ---------------- #
    elif "psychology" in text:
        return (
            "🧠 BASIC: Psychology is the study of human behavior.\n"
            "📘 ADVANCED: Includes cognitive psychology, abnormal psychology, social psychology, "
            "behavioral therapy, developmental psychology, neuropsychology."
        )
    elif "agriculture" in text:
        return (
            "🌱 BASIC: Agriculture is about farming.\n"
            "📘 ADVANCED: Includes agronomy, soil science, irrigation, crop breeding, "
            "organic farming, agricultural technology, food security."
        )

    # ---------------- Exit ---------------- #
    elif "bye" in text or "exit" in text:
        return "👋 Goodbye! Keep learning every day."

    # ---------------- Default ---------------- #
    else:
        return "🤔 I don’t know that yet. Try asking about Engineering, IT, Medical, Commerce, Arts, Science, or Law."
    
    
# ---------------- Knowledge Base (expanded) ---------------- #


    # greetings
    if any(word in q for word in ["hello", "hi", "hey"]):
        return ("Hello! I'm EduBot — an expanded study assistant.\n"
                "Ask me about any subject (e.g., 'mechanical engineering', 'python programming', 'human anatomy', 'accounting').\n"
                "I provide BASIC / INTERMEDIATE / ADVANCED explanations, key topics, sample syllabi, recommended books, and career paths.")

    if "how are you" in q:
        return "I'm a chatbot — ready to help you study! Ask any subject or type 'help' for examples."

    if "help" == q or "examples" in q:
        return ("Try queries like:\n"
                "- 'Explain python'\n- 'Tell me about mechanical engineering'\n- 'Give detailed syllabus for civil engineering diploma'\n- 'Advanced topics in machine learning'\n- 'Career options in pharmacy'")

    # ---------------- IT & CS: Python ---------------- #
    if "python" in q and "advanced" in q or ("explain python" in q and "advanced" in q):
        return make_response(
            title="Python (Advanced)",
            basic="Python is a high-level, interpreted programming language famous for its readability and broad ecosystem.",
            intermediate=("At intermediate level: modules & packages, file I/O, OOP (classes, inheritance), "
                          "exceptions, list/dict comprehensions, decorators, generators, virtual environments."),
            advanced=("Advanced topics: concurrency (asyncio, threading, multiprocessing), metaprogramming, "
                      "C-extension modules, performance tuning, memory profiling, design patterns, "
                      "security considerations, packaging and CI/CD integration."),
            key_topics=["Data structures & algorithms", "OOP & design patterns", "Async programming", "Testing (pytest)", "Packaging (pip)"],
            syllabus_example=("Semester 1: Python basics, data types, control flow\n"
                              "Semester 2: OOP, modules, file handling\n"
                              "Semester 3: Data structures & algorithms, databases\n"
                              "Semester 4: Web frameworks (Flask/Django), REST API, deployment"),
            books=["'Automate the Boring Stuff with Python' - Al Sweigart",
                   "'Fluent Python' - Luciano Ramalho",
                   "'Python Cookbook' - David Beazley"],
            careers=["Software developer", "Data engineer", "Machine Learning engineer", "DevOps engineer"]
        )

    if "python" in q or "explain python" in q or q == "programming python":
        return make_response(
            title="Python (Overview)",
            basic=("Python is an interpreted, high-level language with dynamic typing. "
                   "It is used for web development, scripting, data science, automation, and more."),
            intermediate=("It supports multiple paradigms: procedural, object-oriented, and functional. "
                          "Key libraries include NumPy, Pandas, Matplotlib for data, and Flask/Django for web."),
            advanced=("Advanced use includes building microservices, data pipelines, deep learning models, "
                      "optimizing with C extensions, and integrating with cloud services."),
            key_topics=["Syntax & basics", "Functions & modules", "OOP", "Libraries (Pandas, NumPy)", "Frameworks (Flask, Django)"],
            books=["'Learning Python' - Mark Lutz", "'Python Crash Course' - Eric Matthes"],
            careers=["Backend developer", "Scripting & automation specialist", "Data analyst"]
        )

    # ---------------- IT & CS: Machine Learning & AI ---------------- #
    if "machine learning" in q or "ml" in q or "deep learning" in q:
        return make_response(
            title="Machine Learning & Deep Learning",
            basic=("Machine learning lets computers learn patterns from data to make predictions. "
                   "Common tasks: classification, regression, clustering."),
            intermediate=("Intermediate topics: supervised vs unsupervised learning, model evaluation (precision, recall, F1), "
                          "feature engineering, regularization, hyperparameter tuning."),
            advanced=("Advanced topics: deep neural networks, CNNs for vision, RNNs/LSTMs for sequences, transformers (BERT/GPT), "
                      "model deployment, MLOps, distributed training, explainability (SHAP/LIME), and fairness."),
            key_topics=["Linear regression", "Logistic regression", "Decision trees", "SVM", "Neural networks", "CNNs", "Transformers"],
            syllabus_example=("Course 1: Math for ML (linear algebra, probability)\n"
                              "Course 2: Classical ML algorithms, scikit-learn\n"
                              "Course 3: Deep learning basics, TensorFlow/PyTorch\n"
                              "Course 4: Project & deployment (Flask + Docker + cloud)"),
            books=["'Hands-On Machine Learning' - Aurélien Géron", "'Deep Learning' - Ian Goodfellow et al."],
            careers=["ML engineer", "Data scientist", "Research scientist", "AI product manager"]
        )

    # ---------------- Networking & Cybersecurity ---------------- #
    if "network" in q or "networking" in q:
        return make_response(
            title="Computer Networks",
            basic="Computer networking is about connecting devices to exchange data using protocols like TCP/IP.",
            intermediate=("Includes network models (OSI/TCP), switching vs routing, IP addressing and subnetting, "
                          "routing protocols (OSPF, BGP), and VLANs."),
            advanced=("Advanced topics: network security (IDS/IPS), VPNs, SDN, network automation, QoS, and cloud networking."),
            key_topics=["OSI model", "IP addressing", "Routing & switching", "TCP/UDP", "DNS/DHCP"],
            books=["'Computer Networking: A Top-Down Approach' - Kurose & Ross"],
            careers=["Network engineer", "Cloud network architect", "Security analyst"]
        )

    if "cybersecurity" in q or "security" in q:
        return make_response(
            title="Cybersecurity",
            basic="Cybersecurity protects systems and data from unauthorized access and threats.",
            intermediate=("Topics: encryption basics, authentication mechanisms, secure coding practices, "
                          "firewalls, and vulnerability assessment."),
            advanced=("Advanced: penetration testing, incident response, SIEM, threat hunting, advanced cryptography, "
                      "secure architecture design, and compliance frameworks (ISO, PCI-DSS)."),
            key_topics=["Cryptography", "Network security", "Application security", "Security operations"],
            books=["'The Web Application Hacker's Handbook' - Dafydd Stuttard", "'Security Engineering' - Ross Anderson"],
            careers=["Security analyst", "Pen tester", "CISO (senior)"]
        )

    # ---------------- Engineering: Mechanical ---------------- #
    if "mechanical engineering" in q:
        return make_response(
            title="Mechanical Engineering",
            basic="Mechanical engineering is the discipline that applies engineering, physics and materials science for analysis, design, manufacturing, and maintenance of mechanical systems.",
            intermediate=("Important areas include thermodynamics, mechanics of materials, fluid mechanics, machine design, manufacturing processes, and CAD."),
            advanced=("Advanced study explores computational fluid dynamics (CFD), finite element analysis (FEA), robotics, control systems, mechatronics, "
                      "advanced materials, and thermal system design."),
            key_topics=["Thermodynamics", "Strength of materials", "Kinematics", "Heat transfer", "Manufacturing"],
            syllabus_example=("Diploma Year 1: Engineering mechanics, material science, engineering drawing\n"
                              "Year 2: Thermodynamics, fluid mechanics, manufacturing technology\n"
                              "Year 3: Machine design, CAD/CAM, projects"),
            books=["'Engineering Mechanics' - Hibbeler", "'Mechanics of Materials' - Gere & Timoshenko"],
            careers=["Design engineer", "Manufacturing engineer", "Automation engineer", "R&D"]
        )

    # ---------------- Engineering: Civil ---------------- #
    if "civil engineering" in q:
        return make_response(
            title="Civil Engineering",
            basic="Civil engineering focuses on infrastructure design and construction, including buildings, roads, bridges and water systems.",
            intermediate=("Covers structural analysis, concrete and steel design, geotechnical engineering, hydraulics, transportation engineering and surveying."),
            advanced=("Advanced topics include earthquake engineering, bridge design, finite element analysis of structures, sustainable construction techniques, "
                      "and advanced geotechnical modeling."),
            key_topics=["Structural analysis", "Concrete technology", "Soil mechanics", "Hydraulics", "Surveying"],
            syllabus_example=("Semester 1: Engineering Math, Material Science\n"
                              "Semester 4: Structural analysis, Concrete design\n"
                              "Semester 6: Transportation engineering, Project"),
            books=["'Design of Reinforced Concrete' - Nilson", "'Principles of Geotechnical Engineering' - Braja M. Das"],
            careers=["Site engineer", "Structural engineer", "Urban planner", "Project manager"]
        )

    # ---------------- Engineering: Electrical & Electronics ---------------- #
    if "electrical engineering" in q:
        return make_response(
            title="Electrical Engineering",
            basic="Electrical engineering deals with generation, distribution and application of electrical power and electronic systems.",
            intermediate=("Includes circuit theory, power systems, electrical machines, control systems, and power electronics."),
            advanced=("Advanced areas: smart grids, power system stability, high-voltage engineering, renewable integration, control theory and signal processing."),
            key_topics=["Circuit analysis", "Electrical machines", "Power systems", "Control systems", "Power electronics"],
            syllabus_example=("Year 1: Basic circuits, mathematics\n"
                              "Year 2: Machines, electromagnetic theory\n"
                              "Year 3: Power systems, control engineering"),
            books=["'Electric Machinery' - Fitzgerald", "'Power System Analysis' - Grainger & Stevenson"],
            careers=["Power systems engineer", "Control systems engineer", "Protection engineer"]
        )

    if "electronics" in q or "electronics engineering" in q:
        return make_response(
            title="Electronics & Communication",
            basic="Electronics focuses on semiconductor devices, analog & digital circuits, and communication systems.",
            intermediate=("Topics: analog electronics, digital logic, microcontrollers, communication principles, signal processing."),
            advanced=("Advanced: VLSI design, embedded systems, RF/microwave engineering, 5G communication, FPGA design, IoT systems."),
            key_topics=["Semiconductor devices", "Analog circuits", "Digital logic", "Microcontrollers", "Communication systems"],
            books=["'Microelectronic Circuits' - Sedra & Smith", "'Digital Design' - Morris Mano"],
            careers=["Embedded systems engineer", "VLSI designer", "RF engineer"]
        )

    # ---------------- Medical & Health ---------------- #
    if "anatomy" in q or "human anatomy" in q:
        return make_response(
            title="Human Anatomy",
            basic="Anatomy is the study of the structure of organisms and their parts, especially the human body.",
            intermediate=("Focuses on systems: skeletal, muscular, nervous, cardiovascular, respiratory, digestive, urinary, and reproductive."),
            advanced=("Advanced anatomy covers histology (microscopic anatomy), embryology (development), clinical correlations, surgical anatomy and radiological anatomy."),
            key_topics=["Skeletal system", "Muscular system", "Nervous system", "Cardiovascular system"],
            books=["'Gray's Anatomy' - standard reference", "'Clinically Oriented Anatomy' - Moore"],
            careers=["Surgeon (after medical degree)", "Anatomist researcher", "Clinical technician"]
        )

    if "physiology" in q:
        return make_response(
            title="Human Physiology",
            basic="Physiology studies normal functions of living organisms and their parts.",
            intermediate=("Includes how organ systems function: cardiac output, neural signaling, renal function, endocrine pathways."),
            advanced=("Advanced topics: integrative physiology, pathophysiology (how disease alters physiology), exercise physiology, and research methods."),
            key_topics=["Cell physiology", "Neurophysiology", "Endocrinology", "Cardiovascular physiology"],
            books=["'Guyton and Hall Textbook of Medical Physiology'"],
            careers=["Clinical physiologist", "Medical researcher", "Physio therapist (with specialization)"]
        )

    if "pharmacy" in q or "pharmacology" in q:
        return make_response(
            title="Pharmacy & Pharmacology",
            basic="Pharmacy covers the preparation, dispensing and proper utilization of medicines.",
            intermediate=("Pharmacology focuses on drug mechanisms, pharmacokinetics (ADME), pharmacodynamics, therapeutic uses and toxicology."),
            advanced=("Advanced topics: drug design, clinical trials, regulatory affairs, biopharmaceutics, pharmacovigilance and formulation technology."),
            key_topics=["Pharmacokinetics", "Pharmacodynamics", "Drug interactions", "Dosage forms"],
            books=["'Goodman & Gilman's The Pharmacological Basis of Therapeutics'"],
            careers=["Clinical pharmacist", "Regulatory affairs", "Pharmaceutical R&D"]
        )

    # ---------------- Commerce & Business ---------------- #
    if "accounting" in q:
        return make_response(
            title="Accounting",
            basic="Accounting records and reports financial transactions of a business in ledgers and prepares financial statements.",
            intermediate=("Involves double-entry bookkeeping, preparation of income statement, balance sheet, cash flow statements, basic auditing."),
            advanced=("Financial accounting standards (IFRS/GAAP), management accounting (cost analysis), tax planning, forensic accounting, and auditing standards are advanced areas."),
            key_topics=["Journal entries", "Trial balance", "Financial statements", "Cost accounting", "Taxation"],
            books=["'Financial Accounting' - T.S. Grewal", "'Cost Accounting' - Horngren"],
            careers=["Accountant", "Auditor", "Finance analyst", "Tax consultant"]
        )

    if "economics" in q:
        return make_response(
            title="Economics",
            basic="Economics studies production, distribution, and consumption of goods and services.",
            intermediate=("Microeconomics (markets, consumers), Macroeconomics (GDP, inflation, monetary policy), international trade and public finance."),
            advanced=("Advanced uses econometrics, game theory, policy modeling, international finance, and development economics."),
            key_topics=["Supply & demand", "Elasticity", "GDP & inflation", "Monetary & fiscal policy"],
            books=["'Principles of Economics' - N. Gregory Mankiw", "'Econometrics' - Damodar Gujarati"],
            careers=["Economist", "Policy analyst", "Banking professional", "Researcher"]
        )

    if "business management" in q or "management" in q:
        return make_response(
            title="Business & Management",
            basic="Business management studies planning, organizing, leading and controlling to achieve organizational goals.",
            intermediate=("Covers marketing, human resources, finance, operations, supply chain, and strategic management."),
            advanced=("Includes corporate strategy, international business, mergers & acquisitions, leadership studies and entrepreneurship."),
            key_topics=["Marketing", "Finance", "Operations", "HR", "Strategy"],
            books=["'Principles of Marketing' - Kotler", "'Fundamentals of Management' - Robbins"],
            careers=["Manager", "Business analyst", "HR manager", "Operations manager", "Consultant"]
        )

    # ---------------- Arts & Social Sciences ---------------- #
    if "history" in q and "detailed" in q or ("history" in q and "advanced" in q):
        return make_response(
            title="History (Detailed)",
            basic="History studies past events, civilizations and major turning points that shaped societies.",
            intermediate=("Focuses on political, economic, social and cultural history. In degree-level study you analyze primary sources, historiography and methodologies."),
            advanced=("Advanced history requires critical analysis of sources, comparative history, use of archaeological evidence, digital humanities tools and theoretical approaches like Marxism, postcolonial theory, and cultural studies."),
            key_topics=["Ancient civilizations", "Medieval period", "Colonialism", "World Wars", "Independence movements"],
            syllabus_example=("Year 1: Ancient & Medieval history\nYear 2: Modern history & historiography\nYear 3: Special topics (economic, social, cultural history) & dissertation"),
            books=["'The History of the Ancient World' - Susan Wise Bauer", "'A People's History of the World' - Chris Harman"],
            careers=["Historian", "Archivist", "Teacher", "Museum curator"]
        )

    if "geography" in q and ("detailed" in q or "advanced" in q):
        return make_response(
            title="Geography (Detailed)",
            basic="Geography is the study of Earth's landscapes, environments, and the relationship between people and their environments.",
            intermediate=("Physical geography: geomorphology, climatology, hydrology. Human geography: urbanization, population studies, economic geography. Tools: GIS & remote sensing."),
            advanced=("Advanced topics include spatial analysis using GIS, environmental impact assessment, climate modeling, and geographic information science."),
            key_topics=["Cartography", "GIS", "Climatology", "Population studies", "Resource management"],
            books=["'Physical Geography' - Strahler", "'Geographic Information Systems and Science' - Longley et al."],
            careers=["GIS analyst", "Urban planner", "Environmental consultant"]
        )

    if "literature" in q or "english literature" in q:
        return make_response(
            title="Literature & Languages",
            basic="Literature studies written works — novels, poetry, drama — and how they reflect culture and human experience.",
            intermediate=("This level covers literary periods (Romanticism, Modernism), major authors, literary devices, and critical approaches."),
            advanced=("Advanced study includes theoretical frameworks (structuralism, post-structuralism), comparative literature, and research projects analyzing texts and contexts."),
            key_topics=["Poetry analysis", "Novel study", "Drama", "Literary criticism"],
            books=["'How to Read Literature Like a Professor' - Thomas C. Foster", "'Literary Theory' - Terry Eagleton"],
            careers=["Writer", "Editor", "Teacher", "Content strategist"]
        )

    # ---------------- Law ---------------- #
    if "law" in q and ("detailed" in q or "advanced" in q):
        return make_response(
            title="Law (Comprehensive)",
            basic="Law governs rules and behavior set by a society; it defines rights and obligations.",
            intermediate=("Includes constitutional law, contract law, torts, criminal law, property law, and administrative law."),
            advanced=("Advanced covers corporate law, intellectual property, cyber law, arbitration, international law, litigation strategy, and legal research methods."),
            key_topics=["Constitution", "Criminal procedure", "Contracts", "Torts", "IP law"],
            books=["'An Introduction to the Study of Law' - Various authors depending on jurisdiction"],
            careers=["Lawyer/advocate", "Corporate counsel", "Judge (after further qualifications)", "Legal researcher"]
        )

    # ---------------- Science ---------------- #
    if "physics" in q and ("detailed" in q or "advanced" in q):
        return make_response(
            title="Physics (Advanced)",
            basic="Physics studies matter, energy and the fundamental forces of nature.",
            intermediate=("Classical mechanics, electromagnetism, thermodynamics, and waves form the foundation."),
            advanced=("Modern physics includes quantum mechanics, statistical mechanics, solid-state physics, particle physics and general relativity. Mathematical methods and computational physics are used widely."),
            key_topics=["Mechanics", "Electrodynamics", "Quantum mechanics", "Thermodynamics", "Statistical physics"],
            books=["'Introduction to Quantum Mechanics' - Griffiths", "'Classical Mechanics' - Goldstein"],
            careers=["Research scientist", "Lab technician", "Data analyst", "Engineering roles"]
        )

    if "chemistry" in q and ("detailed" in q or "advanced" in q):
        return make_response(
            title="Chemistry (Advanced)",
            basic="Chemistry is the study of substances, their properties, and how they interact.",
            intermediate=("Organic chemistry, inorganic chemistry, physical chemistry, analytical techniques, titrations and reaction mechanisms."),
            advanced=("Advanced: spectroscopy methods (NMR, IR), kinetics, quantum chemistry, materials chemistry, biochemistry and computational chemistry."),
            key_topics=["Organic reactions", "Periodic properties", "Chemical bonding", "Spectroscopy"],
            books=["'Organic Chemistry' - Clayden", "'Inorganic Chemistry' - Shriver & Atkins"],
            careers=["Chemical analyst", "Research chemist", "Pharmaceutical R&D"]
        )

    if "biology" in q and ("detailed" in q or "advanced" in q):
        return make_response(
            title="Biology (Advanced)",
            basic="Biology studies living organisms, their functions, growth, origin, evolution, and taxonomy.",
            intermediate=("Cell biology, genetics, evolution, ecology, physiology, microbiology."),
            advanced=("Advanced: molecular biology techniques, genomics, biotechnology, bioinformatics, developmental biology and advanced lab methods."),
            key_topics=["Cell structure", "DNA & genetics", "Evolution", "Ecology", "Biotech methods"],
            books=["'Molecular Biology of the Cell' - Alberts", "'Principles of Genetics'"],
            careers=["Biotechnologist", "Research associate", "Clinical lab scientist"]
        )

    if "mathematics" in q or "math" in q and ("detailed" in q or "advanced" in q):
        return make_response(
            title="Mathematics (Advanced)",
            basic="Mathematics deals with numbers, quantities, shapes, structures and their relationships.",
            intermediate=("Calculus, linear algebra, probability & statistics, discrete math, and differential equations."),
            advanced=("Advanced includes real & complex analysis, abstract algebra, topology, numerical methods, optimization, and applied mathematics."),
            key_topics=["Calculus", "Linear algebra", "Probability", "Statistics", "Differential equations"],
            books=["'Calculus' - James Stewart", "'Linear Algebra Done Right' - Sheldon Axler"],
            careers=["Data scientist", "Quantitative analyst", "Research mathematician", "Actuary"]
        )

    # ---------------- Agriculture & Environment ---------------- #
    if "agriculture" in q and ("detailed" in q or "advanced" in q):
        return make_response(
            title="Agriculture (Detailed)",
            basic="Agriculture is the practice of cultivating soil, growing crops, and raising livestock.",
            intermediate=("Soil science, crop rotation, irrigation methods, pest management, and post-harvest techniques."),
            advanced=("Advanced: crop genetics, precision agriculture (drones, sensors), sustainable practices, climate-smart agriculture and agri-business."),
            key_topics=["Soil fertility", "Crop production", "Plant breeding", "Agri-extension"],
            books=["'Principles of Agronomy' - T. Ravi", "'Plant Pathology' - Various authors"],
            careers=["Agronomist", "Soil scientist", "Agri-entrepreneur", "Researcher"]
        )

    # ---------------- Psychology & Education ---------------- #
    if "psychology" in q and ("detailed" in q or "advanced" in q):
        return make_response(
            title="Psychology (Detailed)",
            basic="Psychology studies mental processes and behavior.",
            intermediate=("Covers cognitive psychology, developmental stages, personality theories, and research methods."),
            advanced=("Includes clinical psychology, therapies (CBT, psychodynamic), neuropsychology, psychometrics and advanced research."),
            key_topics=["Cognitive processes", "Development", "Abnormal psychology", "Therapeutic approaches"],
            books=["'Introduction to Psychology' - James W. Kalat", "'Abnormal Psychology' - Barlow & Durand"],
            careers=["Counselor", "Clinical psychologist (requires higher degree)", "HR specialist", "Researcher"]
        )

    if "education" in q and ("detailed" in q or "advanced" in q):
        return make_response(
            title="Education (Teaching & Pedagogy)",
            basic="Education involves teaching and learning processes, curriculum design and assessment.",
            intermediate=("Topics: pedagogy methods, classroom management, assessment strategies, educational psychology."),
            advanced=("Advanced: curriculum development, educational research, edtech integration, inclusive education, policy analysis."),
            key_topics=["Pedagogy", "Assessment", "Educational psychology", "Curriculum design"],
            books=["'How People Learn' - National Research Council", "'Educational Psychology' - Anita Woolfolk"],
            careers=["Teacher", "Curriculum developer", "Educational researcher", "Instructional designer"]
        )

    # ---------------- Multi-subject query fallback behaviors ---------------- #
    # Support queries like: "syllabus for civil diploma", "career in biotechnology", "books for thermodynamics"
    if "syllabus" in q or "semester" in q:
        # Try to detect subject mentioned
        for subj in ["civil", "mechanical", "electrical", "computer", "electronics", "pharmacy", "biology", "chemistry", "physics", "accounting", "economics"]:
            if subj in q:
                # return a generic semesterized syllabus for the detected subject
                if subj == "civil":
                    return make_response(
                        title="Civil Engineering - Sample Diploma Syllabus (Example)",
                        basic="This is a sample semester-wise syllabus for a 3-year diploma in civil engineering.",
                        syllabus_example=(
                            "Year 1: Engineering Mechanics, Material Science, Engineering Drawing, Basic Surveying, Applied Mathematics\n"
                            "Year 2: Strength of Materials, Concrete Technology, Fluid Mechanics, Building Materials, Structural Analysis\n"
                            "Year 3: Design of Structures, Transportation Engineering, Project Management, Estimation & Costing, Practical Training/Project"
                        ),
                        books=["'Building Materials' - P.C. Varghese", "'Strength of Materials' - Gere"],
                        careers=["Junior engineer", "Site supervisor", "Estimator"]
                    )
                if subj == "computer":
                    return make_response(
                        title="Computer Science / IT - Sample Diploma Syllabus",
                        basic="Sample topics across semesters for a 3-year IT / Computer diploma.",
                        syllabus_example=(
                            "Year 1: Fundamentals of Computers, Programming Basics (C/Python), Discrete Maths\n"
                            "Year 2: Data Structures, DBMS, Operating Systems, Computer Networks\n"
                            "Year 3: Web Technologies, Software Engineering, Project Work, Cybersecurity basics"
                        ),
                        books=["'Data Structures' - Seymour Lipschutz", "'Operating Systems' - Silberschatz"],
                        careers=["Junior developer", "Helpdesk", "System administrator"]
                    )
                # generic fallback for other detected subject
                return f"Sample syllabus for {subj.capitalize()} is not available in this offline demo. Ask 'syllabus for {subj} diploma' for a sample."
        return "Please mention a subject explicitly, e.g., 'syllabus for civil engineering diploma' or 'semester topics for computer engineering'."

    if "career" in q or "job" in q or "career options" in q:
        # look for subject
        for subj in ["python", "machine learning", "mechanical", "civil", "electrical", "electronics", "commerce", "accounting", "pharmacy", "nursing", "law", "agriculture"]:
            if subj in q:
                if subj == "machine learning":
                    return make_response(
                        title="Career Options: Machine Learning",
                        basic="ML engineers and data scientists build predictive models and work with data pipelines.",
                        careers=["Machine Learning Engineer", "Data Scientist", "AI Researcher", "MLOps Engineer"],
                        books=["'Hands-On Machine Learning' - Aurélien Géron"]
                    )
                if subj == "python":
                    return make_response(
                        title="Career Options: Python",
                        basic="Python skills are used in backend development, automation, testing, data work, and AI.",
                        careers=["Backend Engineer", "Automation Engineer", "Data Engineer", "Scripting Specialist"]
                    )
                if subj == "mechanical":
                    return make_response(
                        title="Career Options: Mechanical Engineering",
                        basic="Mechanical engineers design and analyze mechanical systems.",
                        careers=["Design Engineer", "Manufacturing Engineer", "Maintenance Engineer", "R&D Engineer"]
                    )
                if subj == "civil":
                    return make_response(
                        title="Career Options: Civil Engineering",
                        basic="Civil engineers work in construction, infrastructure and urban planning.",
                        careers=["Site Engineer", "Structural Engineer", "Transport Planner", "Project Manager"]
                    )
                if subj == "pharmacy":
                    return make_response(
                        title="Career Options: Pharmacy",
                        basic="Pharmacy offers clinical, industrial and regulatory roles.",
                        careers=["Clinical pharmacist", "Quality control analyst", "Pharma production", "Regulatory affairs"]
                    )
        return "Please specify which subject or skill you want career guidance for, e.g., 'career options in civil engineering' or 'jobs after BSc in computer science'."

    # ---------------- Study-help features ---------------- #
    if q.startswith("define ") or q.startswith("what is "):
        # Very generic: try to give a short definition fallback
        term = q.replace("define ", "").replace("what is ", "").strip()
        if term:
            return f"Definition: {term.capitalize()} — (short general definition): This is an important concept. For detailed explanation, ask 'explain {term} in detail' or 'advanced {term}'."

    # ---------------- Fallback: try detect subject words & produce detailed answer ---------------- #
    subject_keywords = {
        "thermodynamics": ("Thermodynamics", 
            "BASIC: Study of heat, work, energy and their transformations.",
            "INTERMEDIATE: Laws of thermodynamics, heat engines, Carnot cycle, entropy, thermodynamic properties.",
            "ADVANCED: Statistical thermodynamics, non-equilibrium thermodynamics, exergy analysis, refrigeration cycles.",
            ["Zeroth/First/Second/Third laws", "Carnot cycle", "Entropy", "Thermal efficiency"],
            "Typical modules include properties of pure substances, power cycles, refrigeration.",
            ["'Thermodynamics' - Cengel & Boles"],
            ["Thermal engineer", "HVAC engineer", "R&D"]
        ),
        "data structures": ("Data Structures",
            "BASIC: Ways to store and organize data like arrays, linked lists, stacks and queues.",
            "INTERMEDIATE: Trees, graphs, hash tables, algorithmic complexity (Big-O).",
            "ADVANCED: Balanced trees, graph algorithms, advanced hashing, cache-friendly data structures and memory optimizations.",
            ["Arrays", "Linked Lists", "Stacks", "Queues", "Trees", "Graphs", "Hash Tables"],
            "Course usually includes implementation in C/C++/Java/Python, problem-solving labs.",
            ["'Introduction to Algorithms' - Cormen et al."],
            ["Software developer", "Algorithm engineer"]
        ),
    }
    for key, val in subject_keywords.items():
        if key in q:
            title, basic, intermediate, advanced, topics, syllabus, books, careers = val
            return make_response(title=title, basic=basic, intermediate=intermediate, advanced=advanced, key_topics=topics, syllabus_example=syllabus, books=books, careers=careers)

    # ---------------- Final fallback: don't know ---------------- #
    return ("🤔 I don't have a ready detailed entry for that exact query in this offline demo.\n"
            "Try asking a subject name directly, e.g., 'Explain mechanical engineering in detail',\n"
            "or request 'syllabus for <subject> diploma' or 'career options in <subject>'.\n"
            "If you want, I can also provide sample exam questions, project ideas, or code examples for many subjects.")

    if "hello" in text or "hi" in text:
        return "Hello! 👋 I'm your study assistant. Ask me about engineering or IT subjects."

    if "how are you" in text:
        return "I'm doing great! 😃 Thanks for asking. How can I help you today?"

    if "bye" in text:
        return "Goodbye! 👋 Have a wonderful day ahead."

    # Computer Science
    if "computer science" in text:
        return "💻 Computer Science deals with programming, data structures, algorithms, OS, DBMS, AI, ML, and more."

    if "data structures" in text:
        return "📘 Data Structures organize data for efficiency: Arrays, Linked Lists, Stacks, Queues, Trees, Graphs, Hash Tables."

    if "operating system" in text or "os" in text:
        return "🖥️ OS manages hardware & software: Process scheduling, Memory, File Systems, Security."

    if "ai" in text:
        return "🤖 AI is about making machines smart. Subfields: Machine Learning, NLP, Robotics, Computer Vision."

    if "ml" in text:
        return "📊 ML teaches machines from data. Types: Supervised, Unsupervised, Reinforcement Learning."

    # Mechanical Engineering
    if "mechanical engineering" in text:
        return "⚙️ Mechanical Engineering studies machines, thermodynamics, fluid mechanics, robotics, CAD/CAM."

    if "thermodynamics" in text:
        return "🔥 Thermodynamics is energy science: Laws of thermodynamics, Entropy, Heat Engines, Refrigeration."

    if "fluid mechanics" in text:
        return "💧 Fluid Mechanics: Liquids & gases in motion, Bernoulli's theorem, CFD, Hydraulics."

    # Civil Engineering
    if "civil engineering" in text:
        return "🏗️ Civil Engineering: Structures, Bridges, Roads, Surveying, Geotechnical Engineering."

    if "surveying" in text:
        return "📐 Surveying measures land. Tools: GPS, Theodolite, Total Station, Drones."

    if "geotechnical" in text:
        return "🌍 Geotechnical Engineering: Soil mechanics, Foundations, Retaining walls, Tunnels."

    # Electrical
    if "electrical engineering" in text:
        return "⚡ Electrical Engineering: Circuits, Power Systems, Machines, Control Systems."

    if "power system" in text:
        return "🔋 Power Systems: Generation, Transmission, Distribution, Renewable Energy, Smart Grids."

    if "control system" in text:
        return "🎛️ Control Systems: Open-loop, Closed-loop, PID controllers, Automation, Robotics."

    # Electronics
    if "electronics" in text:
        return "📡 Electronics: Semiconductors, Circuits, Communication, Embedded Systems."

    if "signal processing" in text:
        return "🎶 Signal Processing: Filters, Fourier Transform, Speech Recognition, Image Processing."

    return "🤔 Sorry, I don’t know that yet. Try asking about Engineering or IT subjects."

# ---------------------------
# Flask Routes
# ---------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_message = request.form["message"]
        bot_reply = chatbot_response(user_message)
        chat_history.append({"user": user_message, "bot": bot_reply})
    return render_template_string(HTML_TEMPLATE, history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
