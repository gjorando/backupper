# Backupper

A simple backup utility. Configurable with a YAML file.

See `./backupper.py -h` for command usage.

## Setup

```
    sudo ./setup.py install
    # ou, pour l'installer pour l'utilisateur courant
    ./setup.py install --user
```

## Configuration reference

### Minimal backupfile.yml

```
backup_dir: /racine/du/dossier/de/sauvegarde
artifacts:
    - un/fichier
    - un/dossier
    - un/autre/dossier/
    - et/caetera
```

### `backup_dir`

* **Definition :** specifies the folder in which the backup directory will be created. If the folder doesn't exist, it will be created.
* **Type :** relative or absolute path.
* **Mandatory :** no, unless `delete_old_backups` is set to `true`.
* **Default value :** current working directory.

### `delete_old_backups`

* **Definition :** allows you to delete old backups from the backup directory specified in `backup_dir`. If `cleaning_policy` isn't set, all previous backups will be deleted.
* **Type :** boolean.
* **Mandatory :** no.
* **Default value :** `false`.

### `cleaning_policy`

* **Definition :** allows you to define a fine-tuned deletion policy. Will do nothing if `delete_old_backups` is set to `false`.
* **Type :** at least one of the following parameters.
* **Mandatory :** no (if not set, all older backups will be deleted).

Each parameter below can be set (at least one). The following schema visually presents how they work, assuming this _cleaning policy_:

```
cleaning_policy:
    most_recents: 2
    first_daily: 1
    first_weekly: 6
    first_monthly: 4
```

![Backup management schema](cleaning_policy.png "such design wow")

N.B.: please keep in mind that if you increase one of the parameters between two backups, deleted backups won't magically pop back from nowhere. We strongly advise you to be careful with these values.

#### `most_recents`

* **Definition :** number of recent backups to keep (in addition to the current one).
* **Type :** natural integer.
* **Mandatory :** no.
* **Default value :** `0`.

#### `first_daily`

* **Definition :** number of daily backups to keep (keeps the n first backups of the current day).
* **Type :** natural integer.
* **Mandatory :** no.
* **Default value :** `0`.

#### `first_weekly`

* **Definition :** number of weekly backups to keep (keeps the n first backups of the current week).
* **Type :** natural integer.
* **Mandatory :** no.
* **Default value :** `0`.

#### `first_monthly`

* **Definition :** number of monthly backups to keep (keeps the n first backups of the current month).
* **Type :** natural integer.
* **Mandatory :** no.
* **Default value :** `0`.

### `artifacts`

* **Definition :** specifies a list of files and folders to backup.
* **Type :** a list of absolute or relative paths.
* **Mandatory :** yes.
