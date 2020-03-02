""" 
contains the functions for accessing/manipulating database and
check the rule against the condition and scheduled time
If rule matched the conditiona and time action service is triggred  
and rule is deactivated. 
"""

import sqlite3
from sqlite3 import Error
import datetime
from action_executor_service import send_mail
from globals import MyGlobals



def sql_connect():
    '''
    method to create a sql connection object 
    '''
    try:
        con = sqlite3.connect('db.sqlite3')
        con.row_factory = sqlite3.Row
        return con

    except Error:
        print(Error)

def sql_select(query, value):
    '''
    method to return the result of query executed.
    '''

    con = sql_connect()
    cursorObj = con.cursor()
    cursorObj.execute(query, value)

    rows = cursorObj.fetchall()
    con.close()

    return rows

def sql_update(query, value):
    '''
    methcd to updated the data in database.
    '''
    con = sql_connect()
    cursorObj = con.cursor()
    cursorObj.execute(query, value)
    con.commit()
    con.close()


def active_rules(rule_id):
    '''
    function to get the data of active rule and pass for checking the schedule time and condition
    '''
    # rule data fetch query
    fetch_rules_data = f'select * from rule_based_engine_camp_rules where id=?'
    rules_data = [dict(rule) for rule in sql_select(fetch_rules_data,(rule_id,))]
    schedule_time = rules_data[0]['schedule_time']
    condition = rules_data[0]['condition']
    campaign = rules_data[0]['campaign']
    
    # rule status upate query
    update_rules_status = f'update rule_based_engine_camp_rules set status=? where campaign=?'
    # checking for scheduled time
    if (check_schedule_time(schedule_time)):
        # checking for condition
        if (check_condition(condition, campaign)):
            # If action is notify , hits the action executor service for sending mail. 
            if (rules_data[0]['action'] == 'notify'):
                print(f"Rule with id : {rule_id} is Satisfied, Sending Notification mail. ")
                sql_update(update_rules_status,(0,campaign))
                print('inside executoe',MyGlobals.active_rules_list)
                MyGlobals.active_rules_list.remove(rule_id) # all rules for campaigns are deactivated.
                send_mail()
                print("mail sent")

def check_schedule_time(schedule_time):
    '''
    checks the scheduled time against the current time and return True is matched.
    '''

    current_time = datetime.datetime.now().time()

    if (current_time.hour == 0 and current_time.minute == 0 and current_time.second == 0):
        return True
    elif (current_time.minute == 0 and current_time.second == 0 and schedule_time != 'every day'): 
        return True
    elif ((current_time.minute % 15 == 0 ) and current_time.second == 0 and schedule_time == 'every 15 min'):
        return True
    return False


def check_condition(condition, campaign):
    '''
    checks for the condition and return True is satisfied.
    '''
    metrics = ['impressions','clicks','installs','spends']
    for metric in metrics:
        metric_query= f"select value from rule_based_engine_camp_data where campaign=? and metric=? order by created_time desc limit 1"
        globals()[metric] = [dict(metric) for metric in sql_select(metric_query,(campaign,metric))][0]['value']

    if (condition == '`eCPM` >= $5.00 AND `Impressions` >= 1000000'):
        ecpm = (spends * 1000 / impressions)
        if (ecpm >= 5.00 and impressions >= 1000000):
            return True

    elif (condition == '`Spend` >= $1000.00 AND `eCPC` <=  $0.20'):
        ecpc = (spends/clicks)
        if (ecpc <= 0.20 and spends >= 1000):
            return True

    elif (condition == '`Clicks` >= 50000 AND `Installs` <= 100'):
        if (clicks >= 50000 and installs <= 100):
            return True

    elif (condition == '`eCPI` >= $2.00 AND `Installs` >= 100'):
        ecpi = (spends/installs)
        if (ecpi >= 2.00 and installs >= 100):
            return True

    


if __name__ == "__main__":

    pass
