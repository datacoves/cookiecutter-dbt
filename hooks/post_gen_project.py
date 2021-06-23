
def gitlab_ci_enabled(adapter):
    if adapter == "snowflake":
        print(
            "Set the following environment variables in your GitLab project to run dbt as part of your CI pipeline:\n"
            " - DBT_ACCOUNT: Your snowflake account.\n"
            " - DBT_USER: Your snowflake username\n"
            " - DBT_PASSWORD: Your snowflake password\n"
            " - TEST_DATABASE: The Database name you use for running CI jobs\n\n"
            "Learn more about GitLab CI/CD variables here: https://docs.gitlab.com/ee/ci/variables/"
        )


def main():
    print("\nProject initialized successfully!\n")
    
    adapter = "{{ cookiecutter.adapter }}"

    if "{{ cookiecutter.ci_tool }}" == "GitLab":
        gitlab_ci_enabled(adapter)


if __name__ == "__main__":
    main()