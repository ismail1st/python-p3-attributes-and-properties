#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None):
        if name is not None:
            self.name = name
        if job is not None:
            self.job = job

    # --------------------
    # NAME PROPERTY
    # --------------------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) is not str or len(value) < 1 or len(value) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value.title()

    # --------------------
    # JOB PROPERTY
    # --------------------
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job = value
