<style>
r { color: Red }
o { color: Orange }
g { color: #b51d4d }
b { color: LightBlue }
</style>

## Commands

### Docker

- Getting inside container to work on database: <g>**docker exec -it my-postgres bash**</g> and after getting into container: <g>**psql**

- Running docker container with database:  **docker run -d -p 5432:5432 --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword postgres**

### Linux

- Before every installation of anything: <g>**sudo apt update**</g> and then <g>**sudo apt upgrade**</g>
- Getting id of running bot: **pidof python newBot.py**
- Killing process: **sudo kill -9 process_id**
- Showing all the processes: **ps aux**
- Starting process without stopping: **nohup process_name &**
- Markdown reader: **glow document_name**
- Creating virtual env: **python3 -m venv venv**
- Activating virtual env: **source venv/bin/activate**
- Formatting python file: **black file_name**
- Using pip: **pip install module**
