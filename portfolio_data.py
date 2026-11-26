PROJECTS = [{'slug': 'netsim-ai',
  'name': 'NetSim AI',
  'type': 'Enterprise AI · Tetcos',
  'category': 'ai',
  'summary': 'An AI application that answers questions about NetSim protocols and cites the documentation behind '
             'each answer.',
  'problem': 'Engineering knowledge was spread across different technical sources and needed to be retrieved in '
             'context for useful AI-assisted answers.',
  'contribution': 'Built retrieval with LangChain, all-MiniLM-L6-v2 and FAISS. '
                  'Implemented deep research, linked protocol concepts, and '
                  'LLM evaluation. Configured AWS hosting, NGINX, TLS, WebSockets, SSO and per-user chat '
                  'history.',
  'decision': 'Treat generation as one stage in a controlled pipeline, with retrieved evidence and validation '
              'surrounding the model call.',
  'technologies': ['Python', 'LangChain', 'Sentence Transformers', 'FAISS', 'LLMOps', 'NGINX', 'AWS'],
  'architecture': ['Docs / artifacts / code',
                   'Retrieval',
                   'Context assembly',
                   'LLM',
                   'Validation + guardrails',
                   'Answer'],
  'source_note': 'Professional work; implementation is not public.'},
 {'slug': 'netsim-mcp',
  'name': 'NetSim MCP',
  'type': 'AI-driven network simulation | Local testing release',
  'category': 'ai',
  'summary': 'A Python Model Context Protocol server that lets an AI assistant configure, run and compare NetSim '
             'experiments from a natural-language request.',
  'problem': 'An engineer comparing scenarios needs to know which settings changed and which measured results '
             'belong to each run.',
  'contribution': 'Implemented Pydantic tool contracts, configuration validation, immutable scenario revisions '
                  'and SQLite experiment tracking. Added asynchronous execution, cancellation, process cleanup '
                  'and paginated access to verified metrics and traces.',
  'decision': 'Store each configuration change as a new revision so results can be traced to the settings used '
              'for a run.',
  'technologies': ['Python', 'MCP', 'Pydantic', 'SQLite', 'NetSim'],
  'architecture': ['Discover scenarios',
                   'Validate parameters',
                   'Version scenario',
                   'Run simulation',
                   'Compare results'],
  'source_note': 'Professional project at Tetcos LLP.'},
 {'slug': 'netsim-astra',
  'name': 'NetSim Astra Identity',
  'type': 'Backend & authentication · Tetcos',
  'category': 'backend',
  'summary': 'Secure authentication for backend microservices using OAuth 2.0, OpenID Connect, Keycloak SSO, and '
             'multi-realm policies.',
  'problem': 'Enterprise deployments needed one authentication path across services while preserving '
             'realm-specific access policies.',
  'contribution': 'Engineered backend microservice authentication, Keycloak-based SSO, custom Java realm-policy '
                  'JARs, and multi-realm authentication.',
  'decision': 'Keep identity policy in the authentication layer and let services validate standard OAuth/OIDC '
              'tokens instead of duplicating login logic.',
  'technologies': ['Microservices', 'OAuth 2.0', 'OpenID Connect', 'Keycloak', 'SSO', 'Java'],
  'architecture': ['User / client', 'Keycloak realms', 'Custom realm policy', 'OAuth / OIDC', 'Backend services'],
  'source_note': 'Professional work; implementation is not public.'},
 {'slug': 'workmind',
  'name': 'Personal Assistant - AI Knowledge Assistant',
  'type': 'Open-source RAG application',
  'category': 'ai',
  'summary': 'A RAG assistant for developers that searches technical documentation and answers questions using '
             'local or hosted language models.',
  'problem': 'Project knowledge in local folders is difficult to query across files and easy to lose between '
             'development sessions.',
  'contribution': 'Built semantic chunking and ChromaDB retrieval, integrated authenticated LLM APIs, and added '
                  'timeouts, retries, validation and vector-write fallbacks.',
  'decision': 'The chunker measures cosine distance between neighboring embedded text units, applies a '
              'percentile breakpoint, preserves bounded overlap, and uses stable content-derived IDs so updated '
              'files can remove stale chunks.',
  'technologies': ['Python',
                   'Streamlit',
                   'OpenRouter',
                   'ChromaDB',
                   'SQLite',
                   'Embeddings',
                   'Semantic search',
                   'Ollama',
                   'Transformers'],
  'architecture': ['Files',
                   'Semantic chunking',
                   'Embeddings',
                   'ChromaDB + SQLite',
                   'Top-k retrieval',
                   'Contextual answer'],
  'repository': 'https://github.com/D-Suraj/Personal-assistant-LLM',
  'source_note': 'Public repository; source and commit history reviewed.'},
 {'slug': 'netsim-cyber',
  'name': 'NetSim Cyber',
  'type': 'Systems & networking · Tetcos',
  'category': 'systems',
  'summary': 'Cyber-simulation features spanning packet inspection, network attacks, protocol behavior, and '
             'Python orchestration of a lower-level simulation core.',
  'problem': 'Simulation behavior had to be coordinated across language boundaries and debugged at the protocol '
             'and packet level.',
  'contribution': 'Implemented Wireshark/PCAP packet analysis, network-attack simulation, and Python low-level '
                  'API integration for cyber-core orchestration.',
  'decision': 'Use packet captures and protocol traces as ground truth when behavior across the Python and '
              'native-code boundary does not match expectations.',
  'technologies': ['Python', 'C / C++', 'Wireshark', 'PCAP', 'Network protocols', 'Cyber simulation'],
  'architecture': ['Scenario',
                   'Python orchestration',
                   'Cyber core',
                   'Protocol engine',
                   'PCAP capture',
                   'Wireshark analysis'],
  'source_note': 'Professional work; implementation is not public.'},
 {'slug': 'doodle-recognition',
  'name': 'Doodle Recognition',
  'type': 'Academic ML internship',
  'category': 'ai',
  'summary': 'A CNN-based image-classification system for recognizing hand-drawn doodles through preprocessing, '
             'training, evaluation, and inference.',
  'problem': 'Classify hand-drawn doodles in an interactive, real-time workflow.',
  'contribution': 'Developed and evaluated the end-to-end deep-learning pipeline in Python during a '
                  'machine-learning internship.',
  'decision': 'Preprocess drawings before inference using the same input representation used to train the CNN.',
  'technologies': ['Python', 'TensorFlow', 'Keras', 'NumPy', 'Matplotlib', 'CNN'],
  'architecture': ['Drawing', 'Preprocessing', 'CNN', 'Evaluation', 'Prediction'],
  'source_note': 'Resume and LinkedIn project; no public repository was verified.'}]

EXPERIENCE = [{'period': 'Oct 2024 — Present',
  'role': 'AI Application Engineer',
  'organization': 'Tetcos LLP',
  'summary': 'Backend, AI, authentication, and protocol-engineering work across NetSim products.',
  'highlights': ['Built citation-backed retrieval for internal protocol documentation.',
                 'Developed NetSim MCP for validated simulation configuration, asynchronous execution and '
                 'comparison of measured results.',
                 'LLMOps pipelines for evaluation, model validation, structured outputs, governance, and '
                 'guardrails.',
                 'OAuth 2.0 and Keycloak SSO for multi-realm enterprise authentication.',
                 'Wireshark/PCAP analysis, attack simulation, and Python integration with a low-level cyber '
                 'core.',
                 'Implemented 5G beamforming analysis with LAPACK, DTDMA time synchronization for military '
                 'radio, and satellite visualization with Cesium.']},
 {'period': 'Apr 2024 — Sep 2024',
  'role': 'Java Full Stack Trainee',
  'organization': 'Java Learning Center',
  'summary': 'Training in Core Java, object-oriented programming, SQL, REST APIs, HTML, CSS, and backend '
             'application development.',
  'highlights': []},
 {'period': 'Oct 2023 — Mar 2024',
  'role': 'Machine Learning Intern',
  'organization': 'Srinivasa Ramanujan Institute of Technology',
  'summary': 'Built and evaluated a CNN-based doodle-recognition system for real-time image classification in '
             'Python.',
  'highlights': []}]

SKILL_GROUPS = [('Languages', ['Python', 'C', 'C++', 'Java', 'SQL']),
 ('Backend & APIs', ['Flask', 'REST APIs', 'Microservices', 'SQLite', 'Streamlit']),
 ('AI / GenAI',
  ['LLM applications',
   'RAG',
   'LangChain',
   'Embeddings',
   'Semantic search',
   'FAISS',
   'ChromaDB',
   'Sentence Transformers',
   'Hugging Face Transformers',
   'Ollama',
   'OpenRouter',
   'Agentic AI',
   'LlamaIndex',
   'MCP']),
 ('AI reliability',
  ['LLM evaluation',
   'Model validation',
   'Structured outputs',
   'Prompt validation',
   'Guardrails',
   'AI governance',
   'Hallucination mitigation']),
 ('Security & identity', ['OAuth 2.0', 'OpenID Connect', 'Keycloak', 'SSO', 'Authentication']),
 ('Cloud & delivery', ['AWS', 'Docker', 'Git', 'GitHub', 'NGINX', 'WebSockets']),
 ('Systems & networking',
  ['Network protocols', 'Wireshark', 'PCAP analysis', 'Cyber simulation', 'Cesium', 'LAPACK', 'DTDMA'])]

