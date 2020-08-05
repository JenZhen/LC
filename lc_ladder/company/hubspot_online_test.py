#! /usr/bin/python
'''
Author: Zhen Zhen, zzhen324@gmail.com
Date: 08/01/2020

This code is using python2.
It uses 'requests' package to handle GET POST requests.
'''

from collections import defaultdict
from datetime import datetime, timedelta
import requests
import json

class Solution:
    def __init__(self):
        self.GET_URL = 'https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=90375bf64143ab38db1e2dbd44f0'
        self.POST_URL = 'https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=90375bf64143ab38db1e2dbd44f0'

    def get_data(self):
        data = requests.get(self.GET_URL).json()
        return data

    def post_data(self, payload):
        resp = requests.post(self.POST_URL, json = payload)
        if resp.status_code != 200:
            print(resp.status_code,resp.content)

    def send_invitation(self):
        data = self.get_data()
        payload = {"countries":[]}

        # key: country_name, val: [partners]
        countries_mp = defaultdict(list)
        for p in data['partners']:
            country = p['country']
            countries_mp[country].append(p)

        for country, partners in countries_mp.items():
            # key: date, val: {partner_email}
            dates_mp = defaultdict(set)
            for p in partners:
                avail_dates = []
                for date in p['availableDates']:
                    avail_dates.append(datetime.strptime(date, '%Y-%m-%d'))

                # sort a partners available dates from earliest to the latest
                avail_dates.sort()
                for i in range(len(avail_dates) - 1):
                    day1 = avail_dates[i]
                    day2 = avail_dates[i + 1]
                    if day2 - day1 == timedelta(days=1):
                        dates_mp[day1].add(p['email'])

            max_cnt = 0
            max_date = None
            for date, partner_emails in dates_mp.items():
                if len(partner_emails) > max_cnt:
                    max_cnt = len(partner_emails)
                    max_date = date
                elif len(partner_emails) == max_cnt:
                    max_date = date if date < max_date else max_date

            payload['countries'].append(
                {
                    "attendeeCount": len(dates_mp[max_date]),
                    "attendees": list(dates_mp[max_date]),
                    "name": country,
                    # convert datetime to iso format with y-m-d only
                    "startDate": max_date.isoformat()[:10]
                }
            )
        self.post_data(payload)


if __name__ == "__main__":
    solution = Solution()
    solution.send_invitation()
