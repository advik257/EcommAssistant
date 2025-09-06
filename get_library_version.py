import importlib.metadata
packages = [
    "langchain",
    "langchain_core", 
    "python-dotenv",
    "streamlit",
    "ipykernel",
    "beautifulsoup4"
    "fastapi",
    "uvicorn",
    "jinja2",
    "langchain-astradb",
    "langchain-google-genai",
    "langchain-groq",
    "lxml",
    "selenium",
    "python-multipart",
    "undetected-chromedriver",
    "uvicorn",
    "structlog",
    "html5lib"
    ]

for package in packages:
    try:
        version = importlib.metadata.version(package)
        print(f"{package}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{package} is not installed.")