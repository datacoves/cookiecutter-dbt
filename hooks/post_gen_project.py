
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
      f"A base profile.yml file has been created in folder .config\n"
      f"Copy it to ~/.dbt and edit its contents\n"
      f"For more information see https://docs.getdbt.com/dbt-cli/configure-your-profile \n\n"
    )
  else:
    message = (
      f"A base profile.yml file has been created in the .config folder\n"
      f"You will need to copy it to ~/.dbt and then edit file for you local development\n"
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

    post_init_messages(adapter, ci_tool)

if __name__ == "__main__":
    main()