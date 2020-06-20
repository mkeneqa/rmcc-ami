## RMCC Audio Message Index

This is an unofficial Audio Message Index for messages and studies from the [RMCC Church](https://messages.calvarychapel.ca/). I needed an easy way to find messages by date and topic and this is what I've come up with. 

This is a WIP solution. Use at your own risk.

The [RMCC Church](https://messages.calvarychapel.ca/) has some great messages publically available on their website but navigating the message archive can seem daunting at times when looking for a specific set of messages to follow.

This python script indexes and downloads the meta-data for all the available audio messages on the [RMCC Audio Archive](https://messages.calvarychapel.ca/) and saves them in the `db.json` file which is generated and utilized by **[TinyDB]([https://tinydb.readthedocs.io/en/latest/index.html#])**

## To Do

 - [x] ~~_Index audio archive_~~
 - [ ] Ability to search data
 - [ ] Download audio files
 - [ ] Option to rename audio files

## Get Started
1. `git clone https://github.com/mkeneqa/rmcc-ami.git`
2. Create python virtual environment:
    - **UNIX**: `python3 -m venv env`
    - **WINDOWS**: `py -m venv env`
3. Activate Environment:
    - **UNIX**: `source env/bin/activate` 
    - **WINDOWS**: `.\env\Scripts\activate`
4. **Optional:** `python -m pip install --upgrade pip`
5. `python -m pip install -r requirements.txt`
6. **Optional:** To deactivate virtual environment; within the project directory type `deactivate`

## Commands
##### Fetch and Save Audio Archive Meta-data to `json.db` file
```python
python download.py crawl_archive
```
##### More  . . . 
```python
# python .... more to come
```

## Data Structure 

The database is saved in the `db.json` file which is generated using **[TinyDB]([https://tinydb.readthedocs.io/en/latest/index.html#])** and contains two _tables:_ **episode** and **series**. The two tables are linked via the `series_id` . 

A **Series** can contain multiple **Episodes** but each **Episode** belongs to only one **Series**.

```json
{
  "episode": {
    "1": {
      "date": "2016-10-16",
      "link": "https://s3.amazonaws.com/rmcc/Messages/Genesis_ch1-v1-v1_2016-OCT-16.mp3",
      "series_id": 1,
      "title": "Genesis 1:1"
    }
  },
  "series": {
    "1": {
      "category": "Old Testament",
      "label": "Genesis",
      "series_id": 1,
      "title": "Current Study"
    }
  }
}
```

## Credits

 - Beautiful Soup
 - TinyDB
 - Fire
 - Requests
 - Python3
 - RMCC
