import os  
from combine_reports import combine_html
from Send_email import send_email
from drift_metrics import classification_metric, label_binary_classification, data_stability, data_drift, customizedKsMetric
import datetime
from dateutil.relativedelta import relativedelta
import warnings
warnings.filterwarnings("ignore") 


current_date = datetime.date.today()
previous_to_previous_month = current_date - relativedelta(months=2)
month = previous_to_previous_month.strftime("%b")  

def main(): 
    # try: 
        label_binary_classification(month)
        data_drift(month)
        data_stability(month)
        classification_metric(month)
        customizedKsMetric(month)

        combine_html()
        send_email(month)
        print("Email send!!")

    # except Exception as e:
    #     print('!! Error in running main :', e)

if __name__ == "__main__": 
    main()





