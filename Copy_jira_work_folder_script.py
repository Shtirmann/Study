import paramiko
import os
import schedule
import time

def copy_files():
    # Установите соединение с удаленным сервером
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='remote_server_ip', username='username', password='password')

    # Получите файлы из папки
    sftp = ssh.open_sftp()
    file_list = sftp.listdir('/var/atlassian/application-data/jira')

    # Скопируйте файлы в ту же папку на удаленном сервере
    for filename in file_list:
        sftp.get('/var/atlassian/application-data/jira/' + filename, '/var/atlassian/application-data/jira/' + filename)

    # Закройте соединение с удаленным сервером
    sftp.close()
    ssh.close()

schedule.every().day.at("07:00").do(copy_files)

while True:
    schedule.run_pending()
    time.sleep(1)