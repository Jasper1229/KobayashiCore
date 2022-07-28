from pstats import Stats
import requests
import json

from config import *

API_URL = 'https://osu.ppy.sh/api/v2'
TOKEN_URL = 'https://osu.ppy.sh/oauth/token'

def get_token():
    data = {
        'client_id': 16870,
        'client_secret': OSU_SECRET,
        'grant_type': 'client_credentials',
        'scope': 'public'
    }
    response = requests.post(TOKEN_URL, data = data)
    
    return response.json().get('access_token')


token = get_token()

def get_user(username):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(API_URL + '/users/' + username + '/', headers=headers)
    return response.json()

def get_stats(user):
    stats = user['statistics']
    return stats

def get_level_stat(stats):
    levels = stats['level']
    level = levels['current']
    return level

def get_level_progress_stat(stats):
    levels = stats['level']
    progress = levels['progress']
    return progress

kobstats = get_stats(get_user('kobayashi'))



print(get_level_stat(kobstats))
print(get_level_progress_stat(kobstats))