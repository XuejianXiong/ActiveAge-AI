# Setup
## Environment Setup Guide
Before using this repo, make sure you’ve completed the environment setup, which installs the core tools you’ll need for this module, such as:

- Git  
- UV
- Visual Studio Code

## Necessary Packages
We use **uv** to create the Active-AI environment, activate it, and install the required packages listed in the module’s `pyproject.toml`.  
This setup only needs to be done **once per module**, after that, you just activate the environment whenever you want to work in this repo.  

Open a terminal (macOS/Linux) or Git Bash (Windows) in this repo, and run the following commands in order:

1. Create a virtual environment called `activeAge-ai-env`:
    ```
    uv venv activeAge-ai-env --python 3.11
    ```

2. Activate the environment:
    - for macOS/Linux:
        ```
        source activeAge-ai-env/bin/activate
        ```
        
    - for windows (git bash):    
        ```
        source activeAge-ai-env/Scripts/activate
        ```

3. Install all required packages from the [pyproject.toml](./pyproject.toml)
    ```
    uv sync --active
    ```

4. When you’re finished, you can deactivate it with:  
```
deactivate
```

> **👉 Remember**   
> Only one environment can be active at a time. If you switch to a different repo, first deactivate this one (or just close the terminal) and then activate the new repo’s environment.
