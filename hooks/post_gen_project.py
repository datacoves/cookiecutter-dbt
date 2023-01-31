from pathlib import Path
import os
import shutil

PROJECT_DIRECTORY = Path().resolve()



def initialize_git_repo(initialize_repo):
    if initialize_repo == "Yes":
        os.system("git init")

def init_env(run_env_creation, environment_manager):
    if run_env_creation == 'No':
        pass 

    if environment_manager == 'pipenv':
        try:
            os.system('pipenv install')
        except:
            print('Env creation failed. You must run the following commands to finish the installation:')
            print('pip install pipenv')
            print('pipenv install')
    elif environment_manager == 'pip': 
        os.system('pip install dbt-snowflake')

    

def post_init_messages(adapter, ci_tool):

    print(
        "\nProject initialized successfully!\n"
    )
    docs = 'https://circleci.com/docs/env-vars/'
    message = (
        f"A base profiles.yml file has been created in your project folder\n"
        f"Copy it to ~/.dbt and edit its contents for local development\n"
        f"For more information see https://docs.getdbt.com/dbt-cli/configure-your-profile \n\n"

        f"The CI job will leverage the profiles.yml file in the .circleci/dbt_config folder.\n"
        f"You will need to set the corresponding environment variables in {ci_tool}\n"
        f"project to run dbt as part of your CI pipeline.\n"
        f"Learn more about {ci_tool} CI/CD variables here: {docs}"
        )
    print(message)


def cleanup():
    remove_paths = [
    ]

    for path in remove_paths:
        path = path.strip()
        if path and os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path, ignore_errors=True)
            else:
                os.unlink(path)


def main():
    ci_tool = "CircleCI"
    initialize_repo = "{{ cookiecutter.run_git_init }}"
    run_env_creation = "{{ cookiecutter.run_env_creation }}"
    environment_manager = "{{ cookiecutter.environment_manager }}"

    initialize_git_repo(initialize_repo)
    init_env(run_env_creation, environment_manager)
    post_init_messages('snowflake', ci_tool)
    cleanup()


if __name__ == "__main__":
    main()
