from setuptools import setup, find_packages

# Define a constant for the hyphen dot if necessary, or adjust as needed.
HYFEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> list[str]:
    requirements = []
    with open(file_path) as file_object:
        # Read the lines from the requirements file
        requirements = file_object.readlines()
        # Remove the newline character from each line
        requirements = [req.strip() for req in requirements]
        
        # Remove any instance of '-e .' (editable install)
        if HYFEN_E_DOT in requirements:
            requirements.remove(HYFEN_E_DOT)

    return requirements


# Setup function to define the package
setup(
    name='Xray',
    version='0.0.1',
    author='Fadoua Mili',
    author_email='Fadwa.mili14@gmail.com',
    install_requires=get_requirements('requirements_dev.txt'),  # Populate install_requires with the requirements
    packages=find_packages(),  # Find packages in the current directory
)

