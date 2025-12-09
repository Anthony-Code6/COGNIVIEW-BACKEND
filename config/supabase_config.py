import os
from supabase import create_client

SUPABASE_URL = "https://zyiqyocffbiamavoscdf.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp5aXF5b2NmZmJpYW1hdm9zY2RmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE3NTAzMzcsImV4cCI6MjA2NzMyNjMzN30.eWyrd07sUtsJmP32Pug4JeUz35Vg4XENF9qqNgZnU94"

BUCKET = 'images'

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
