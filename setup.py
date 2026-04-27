from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Read requirements from requirements.txt if it exists
def read_requirements(filename="requirements.txt"):
    req_path = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(req_path):
        with open(req_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return []


setup(
    name="unsloth",
    version="2024.12.0",
    author="Unsloth AI",
    author_email="danielhanchen@gmail.com",
    description="Fine-tune LLMs 2-5x faster with 80% less memory",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/unslothai/unsloth",
    project_urls={
        "Bug Tracker": "https://github.com/unslothai/unsloth/issues",
        "Documentation": "https://docs.unsloth.ai",
        "Source Code": "https://github.com/unslothai/unsloth",
    },
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    python_requires=">=3.9",
    install_requires=[
        "torch>=2.1.0",
        "transformers>=4.38.0",
        "datasets>=2.16.0",
        "sentencepiece>=0.1.99",
        "tqdm>=4.64.0",
        "psutil",
        "wheel>=0.42.0",
        "packaging>=23.1",
        "tyro>=0.5.11",
        "peft>=0.7.1",
        "accelerate>=0.26.0",
        "trl>=0.7.9",
        "xformers",
        "bitsandbytes",
        "triton",
        "einops",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov",
            "black",
            "isort",
            "flake8",
            # Added mypy for type checking during local development
            "mypy",
        ],
        "colab": [
            "ipywidgets",
            "ipython",
        ],
        # Convenience group to install all optional deps at once
        "all": [
            "ipywidgets",
            "ipython",
            "mypy",
            "pytest>=7.0",
            "pytest-cov",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        # Added 3.12 classifier since it works fine in my testing
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "llm",
        "fine-tuning",
        "lora",
        "qlora",
        "transformers",
        "huggingface",
        # added a couple extra keywords to help with discoverability when I publish my fork
        "llama",
        "mistral",
        "efficient-training",
    ],
)
