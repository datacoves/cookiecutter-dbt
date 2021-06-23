

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

DEBUG_VALUE = "debug"

def gitlab_ci_enabled(adapter):
    if adapter == "snowflake":
        print(
            "To run your transformations, set the following environment variables in your GitLab project:\n"
            " - DBT_ACCOUNT: Your snowflake account.\n"
            " - DBT_USER: Your snowflake username\n"
            " - DBT_PASSWORD: Your snowflake password\n"
            " - TEST_DATABASE: The Database name you use for running CI jobs\n\n"
            "Learn more here: https://docs.gitlab.com/ee/ci/variables/"
        )


def main():
    print(SUCCESS + "Project initialized successfully!" + TERMINATOR)
    
    adapter = "{{ cookiecutter.adapter }}"

    if "{{ cookiecutter.ci_tool }}" == "GitLab":
        gitlab_ci_enabled(adapter)


if __name__ == "__main__":
    main()