from pathlib import Path
import os

PROJECT_DIRECTORY = Path().resolve()
def move_user_profiles():
  source_file = PROJECT_DIRECTORY.joinpath('.config/user_profiles.yml')
  target_file = PROJECT_DIRECTORY.joinpath('profiles.yml')
  Path(source_file).rename(target_file)

def initialize_git_repo(initialize_repo):
  if initialize_repo == "Yes":
    os.system("git init")

def post_init_messages(adapter, ci_tool):

  if ci_tool == "GitHub":
    docs = "https://docs.github.com/en/actions/reference/environment-variables"
  elif ci_tool == "GitLab":
    docs = "https://docs.gitlab.com/ee/ci/variables/"

  print(
    "\nProject initialized successfully!\n"
  )

  if ci_tool == "None":
    message = (
      f"A base profile.yml file has been created in folder your project folder\n"
      f"Copy it to ~/.dbt and edit its contents\n"
      f"For more information see https://docs.getdbt.com/dbt-cli/configure-your-profile \n\n"
    )
  else:
    message = (
      f"A base profile.yml file has been created in your project folder\n"
      f"Copy it to ~/.dbt and edit its contents for local development\n"
      f"For more information see https://docs.getdbt.com/dbt-cli/configure-your-profile \n\n"

      f"The CI job will leverage the profile.yml file in the .config folder.\n"
      f"You will need to set the corresponding environment variables in the {ci_tool}\n"
      f"project to run dbt as part of your CI pipeline.\n"
      f"Learn more about {ci_tool} CI/CD variables here: {docs}"
    )
  print(message)

def main():
    adapter = "{{ cookiecutter.adapter }}"
    ci_tool = "{{ cookiecutter.ci_tool }}"
    initialize_repo = "{{ cookiecutter.run_git_init }}"

    move_user_profiles()
    initialize_git_repo(initialize_repo)
    post_init_messages(adapter, ci_tool)

if __name__ == "__main__":
    main()