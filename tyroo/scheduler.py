''' Runs scheduler on every 15 mins and execute rule on every 1 sec'''

from rule_executor_service import sql_connect,sql_select,active_rules
import time, threading
import concurrent.futures
from globals import MyGlobals


def fetch_rules():
    ''' fetch the active rules from the database and pass the result to list'''

    ruleId_query = 'select id from rule_based_engine_camp_rules where status=?'
    rules_id = sql_select(ruleId_query,(1,))
    active_rules_list = [dict(rule_id)['id'] for rule_id in rules_id]
    return active_rules_list


def execute_rules_service():
    ''' execute the active_rules function from rule_executor_service for 
        each active rule using seprate thread for each execution'''

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(active_rules, MyGlobals.active_rules_list)
    # create another thread for same function at interval of 1 sec
    threading.Timer(1,execute_rules_service).start()





if __name__ == "__main__":
    
    scheduler_time = 15  # mention time in which scheduler will periodically run (in minutes)
    time_in_sec = (60*15)
    execute_rules_service()
    
    while True:
        
        MyGlobals.active_rules_list = fetch_rules()
        #print(MyGlobals.active_rules_list)
        time.sleep(time_in_sec)
    
