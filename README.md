
Django Track Bugz
===========

Will be an integrated web-based project management system featuring bug/issue tracking, scheduling and estimation reporting with REST API integration. 

The feature tracker allows users to manage, filter, sort and navigate a tree-structure of tasks, that contain information, tags, comments and attached files related to a particular issue.  Users may integrate their email accounts into the system to send/receive email and create issues regarding the same.

Features
--------

Project management

* Manage multiple projects, with milestones within each
* Tree-structure outline of tasks, issues, bugs, features or customer inquiries
* Full history maintained per task, including edits, user assignments and updates
* Local search to filter list of tasks based upon keywords in title, description, etc.

Time management

* Manually entered estimates per task, along with manually set start/end times
* Timesheet and user history based upon work done on tasks, per day

Overall management

* Display line, bar, column or pie charts for any filtered view of the task tree-structure
* View charts based upon present data, or past historical records of tasks
* Tabular reports of tasks, users, projects and their parameters or records
* Drill down to view hierarchical information within a section of a chart



Installation
------------

This application requires Django version 1.4; all versions above should be fine.

Just install the package using `pip install django-solo` and add ``solo`` to
your ``INSTALLED_APPS`` setting.

This is how you run tests:

    ./manage.py test solo --settings=solo.tests.settings


Admin
-----


* The django admin site will be used as a starting point for the UX


Settings
--------

### TODO

Description


    SOME_SETTING = 'Something''
