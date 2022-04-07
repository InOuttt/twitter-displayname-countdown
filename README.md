## COUNTDOWN IN TWITTER DISPLAYNAME
- python 3.8
- docker 20.10 (optional)
- docker-compose 1.29 (optional)


## How to use
- clone this repo.
- put your twitter API token credentials in **.env** file.
- put your desired end date of the counter on **end_date** in **.env** file.
- in **.env** file **label** is the text after the countdown 
- in **.env** file **prefix** is the text before the countdown 

### Using docker
- run the program with `docker-compose up -d`

### Without Docker
- install python package dependencies using `pip install -r requirements.txt`.
- run `python3 countdown.py`
