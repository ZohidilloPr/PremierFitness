import os

os.system("sudo systemctl daemon-reload")
os.system("sudo systemctl restart f.service f.socket")
os.system("sudo nginx -t ")
os.system("sudo systemctl restart nginx")
print("Finished Restarting ...")