"""
    Some functions used by backupper.cli.main during the initialisation process.
"""

import os

def getHelp(command_name, configuration_file):
    """
        Returns the cli help string.

        :param command_name: Name of the cli call (usually sys.argv[0]).
        :type command_name: str
        :param configuration_file: Name of the default configuration file.
        :type configuration_file: str
        :return: The formatted help string ready to be displayed.
        :rtype: str

        .. seealso:: backupper.cli.main
    """

    help_string = """Usage: {} [OPTIONS...]

  -h, --help\t\tDisplays the current help and exits.
  -f, --config-file\tSpecifies an alternative YAML config file (default: {}).
""".format(command_name, configuration_file)

    return help_string

def validateConfiguration(configuration):
    """
        Validates a configuration (usually loaded from a yml file).

        :param configuration: A dictionary storing the configuration attributes (usually loaded from yaml.load).
        :type configuration: dict

        :raises Exception: If an error is encountered during the validation, an Exception is raised, describing the issue.
        .. seealso:: backupper.cli.main
    """

    # No empty configuration file
    if not isinstance(configuration, dict):
        raise Exception("Empty or malformed configuration.")

    # artifacts
    if not "artifacts" in configuration:
        raise Exception("Missing \"artifacts\" node.")
    elif not isinstance(configuration["artifacts"], list):
        raise Exception("Please provide a list of paths in the \"artifacts\" node.")
    else:
        for element in configuration["artifacts"]:
            if not isinstance(element, str):
                raise Exception("In \"artifacts\": {} isn't a string.".format(element))

    # delete_old_backups
    if not "delete_old_backups" in configuration:
        configuration["delete_old_backups"] = False
    elif configuration["delete_old_backups"] and not "backup_dir" in configuration:
        raise Exception("\"delete_old_backups\" is set to true, but there is no \"backup_dir\".")
    elif not isinstance(configuration["delete_old_backups"], bool):
        raise Exception("\"delete_old_backups\" should be a boolean.")

    # cleaning_policy
    valid_cleaning_policies = ["most_recents", "first_daily", "first_weekly", "first_monthly"]
    if not "cleaning_policy" in configuration or configuration["cleaning_policy"] is None:
        configuration["cleaning_policy"] = {}
    elif not isinstance(configuration["cleaning_policy"], dict):
        raise Exception("\"cleaning_policy\" should be a list of nodes.")
    else:
        for key in configuration["cleaning_policy"]:
            if not key in valid_cleaning_policies:
                raise Exception("\"{}\" is an incorrect \"cleaning_policy\" option.".format(key))
            elif not (isinstance(configuration["cleaning_policy"][key], int) and configuration["cleaning_policy"][key] >= 0) :
                raise Exception("\"{}\" should be a positive integer.".format(key))
    for policy in valid_cleaning_policies:
        if not policy in configuration["cleaning_policy"]:
            configuration["cleaning_policy"][policy] = 0

    # backup_dir
    if not "backup_dir" in configuration:
        configuration["backup_dir"] = os.getcwd()
    if not isinstance(configuration["backup_dir"], str):
        raise Exception("\"backup_dir\" should be a string.")