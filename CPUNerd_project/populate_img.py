import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CPUNerd_project.settings')

import django
django.setup()

from CPUNerd.models import CpuModel

def populate():



if __name__=='__main__':
    print('Starting CPUNerd population script...')
    populate()