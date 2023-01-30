# XX-12345 Test Project Data Models

# Installing
Run this from your command line of choice. NOTE- this assumes you have python installed on your machine. 

```
pipenv install
pipenv run dbt deps
```

That's it.  


# Configuring
There is a [sample config template](.config/sample.profiles.yml) in the `.config` folder of the repository.  

1. Copy the file and name it `.config/profiles.yml`. 
2. Update the following variables with _your_ credentials:
- `user`: Your Keystone Microsoft SSO user name. Probably your email. 
- `account`: The host name without any protocol prefix or `snowflakecomputing.com` suffix. 
- `schema`: replace `YOURINITIALS` with your initials

You can keep the rest of the configuration file the same as these are standard values.  

NOTE: We strongly prefer a project specific configuration file instead of a global config file with all credentials.  The `activate` script is configured to set the environment variable for you.  Otherwise, you will need to copy the `profiles.yml` to `~/.dbt/profiles.yml` and integrate with other connection settings. 

# Running
This assumes you have followed the instructions in [Installing](#installing) and [Configuring](#configuring).

Now that you have installed and configured `dbt` you can run it using the [`activate`](activate) convenience script provided in this repository.  See the [DEVELOPING](DEVELOPING.md) instructions for more detail. 

To create the models run this command:
```
$ ./activate dbt run 
```

If you are using a global environment config, you can simply `dbt run` without running `activate`. 

Pay attention to the log output as it will identify any issues that occur long the way.  A more detailed log is stored at `logs/dbt.log`.

<hr>

#### IMPORTANT NOTE
If you are running on a Windows machine, you need to use a `bash`-like command line for the `activate` script to work properly.  If you do not have one installed (Git Bash, WSL, etc), you can take advantage of `pipenv`'s built in `dotenv` integration and use the [sample.env](sample.env) file to set the variable.  Copy it to `.env` and it'll load automatically. 


```
pipenv run dbt run 
```

If you get tired of that, step into the environment with `pipenv shell`.  This loads the env variable at the start.

```
pipenv shell
dbt run 
```

Use `exit` to get out of the virtual environment. 

<hr>

## Loading external sources
The external loading process uses `dbt-external-tables` with a slight modification (forked) to handle our specific DMS use case. Note: you need the `ops_admin` role to be able to execute these commands.  There is no DEV mode for this operation, so be careful with what you're running. 

To run all external loads:
```
./activate dbt run-operation stage_external_sources 
```

To run all external loads and force a reload:
```
./activate dbt run-operation stage_external_sources --vars "ext_full_refresh: true"
```

Be careful with a full reload since Snowpipe will only load the most recent seven days of data by default. 

To run a specific external load and force a refresh:
```
./activate dbt run-operation stage_external_sources --vars "ext_full_refresh: true" --args "select: the_model_name"
```

See https://github.com/dbt-labs/dbt-external-tables for more details.



### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
