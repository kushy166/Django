from django.shortcuts import render

from django.http import HttpResponse
import getpass
import subprocess
from datetime import datetime
import pytz

def htop(request):
 
    full_name = "Kush Kumar Yadav"  
    username = getpass.getuser()
    
    
    ist = pytz.timezone('Asia/Kolkata')
    ist_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    top_output_lines = '\n'.join(top_output.splitlines()[:10])
    
  
    response = f"""
    
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <pre>{top_output_lines}</pre>
    """
    return HttpResponse(response)
