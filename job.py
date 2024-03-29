"""import subprocess
import os
import time

def download_splunk():
    print("Download the Splunk Enterprise tar file")
    subprocess.run(["sudo", "rm", "-rf", "/opt/splunk*"])
    os.chdir("/opt")
    subprocess.run(["sudo", "wget", "-O", "splunk-9.0.4.1-419ad9369127-Linux-x86_64.tgz", "https://download.splunk.com/products/splunk/releases/9.0.4.1/linux/splunk-9.0.4.1-419ad9369127-Linux-x86_64.tgz"])
    print("Extract the tar file to /opt")
    subprocess.run(["sudo", "tar", "-zxvf", "splunk-9.0.4.1-419ad9369127-Linux-x86_64.tgz", "-C", "/opt"])

def start_splunk():
    print("Start Splunk Enterprise and set up the admin user and password")
    os.chdir("/opt/splunk/bin/")
    subprocess.run(["sudo", "./splunk", "start", "--accept-license", "--answer-yes", "--no-prompt", "--seed-passwd", "abcd1234"])
    print("Enable Splunk at the startup")
    subprocess.run(["sudo", "./splunk", "enable", "boot-start"])
    print("Please go on the browser, access splunk on port 8000, username: admin, password: abcd1234")

def main():
    download_splunk()
    start_splunk()
    time.sleep(4)

if __name__ == "__main__":
    main()"""
